#!/usr/bin/python2.7
#  Originally made by Luke Hackworth

# for reference see
# https://www.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/

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
        
    vel = []


def main():
    mouseCheck()

    # very greedy
    for part_a in particle_array:
        part_a.vel[1] += 0.02
        for part_b in particle_array:
            if(part_a.x != part_b.x and part_a.y != part_b.y):
                part_dist = particlesDistCalc(part_a, part_b)
                if(part_dist < max_dist):
                    j = particleBoundsCheck(part_a, part_b, part_dist)
                    
                    part_a = j[0]
                    part_b = j[1]
        part_a.y += part_a.vel[1]


def mouseCheck():
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


def particleBoundsCheck(part_a, part_b, part_dist):
    # TODO: Add particle edge bounds here, too
    part_delta = particleDeltaFind(part_a, part_b)
    m = 0.5 * (max_dist - part_dist)
    delta_x_a = (m*part_delta[0])/part_dist
    delta_y_a = (m*part_delta[1])/part_dist
    part_b.x += delta_x_a   
    part_b.y += delta_y_a
    part_a.x -= delta_x_a
    part_a.y -= delta_y_a
    return [part_a, part_b]


def particleCorrectLocFind(particle_a, particle_b):
    particle_delta = particleDeltaFind(particle_a, loc_particle_2)
    c = math.sqrt(particle_delta[0]**2 + particle_delta[1]**2)

    correct_delta_x = (particle_delta[0]*max_dist)/c
    correct_delta_y = (particle_delta[1]*max_dist)/c

    # offset delta from base_particle_loc
    correct_x = base_particle_loc[0] + correct_delta_x
    correct_y = base_particle_loc[1] + correct_delta_y

    correct_loc = (correct_x, correct_y)
    return correct_loc


def particleDeltaFind(a, b):
    x1 = a.x
    y1 = a.y
    x2 = b.x
    y2 = b.y
    delta_x = x2 - x1
    delta_y = y2 - y1
    return [delta_x, delta_y]


def particlesDistCalc(a, b):
    x1 = a.x
    y1 = a.y
    x2 = b.x
    y2 = b.y
    answer = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return answer


def screenUpdate():
    screen.fill(background_color)

    for particle in particle_array:
        pygame.draw.circle(
            screen, black,
            (int(particle.x), int(particle.y)),
            5, 2
        )

    pygame.display.update()


def quitCheck():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


while True:
    quitCheck()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                particle_array = []
        pass
    main()
    screenUpdate()  # draws everything
