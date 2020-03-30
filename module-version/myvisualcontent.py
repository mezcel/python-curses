## myvisualcontent.py ##
## Populate Screen Display

import textwrap

## my modules
from mycontrolls import *
from main import screen

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
