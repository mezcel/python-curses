## main.py ##

import os
import sys
import json
import platform
import datetime
import textwrap

## pip install term, only for unix-like systems
if (os.name == "posix"):
	try:
		import term
	except ImportError:
		## Debian: sudo apt-get install python-pip python3 python3-pip
		## Arch: sudo pacman -S --needed python python2
		os.system("python -m pip install term")

	from term import opentty, cbreakmode

## import curses
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

## global vars
accumulator = 0

screen = curses.initscr() #initialize the curses window

## return db query view
def jsonView(json, accumulator, jsonDB):
	rosaryBeadID = accumulator

	## FKs
	beadIndexFK = int(jsonDB['rosaryBead'][rosaryBeadID]['beadIndex'])
	decadeIndexFK = int(jsonDB['rosaryBead'][rosaryBeadID]['decadeIndex'])
	mysteryIndexFK = int(jsonDB['rosaryBead'][rosaryBeadID]['mysteryIndex'])
	prayerIndexFK = int(jsonDB['rosaryBead'][rosaryBeadID]['prayerIndex'])
	scriptureIndexFK = int(jsonDB['rosaryBead'][rosaryBeadID]['scriptureIndex'])
	messageIndexFK = int(jsonDB['rosaryBead'][rosaryBeadID]['messageIndex'])

	## Progress and position Flags
	loopBody = int(jsonDB['rosaryBead'][rosaryBeadID]['loopBody'])
	smallbeadPercent = int(jsonDB['rosaryBead'][rosaryBeadID]['smallbeadPercent'])
	mysteryPercent = int(jsonDB['rosaryBead'][rosaryBeadID]['mysteryPercent'])

	## Consolidated attribute view
	jsonOutput = {
		"beadType": str(jsonDB['bead'][beadIndexFK]['beadType']),
		"mysteryName": str(jsonDB['mystery'][mysteryIndexFK]['mysteryName']),
		"mysteryDecade": str(jsonDB['decade'][decadeIndexFK]['decadeName']),
		"mesageText": str(jsonDB['message'][messageIndexFK]['mesageText']),
		"scriptureText": str(jsonDB['scripture'][scriptureIndexFK]['scriptureText']),
		"prayerName": str(jsonDB['prayer'][prayerIndexFK]['prayerName']),
		"prayerText": str(jsonDB['prayer'][prayerIndexFK]['prayerText']),
		"loopBody": str(loopBody),
		"smallbeadPercent": str(smallbeadPercent),
		"mysteryPercent": str(mysteryPercent)
	}

	return jsonOutput

'''
### Key Press #################################################
'''

def navInput(myKeyPress, accumulatorInput):
	switcher = {
		## jump to mystery using numbers
		48: mysteryOfDay(), ## 0
		49: 0,				## 1
		50: 79,				## 2
		51: 158,			## 3
		52: 237,			## 4
		## forward and reverse navigation
		261: navFwd(accumulatorInput),	## rt arrow
		108: navFwd(accumulatorInput),	## vim l
		100: navFwd(accumulatorInput),	## game d
		260: navRev(accumulatorInput),	## lt arrow
		104: navRev(accumulatorInput),	## vim h
		97: navRev(accumulatorInput),	## game a
	}

	return switcher.get(myKeyPress, accumulatorInput)

def navFwd(accumulatorInput):
	accumulatorInput += 1

	accumulatorMax=315
	if (accumulatorInput > accumulatorMax):
		accumulatorInput = 0

	return accumulatorInput

def navRev(accumulatorInput):
	accumulatorInput -= 1

	accumulatorMin=0
	if (accumulatorInput < accumulatorMin):
		accumulatorInput = 315

	return accumulatorInput

def mysteryOfDay():
	dayOfWeek = datetime.datetime.today().weekday() ##  Monday is 0 and Sunday is 6.

	switcher = {
		6: 237, 0: 0, 1: 158, 2: 237, 3: 79, 4: 158, 5: 0
	}

	return switcher.get(dayOfWeek, 0)

