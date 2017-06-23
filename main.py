# IMPORTS
import pygame as pg
import sys
import player as pl
import enemy as en
from random import randint
from colors import *
from pygame.locals import *


# DEFAULTS
HEIGHT = 100
WIDTH = 120
BS = 6 #BLOCKSIZE
BSI = 4 #INNER BLOCKSIZE
SPEED = 50

# DIRECTIONS
NONE = 0
UP    = 1
DOWN  = 2
LEFT  = 3
RIGHT = 4

# TESTBLOCK
redblock = pg.Surface((BS, BS))
redblock.set_alpha(255)
redblock.fill(RED)

# WALLBLOCK
wallblock = pg.Surface((BS, BS))
wallblock.set_alpha(255)
wallblock.fill(BLUE)
wallblockdark = pg.Surface((BSI, BSI))
wallblockdark.set_alpha(255)
wallblockdark.fill(BLUE_DARK)

# SETUP
pg.init()
window = pg.display.set_mode(((WIDTH)*BS, (HEIGHT)*BS))
window.fill(BLACK)
font = pg.font.SysFont(pg.font.get_default_font(), 40)
gameovertext = font.render("GAME OVER", 1, WHITE)
starttext = font.render("PRESS ANY KEY TO START", 1, WHITE)
clock = pg.time.Clock()
player = pl.player(window, WIDTH/2, HEIGHT/2, BS, BSI)
move = NONE
tick = 0
time = 0
points = 0
pg.display.set_caption("Dodger! | Points = %i" % time)
enemy_list = []


# draw walls
def drawWalls(surface):

	# left and right walls
	for y in range(HEIGHT):
		surface.blit(wallblock,(0, y*BS))
		surface.blit(wallblockdark,(1, y*BS+1))
		surface.blit(wallblock,((WIDTH-1)*BS, y*BS))
		surface.blit(wallblockdark,((WIDTH-1)*BS+1, y*BS+1))

	# upper and bottom walls
	for x in range(WIDTH):
		surface.blit(wallblock,(x*BS, 0))
		surface.blit(wallblockdark,(x*BS+1, 1))
		surface.blit(wallblock,(x*BS,(HEIGHT-1)*BS,))
		surface.blit(wallblockdark,(x*BS+1, (HEIGHT-1)*BS+1))
		
def notLimit(pos, move):
	if (move == UP and pos[1]-1 != 0) or (move == DOWN and pos[1]+1 != HEIGHT-1) or (move == LEFT and pos[0]-1 != 0) or (move == RIGHT and pos[0]+1 != WIDTH-1):
		return True
	else:
		return False
		
def isEnemy(pos):
	for enemy in enemy_list:
		if pos == enemy.getPos():
			return True

def addEnemy():
	enemy = en.enemy(window, BS, BSI)
	vertical = randint(0, 1) # generated in the top/down or left/right borders
		
	if vertical == 0: # left/right
		posy = randint(1, HEIGHT - 2)
		left_right = randint(0, 1)
		
		if left_right == 0:
			posx = 1
		else:
			posx = WIDTH - 2
	
	else: # top/down
		posx = randint(1, WIDTH - 2)
		top_down = randint(0, 1)
		
		if top_down == 0:
			posy = 1
		else:
			posy = HEIGHT - 2

	enemy.setPos(posx, posy)
	enemy_list.append(enemy)

def moveEnemy():
	for enemy in enemy_list:
		move = randint(1, 4)
		pos = enemy.getPos()
		
		if notLimit(pos, move):
			enemy.move(move)
	
def drawEnemy():
	for enemy in enemy_list:
		enemy.draw()


running = True
while running:

	moveEnemy()
	direction = player.getDirection()
	
	for event in pg.event.get():
		if event.type == QUIT:
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				sys.exit()
			elif event.key == K_UP and direction != UP:
				move = UP
			elif event.key == K_DOWN and direction != DOWN:
				move = DOWN
			elif event.key == K_RIGHT and direction != RIGHT:
				move = RIGHT
			elif event.key == K_LEFT and direction != LEFT:
				move = LEFT
		
	if move != NONE:
		if notLimit(player.getPos(), move):
			player.move(move)
		elif notLimit(player.getPos(), direction):
			player.move(direction)
	
	if isEnemy(player.getPos()):
		running = False
	
	drawWalls(window)
	player.draw()
	drawEnemy()
	clock.tick(SPEED)
	tick += 1
	
	if tick == SPEED:
		time += 1
		tick = 0
		pg.display.set_caption("Dodger! | Time = %i" % time)
		addEnemy()
	
	pg.display.update()
	
while True:
	window.blit(gameovertext, ((WIDTH-WIDTH/4)*BS/2, (HEIGHT-HEIGHT/10)*BS/2))
	pg.display.flip()
	event = pg.event.wait()
	if event.type == QUIT:
		sys.exit()
	elif event.type == pg.KEYDOWN:
		if event.key == pg.K_ESCAPE:
			sys.exit()

