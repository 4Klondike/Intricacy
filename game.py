import pygame
import entities
import menus

class game:
	def __init__(self):
		r = menus.mainMenu()
		self.flag = r.run()

	def runloop(self):
		while self.flag:
			player = entities.player()


