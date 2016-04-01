#!/usr/bin/python2.7
#  Originally made by Luke Hackworth

# for reference see
# https://www.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/
# I pity the fool who tries to read through this

import sys
import os
import math
import pygame
import time
import random
from pygame.locals import *
pygame.init()


size = width, height = 640, 480
screen = pygame.display.set_mode(size)

black = (0, 0, 0)
background_color = (100, 150, 50)

base_particle_loc = (width/2, height/2)
max_dist = 7
particle_array = []


class Particle:
    def __init__(self, x, y):
        self.vel = [0, 0]
        self.x = x
        self.y = y
        self.x_vel = 0
        self.y_vel = 0
        self.prev_x = x
        self.prev_y = y
        

def main():
    mouse_check()

    for part_a in particle_array:
        
        part_a.x += part_a.x_vel
        part_a.y += part_a.y_vel
        
        for part_b in particle_array:
            if(part_a.x != part_b.x and part_a.y != part_b.y):
                part_dist = particles_dist_calc(part_a, part_b)
                if(part_dist < max_dist):
                    j = particle_distance_check(part_a, part_b, part_dist)
                    
                    part_a = j[0]
                    part_b = j[1]

        part_a.x_vel = (part_a.x - part_a.prev_x)*0.002
        part_a.y_vel = (part_a.y - part_a.prev_x)*0.002
        part_a.y_vel += -0.002
        part_a = outer_bounds_check(part_a)
        part_a.prev_x = part_a.x
        part_a.prev_y = part_a.y


def mouse_check():
    is_mouse_pressed = pygame.mouse.get_pressed()[0]

    # Adds particle
    if(is_mouse_pressed):
        mouse_loc = pygame.mouse.get_pos()
        mouse_loc_array = [mouse_loc[0], mouse_loc[1]]

        m = Particle(
            mouse_loc_array[0]+random.random(),
            mouse_loc_array[1]+random.random()
        )

        particle_array.append(m)

def outer_bounds_check(input_particle):
    if(input_particle.x < 0):
        input_particle.x = 0
        input_particle.x_vel *= -0.5
    elif(input_particle.x > size[0]):
        input_particle.x = size[0]
        input_particle.x_vel *= -0.5
    if(input_particle.y < 0):
        input_particle.y = 0
        input_particle.y_vel *= -0.5
    elif(input_particle.y > size[1]):
        input_particle.y = size[1]
        input_particle.y_vel *= -0.5
    return input_particle

def particle_distance_check(part_a, part_b, part_dist):
    # TODO: Add particle edge bounds here, too
    part_delta = particle_delta_find(part_a, part_b)
    m = 0.5 * (max_dist - part_dist)
    delta_x_a = (m*part_delta[0])/part_dist
    delta_y_a = (m*part_delta[1])/part_dist
    part_b.x += delta_x_a   
    part_b.y += delta_y_a
    part_a.x -= delta_x_a
    part_a.y -= delta_y_a
    return [part_a, part_b]


def particle_delta_find(a, b):
    delta_x = b.x - a.x
    delta_y = b.y - a.y
    return [delta_x, delta_y]


def particles_dist_calc(a, b):
    answer = math.hypot((b.x-a.x),(b.y-a.y))
    return answer


def screen_update():
    screen.fill(background_color)

    for particle in particle_array:
        try:
            pygame.draw.circle(
                screen, black,
                (int(particle.x), int(particle.y)),
                5, 2
            )
        except:
            print("Oops")
    pygame.display.update()


def quit_check():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


while True:
    quit_check()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                particle_array = []
        pass
    main()
    screen_update()  # draws everything
