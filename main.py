## main.py ##

import os
import curses

from mycontrolls import *
from myvisualcontent import *

## global vars
accumulator = 0
screen = curses.initscr() #initialize the curses window

'''
### Main Processes ############################################
'''

def initDisplay(curses):

	## Configure global variables for Curses
	curses.noecho() #disable the keypress echo to prevent double input
	curses.cbreak() #disable line buffers to run the keypress immediately
	curses.curs_set(0)
	screen.keypad(1) #enable keyboard use

	## Bash resize
	## resize -s 40 140 &>/dev/null
	## stty rows 40
	os.system("resize -s 40 140")

def populateDisplay(jsonData):

	screen.refresh()
	maxY, maxX = screen.getmaxyx()

	if ( (maxY < 40) or (maxX < 140) ):
		os.system("resize -s 40 140")
		## consider making an error display

	screen.clear()

	## screen border
	screen.border('|', '|', '-', '-', '+', '+', '+', '+')

	## header
	headerTextblock(json, maxX, jsonData)

	## body
	bodyDisplay(json, maxX, maxY, jsonData)

	## footer
	footerProgressBlock(json, maxX, maxY, jsonData)

def myMain():

	jsonDB = importJsonFile(json, 'rosaryJSON-nab.json')
	initDisplay(curses)

	escape = False
	myKeyPress = "n/a"

	while (escape == False):

		global accumulator
		jsonData =jsonView(json, accumulator, jsonDB);

		populateDisplay(jsonData)

		myKeyPress = screen.getch()
		accumulator = navInput(myKeyPress, accumulator)

		## q|Q is quit
		if myKeyPress == 113:
			escape = True
			curses.endwin()
		elif myKeyPress == curses.KEY_RESIZE:
			screen.erase()

## Run

if __name__ == '__main__':
	myMain()
