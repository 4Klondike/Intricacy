from pygame import font
from colours import *

font.init()


class menu:
	def __init__(self, text, back=False):
		self.titleFont = font.Font()
		self.optionFont = font.Font()

		self.options = []
		self.text = []

	def addOption(self,text,function):


	def addText(self,text,menu=False):
		if menu:
			self.text.append(self.titleFont.render(text, False, COLOUR.GREY))
		else:
			self.text.append(self.optionFont.render(text, False, COLOUR.GREY))

	def run(self):
		while self.menuFlag:
			if back:
				drawBack()
			for i in self.text:

			for i in self.options:

	def exitRun(self):
		self.menuFlag = False

	def drawText(self):





class mainMenu(menu):
	def __init__(self):

		super(mainMenu, self).__init__()

		settings = settingsMenu()
		credits = creditsMenu()

		self.addOption("Play",self.exitRun)
		self.addOption("Settings",self.settings.run)
		self.addOption("Credits",self.credits.run)
		self.addOption("exit",self.exitApp)
	def exitApp(self):



class settingsMenu(menu):
	def __init__(self):
		super(settingsMenu, self).__init__(back=True)



class creditsMenu(menu):
	def __init__(self):
		super(creditsMenu, self).__init__(back=True)
		self.addText()