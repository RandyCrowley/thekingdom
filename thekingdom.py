#import python libraries
import pygame
from pygame.locals import *
import math 
import random

#initilize the game 
pygame.init()
width = 640
height = 480
screen = pygame.display.set_mode((width,height))
keys = [False,False,False,False]

playerPosition = [200,100]
pygame.mixer.init()

#load the game images
player = pygame.image.load("resources/images/player.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
healthbar = pygame.image.load("resources/images/healthbar.png")
mute = pygame.image.load("resources/images/mute.png")
#load audio
pygame.mixer.music.load("resources/audio/intro.wav")
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(0.25)

#keep loop through the game
running = 1
exitCode = 0
while running:
	#clear screen
	screen.fill(0)
	#draw the player on the screen @ player pos
	for x in range(width/grass.get_width()+1):
		for y in range(height/grass.get_height()+1):
			screen.blit(grass,(x*100,y*100))
	screen.blit(castle,(0,30))
	screen.blit(castle,(0,135))
	screen.blit(castle,(0,240))
	screen.blit(castle,(0,345))
	#set player pos
	position = pygame.mouse.get_pos()
	angle = math.atan2(position[1]-(playerPosition[1]+32),position[0]-(playerPosition[0]-26))
	playerRotation = pygame.transform.rotate(player,0)
	playerPosition1 = (playerPosition[0]-playerRotation.get_rect().width/2,playerPosition[1]-playerRotation.get_rect().height/2)
	screen.blit(playerRotation,playerPosition1)

	#draw mute
	screen.blit(mute,(600,430))
	#if I click on the mute image
	#set music volume to 0
	#set new image to unmute
	 

	# draw health bar
	screen.blit(healthbar,(450,0))
	
	#update the screen
	pygame.display.flip()
	
	#loop through the events
	for event in pygame.event.get():
		#check if event is x button
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)
		if event.type == pygame.KEYDOWN:
			if event.key == K_w:
				keys[0] = True
			elif event.key == K_a:
				keys[1] = True
			elif event.key == K_s:
				keys[2] = True
			elif event.key == K_d:
				keys[3] = True

		if event.type == pygame.KEYUP:
			if event.key == K_w:
				keys[0] = False
			elif event.key == K_a:
				keys[1] = False
			elif event.key == K_s:
				keys[2] = False
			elif event.key == K_d:
				keys[3] = False

	#move player
	if keys[0]:
		playerPosition[1] -= 5
	elif keys[2]:
		playerPosition[1] += 5
	elif keys[1]:
		playerPosition[0] -= 5
	elif keys[3]:
		playerPosition[0] += 5

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit(0)
		pygame.display.flip()