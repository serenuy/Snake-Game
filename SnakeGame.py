import pygame
import time
import random
from tkinter import *
from tkinter import messagebox
import customtkinter
import sys
import os
import uuid as u

pygame.init()

# Set User exist
user = False

# Get username
def username():
	customtkinter.CTk()
	username_request = customtkinter.CTkInputDialog(title="Greetings Echelon", text="Type your username:")
	# even if username is blank, accept it and use a default username
	username = username_request.get_input()
	return username

while user == False:
	username = username()
	user = True

# Fonts
font_path = 'font/Grand9k Pixel.ttf'
size = 20
pixel_font = pygame.font.Font(font_path,size)

# Colors
pink = (255,20,147)
purple = (138,43,226)
black = (0,0,0)
white = (255,255,255)
green = (0, 255, 0)
red = (255,0,0)

# Display variables/Appearance
display_width = 600
display_height = 400
display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Hungry Echelon")
customtkinter.set_appearance_mode("#303030")
customtkinter.set_default_color_theme("blue")

FPS = pygame.time.Clock()

# Snake variables/Appearance
snake_block = 10
snake_speed = 13
snakeH = pygame.image.load("images/snakehead2.png").convert_alpha()
snakeB = pygame.image.load("images/snakebody2.png").convert_alpha()

# Exit Application
def quit():
	pygame.quit()
	sys.exit()

def instructions():
	story = "Tom Reed's enemies are back for blood."
	story_2 = "This time, you must save yourself."
	instr = "P - Pause"
	instr_2 = "You can only kill using your head."
	instr_3 = "After killing 30 enemies, be ready to charge-up."
	instr_4 = "You cannot backtrack or you get caught."
	instr_5 = "Use WASD or arrow keys to move around."
	story_font = pygame.font.Font(font_path, 12).render(story, True, white)
	story_font2 = pygame.font.Font(font_path, 12).render(story_2, True, white)
	instr_font = pygame.font.Font(font_path, 12).render(instr, True, white)
	instr_font2 = pygame.font.Font(font_path, 12).render(instr_2, True, white)
	instr_font3 = pygame.font.Font(font_path, 12).render(instr_3, True, white)
	instr_font4 = pygame.font.Font(font_path, 12).render(instr_4, True, white)
	instr_font5 = pygame.font.Font(font_path, 12).render(instr_5, True, white)
	display.blit(story_font,[170, 80])
	display.blit(story_font2,[190, 100])
	display.blit(instr_font, [260,230])
	display.blit(instr_font2, [193,250])
	display.blit(instr_font3, [140,270])
	display.blit(instr_font4, [160,290])
	display.blit(instr_font5, [160,310])

def message(m, color):
	if m == "":
		welcome = "Welcome Back Echelon!"
	else:
		welcome = "Welcome Back "+m+"!"
	message = pygame.font.Font(font_path, 20).render(welcome, True, color)
	display.blit(message, [180, display_height/3])

# Pause Game Screen
def pause():
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					return
			if event.type == pygame.QUIT:
				quit()

		display.fill(black)
		main_message("Game Paused. Press P to unpause.", white)
		pygame.display.update()

def main_message(m, color):
	message = pixel_font.render(m, True, color)
	display.blit(message, message.get_rect(center = display.get_rect().center))
	Icon = pygame.image.load("images/SplinterCell_Icon.png").convert_alpha()
	display.blit(Icon, [250,330])

# Display Score on screen
def score(s):
	val = pixel_font.render("Score: "+str(s),True,purple)
	display.blit(val,[0,0])
	return s

def high_score():
	music(3)
	sound_fx(2)
	display.fill(white)
	main_message("CONGRATS! Max Score Reached!", green)
	credits("Instagram: @Serenuy", black)
	pygame.display.update()
	winner()
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()

def write_scores(s): # needs to be readjusted to put all scores caught
	with open('highscores.txt', 'a') as f:
		if os.path.getsize('highscores.txt') != 0:
			f.write("\n")
		if username == "":
			f.write("Echelon"+u.uuid4().hex[:5]+": "+str(s))
		else: 
			f.write(username+": "+str(s))
		f.close()
	return

def winner():
	messagebox.showinfo("Winner!","Redeem Code: Check 'readme.txt' in game folder.")
	with open('readme.txt', 'w') as f:
			f.write('[Redeem via Steam] 1111-2222-3333')

def credits(m, color):
	credits_1 = "Music: David Renda"
	credits_2 = "Github: @serenuy"
	message = pygame.font.Font(font_path, 12).render(m, True, color)
	message2 = pygame.font.Font(font_path, 12).render(credits_1, True, color)
	message3 = pygame.font.Font(font_path, 12).render(credits_2, True, color)
	display.blit(message, [220,30])
	display.blit(message2, [225,50])
	display.blit(message3, [225,70])

# Music selected based on stage/level/completed
def music(x):
	if x == 0:
		pygame.mixer.music.load("bg_music/Castle_of_Fear.mp3")
		pygame.mixer.music.play(-1)
	elif x == 1:
		pygame.mixer.music.load("bg_music/BossTime.mp3")
		pygame.mixer.music.play(-1)
	elif x == 2:
		pygame.mixer.music.load("bg_music/gameOver.wav")
		pygame.mixer.music.play(0)
	elif x == 3:
		pygame.mixer.music.load("bg_music/sweet_victory.mp3")
		pygame.mixer.music.set_volume(0.3)
		pygame.mixer.music.play(-1)

