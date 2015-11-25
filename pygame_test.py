#!/usr/bin/python2.7

import sys, os
import math
import pygame
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
max_dist = 50

def main():
	global loc_particle_2
	
	mouse_loc = pygame.mouse.get_pos()
	#loc_particle_2 = mouse_loc
	
	particle_dist = locsDistCalc(base_particle_loc, mouse_loc)
	if(particle_dist > max_dist):
		loc_particle_2 = particleCorrectLocFind(base_particle_loc, loc_particle_2)


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
	return (delta_x, delta_y)

def locsDistCalc((x1, y1), (x2, y2)):
	answer = math.sqrt((x2 - x1)**2+(y2 - y1)**2)
	return answer

def screenUpdate():
	screen.fill(background_color)
	pygame.draw.lines(screen, black, False, [base_particle_loc, loc_particle_2], 2)
	
	pygame.draw.circle(screen, black, (50,50), 30, 2)
	
	pygame.display.update()
	
	
#main loop	
while True:
	for event in pygame.event.get():
		pass
	#print pygame.mouse.get_pos()
	main()
	screenUpdate() #draws everything(be sure to put what to render in there)