def returnDateString():
	dt = datetime.datetime.now().strftime("%d/%m/%Y")
	day, month, year = (int(x) for x in dt.split('/'))
	ans = datetime.date(year, month, day)

	now = str(ans.strftime("%A")) + " " + str(day) + " " + str(ans.strftime("%b")) + " " + str(year)

	return now

'''
### Text Alignment ###########################################
'''

def centerText(row, maxX, myString):
	strLen = len(myString)
	startCol = (maxX / 2) - (strLen / 2)
	screen.addstr(row, int(startCol), myString )

def leftJustifyText(row, myString):
	startCol = 2
	screen.addstr(row, startCol, myString )

def rightJustifyText(row, maxX, myString):
	strLen = len(myString)
	startCol = (maxX - 2) - (strLen)
	screen.addstr(row, int(startCol), myString )

def myHR(row, maxX):
	rowlength = maxX - 2
	for col in range(rowlength):
		screen.addstr(row, (col + 1), '.')

def decadeProgressInfo(maxX, maxY, decadeLabel, decadeFraction, beadType, prayerName):
	topRow = maxY - 8
	screen.addstr(topRow + 2, 2, decadeLabel )
	screen.addstr(topRow + 2, 22, decadeFraction)
	screen.addstr(topRow + 2, 30, beadType )
	rightJustifyText(topRow + 2, maxX, prayerName)

def mysteryProgressInfo(maxX, maxY, mysteryLabel, mysteryFraction, mysteryName, decadeName):
	topRow = maxY - 8
	screen.addstr(topRow + 5, 2, mysteryLabel )
	screen.addstr(topRow + 5, 22, mysteryFraction)
	screen.addstr(topRow + 5, 30, mysteryName )
	rightJustifyText(topRow + 5, maxX, decadeName)

def progressBar(row, volumePercent):
	rowlength = volumePercent - 4
	for col in range(rowlength):
		screen.addstr(row, (col + 2), '|')

'''
### Bundled Blocks  ##########################################
'''

def headerTextblock(json, maxX, jsonData):

	topPadding = 1

	now = returnDateString()

	leftJustifyText( topPadding, "New American Bible (NAB) - English" )
	centerText( topPadding, maxX, "Python Terminal Rosary" )
	rightJustifyText( topPadding, maxX, str(now) )
	myHR( topPadding + 1, maxX )

def myWordWrap(row, sentenceString, maxX):

	desiredLength = maxX - 6

	wrapper = textwrap.TextWrapper(width=desiredLength)
	wrapper.subsequent_indent = "  "
	wrappedText = wrapper.fill(text=sentenceString)

	screen.addstr(row, 4, wrappedText)

def bodyDisplay(json, maxX, maxY, jsonData, lblStyle):

	labelPadding = 2
	valuePadding = 4

	row = 4
	screen.addstr(row, labelPadding, "Mystery Name:", lblStyle)
	row += 2
	screen.addstr(row, valuePadding, jsonData['mysteryName'] )

	row += 2
	screen.addstr(row, labelPadding, "Mystery Decade:", lblStyle )
	row += 2
	screen.addstr(row, valuePadding, jsonData['mysteryDecade'] )

	row += 2
	screen.addstr(row, labelPadding, "Mystery Message:", lblStyle )
	row += 2
	screen.addstr(row, valuePadding, jsonData['mesageText'] )

	row += 2
	screen.addstr(row, labelPadding, "Scripture Text:", lblStyle )
	row += 2
	myWordWrap(row, str(jsonData['scriptureText']), maxX)

	row += 4
	screen.addstr(row, labelPadding, "Prayer Text:", lblStyle )
	row += 2
	myWordWrap(row, str(jsonData['prayerText']), maxX)

