#!/usr/bin/python2.7

import sys, os
import math
import pygame
import time #for time.sleep testing, can be removed after testing
import random #for rand float entry so (hopefully) no two mouse_locations are the same
from pygame.locals import *
pygame.init()

# for reference see https://www.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/

##Variable initialization
#screen
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
#colors
black = (0, 0, 0)
background_color = (100, 150, 50)
#particle variables
base_particle_loc = (width/2,height/2)
loc_particle_2 = (2,2)
max_dist = 15
particle_loc_array = []

def main():
	global loc_particle_2
	mouse_loc = pygame.mouse.get_pos()
	#pygame.mouse.get_pos is a tuple(immutable), must be changed to array before assigning to particle so particle loc can be updated
	mouse_loc_array = [mouse_loc[0], mouse_loc[1]]

	is_mouse_pressed = pygame.mouse.get_pressed()[0]
	
	if(is_mouse_pressed):
		#Random float added to locs so no two particles have same coordinates
		particle_loc_array.append([mouse_loc_array[0]+random.random(), mouse_loc_array[1]+random.random()])
		
	
	particle_count = 0
	#very greedy
	for part_a in particle_loc_array:
		for part_b in particle_loc_array:
			if(part_a != part_b):
				part_dist = locsDistCalc(part_a, part_b)
				if(part_dist < max_dist):
					###REFACTOR
					
					###
					j = particleBoundsCheck(part_a, part_b, part_dist)
					part_a = j[0]
					part_b = j[1]
	
		particle_count += 1
	#time.sleep(.25)
	print particle_count

def particleBoundsCheck(part_a, part_b, part_dist):
	#TODO: Add particle edge bounds here, too
	part_delta = particleDeltaFind(part_a, part_b)
	m = 0.5 * (max_dist - part_dist)
	delta_x_a = (m*part_delta[0])/part_dist
	delta_y_a = (m*part_delta[1])/part_dist
	part_b[0] += delta_x_a
	part_b[1] += delta_y_a
	part_a[0] -= delta_x_a
	part_a[1] -= delta_y_a
	return [part_a,part_b]

def particleCorrectLocFind(particle_a, particle_b):
	#base_particle_loc = particle_a
	#loc_particle_2 = particle_b
	particle_delta = particleDeltaFind(particle_a, loc_particle_2)
	c = math.sqrt(particle_delta[0]**2 + particle_delta[1]**2)
	
	correct_delta_x = (particle_delta[0]*max_dist)/c
	correct_delta_y = (particle_delta[1]*max_dist)/c
		
	#offset delta from base_particle_loc
	correct_x = base_particle_loc[0] + correct_delta_x
	correct_y = base_particle_loc[1] + correct_delta_y
	
	correct_loc = (correct_x, correct_y)
	return correct_loc
	
def particleDeltaFind((x1, y1), (x2, y2)):
	delta_x = x2 - x1
	delta_y = y2 - y1
	return [delta_x, delta_y]

def locsDistCalc(a, b):
	x1 = a[0]
	y1 = a[1]
	x2 = b[0]
	y2 = b[1]
	answer = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
	return answer

def screenUpdate():
	screen.fill(background_color)
	
	pygame.draw.circle(screen, black, (50,50), 30, 2)
	
	for particle in particle_loc_array:
		pygame.draw.circle(screen, black, (int(particle[0]), int(particle[1])), 5, 2)
	
	pygame.display.update()
	
	
#main loop	
while True:
	for event in pygame.event.get():
		pass
	#print pygame.mouse.get_pos()
	main()
	screenUpdate() #draws everything(be sure to put what to render in there)