def sound_fx(x):
	SF = pygame.mixer.Sound("sound_fx/SF_audio.mp3")
	hurt = pygame.mixer.Sound("sound_fx/ManHurt.mp3")
	hurt2 = pygame.mixer.Sound("sound_fx/ManHurt2.mp3")
	hurt3 = pygame.mixer.Sound("sound_fx/ManHurt3.mp3")

	if x == 1:
		randx = random.randrange(1,4)
		if randx == 1:
			pygame.mixer.Sound.set_volume(hurt, 1.0)
			pygame.mixer.Sound.play(hurt)
		if randx == 2:
			pygame.mixer.Sound.set_volume(hurt2, 1.0)
			pygame.mixer.Sound.play(hurt2)
		if randx == 3:
			pygame.mixer.Sound.set_volume(hurt3, 1.0)
			pygame.mixer.Sound.play(hurt3)
	if x == 2:
		pygame.mixer.Sound.set_volume(SF, 1.0)
		pygame.mixer.Sound.play(SF)

def snake_body(snake_block, snake_list, score):
	for x in snake_list:
		if score >= 1:
			display.blit(snakeH, [x[0],x[1], snake_block, snake_block])
			for i in snake_list[:-1]:
				display.blit(snakeB, [i[0],i[1], snake_block, snake_block])
		else:
			display.blit(snakeH, [x[0],x[1], snake_block, snake_block])

# Start Game
def gameLoop():
	music(0)
	gameOver = False
	gameClose = False
	BossTime = False
	begin = False

	x1 = display_width/2
	y1 = display_height/2

	x_update = 0
	y_update = 0

	snake_List = []
	snakeLen = 1

	enemyX = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
	enemyY = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

	# if the enemy is too close to the edge of the screen, re-position the enemy randomly again 
	# or if the enemy is in the same spot as the score letters, re-position
	while (enemyY <= 27 or enemyY >= 390 or enemyX <= 5 or enemyX >= 590):
				enemyX = round(random.randrange(0, (300) - snake_block) / 10.0) * 10.0
				enemyY = round(random.randrange(0, (300) - snake_block) / 10.0) * 10.0

	while not gameOver:
		# Start Screen
		while begin == False:
			display.fill(black)
			instructions()
			message(username, white)
			main_message("Let's see if you can kill all gaurds in your way.", green)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_p:
						begin = True
				if event.type == pygame.QUIT:
					begin = True
					gameOver = True
		# While game lost
		while gameClose == True:
			display.fill(black)
			display.fill(white,[0,0,115,27])
			main_message("Focus! Press P to 'Play Again' or Q for 'Quit'",green)
			snake_score = score(snakeLen-1)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameOver = True
						gameClose = False
						write_scores(snake_score)
					if event.key == pygame.K_p:
						write_scores(snake_score)
						gameLoop() # re-play

		# Get the users key inputs WASD or Key Arrows allowed
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameOver = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT or event.key == pygame.K_a:
					x_update = -snake_block
					y_update = 0
				elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					x_update = snake_block
					y_update = 0
				elif event.key == pygame.K_UP or event.key == pygame.K_w:
					y_update = -snake_block
					x_update = 0
				elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
					y_update = snake_block
					x_update = 0
				elif event.key == pygame.K_p:
					pause()

		# Check if user hits the display boundaries for gameover
		if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0: 
			music(2)
			gameClose = True

		x1 += x_update
		y1 += y_update

		display.fill(black)
		display.fill(white,[0,0,115,27])

		# Update score
		snake_score = score(snakeLen-1)

		# Update enemies color
		if snake_score >= 30:
			pygame.draw.rect(display, red, [enemyX,enemyY,snake_block,snake_block])
		else:
			pygame.draw.rect(display, white, [enemyX,enemyY,snake_block,snake_block])

		snake_Head = []
		snake_Head.append(x1)
		snake_Head.append(y1)
		snake_List.append(snake_Head)

		if len(snake_List) > snakeLen:
			del snake_List[0]

		# If snake head makes contact with the body, gameover
		for x in snake_List[:-1]:
			if x == snake_Head:
				music(2)
				gameClose = True
		
		# Update snake body
		snake_body(snake_block, snake_List, snake_score)

		# Update level speed
		if snake_score == 30 and BossTime == False:
			music(1)
			BossTime = True
		# If user reaches max score
		elif snake_score == 0:
			write_scores(snake_score)
			high_score()

		pygame.display.update()

		if x1 == enemyX and y1 == enemyY:
			enemyX = round(random.randrange(0, (300) - snake_block) / 10.0) * 10.0
			enemyY = round(random.randrange(0, (300) - snake_block) / 10.0) * 10.0
			# if enemyY/x is near score width/height or too close to the edge of the width/height, re-place enemy
			while (enemyY <= 27 or enemyY >= 390 or enemyX <= 5 or enemyX >= 590 or [enemyX,enemyY] in snake_List):
				enemyX = round(random.randrange(0, (300) - snake_block) / 10.0) * 10.0
				enemyY = round(random.randrange(0, (300) - snake_block) / 10.0) * 10.0
			snakeLen += 1
			sound_fx(1)
			
		if snake_score >= 5 and snake_score < 30:
			FPS.tick(snake_speed + 1)
		elif snake_score >= 30:
			FPS.tick(snake_speed + 4)
		else:
			FPS.tick(snake_speed)

	quit()

while user == True:
	gameLoop()