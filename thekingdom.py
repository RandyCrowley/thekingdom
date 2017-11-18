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
pygame.display.set_caption("The Kingdom")
keys = [False,False,False,False]


playerPosition = [200,100]
acc = [0,0]
arrows = []
enemyTimer = 100
enemyTimer1 = 0
enemies = [[640,100]]
healthvalue = 194
pygame.mixer.init()

#load the game images
player = pygame.image.load("resources/images/player.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
healthbar = pygame.image.load("resources/images/healthbar.png")
mute = pygame.image.load("resources/images/mute.png")
goblin = pygame.image.load("resources/images/Goblin.png")
enemy = goblin
arrow = pygame.image.load("resources/images/fireball.png")
#load audio
#pygame.mixer.music.load("resources/audio/intro.wav")
#pygame.mixer.music.play(-1,0.0)
#pygame.mixer.music.set_volume(0.25)
shoot = pygame.mixer.Sound("resources/audio/shoot.wav")
shoot.set_volume(0.05)
hit = pygame.mixer.Sound("resources/audio/hit.mp3")
hit.set_volume(0.5)

#keep loop through the game
running = 1
exitCode = 0
while running:
	enemyTimer-=1
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

	#draw arrows to screen
	for bullet in arrows:
		index = 0
		velx = math.cos(bullet[0])*10
		vely = math.sin(bullet[0])*10
		bullet[1]+= velx
		bullet[2]+= vely
		if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
			arrows.pop(index)
		index += 1
		for projectile in arrows:
			arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
			screen.blit(arrow1, (projectile[1], projectile[2])) 

	#Draw Enemies To screen
	if enemyTimer == 0:
		enemies.append([640,random.randint(50,430)])
		enemyTimer = 100-(enemyTimer1*2)
		if enemyTimer1 >= 35:
			enemyTimer1 = 35
		else:
		 enemyTimer1 += 5
	index = 0
	for badguy in enemies:
		if badguy[0]<64:
			enemies.pop(index)
		badguy[0]-= 7

		#attack Castle 
		badrect = pygame.Rect(enemy.get_rect())
		badrect.top = badguy[1]
		badrect.left = badguy[0]
		if badrect.left<64:
			hit.play()
			healthvalue-= random.randint(5,20)
			enemies.pop(index)
			#check for collisions
		index1 = 0
		for bullet in arrows:
			bullrect = pygame.Rect(arrow.get_rect())
			bullrect.left = bullet[1]
			bullrect.top = bullet[2]
			if badrect.colliderect(bullrect):
				#ene,y play
				acc[0] +=1
				enemies.pop(index)
				arrows.pop(index1)
			index1+=1

		#draw next goblin
		index += 1
	for badguy in enemies:
		screen.blit(enemy,badguy)
	#screen.blit(goblin,(450,100))



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
		if event.type == pygame.MOUSEBUTTONDOWN:
			shoot.play()
			position = pygame.mouse.get_pos()
			acc[1]+= 1
			arrows.append([math.atan2(position[1]-(playerPosition1[1]+32), position[0]-(playerPosition1[0]+26)), playerPosition1[0]+32, playerPosition1[1]+32])
			#elif event.key == K_m:
				#keys[4] = False
		if (pygame.key.get_pressed()[pygame.K_m] == 1):
			pygame.mixer.music.pause()
			#draw mute
			screen.blit(mute,(600,430))
	
		elif (pygame.key.get_pressed()[pygame.K_u] == 1):
			pygame.mixer.music.play(-1,0.0) 


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

	