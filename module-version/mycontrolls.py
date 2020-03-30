## mycontrolls.py ##
## Data and Navigation Calculations

import json
import platform
import datetime

#from myvisualcontent import mysteryMenu

'''
### JSON ######################################################
'''

def importJsonFile2(json, filePath):
	## Json for python 2.7

	with open(filePath, 'r') as json_file:
		data = json.load(json_file)

	json_str = json.dumps(data, ensure_ascii=False, encoding='utf8')
	return json.loads(json_str)

def importJsonFile3(json, filePath):
	## Json for python 3.7

    with open(filePath, encoding='utf-8') as data_file:
        data = json.loads(data_file.read())

    return data

def importJsonFile(json, filePath):
	pythonVersion = str(platform.python_version())
	pythonVersion = int(pythonVersion[0])

	if(pythonVersion == 2):
		jsonOutput = importJsonFile2(json, filePath)
	else:
		jsonOutput = importJsonFile3(json, filePath)

	return jsonOutput

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
