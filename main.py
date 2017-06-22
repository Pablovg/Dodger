# IMPORTS
import pygame as pg
import sys
import player as pl
from colors import *
from pygame.locals import *


# DEFAULTS
HEIGHT = 60
WIDTH = 80
BS = 10 #BLOCKSIZE
BSI = 8 #INNER BLOCKSIZE
SPEED = 30

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
clock = pg.time.Clock()
player = pl.player(window, WIDTH/2, HEIGHT/2, BS, BSI)
move = NONE
tick = 0
counter = 0
pg.display.set_caption("Dodger! | Points = " + str(counter))


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
		
def notLimit(move):
	pos = player.getPos()
	
	if (move == UP and pos[1]-1 != 0) or (move == DOWN and pos[1]+1 != HEIGHT-1) or (move == LEFT and pos[0]-1 != 0) or (move == RIGHT and pos[0]+1 != WIDTH-1):
		return True
	else:
		return False
		print("tocandooo")


'''
gameovertext = font.render("GAME OVER", 1, WHITE)
starttext = font.render("PRESS ANY KEY TO START", 1, WHITE)
'''



while True:

	drawWalls(window)
	direction = player.getDirection()
	
	tick += 1
	
	if tick == SPEED:
		counter += 1
		tick = 0
		pg.display.set_caption("Dodger! | Points = " + str(counter))
		
	
	
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
		if notLimit(move):
			player.move(move)
		elif notLimit(direction):
			player.move(direction)
		
	player.draw()
	clock.tick(SPEED)
	pg.display.update()

