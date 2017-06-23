# IMPORTS
import pygame as pg
from random import randint
from colors import *

class enemy:
	
	def __init__(self, surface, BS, BSI):
		self.surface = surface
		self.bs = BS
		self.bsi = BSI
		
		# for drawing the block
		self.enemyblock = pg.Surface((BS, BS))
		self.enemyblock.set_alpha(255)
		self.enemyblock.fill(RED)
		self.enemyblockdark = pg.Surface((BSI, BSI))
		self.enemyblockdark.set_alpha(255)
		self.enemyblockdark.fill(RED_DARK)
		
		# for deleting blocks
		self.blackblock = pg.Surface((BS, BS))
		self.blackblock.set_alpha(255)
		self.blackblock.fill(BLACK)

	def setPos(self, posx, posy):
		self.pos = [posx, posy]
		
	def getPos(self):
		return self.pos
		
	def isEnemy():
		return True

	def move(self, move):
		pos = self.getPos()
		self.surface.blit(self.blackblock, (pos[0]*self.bs, pos[1]*self.bs))

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
		self.surface.blit(self.enemyblock, (self.pos[0]*self.bs, self.pos[1]*self.bs))
		self.surface.blit(self.enemyblockdark,(self.pos[0]*self.bs+1, self.pos[1]*self.bs+1))
