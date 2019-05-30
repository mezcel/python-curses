## main.py ##

import os
import curses

## my modules
from mycontrolls import *
from myvisualcontent import *

## global vars
accumulator = 0
screen = curses.initscr() #initialize the curses window

'''
### Main Processes ############################################
'''

def minimumResize(maxY, maxX):

	if (os.name == "posix"):
		os.system("resize -s 40 140") ## Linux
		screen.erase()
		screen.refresh()

	if (os.name == "nt"):
		os.system("mode 140, 40") ## Win NT
		screen.erase()
		screen.refresh()
		screen.addstr(1, 2, "Window is too small: ( Restart with a larger window )")
		screen.addstr(3, 2, "Current Window:" )
		screen.addstr(3, 30, str(maxX) + " x " + str(maxX) )
		screen.addstr(5, 2, "Required Minimum Window:" )
		screen.addstr(5, 30, "140 x 40" )
		screen.addstr(7, 2, "(press Q to exit)" )

		screen.getch()
		escape = True
		#screen.endwin()

def initDisplay(curses):

	## Configure global variables for Curses
	curses.noecho() #disable the key press echo to prevent double input
	curses.cbreak() #disable line buffers to run the key press immediately
	curses.curs_set(0)
	screen.keypad(1) #enable keyboard use

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
	bodyDisplay(json, maxX, maxY, jsonData)

	## footer
	footerProgressBlock(json, maxX, maxY, jsonData)

	## screen border
	screen.border('|', '|', '-', '-', '+', '+', '+', '+')

def myMain():

	jsonDB = importJsonFile(json, 'rosaryJSON-nab.json')
	initDisplay(curses)

	escape = False
	myKeyPress = "n/a"

	while (escape == False):

		global accumulator
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
		elif (myKeyPress <> 261 and myKeyPress <> 260): ## rt/lt keys
			screen.erase()
			controllInstruction()
			screen.getch()

## Run

if __name__ == '__main__':

	myMain()
