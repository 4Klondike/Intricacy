import pygame
import enitities
import menus

class game:
	def __init__(self):
		r = menus.mainMenu()
		self.flag = r.run()

	def runloop(self):
		while self.flag:
			player = enitities.player()


