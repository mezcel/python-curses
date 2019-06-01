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

	leftJustifyText( topPadding, "NAB - English" )
	centerText( topPadding, maxX, "Python Terminal Rosary" )
	rightJustifyText( topPadding, maxX, str(now) )
	myHR( topPadding + 1, maxX )

def myWordWrap(row, sentenceString, maxX):

	desiredLength = maxX - 6

	wrapper = textwrap.TextWrapper(width=desiredLength)
	wrapper.subsequent_indent = "  "
	wrappedText = wrapper.fill(text=sentenceString)

	screen.addstr(row, 4, wrappedText)

def bodyDisplay(json, maxX, maxY, jsonData, lblHighlight):

	labelPadding = 2
	valuePadding = 4

	row = 4
	screen.addstr(row, labelPadding, "Mystery Name:", lblHighlight)
	row += 2
	screen.addstr(row, valuePadding, jsonData['mysteryName'] )

	row += 2
	screen.addstr(row, labelPadding, "Mystery Decade:", lblHighlight )
	row += 2
	screen.addstr(row, valuePadding, jsonData['mysteryDecade'] )

	row += 2
	screen.addstr(row, labelPadding, "Mystery Message:", lblHighlight )
	row += 2
	screen.addstr(row, valuePadding, jsonData['mesageText'] )

	row += 2
	screen.addstr(row, labelPadding, "Scripture Text:", lblHighlight )
	row += 2
	myWordWrap(row, str(jsonData['scriptureText']), maxX)

	row += 4
	screen.addstr(row, labelPadding, "Prayer Text:", lblHighlight )
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

def controllInstruction():

	screen.addstr(0, 2, "Instructions:")
	screen.addstr(2, 2, "* press the right/left arrow keys to navigate forward/reverse.")
	screen.addstr(3, 2, "* press Q to quit")
	screen.addstr(5, 2, "(press any key to continue)")
