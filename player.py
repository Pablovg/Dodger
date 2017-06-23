# IMPORTS
import pygame as pg
from colors import *

# DIRECTIONS
NONE = 0
UP    = 1
DOWN  = 2
LEFT  = 3
RIGHT = 4

class player:

	# constructor
	def __init__(self, surface, POSX, POSY, BS, BSI):
		self.surface = surface
		self.pos = [POSX, POSY]
		self.bs = BS
		self.bsi = BSI
		self.direction = NONE

		# for drawing the block
		self.playerblock = pg.Surface((BS, BS))
		self.playerblock.set_alpha(255)
		self.playerblock.fill(YELLOW)
		self.playerblockdark = pg.Surface((BSI,BSI))
		self.playerblockdark.set_alpha(255)
		self.playerblockdark.fill(YELLOW_DARK)
		
		# for deleting blocks
		self.blackblock = pg.Surface((BS, BS))
		self.blackblock.set_alpha(255)
		self.blackblock.fill(BLACK)


	def getPos(self):
		return self.pos
		
	def getDirection(self):
		return self.direction
	
	def move(self, move):
		pos = self.getPos()

		self.surface.blit(self.blackblock,(pos[0]*self.bs, pos[1]*self.bs))
		self.direction = move

		# update positions
		if move == 1: #UP
			pos = [pos[0], pos[1]-1]
		elif move == 2: #DOWN
			pos = [pos[0], pos[1]+1]
		elif move == 3: #LEFT
			pos = [pos[0]-1, pos[1]]
		elif move == 4: #RIGHT
			pos = [pos[0]+1, pos[1]]

		self.pos = pos

	def draw(self):
		self.surface.blit(self.playerblock, (self.pos[0]*self.bs, self.pos[1]*self.bs))
		self.surface.blit(self.playerblockdark,(self.pos[0]*self.bs+1, self.pos[1]*self.bs+1))