def footerProgressBlock(json, maxX, maxY, jsonData):

	topRow = maxY - 8

	smallbeadPercent = int(jsonData['smallbeadPercent'])
	mysteryPercent = int(jsonData['mysteryPercent'])
	isBodyLoop = int(jsonData['loopBody'])

	beadType = str(jsonData['beadType'])
	prayerName = str(jsonData['prayerName'])
	decadeName = str(jsonData['mysteryDecade'])
	mysteryName = str(jsonData['mysteryName'])

	myHR( topRow, maxX )
	centerText( topRow + 1, maxX, "Progress Status" )

	## Decade and Bead Progress Display

	decadeLabel = "Decade Progress:"
	decadeFraction = str(smallbeadPercent) + "/10"
	volumePercent = int(maxX * (smallbeadPercent / 10.0) )

	if (isBodyLoop == 0 ):
		if ( int(jsonData['smallbeadPercent']) < 1):
			volumePercent = int(maxX * (smallbeadPercent / 7.0) )
			decadeLabel = "Intro. Progress:"
			decadeFraction = "start"
		elif (mysteryPercent == 50 ):
			#volumePercent = maxX
			decadeLabel = "Outro. Progress:"
			decadeFraction = "ending"
		else:
			volumePercent = int(maxX * (smallbeadPercent / 7.0) )
			decadeLabel = "Intro. Progress:"
			decadeFraction = str(smallbeadPercent) + "/7"

	decadeProgressInfo(maxX, maxY, decadeLabel, decadeFraction, beadType, prayerName)
	progressBar( topRow + 3, volumePercent)

	## Mystery Total Progress Display

	mysteryLabel = "Mystery Progress:"
	mysteryFraction = str(mysteryPercent) + "/50"

	mysteryProgressInfo(maxX, maxY, mysteryLabel, mysteryFraction, mysteryName, decadeName)

	mysteryPercent = mysteryPercent / 50.0
	volumePercent = int(maxX * mysteryPercent )
	progressBar( topRow + 6, volumePercent)

'''
### About ##############################################################
'''

def titleScreen():
	maxY, maxX = screen.getmaxyx()
	firstLine = int((maxY / 2) - 3)
	centerText(firstLine, maxX, "python-curses")
	nextLine = firstLine + 2
	centerText(nextLine, maxX, "A CLI scriptural Rosary using Python and Curses")
	nextLine = nextLine + 2
	centerText(nextLine, maxX, "by Mezcel")
	screen.getch()

def aboutScreen(lblUnderline):

	maxY, maxX = screen.getmaxyx()
	screen.addstr(0, 0, '')
	screen.clrtobot()

	centerText(1, maxX, "python-curses")
	screen.addstr(3, 2, "About:", lblUnderline)
	leftJustifyText(5, "A CLI scriptural Rosary using Python and Curses")
	leftJustifyText(6, "\tby Mezcel, https://github.com/mezcel/python-curses.git")

	screen.addstr(8, 2, "Display:", lblUnderline)
	leftJustifyText(10, "Dynamic resize primarily works on Linux style POSIX terminal types like WSL, Xterm or xfce4-terminal, ect." )
	leftJustifyText(11, "Current display: (" + str(maxX) + "x, " + str(maxY) + "y)." + " | Minimum display: (140x, 40y)" )
	screen.addstr(13, 2, "Instructions:", lblUnderline)
	leftJustifyText(15, "The first mystery defaults to the mystery of the day." )
	leftJustifyText(16, "Reset to a desired mystery. Number Keys (0-4) correspond with: Daily, Joy, Luminous, Sorrow, & Glory." )
	leftJustifyText(17, "Press the right/left arrow keys to navigate forward/reverse." )
	leftJustifyText(18, "\tthe h/l vim keys to navigate forward/reverse." )
	leftJustifyText(19, "\tthe a/d game arrow keys to navigate forward/reverse." )
	leftJustifyText(20, "Number keys 0-4 will jump to a mystery, 0 is the mystery of the day." )
	leftJustifyText(21, "Press Q to quit." )

	centerText(maxY - 1, maxX, "(press any key to continue)")
	screen.getch()

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

	## Rosary Json DB
	jsonFilePath = "module-version/rosaryJSON-nab.json"
	jsonDB = json.load(open(jsonFilePath, 'r'))

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
