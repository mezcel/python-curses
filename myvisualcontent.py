## myvisualcontent.py ##
## Populate Screen Display

import datetime

from mycontrolls import *
from main import screen

'''
### Text Alignment ###########################################
'''

def centerText(row, maxX, myString):
	strLen = len(myString)
	startCol = (maxX / 2) - (strLen / 2)
	screen.addstr(row, startCol, myString )

def leftJustifyText(row, myString):
	startCol = 2
	screen.addstr(row, startCol, myString )

def rightJustifyText(row, maxX, myString):
	strLen = len(myString)
	startCol = (maxX - 2) - (strLen)
	screen.addstr(row, startCol, myString )

def myHR(row, maxX):
	rowlength = maxX - 2
	for col in range(rowlength):
		screen.addstr(row, (col + 1), '.')

def progressBar(row, volumePercent):
	rowlength = volumePercent - 4
	for col in range(rowlength):
		screen.addstr(row, (col + 2), '|')

'''
### Bundled Blocks  ##########################################
'''

def headerTextblock(json, maxX, jsonData):

	topPadding = 1

	dt = datetime.datetime.now().strftime("%d/%m/%Y")
	day, month, year = (int(x) for x in dt.split('/'))
	ans = datetime.date(year, month, day)

	now = str(ans.strftime("%A")) + " " + str(day) + " " + str(ans.strftime("%b")) + " " + str(year)

	leftJustifyText( topPadding, "NAB - English" )
	centerText( topPadding, maxX, "Python Terminal Rosary" )
	rightJustifyText( topPadding, maxX, str(now) )
	myHR( topPadding + 1, maxX )

def bodyDisplay(json, maxX, maxY, jsonData):

	labelPadding = 2
	valuePadding = 4

	row = 4
	screen.addstr(row, labelPadding, "[Mystery Name]:")
	row += 2
	screen.addstr(row, valuePadding, jsonData['mysteryName'] )

	row += 2
	screen.addstr(row, labelPadding, "[Mystery Decade]:" )
	row += 2
	screen.addstr(row, valuePadding, jsonData['mysteryDecade'] )

	row += 2
	screen.addstr(row, labelPadding, "[Mystery Message]:" )
	row += 2
	screen.addstr(row, valuePadding, jsonData['mesageText'] )

	row += 2
	screen.addstr(row, labelPadding, "[Scripture Text]:" )
	row += 2
	screen.addstr(row, valuePadding, jsonData['scriptureText'] )

	row += 4
	screen.addstr(row, labelPadding, "[Prayer Text]:" )
	row += 2
	screen.addstr(row, valuePadding, jsonData['prayerText'] )

def footerProgressBlock(json, maxX, maxY, jsonData):

	topRow = maxY - 8

	smallbeadPercent = int(jsonData['smallbeadPercent'])
	mysteryPercent = int(jsonData['mysteryPercent'])
	beadType = str(jsonData['beadType'])
	prayerName = str(jsonData['prayerName'])
	decadeName = str(jsonData['mysteryDecade'])
	mysteryName = str(jsonData['mysteryName'])

	myHR( topRow, maxX )
	centerText( topRow + 1, maxX, "Progress Status" )

	## Decade and Bead Progress Display

	isBodyLoop = int(jsonData['loopBody'])
	if (isBodyLoop == 0 ):
		if ( int(jsonData['smallbeadPercent']) < 1):
			smallbeadPercent = smallbeadPercent / 7.0
			volumePercent = int(maxX * smallbeadPercent)
			leftJustifyText( topRow + 2, "Introduction Progress:  0/0 beginning crucifix " + beadType)
		elif (mysteryPercent == 50 ):
			volumePercent = maxX
			leftJustifyText( topRow + 2, "Conclusion Progress:  --/-- Conclusion Prayers " + beadType)
		else:
			smallbeadPercent = smallbeadPercent / 7.0
			volumePercent = int(maxX * smallbeadPercent)
			leftJustifyText( topRow + 2, "Introduction Progress:  " + str(jsonData['smallbeadPercent']) + "/7 " + beadType)
	else:
		smallbeadPercent = smallbeadPercent / 10.0
		volumePercent = int(maxX * smallbeadPercent)
		leftJustifyText( topRow + 2, "Decade Progress:  " + str(jsonData['smallbeadPercent']) + "/10 " + beadType)

	rightJustifyText(topRow + 2, maxX, prayerName)
	progressBar( topRow + 3, volumePercent)

	## Mystery Total Progress Display

	leftJustifyText( topRow + 5, "Mystery Progress: " + str(jsonData['mysteryPercent']) + "/50 " +  mysteryName )
	rightJustifyText(topRow + 5, maxX, decadeName)
	mysteryPercent = mysteryPercent / 50.0
	volumePercent = int(maxX * mysteryPercent )
	progressBar( topRow + 6, volumePercent)
