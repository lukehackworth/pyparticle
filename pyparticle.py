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


window_size = width, height = 640, 480
screen = pygame.display.set_mode(window_size)

black = (0, 0, 0)
background_color = (100, 150, 50)

max_dist = 14
particle_list = []


class Particle:
    def __init__(self, x, y):
        self.vel = [0, 0]
        self.x = x
        self.y = y
        self.x_vel = 0
        self.y_vel = 0
        self.prev_x = x
        self.prev_y = y

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def calculate_velocity(self):
        self.x_vel = (self.x - self.prev_x)
        self.y_vel = (self.y - self.prev_y)

    def add_gravity(self, input_gravity):
        self.y_vel += input_gravity

    def check_bounds(self):
        if(self.x < 0):
            self.x = 0
            self.x_vel *= -0.5
        elif(self.x > window_size[0]):
            self.x = window_size[0]
            self.x_vel *= -0.5
        if(self.y < 0):
            self.y = 0
            self.y_vel *= -0.5
        elif(self.y > window_size[1]):
            self.y = window_size[1]
            self.y_vel *= -0.5

    def assign_prev_loc(self):
        self.prev_x = self.x
        self.prev_y = self.y

def main():
    mouse_check()

    for part_a in particle_list:

        part_a.move()

        for part_b in particle_list:
            if(part_a.x != part_b.x and part_a.y != part_b.y):
                part_dist = particles_dist_calc(part_a, part_b)
                if(part_dist < max_dist):
                    j = move_particles_away(part_a, part_b, part_dist)

                    part_a = j[0]
                    part_b = j[1]

        part_a.calculate_velocity()
        part_a.add_gravity(0.5)
        part_a.check_bounds()
        part_a.assign_prev_loc()


def mouse_check():
    is_mouse_pressed = pygame.mouse.get_pressed()[0]

    # Adds particle
    if(is_mouse_pressed):
        mouse_loc = pygame.mouse.get_pos()
        mouse_loc_list = [mouse_loc[0], mouse_loc[1]]

        m = Particle(
            mouse_loc_list[0]+random.random(),
            mouse_loc_list[1]+random.random()
        )

        particle_list.append(m)





def move_particles_away(part_a, part_b, part_dist):
    # returns particles separated by distance part_dist
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
    answer = math.hypot((b.x-a.x), (b.y-a.y))
    return answer


def screen_update():
    screen.fill(background_color)

    for particle in particle_list:
            pygame.draw.circle(
                screen, black,
                (int(particle.x), int(particle.y)),
                5, 2
            )
    pygame.display.update()


def quit_check():
    global particle_list
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                particle_list = []


while True:
    quit_check()

    main()
    screen_update()  # draws everything
