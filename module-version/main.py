## main.py ##

import os
import sys
import platform
#import curses
try:
	import curses
except ImportError:
	if (platform.system() == "Linux"):
		os.system("python -m pip install curses")
		import curses
	elif (platform.system() == "Windows"):
		os.system("pip install --upgrade pip")
		os.system("python -m pip install windows-curses")
		import curses

## my modules
from mycontrolls import *
from myvisualcontent import *

if (os.name == "posix"):
	try:
		import term
	except ImportError:
		## Debian: sudo apt-get install python-pip python3 python3-pip
		## Arch: sudo pacman -S --needed python python2
		os.system("python -m pip install term")
	
	from term import opentty, cbreakmode

## global vars
accumulator = 0

screen = curses.initscr() #initialize the curses window

'''
### Main Processes ############################################
'''

def minimumResize(maxY, maxX):

	if (os.name == "posix"):
		'''os.system("resize -s 40 140") ## Linux
		screen.erase()
		screen.refresh()'''

		## pip install term, only for unix-like systems
		from term import opentty, cbreakmode

		## resize terminal
		with opentty() as tty:
			if tty is not None:
				with cbreakmode(tty, min=0):
					ttyWidth=140
					ttyHeight=40
					newScreenDimentions = '\033[8;' + str(ttyHeight) + ';' + str(ttyWidth) + 't'
					tty.write(newScreenDimentions)

	if (os.name == "nt"):
		#os.system("mode 140, 40") ## Win NT
		os.system('mode con: cols=140 lines=40')

		thisDir = str(os.getcwd())
		thisFile = "main.py"
		thisFilePath = thisDir + "\\" + thisFile
		newAppInstance = "python  " + thisFilePath
		os.system(newAppInstance)
		sys.exit(0) ## kill this instance of the app

def initDisplay():

	#screen = curses.initscr() #initialize the curses window
	## Configure global variables for Curses
	curses.noecho() #disable the key press echo to prevent double input
	curses.cbreak() #disable line buffers to run the key press immediately
	curses.curs_set(0)
	screen.keypad(1) #enable keyboard use
	#curses.start_color()
	#curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)

def populateDisplay(jsonData):

	screen.refresh()
	maxY, maxX = screen.getmaxyx()

	if ( (maxY < 40) or (maxX < 140) ):
		minimumResize(maxY, maxX)
		return

	screen.clear()

	## header
	headerTextblock(json, maxX, jsonData)

	## body
	lblUnderline = curses.A_UNDERLINE
	bodyDisplay(json, maxX, maxY, jsonData, lblUnderline)

	## footer
	footerProgressBlock(json, maxX, maxY, jsonData)

	## screen border
	screen.border('|', '|', '-', '-', '+', '+', '+', '+')

def myMain():

	jsonDB = importJsonFile(json, 'rosaryJSON-nab.json')

	global accumulator
	accumulator = int(mysteryOfDay())

	escape = False

	titleScreen() ## cover page splash

	while (escape == False):

		jsonData =jsonView(json, accumulator, jsonDB)
		populateDisplay(jsonData)

		myKeyPress = screen.getch()
		accumulator = navInput(myKeyPress, accumulator)

		## q|Q is quit
		if (myKeyPress == 113):
			escape = True
			curses.endwin()

		elif (myKeyPress == curses.KEY_RESIZE):
			screen.erase()

		elif (
			myKeyPress != 261 and myKeyPress != 260 and myKeyPress != 49
			and myKeyPress != 50 and myKeyPress != 51 and myKeyPress != 52
			and myKeyPress != 48 and myKeyPress != 100 and myKeyPress != 108
			and myKeyPress != 97 and myKeyPress != 104
		): ## rt/lt keys
			screen.erase()
			lblUnderline = curses.A_UNDERLINE
			aboutScreen(lblUnderline)

## Run

if __name__ == '__main__':

	initDisplay()
	myMain()
