## mycontrolls.py ##
## Data and Navigation Calculations

import json

'''
### JSON ######################################################
'''

def importJsonFile(json, filePath):

	# , 'r'
	with open(filePath, 'r') as json_file:
		data = json.load(json_file)

	json_str = json.dumps(data, ensure_ascii=False, encoding='utf8')
	return json.loads(json_str)

def rosaryTextJson(json, accumulator, jsonDB):

	rosaryBeadID = accumulator

	decadeIndexFK = int(jsonDB['rosaryBead'][rosaryBeadID]['decadeIndex'])
	mysteryIndexFK = int(jsonDB['rosaryBead'][rosaryBeadID]['mysteryIndex'])
	prayerIndexFK = int(jsonDB['rosaryBead'][rosaryBeadID]['prayerIndex'])
	scriptureIndexFK = int(jsonDB['rosaryBead'][rosaryBeadID]['scriptureIndex'])
	messageIndexFK = int(jsonDB['rosaryBead'][rosaryBeadID]['messageIndex'])

	jsonOutput = {
		"mysteryName": str(jsonDB['mystery'][mysteryIndexFK]['mysteryName']),
		"mysteryDecade": str(jsonDB['decade'][decadeIndexFK]['decadeName']),
		"message": str(jsonDB['message'][messageIndexFK]['mesageText']),
		"scripture": str(jsonDB['scripture'][scriptureIndexFK]['scriptureText']),
		"prayer": str(jsonDB['prayer'][prayerIndexFK]['prayerText'])
	}

	return jsonOutput

def rosaryPositionJson(json, accumulator, jsonDB):
	rosaryBeadID = accumulator

	loopBody = int(jsonDB['rosaryBead'][rosaryBeadID]['loopBody'])
	smallbeadPercent = int(jsonDB['rosaryBead'][rosaryBeadID]['smallbeadPercent'])
	mysteryPercent = int(jsonDB['rosaryBead'][rosaryBeadID]['mysteryPercent'])

	jsonOutput = {
		"loopBody": str(loopBody),
		"smallbeadPercent": str(smallbeadPercent),
		"mysteryPercent": str(mysteryPercent)
	}

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
		10: navFwd(accumulatorInput),	## enter
		261: navFwd(accumulatorInput),	## rt arrow
		260: navRev(accumulatorInput),	## lt arrow
		263: navRev(accumulatorInput)	## backspacee
	}

	return switcher.get(myKeyPress, accumulatorInput)

def navFwd(accumulatorInput):
	accumulatorInput += 1

	accumulatorMax=200
	tmpMax = 78
	if (accumulatorInput > tmpMax):
		accumulatorInput = 0

	return accumulatorInput

def navRev(accumulatorInput):
	accumulatorInput -= 1

	accumulatorMin=0
	if (accumulatorInput < 0):
		#accumulatorInput = 200
		accumulatorInput = 78

	return accumulatorInput
