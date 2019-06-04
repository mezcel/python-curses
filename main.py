## main.py ##

import os
import curses
import json
import platform
import datetime
import textwrap

## global vars
accumulator = 0

screen = curses.initscr() #initialize the curses window

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
	'''pythonVersion = str(platform.python_version())
	pythonVersion = int(pythonVersion[0])

	if(pythonVersion == 2):
		jsonOutput = importJsonFile2(json, filePath)
	else:
		jsonOutput = importJsonFile3(json, filePath)'''

	return {
		"rosaryBead": [
			{
				"rosaryBeadID": 0,
				"beadIndex": 0,
				"decadeIndex": 0,
				"mysteryIndex": 1,
				"prayerIndex": 1,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 0,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 1,
				"beadIndex": 6,
				"decadeIndex": 0,
				"mysteryIndex": 0,
				"prayerIndex": 2,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 1,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 2,
				"beadIndex": 3,
				"decadeIndex": 0,
				"mysteryIndex": 0,
				"prayerIndex": 3,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 2,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 3,
				"beadIndex": 2,
				"decadeIndex": 0,
				"mysteryIndex": 0,
				"prayerIndex": 4,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 3,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 4,
				"beadIndex": 2,
				"decadeIndex": 0,
				"mysteryIndex": 0,
				"prayerIndex": 4,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 4,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 5,
				"beadIndex": 2,
				"decadeIndex": 0,
				"mysteryIndex": 0,
				"prayerIndex": 4,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 5,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 6,
				"beadIndex": 3,
				"decadeIndex": 0,
				"mysteryIndex": 0,
				"prayerIndex": 5,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 6,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 7,
				"beadIndex": 5,
				"decadeIndex": 1,
				"mysteryIndex": 1,
				"prayerIndex": 0,
				"scriptureIndex": 0,
				"messageIndex": 1,
				"loopBody": 0,
				"smallbeadPercent": 7,
				"mysteryPercent": 1
			}, {
				"rosaryBeadID": 8,
				"beadIndex": 3,
				"decadeIndex": 1,
				"mysteryIndex": 1,
				"prayerIndex": 3,
				"scriptureIndex": 0,
				"messageIndex": 1,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 1
			}, {
				"rosaryBeadID": 9,
				"beadIndex": 2,
				"decadeIndex": 1,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 1,
				"messageIndex": 1,
				"loopBody": 1,
				"smallbeadPercent": 1,
				"mysteryPercent": 1
			}, {
				"rosaryBeadID": 10,
				"beadIndex": 2,
				"decadeIndex": 1,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 2,
				"messageIndex": 1,
				"loopBody": 1,
				"smallbeadPercent": 2,
				"mysteryPercent": 2
			}, {
				"rosaryBeadID": 11,
				"beadIndex": 2,
				"decadeIndex": 1,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 3,
				"messageIndex": 1,
				"loopBody": 1,
				"smallbeadPercent": 3,
				"mysteryPercent": 3
			}, {
				"rosaryBeadID": 12,
				"beadIndex": 2,
				"decadeIndex": 1,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 4,
				"messageIndex": 1,
				"loopBody": 1,
				"smallbeadPercent": 4,
				"mysteryPercent": 4
			}, {
				"rosaryBeadID": 13,
				"beadIndex": 2,
				"decadeIndex": 1,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 5,
				"messageIndex": 1,
				"loopBody": 1,
				"smallbeadPercent": 5,
				"mysteryPercent": 5
			}, {
				"rosaryBeadID": 14,
				"beadIndex": 2,
				"decadeIndex": 1,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 6,
				"messageIndex": 1,
				"loopBody": 1,
				"smallbeadPercent": 6,
				"mysteryPercent": 6
			}, {
				"rosaryBeadID": 15,
				"beadIndex": 2,
				"decadeIndex": 1,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 7,
				"messageIndex": 1,
				"loopBody": 1,
				"smallbeadPercent": 7,
				"mysteryPercent": 7
			}, {
				"rosaryBeadID": 16,
				"beadIndex": 2,
				"decadeIndex": 1,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 8,
				"messageIndex": 1,
				"loopBody": 1,
				"smallbeadPercent": 8,
				"mysteryPercent": 8
			}, {
				"rosaryBeadID": 17,
				"beadIndex": 2,
				"decadeIndex": 1,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 9,
				"messageIndex": 1,
				"loopBody": 1,
				"smallbeadPercent": 9,
				"mysteryPercent": 9
			}, {
				"rosaryBeadID": 18,
				"beadIndex": 2,
				"decadeIndex": 1,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 10,
				"messageIndex": 1,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 10
			}, {
				"rosaryBeadID": 19,
				"beadIndex": 4,
				"decadeIndex": 1,
				"mysteryIndex": 1,
				"prayerIndex": 5,
				"scriptureIndex": 0,
				"messageIndex": 1,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 10
			}, {
				"rosaryBeadID": 20,
				"beadIndex": 4,
				"decadeIndex": 1,
				"mysteryIndex": 1,
				"prayerIndex": 6,
				"scriptureIndex": 0,
				"messageIndex": 1,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 10
			}, {
				"rosaryBeadID": 21,
				"beadIndex": 3,
				"decadeIndex": 2,
				"mysteryIndex": 1,
				"prayerIndex": 0,
				"scriptureIndex": 0,
				"messageIndex": 2,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 11
			}, {
				"rosaryBeadID": 22,
				"beadIndex": 3,
				"decadeIndex": 2,
				"mysteryIndex": 1,
				"prayerIndex": 3,
				"scriptureIndex": 0,
				"messageIndex": 2,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 11
			}, {
				"rosaryBeadID": 23,
				"beadIndex": 2,
				"decadeIndex": 2,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 11,
				"messageIndex": 2,
				"loopBody": 1,
				"smallbeadPercent": 1,
				"mysteryPercent": 11
			}, {
				"rosaryBeadID": 24,
				"beadIndex": 2,
				"decadeIndex": 2,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 12,
				"messageIndex": 2,
				"loopBody": 1,
				"smallbeadPercent": 2,
				"mysteryPercent": 12
			}, {
				"rosaryBeadID": 25,
				"beadIndex": 2,
				"decadeIndex": 2,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 13,
				"messageIndex": 2,
				"loopBody": 1,
				"smallbeadPercent": 3,
				"mysteryPercent": 13
			}, {
				"rosaryBeadID": 26,
				"beadIndex": 2,
				"decadeIndex": 2,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 14,
				"messageIndex": 2,
				"loopBody": 1,
				"smallbeadPercent": 4,
				"mysteryPercent": 14
			}, {
				"rosaryBeadID": 27,
				"beadIndex": 2,
				"decadeIndex": 2,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 15,
				"messageIndex": 2,
				"loopBody": 1,
				"smallbeadPercent": 5,
				"mysteryPercent": 15
			}, {
				"rosaryBeadID": 28,
				"beadIndex": 2,
				"decadeIndex": 2,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 16,
				"messageIndex": 2,
				"loopBody": 1,
				"smallbeadPercent": 6,
				"mysteryPercent": 16
			}, {
				"rosaryBeadID": 29,
				"beadIndex": 2,
				"decadeIndex": 2,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 17,
				"messageIndex": 2,
				"loopBody": 1,
				"smallbeadPercent": 7,
				"mysteryPercent": 17
			}, {
				"rosaryBeadID": 30,
				"beadIndex": 2,
				"decadeIndex": 2,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 18,
				"messageIndex": 2,
				"loopBody": 1,
				"smallbeadPercent": 8,
				"mysteryPercent": 18
			}, {
				"rosaryBeadID": 31,
				"beadIndex": 2,
				"decadeIndex": 2,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 19,
				"messageIndex": 2,
				"loopBody": 1,
				"smallbeadPercent": 9,
				"mysteryPercent": 19
			}, {
				"rosaryBeadID": 32,
				"beadIndex": 2,
				"decadeIndex": 2,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 20,
				"messageIndex": 2,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 20
			}, {
				"rosaryBeadID": 33,
				"beadIndex": 4,
				"decadeIndex": 2,
				"mysteryIndex": 1,
				"prayerIndex": 5,
				"scriptureIndex": 0,
				"messageIndex": 2,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 20
			}, {
				"rosaryBeadID": 34,
				"beadIndex": 4,
				"decadeIndex": 2,
				"mysteryIndex": 1,
				"prayerIndex": 6,
				"scriptureIndex": 0,
				"messageIndex": 2,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 20
			}, {
				"rosaryBeadID": 35,
				"beadIndex": 3,
				"decadeIndex": 3,
				"mysteryIndex": 1,
				"prayerIndex": 0,
				"scriptureIndex": 0,
				"messageIndex": 3,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 21
			}, {
				"rosaryBeadID": 36,
				"beadIndex": 3,
				"decadeIndex": 3,
				"mysteryIndex": 1,
				"prayerIndex": 3,
				"scriptureIndex": 0,
				"messageIndex": 3,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 21
			}, {
				"rosaryBeadID": 37,
				"beadIndex": 2,
				"decadeIndex": 3,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 21,
				"messageIndex": 3,
				"loopBody": 1,
				"smallbeadPercent": 1,
				"mysteryPercent": 21
			}, {
				"rosaryBeadID": 38,
				"beadIndex": 2,
				"decadeIndex": 3,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 22,
				"messageIndex": 3,
				"loopBody": 1,
				"smallbeadPercent": 2,
				"mysteryPercent": 22
			}, {
				"rosaryBeadID": 39,
				"beadIndex": 2,
				"decadeIndex": 3,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 23,
				"messageIndex": 3,
				"loopBody": 1,
				"smallbeadPercent": 3,
				"mysteryPercent": 23
			}, {
				"rosaryBeadID": 40,
				"beadIndex": 2,
				"decadeIndex": 3,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 24,
				"messageIndex": 3,
				"loopBody": 1,
				"smallbeadPercent": 4,
				"mysteryPercent": 24
			}, {
				"rosaryBeadID": 41,
				"beadIndex": 2,
				"decadeIndex": 3,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 25,
				"messageIndex": 3,
				"loopBody": 1,
				"smallbeadPercent": 5,
				"mysteryPercent": 25
			}, {
				"rosaryBeadID": 42,
				"beadIndex": 2,
				"decadeIndex": 3,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 26,
				"messageIndex": 3,
				"loopBody": 1,
				"smallbeadPercent": 6,
				"mysteryPercent": 26
			}, {
				"rosaryBeadID": 43,
				"beadIndex": 2,
				"decadeIndex": 3,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 27,
				"messageIndex": 3,
				"loopBody": 1,
				"smallbeadPercent": 7,
				"mysteryPercent": 27
			}, {
				"rosaryBeadID": 44,
				"beadIndex": 2,
				"decadeIndex": 3,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 28,
				"messageIndex": 3,
				"loopBody": 1,
				"smallbeadPercent": 8,
				"mysteryPercent": 28
			}, {
				"rosaryBeadID": 45,
				"beadIndex": 2,
				"decadeIndex": 3,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 29,
				"messageIndex": 3,
				"loopBody": 1,
				"smallbeadPercent": 9,
				"mysteryPercent": 29
			}, {
				"rosaryBeadID": 46,
				"beadIndex": 2,
				"decadeIndex": 3,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 30,
				"messageIndex": 3,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 30
			}, {
				"rosaryBeadID": 47,
				"beadIndex": 4,
				"decadeIndex": 3,
				"mysteryIndex": 1,
				"prayerIndex": 5,
				"scriptureIndex": 0,
				"messageIndex": 3,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 30
			}, {
				"rosaryBeadID": 48,
				"beadIndex": 4,
				"decadeIndex": 3,
				"mysteryIndex": 1,
				"prayerIndex": 6,
				"scriptureIndex": 0,
				"messageIndex": 3,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 30
			}, {
				"rosaryBeadID": 49,
				"beadIndex": 3,
				"decadeIndex": 4,
				"mysteryIndex": 1,
				"prayerIndex": 0,
				"scriptureIndex": 0,
				"messageIndex": 4,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 31
			}, {
				"rosaryBeadID": 50,
				"beadIndex": 3,
				"decadeIndex": 4,
				"mysteryIndex": 1,
				"prayerIndex": 3,
				"scriptureIndex": 0,
				"messageIndex": 4,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 31
			}, {
				"rosaryBeadID": 51,
				"beadIndex": 2,
				"decadeIndex": 4,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 31,
				"messageIndex": 4,
				"loopBody": 1,
				"smallbeadPercent": 1,
				"mysteryPercent": 31
			}, {
				"rosaryBeadID": 52,
				"beadIndex": 2,
				"decadeIndex": 4,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 32,
				"messageIndex": 4,
				"loopBody": 1,
				"smallbeadPercent": 2,
				"mysteryPercent": 32
			}, {
				"rosaryBeadID": 53,
				"beadIndex": 2,
				"decadeIndex": 4,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 33,
				"messageIndex": 4,
				"loopBody": 1,
				"smallbeadPercent": 3,
				"mysteryPercent": 33
			}, {
				"rosaryBeadID": 54,
				"beadIndex": 2,
				"decadeIndex": 4,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 34,
				"messageIndex": 4,
				"loopBody": 1,
				"smallbeadPercent": 4,
				"mysteryPercent": 34
			}, {
				"rosaryBeadID": 55,
				"beadIndex": 2,
				"decadeIndex": 4,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 35,
				"messageIndex": 4,
				"loopBody": 1,
				"smallbeadPercent": 5,
				"mysteryPercent": 35
			}, {
				"rosaryBeadID": 56,
				"beadIndex": 2,
				"decadeIndex": 4,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 36,
				"messageIndex": 4,
				"loopBody": 1,
				"smallbeadPercent": 6,
				"mysteryPercent": 36
			}, {
				"rosaryBeadID": 57,
				"beadIndex": 2,
				"decadeIndex": 4,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 37,
				"messageIndex": 4,
				"loopBody": 1,
				"smallbeadPercent": 7,
				"mysteryPercent": 37
			}, {
				"rosaryBeadID": 58,
				"beadIndex": 2,
				"decadeIndex": 4,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 38,
				"messageIndex": 4,
				"loopBody": 1,
				"smallbeadPercent": 8,
				"mysteryPercent": 38
			}, {
				"rosaryBeadID": 59,
				"beadIndex": 2,
				"decadeIndex": 4,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 39,
				"messageIndex": 4,
				"loopBody": 1,
				"smallbeadPercent": 9,
				"mysteryPercent": 39
			}, {
				"rosaryBeadID": 60,
				"beadIndex": 2,
				"decadeIndex": 4,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 40,
				"messageIndex": 4,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 40
			}, {
				"rosaryBeadID": 61,
				"beadIndex": 4,
				"decadeIndex": 4,
				"mysteryIndex": 1,
				"prayerIndex": 5,
				"scriptureIndex": 0,
				"messageIndex": 4,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 40
			}, {
				"rosaryBeadID": 62,
				"beadIndex": 4,
				"decadeIndex": 4,
				"mysteryIndex": 1,
				"prayerIndex": 6,
				"scriptureIndex": 0,
				"messageIndex": 4,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 40
			}, {
				"rosaryBeadID": 63,
				"beadIndex": 3,
				"decadeIndex": 5,
				"mysteryIndex": 1,
				"prayerIndex": 0,
				"scriptureIndex": 0,
				"messageIndex": 5,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 41
			}, {
				"rosaryBeadID": 64,
				"beadIndex": 3,
				"decadeIndex": 5,
				"mysteryIndex": 1,
				"prayerIndex": 3,
				"scriptureIndex": 0,
				"messageIndex": 5,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 41
			}, {
				"rosaryBeadID": 65,
				"beadIndex": 2,
				"decadeIndex": 5,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 41,
				"messageIndex": 5,
				"loopBody": 1,
				"smallbeadPercent": 1,
				"mysteryPercent": 41
			}, {
				"rosaryBeadID": 66,
				"beadIndex": 2,
				"decadeIndex": 5,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 42,
				"messageIndex": 5,
				"loopBody": 1,
				"smallbeadPercent": 2,
				"mysteryPercent": 42
			}, {
				"rosaryBeadID": 67,
				"beadIndex": 2,
				"decadeIndex": 5,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 43,
				"messageIndex": 5,
				"loopBody": 1,
				"smallbeadPercent": 3,
				"mysteryPercent": 43
			}, {
				"rosaryBeadID": 68,
				"beadIndex": 2,
				"decadeIndex": 5,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 44,
				"messageIndex": 5,
				"loopBody": 1,
				"smallbeadPercent": 4,
				"mysteryPercent": 44
			}, {
				"rosaryBeadID": 69,
				"beadIndex": 2,
				"decadeIndex": 5,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 45,
				"messageIndex": 5,
				"loopBody": 1,
				"smallbeadPercent": 5,
				"mysteryPercent": 45
			}, {
				"rosaryBeadID": 70,
				"beadIndex": 2,
				"decadeIndex": 5,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 46,
				"messageIndex": 5,
				"loopBody": 1,
				"smallbeadPercent": 6,
				"mysteryPercent": 46
			}, {
				"rosaryBeadID": 71,
				"beadIndex": 2,
				"decadeIndex": 5,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 47,
				"messageIndex": 5,
				"loopBody": 1,
				"smallbeadPercent": 7,
				"mysteryPercent": 47
			}, {
				"rosaryBeadID": 72,
				"beadIndex": 2,
				"decadeIndex": 5,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 48,
				"messageIndex": 5,
				"loopBody": 1,
				"smallbeadPercent": 8,
				"mysteryPercent": 48
			}, {
				"rosaryBeadID": 73,
				"beadIndex": 2,
				"decadeIndex": 5,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 49,
				"messageIndex": 5,
				"loopBody": 1,
				"smallbeadPercent": 9,
				"mysteryPercent": 49
			}, {
				"rosaryBeadID": 74,
				"beadIndex": 2,
				"decadeIndex": 5,
				"mysteryIndex": 1,
				"prayerIndex": 4,
				"scriptureIndex": 50,
				"messageIndex": 5,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 50
			}, {
				"rosaryBeadID": 75,
				"beadIndex": 4,
				"decadeIndex": 5,
				"mysteryIndex": 1,
				"prayerIndex": 5,
				"scriptureIndex": 0,
				"messageIndex": 5,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 50
			}, {
				"rosaryBeadID": 76,
				"beadIndex": 4,
				"decadeIndex": 5,
				"mysteryIndex": 1,
				"prayerIndex": 6,
				"scriptureIndex": 0,
				"messageIndex": 5,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 50
			}, {
				"rosaryBeadID": 77,
				"beadIndex": 5,
				"decadeIndex": 0,
				"mysteryIndex": 5,
				"prayerIndex": 7,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 5,
				"mysteryPercent": 50
			}, {
				"rosaryBeadID": 78,
				"beadIndex": 5,
				"decadeIndex": 0,
				"mysteryIndex": 5,
				"prayerIndex": 8,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 10,
				"mysteryPercent": 50
			}, {
				"rosaryBeadID": 79,
				"beadIndex": 0,
				"decadeIndex": 0,
				"mysteryIndex": 2,
				"prayerIndex": 1,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 0,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 80,
				"beadIndex": 6,
				"decadeIndex": 0,
				"mysteryIndex": 0,
				"prayerIndex": 2,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 1,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 81,
				"beadIndex": 3,
				"decadeIndex": 0,
				"mysteryIndex": 0,
				"prayerIndex": 3,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 2,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 82,
				"beadIndex": 2,
				"decadeIndex": 0,
				"mysteryIndex": 0,
				"prayerIndex": 4,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 3,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 83,
				"beadIndex": 2,
				"decadeIndex": 0,
				"mysteryIndex": 0,
				"prayerIndex": 4,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 4,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 84,
				"beadIndex": 2,
				"decadeIndex": 0,
				"mysteryIndex": 0,
				"prayerIndex": 4,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 5,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 85,
				"beadIndex": 3,
				"decadeIndex": 0,
				"mysteryIndex": 0,
				"prayerIndex": 5,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 6,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 86,
				"beadIndex": 5,
				"decadeIndex": 6,
				"mysteryIndex": 2,
				"prayerIndex": 0,
				"scriptureIndex": 0,
				"messageIndex": 6,
				"loopBody": 0,
				"smallbeadPercent": 7,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 87,
				"beadIndex": 3,
				"decadeIndex": 6,
				"mysteryIndex": 2,
				"prayerIndex": 3,
				"scriptureIndex": 0,
				"messageIndex": 6,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 1
			}, {
				"rosaryBeadID": 88,
				"beadIndex": 2,
				"decadeIndex": 6,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 51,
				"messageIndex": 6,
				"loopBody": 1,
				"smallbeadPercent": 1,
				"mysteryPercent": 1
			}, {
				"rosaryBeadID": 89,
				"beadIndex": 2,
				"decadeIndex": 6,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 52,
				"messageIndex": 6,
				"loopBody": 1,
				"smallbeadPercent": 2,
				"mysteryPercent": 2
			}, {
				"rosaryBeadID": 90,
				"beadIndex": 2,
				"decadeIndex": 6,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 53,
				"messageIndex": 6,
				"loopBody": 1,
				"smallbeadPercent": 3,
				"mysteryPercent": 3
			}, {
				"rosaryBeadID": 91,
				"beadIndex": 2,
				"decadeIndex": 6,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 54,
				"messageIndex": 6,
				"loopBody": 1,
				"smallbeadPercent": 4,
				"mysteryPercent": 4
			}, {
				"rosaryBeadID": 92,
				"beadIndex": 2,
				"decadeIndex": 6,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 55,
				"messageIndex": 6,
				"loopBody": 1,
				"smallbeadPercent": 5,
				"mysteryPercent": 5
			}, {
				"rosaryBeadID": 93,
				"beadIndex": 2,
				"decadeIndex": 6,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 56,
				"messageIndex": 6,
				"loopBody": 1,
				"smallbeadPercent": 6,
				"mysteryPercent": 6
			}, {
				"rosaryBeadID": 94,
				"beadIndex": 2,
				"decadeIndex": 6,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 57,
				"messageIndex": 6,
				"loopBody": 1,
				"smallbeadPercent": 7,
				"mysteryPercent": 7
			}, {
				"rosaryBeadID": 95,
				"beadIndex": 2,
				"decadeIndex": 6,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 58,
				"messageIndex": 6,
				"loopBody": 1,
				"smallbeadPercent": 8,
				"mysteryPercent": 8
			}, {
				"rosaryBeadID": 96,
				"beadIndex": 2,
				"decadeIndex": 6,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 59,
				"messageIndex": 6,
				"loopBody": 1,
				"smallbeadPercent": 9,
				"mysteryPercent": 9
			}, {
				"rosaryBeadID": 97,
				"beadIndex": 2,
				"decadeIndex": 6,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 60,
				"messageIndex": 6,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 10
			}, {
				"rosaryBeadID": 98,
				"beadIndex": 4,
				"decadeIndex": 6,
				"mysteryIndex": 2,
				"prayerIndex": 5,
				"scriptureIndex": 0,
				"messageIndex": 6,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 10
			}, {
				"rosaryBeadID": 99,
				"beadIndex": 4,
				"decadeIndex": 6,
				"mysteryIndex": 2,
				"prayerIndex": 6,
				"scriptureIndex": 0,
				"messageIndex": 6,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 10
			}, {
				"rosaryBeadID": 100,
				"beadIndex": 3,
				"decadeIndex": 7,
				"mysteryIndex": 2,
				"prayerIndex": 0,
				"scriptureIndex": 0,
				"messageIndex": 7,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 11
			}, {
				"rosaryBeadID": 101,
				"beadIndex": 3,
				"decadeIndex": 7,
				"mysteryIndex": 2,
				"prayerIndex": 3,
				"scriptureIndex": 0,
				"messageIndex": 7,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 11
			}, {
				"rosaryBeadID": 102,
				"beadIndex": 2,
				"decadeIndex": 7,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 61,
				"messageIndex": 7,
				"loopBody": 1,
				"smallbeadPercent": 1,
				"mysteryPercent": 11
			}, {
				"rosaryBeadID": 103,
				"beadIndex": 2,
				"decadeIndex": 7,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 62,
				"messageIndex": 7,
				"loopBody": 1,
				"smallbeadPercent": 2,
				"mysteryPercent": 12
			}, {
				"rosaryBeadID": 104,
				"beadIndex": 2,
				"decadeIndex": 7,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 63,
				"messageIndex": 7,
				"loopBody": 1,
				"smallbeadPercent": 3,
				"mysteryPercent": 13
			}, {
				"rosaryBeadID": 105,
				"beadIndex": 2,
				"decadeIndex": 7,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 64,
				"messageIndex": 7,
				"loopBody": 1,
				"smallbeadPercent": 4,
				"mysteryPercent": 14
			}, {
				"rosaryBeadID": 106,
				"beadIndex": 2,
				"decadeIndex": 7,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 65,
				"messageIndex": 7,
				"loopBody": 1,
				"smallbeadPercent": 5,
				"mysteryPercent": 15
			}, {
				"rosaryBeadID": 107,
				"beadIndex": 2,
				"decadeIndex": 7,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 66,
				"messageIndex": 7,
				"loopBody": 1,
				"smallbeadPercent": 6,
				"mysteryPercent": 16
			}, {
				"rosaryBeadID": 108,
				"beadIndex": 2,
				"decadeIndex": 7,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 67,
				"messageIndex": 7,
				"loopBody": 1,
				"smallbeadPercent": 7,
				"mysteryPercent": 17
			}, {
				"rosaryBeadID": 109,
				"beadIndex": 2,
				"decadeIndex": 7,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 68,
				"messageIndex": 7,
				"loopBody": 1,
				"smallbeadPercent": 8,
				"mysteryPercent": 18
			}, {
				"rosaryBeadID": 110,
				"beadIndex": 2,
				"decadeIndex": 7,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 69,
				"messageIndex": 7,
				"loopBody": 1,
				"smallbeadPercent": 9,
				"mysteryPercent": 19
			}, {
				"rosaryBeadID": 111,
				"beadIndex": 2,
				"decadeIndex": 7,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 70,
				"messageIndex": 7,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 20
			}, {
				"rosaryBeadID": 112,
				"beadIndex": 4,
				"decadeIndex": 7,
				"mysteryIndex": 2,
				"prayerIndex": 5,
				"scriptureIndex": 0,
				"messageIndex": 7,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 20
			}, {
				"rosaryBeadID": 113,
				"beadIndex": 4,
				"decadeIndex": 7,
				"mysteryIndex": 2,
				"prayerIndex": 6,
				"scriptureIndex": 0,
				"messageIndex": 7,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 20
			}, {
				"rosaryBeadID": 114,
				"beadIndex": 3,
				"decadeIndex": 8,
				"mysteryIndex": 2,
				"prayerIndex": 0,
				"scriptureIndex": 0,
				"messageIndex": 8,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 21
			}, {
				"rosaryBeadID": 115,
				"beadIndex": 3,
				"decadeIndex": 8,
				"mysteryIndex": 2,
				"prayerIndex": 3,
				"scriptureIndex": 0,
				"messageIndex": 8,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 21
			}, {
				"rosaryBeadID": 116,
				"beadIndex": 2,
				"decadeIndex": 8,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 71,
				"messageIndex": 8,
				"loopBody": 1,
				"smallbeadPercent": 1,
				"mysteryPercent": 21
			}, {
				"rosaryBeadID": 117,
				"beadIndex": 2,
				"decadeIndex": 8,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 72,
				"messageIndex": 8,
				"loopBody": 1,
				"smallbeadPercent": 2,
				"mysteryPercent": 22
			}, {
				"rosaryBeadID": 118,
				"beadIndex": 2,
				"decadeIndex": 8,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 73,
				"messageIndex": 8,
				"loopBody": 1,
				"smallbeadPercent": 3,
				"mysteryPercent": 23
			}, {
				"rosaryBeadID": 119,
				"beadIndex": 2,
				"decadeIndex": 8,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 74,
				"messageIndex": 8,
				"loopBody": 1,
				"smallbeadPercent": 4,
				"mysteryPercent": 24
			}, {
				"rosaryBeadID": 120,
				"beadIndex": 2,
				"decadeIndex": 8,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 75,
				"messageIndex": 8,
				"loopBody": 1,
				"smallbeadPercent": 5,
				"mysteryPercent": 25
			}, {
				"rosaryBeadID": 121,
				"beadIndex": 2,
				"decadeIndex": 8,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 76,
				"messageIndex": 8,
				"loopBody": 1,
				"smallbeadPercent": 6,
				"mysteryPercent": 26
			}, {
				"rosaryBeadID": 122,
				"beadIndex": 2,
				"decadeIndex": 8,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 77,
				"messageIndex": 8,
				"loopBody": 1,
				"smallbeadPercent": 7,
				"mysteryPercent": 27
			}, {
				"rosaryBeadID": 123,
				"beadIndex": 2,
				"decadeIndex": 8,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 78,
				"messageIndex": 8,
				"loopBody": 1,
				"smallbeadPercent": 8,
				"mysteryPercent": 28
			}, {
				"rosaryBeadID": 124,
				"beadIndex": 2,
				"decadeIndex": 8,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 79,
				"messageIndex": 8,
				"loopBody": 1,
				"smallbeadPercent": 9,
				"mysteryPercent": 29
			}, {
				"rosaryBeadID": 125,
				"beadIndex": 2,
				"decadeIndex": 8,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 80,
				"messageIndex": 8,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 30
			}, {
				"rosaryBeadID": 126,
				"beadIndex": 4,
				"decadeIndex": 8,
				"mysteryIndex": 2,
				"prayerIndex": 5,
				"scriptureIndex": 0,
				"messageIndex": 8,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 30
			}, {
				"rosaryBeadID": 127,
				"beadIndex": 4,
				"decadeIndex": 8,
				"mysteryIndex": 2,
				"prayerIndex": 6,
				"scriptureIndex": 0,
				"messageIndex": 8,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 30
			}, {
				"rosaryBeadID": 128,
				"beadIndex": 3,
				"decadeIndex": 9,
				"mysteryIndex": 2,
				"prayerIndex": 0,
				"scriptureIndex": 0,
				"messageIndex": 9,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 31
			}, {
				"rosaryBeadID": 129,
				"beadIndex": 3,
				"decadeIndex": 9,
				"mysteryIndex": 2,
				"prayerIndex": 3,
				"scriptureIndex": 0,
				"messageIndex": 9,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 31
			}, {
				"rosaryBeadID": 130,
				"beadIndex": 2,
				"decadeIndex": 9,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 81,
				"messageIndex": 9,
				"loopBody": 1,
				"smallbeadPercent": 1,
				"mysteryPercent": 31
			}, {
				"rosaryBeadID": 131,
				"beadIndex": 2,
				"decadeIndex": 9,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 82,
				"messageIndex": 9,
				"loopBody": 1,
				"smallbeadPercent": 2,
				"mysteryPercent": 32
			}, {
				"rosaryBeadID": 132,
				"beadIndex": 2,
				"decadeIndex": 9,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 83,
				"messageIndex": 9,
				"loopBody": 1,
				"smallbeadPercent": 3,
				"mysteryPercent": 33
			}, {
				"rosaryBeadID": 133,
				"beadIndex": 2,
				"decadeIndex": 9,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 84,
				"messageIndex": 9,
				"loopBody": 1,
				"smallbeadPercent": 4,
				"mysteryPercent": 34
			}, {
				"rosaryBeadID": 134,
				"beadIndex": 2,
				"decadeIndex": 9,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 85,
				"messageIndex": 9,
				"loopBody": 1,
				"smallbeadPercent": 5,
				"mysteryPercent": 35
			}, {
				"rosaryBeadID": 135,
				"beadIndex": 2,
				"decadeIndex": 9,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 86,
				"messageIndex": 9,
				"loopBody": 1,
				"smallbeadPercent": 6,
				"mysteryPercent": 36
			}, {
				"rosaryBeadID": 136,
				"beadIndex": 2,
				"decadeIndex": 9,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 87,
				"messageIndex": 9,
				"loopBody": 1,
				"smallbeadPercent": 7,
				"mysteryPercent": 37
			}, {
				"rosaryBeadID": 137,
				"beadIndex": 2,
				"decadeIndex": 9,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 88,
				"messageIndex": 9,
				"loopBody": 1,
				"smallbeadPercent": 8,
				"mysteryPercent": 38
			}, {
				"rosaryBeadID": 138,
				"beadIndex": 2,
				"decadeIndex": 9,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 89,
				"messageIndex": 9,
				"loopBody": 1,
				"smallbeadPercent": 9,
				"mysteryPercent": 39
			}, {
				"rosaryBeadID": 139,
				"beadIndex": 2,
				"decadeIndex": 9,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 90,
				"messageIndex": 9,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 40
			}, {
				"rosaryBeadID": 140,
				"beadIndex": 4,
				"decadeIndex": 9,
				"mysteryIndex": 2,
				"prayerIndex": 5,
				"scriptureIndex": 0,
				"messageIndex": 9,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 40
			}, {
				"rosaryBeadID": 141,
				"beadIndex": 4,
				"decadeIndex": 9,
				"mysteryIndex": 2,
				"prayerIndex": 6,
				"scriptureIndex": 0,
				"messageIndex": 9,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 40
			}, {
				"rosaryBeadID": 142,
				"beadIndex": 3,
				"decadeIndex": 10,
				"mysteryIndex": 2,
				"prayerIndex": 0,
				"scriptureIndex": 0,
				"messageIndex": 10,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 41
			}, {
				"rosaryBeadID": 143,
				"beadIndex": 3,
				"decadeIndex": 10,
				"mysteryIndex": 2,
				"prayerIndex": 3,
				"scriptureIndex": 0,
				"messageIndex": 10,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 41
			}, {
				"rosaryBeadID": 144,
				"beadIndex": 2,
				"decadeIndex": 10,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 91,
				"messageIndex": 10,
				"loopBody": 1,
				"smallbeadPercent": 1,
				"mysteryPercent": 41
			}, {
				"rosaryBeadID": 145,
				"beadIndex": 2,
				"decadeIndex": 10,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 92,
				"messageIndex": 10,
				"loopBody": 1,
				"smallbeadPercent": 2,
				"mysteryPercent": 42
			}, {
				"rosaryBeadID": 146,
				"beadIndex": 2,
				"decadeIndex": 10,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 93,
				"messageIndex": 10,
				"loopBody": 1,
				"smallbeadPercent": 3,
				"mysteryPercent": 43
			}, {
				"rosaryBeadID": 147,
				"beadIndex": 2,
				"decadeIndex": 10,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 94,
				"messageIndex": 10,
				"loopBody": 1,
				"smallbeadPercent": 4,
				"mysteryPercent": 44
			}, {
				"rosaryBeadID": 148,
				"beadIndex": 2,
				"decadeIndex": 10,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 95,
				"messageIndex": 10,
				"loopBody": 1,
				"smallbeadPercent": 5,
				"mysteryPercent": 45
			}, {
				"rosaryBeadID": 149,
				"beadIndex": 2,
				"decadeIndex": 10,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 96,
				"messageIndex": 10,
				"loopBody": 1,
				"smallbeadPercent": 6,
				"mysteryPercent": 46
			}, {
				"rosaryBeadID": 150,
				"beadIndex": 2,
				"decadeIndex": 10,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 97,
				"messageIndex": 10,
				"loopBody": 1,
				"smallbeadPercent": 7,
				"mysteryPercent": 47
			}, {
				"rosaryBeadID": 151,
				"beadIndex": 2,
				"decadeIndex": 10,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 98,
				"messageIndex": 10,
				"loopBody": 1,
				"smallbeadPercent": 8,
				"mysteryPercent": 48
			}, {
				"rosaryBeadID": 152,
				"beadIndex": 2,
				"decadeIndex": 10,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 99,
				"messageIndex": 10,
				"loopBody": 1,
				"smallbeadPercent": 9,
				"mysteryPercent": 49
			}, {
				"rosaryBeadID": 153,
				"beadIndex": 2,
				"decadeIndex": 10,
				"mysteryIndex": 2,
				"prayerIndex": 4,
				"scriptureIndex": 100,
				"messageIndex": 10,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 50
			}, {
				"rosaryBeadID": 154,
				"beadIndex": 4,
				"decadeIndex": 10,
				"mysteryIndex": 2,
				"prayerIndex": 5,
				"scriptureIndex": 0,
				"messageIndex": 10,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 50
			}, {
				"rosaryBeadID": 155,
				"beadIndex": 4,
				"decadeIndex": 10,
				"mysteryIndex": 2,
				"prayerIndex": 6,
				"scriptureIndex": 0,
				"messageIndex": 10,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 50
			}, {
				"rosaryBeadID": 156,
				"beadIndex": 5,
				"decadeIndex": 0,
				"mysteryIndex": 5,
				"prayerIndex": 7,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 5,
				"mysteryPercent": 50
			}, {
				"rosaryBeadID": 157,
				"beadIndex": 5,
				"decadeIndex": 0,
				"mysteryIndex": 5,
				"prayerIndex": 8,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 10,
				"mysteryPercent": 50
			}, {
				"rosaryBeadID": 158,
				"beadIndex": 0,
				"decadeIndex": 0,
				"mysteryIndex": 3,
				"prayerIndex": 1,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 0,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 159,
				"beadIndex": 6,
				"decadeIndex": 0,
				"mysteryIndex": 0,
				"prayerIndex": 2,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 1,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 160,
				"beadIndex": 3,
				"decadeIndex": 0,
				"mysteryIndex": 0,
				"prayerIndex": 3,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 2,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 161,
				"beadIndex": 2,
				"decadeIndex": 0,
				"mysteryIndex": 0,
				"prayerIndex": 4,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 3,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 162,
				"beadIndex": 2,
				"decadeIndex": 0,
				"mysteryIndex": 0,
				"prayerIndex": 4,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 4,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 163,
				"beadIndex": 2,
				"decadeIndex": 0,
				"mysteryIndex": 0,
				"prayerIndex": 4,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 5,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 164,
				"beadIndex": 3,
				"decadeIndex": 0,
				"mysteryIndex": 0,
				"prayerIndex": 5,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 6,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 165,
				"beadIndex": 5,
				"decadeIndex": 11,
				"mysteryIndex": 3,
				"prayerIndex": 0,
				"scriptureIndex": 0,
				"messageIndex": 11,
				"loopBody": 0,
				"smallbeadPercent": 7,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 166,
				"beadIndex": 3,
				"decadeIndex": 11,
				"mysteryIndex": 3,
				"prayerIndex": 3,
				"scriptureIndex": 0,
				"messageIndex": 11,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 1
			}, {
				"rosaryBeadID": 167,
				"beadIndex": 2,
				"decadeIndex": 11,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 101,
				"messageIndex": 11,
				"loopBody": 1,
				"smallbeadPercent": 1,
				"mysteryPercent": 1
			}, {
				"rosaryBeadID": 168,
				"beadIndex": 2,
				"decadeIndex": 11,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 102,
				"messageIndex": 11,
				"loopBody": 1,
				"smallbeadPercent": 2,
				"mysteryPercent": 2
			}, {
				"rosaryBeadID": 169,
				"beadIndex": 2,
				"decadeIndex": 11,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 103,
				"messageIndex": 11,
				"loopBody": 1,
				"smallbeadPercent": 3,
				"mysteryPercent": 3
			}, {
				"rosaryBeadID": 170,
				"beadIndex": 2,
				"decadeIndex": 11,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 104,
				"messageIndex": 11,
				"loopBody": 1,
				"smallbeadPercent": 4,
				"mysteryPercent": 4
			}, {
				"rosaryBeadID": 171,
				"beadIndex": 2,
				"decadeIndex": 11,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 105,
				"messageIndex": 11,
				"loopBody": 1,
				"smallbeadPercent": 5,
				"mysteryPercent": 5
			}, {
				"rosaryBeadID": 172,
				"beadIndex": 2,
				"decadeIndex": 11,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 106,
				"messageIndex": 11,
				"loopBody": 1,
				"smallbeadPercent": 6,
				"mysteryPercent": 6
			}, {
				"rosaryBeadID": 173,
				"beadIndex": 2,
				"decadeIndex": 11,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 107,
				"messageIndex": 11,
				"loopBody": 1,
				"smallbeadPercent": 7,
				"mysteryPercent": 7
			}, {
				"rosaryBeadID": 174,
				"beadIndex": 2,
				"decadeIndex": 11,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 108,
				"messageIndex": 11,
				"loopBody": 1,
				"smallbeadPercent": 8,
				"mysteryPercent": 8
			}, {
				"rosaryBeadID": 175,
				"beadIndex": 2,
				"decadeIndex": 11,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 109,
				"messageIndex": 11,
				"loopBody": 1,
				"smallbeadPercent": 9,
				"mysteryPercent": 9
			}, {
				"rosaryBeadID": 176,
				"beadIndex": 2,
				"decadeIndex": 11,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 110,
				"messageIndex": 11,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 10
			}, {
				"rosaryBeadID": 177,
				"beadIndex": 4,
				"decadeIndex": 11,
				"mysteryIndex": 3,
				"prayerIndex": 5,
				"scriptureIndex": 0,
				"messageIndex": 11,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 10
			}, {
				"rosaryBeadID": 178,
				"beadIndex": 4,
				"decadeIndex": 11,
				"mysteryIndex": 3,
				"prayerIndex": 6,
				"scriptureIndex": 0,
				"messageIndex": 11,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 10
			}, {
				"rosaryBeadID": 179,
				"beadIndex": 3,
				"decadeIndex": 12,
				"mysteryIndex": 3,
				"prayerIndex": 0,
				"scriptureIndex": 0,
				"messageIndex": 12,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 11
			}, {
				"rosaryBeadID": 180,
				"beadIndex": 3,
				"decadeIndex": 12,
				"mysteryIndex": 3,
				"prayerIndex": 3,
				"scriptureIndex": 0,
				"messageIndex": 12,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 11
			}, {
				"rosaryBeadID": 181,
				"beadIndex": 2,
				"decadeIndex": 12,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 111,
				"messageIndex": 12,
				"loopBody": 1,
				"smallbeadPercent": 1,
				"mysteryPercent": 11
			}, {
				"rosaryBeadID": 182,
				"beadIndex": 2,
				"decadeIndex": 12,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 112,
				"messageIndex": 12,
				"loopBody": 1,
				"smallbeadPercent": 2,
				"mysteryPercent": 12
			}, {
				"rosaryBeadID": 183,
				"beadIndex": 2,
				"decadeIndex": 12,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 113,
				"messageIndex": 12,
				"loopBody": 1,
				"smallbeadPercent": 3,
				"mysteryPercent": 13
			}, {
				"rosaryBeadID": 184,
				"beadIndex": 2,
				"decadeIndex": 12,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 114,
				"messageIndex": 12,
				"loopBody": 1,
				"smallbeadPercent": 4,
				"mysteryPercent": 14
			}, {
				"rosaryBeadID": 185,
				"beadIndex": 2,
				"decadeIndex": 12,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 115,
				"messageIndex": 12,
				"loopBody": 1,
				"smallbeadPercent": 5,
				"mysteryPercent": 15
			}, {
				"rosaryBeadID": 186,
				"beadIndex": 2,
				"decadeIndex": 12,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 116,
				"messageIndex": 12,
				"loopBody": 1,
				"smallbeadPercent": 6,
				"mysteryPercent": 16
			}, {
				"rosaryBeadID": 187,
				"beadIndex": 2,
				"decadeIndex": 12,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 117,
				"messageIndex": 12,
				"loopBody": 1,
				"smallbeadPercent": 7,
				"mysteryPercent": 17
			}, {
				"rosaryBeadID": 188,
				"beadIndex": 2,
				"decadeIndex": 12,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 118,
				"messageIndex": 12,
				"loopBody": 1,
				"smallbeadPercent": 8,
				"mysteryPercent": 18
			}, {
				"rosaryBeadID": 189,
				"beadIndex": 2,
				"decadeIndex": 12,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 119,
				"messageIndex": 12,
				"loopBody": 1,
				"smallbeadPercent": 9,
				"mysteryPercent": 19
			}, {
				"rosaryBeadID": 190,
				"beadIndex": 2,
				"decadeIndex": 12,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 120,
				"messageIndex": 12,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 20
			}, {
				"rosaryBeadID": 191,
				"beadIndex": 4,
				"decadeIndex": 12,
				"mysteryIndex": 3,
				"prayerIndex": 5,
				"scriptureIndex": 0,
				"messageIndex": 12,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 20
			}, {
				"rosaryBeadID": 192,
				"beadIndex": 4,
				"decadeIndex": 12,
				"mysteryIndex": 3,
				"prayerIndex": 6,
				"scriptureIndex": 0,
				"messageIndex": 12,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 20
			}, {
				"rosaryBeadID": 193,
				"beadIndex": 3,
				"decadeIndex": 13,
				"mysteryIndex": 3,
				"prayerIndex": 0,
				"scriptureIndex": 0,
				"messageIndex": 13,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 21
			}, {
				"rosaryBeadID": 194,
				"beadIndex": 3,
				"decadeIndex": 13,
				"mysteryIndex": 3,
				"prayerIndex": 3,
				"scriptureIndex": 0,
				"messageIndex": 13,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 21
			}, {
				"rosaryBeadID": 195,
				"beadIndex": 2,
				"decadeIndex": 13,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 121,
				"messageIndex": 13,
				"loopBody": 1,
				"smallbeadPercent": 1,
				"mysteryPercent": 21
			}, {
				"rosaryBeadID": 196,
				"beadIndex": 2,
				"decadeIndex": 13,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 122,
				"messageIndex": 13,
				"loopBody": 1,
				"smallbeadPercent": 2,
				"mysteryPercent": 22
			}, {
				"rosaryBeadID": 197,
				"beadIndex": 2,
				"decadeIndex": 13,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 123,
				"messageIndex": 13,
				"loopBody": 1,
				"smallbeadPercent": 3,
				"mysteryPercent": 23
			}, {
				"rosaryBeadID": 198,
				"beadIndex": 2,
				"decadeIndex": 13,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 124,
				"messageIndex": 13,
				"loopBody": 1,
				"smallbeadPercent": 4,
				"mysteryPercent": 24
			}, {
				"rosaryBeadID": 199,
				"beadIndex": 2,
				"decadeIndex": 13,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 125,
				"messageIndex": 13,
				"loopBody": 1,
				"smallbeadPercent": 5,
				"mysteryPercent": 25
			}, {
				"rosaryBeadID": 200,
				"beadIndex": 2,
				"decadeIndex": 13,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 126,
				"messageIndex": 13,
				"loopBody": 1,
				"smallbeadPercent": 6,
				"mysteryPercent": 26
			}, {
				"rosaryBeadID": 201,
				"beadIndex": 2,
				"decadeIndex": 13,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 127,
				"messageIndex": 13,
				"loopBody": 1,
				"smallbeadPercent": 7,
				"mysteryPercent": 27
			}, {
				"rosaryBeadID": 202,
				"beadIndex": 2,
				"decadeIndex": 13,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 128,
				"messageIndex": 13,
				"loopBody": 1,
				"smallbeadPercent": 8,
				"mysteryPercent": 28
			}, {
				"rosaryBeadID": 203,
				"beadIndex": 2,
				"decadeIndex": 13,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 129,
				"messageIndex": 13,
				"loopBody": 1,
				"smallbeadPercent": 9,
				"mysteryPercent": 29
			}, {
				"rosaryBeadID": 204,
				"beadIndex": 2,
				"decadeIndex": 13,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 130,
				"messageIndex": 13,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 30
			}, {
				"rosaryBeadID": 205,
				"beadIndex": 4,
				"decadeIndex": 13,
				"mysteryIndex": 3,
				"prayerIndex": 5,
				"scriptureIndex": 0,
				"messageIndex": 13,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 30
			}, {
				"rosaryBeadID": 206,
				"beadIndex": 4,
				"decadeIndex": 13,
				"mysteryIndex": 3,
				"prayerIndex": 6,
				"scriptureIndex": 0,
				"messageIndex": 13,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 30
			}, {
				"rosaryBeadID": 207,
				"beadIndex": 3,
				"decadeIndex": 14,
				"mysteryIndex": 3,
				"prayerIndex": 0,
				"scriptureIndex": 0,
				"messageIndex": 14,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 31
			}, {
				"rosaryBeadID": 208,
				"beadIndex": 3,
				"decadeIndex": 14,
				"mysteryIndex": 3,
				"prayerIndex": 3,
				"scriptureIndex": 0,
				"messageIndex": 14,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 31
			}, {
				"rosaryBeadID": 209,
				"beadIndex": 2,
				"decadeIndex": 14,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 131,
				"messageIndex": 14,
				"loopBody": 1,
				"smallbeadPercent": 1,
				"mysteryPercent": 31
			}, {
				"rosaryBeadID": 210,
				"beadIndex": 2,
				"decadeIndex": 14,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 132,
				"messageIndex": 14,
				"loopBody": 1,
				"smallbeadPercent": 2,
				"mysteryPercent": 32
			}, {
				"rosaryBeadID": 211,
				"beadIndex": 2,
				"decadeIndex": 14,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 133,
				"messageIndex": 14,
				"loopBody": 1,
				"smallbeadPercent": 3,
				"mysteryPercent": 33
			}, {
				"rosaryBeadID": 212,
				"beadIndex": 2,
				"decadeIndex": 14,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 134,
				"messageIndex": 14,
				"loopBody": 1,
				"smallbeadPercent": 4,
				"mysteryPercent": 34
			}, {
				"rosaryBeadID": 213,
				"beadIndex": 2,
				"decadeIndex": 14,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 135,
				"messageIndex": 14,
				"loopBody": 1,
				"smallbeadPercent": 5,
				"mysteryPercent": 35
			}, {
				"rosaryBeadID": 214,
				"beadIndex": 2,
				"decadeIndex": 14,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 136,
				"messageIndex": 14,
				"loopBody": 1,
				"smallbeadPercent": 6,
				"mysteryPercent": 36
			}, {
				"rosaryBeadID": 215,
				"beadIndex": 2,
				"decadeIndex": 14,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 137,
				"messageIndex": 14,
				"loopBody": 1,
				"smallbeadPercent": 7,
				"mysteryPercent": 37
			}, {
				"rosaryBeadID": 216,
				"beadIndex": 2,
				"decadeIndex": 14,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 138,
				"messageIndex": 14,
				"loopBody": 1,
				"smallbeadPercent": 8,
				"mysteryPercent": 38
			}, {
				"rosaryBeadID": 217,
				"beadIndex": 2,
				"decadeIndex": 14,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 139,
				"messageIndex": 14,
				"loopBody": 1,
				"smallbeadPercent": 9,
				"mysteryPercent": 39
			}, {
				"rosaryBeadID": 218,
				"beadIndex": 2,
				"decadeIndex": 14,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 140,
				"messageIndex": 14,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 40
			}, {
				"rosaryBeadID": 219,
				"beadIndex": 4,
				"decadeIndex": 14,
				"mysteryIndex": 3,
				"prayerIndex": 5,
				"scriptureIndex": 0,
				"messageIndex": 14,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 40
			}, {
				"rosaryBeadID": 220,
				"beadIndex": 4,
				"decadeIndex": 14,
				"mysteryIndex": 3,
				"prayerIndex": 6,
				"scriptureIndex": 0,
				"messageIndex": 14,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 40
			}, {
				"rosaryBeadID": 221,
				"beadIndex": 3,
				"decadeIndex": 15,
				"mysteryIndex": 3,
				"prayerIndex": 0,
				"scriptureIndex": 0,
				"messageIndex": 15,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 41
			}, {
				"rosaryBeadID": 222,
				"beadIndex": 3,
				"decadeIndex": 15,
				"mysteryIndex": 3,
				"prayerIndex": 3,
				"scriptureIndex": 0,
				"messageIndex": 15,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 41
			}, {
				"rosaryBeadID": 223,
				"beadIndex": 2,
				"decadeIndex": 15,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 141,
				"messageIndex": 15,
				"loopBody": 1,
				"smallbeadPercent": 1,
				"mysteryPercent": 41
			}, {
				"rosaryBeadID": 224,
				"beadIndex": 2,
				"decadeIndex": 15,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 142,
				"messageIndex": 15,
				"loopBody": 1,
				"smallbeadPercent": 2,
				"mysteryPercent": 42
			}, {
				"rosaryBeadID": 225,
				"beadIndex": 2,
				"decadeIndex": 15,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 143,
				"messageIndex": 15,
				"loopBody": 1,
				"smallbeadPercent": 3,
				"mysteryPercent": 43
			}, {
				"rosaryBeadID": 226,
				"beadIndex": 2,
				"decadeIndex": 15,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 144,
				"messageIndex": 15,
				"loopBody": 1,
				"smallbeadPercent": 4,
				"mysteryPercent": 44
			}, {
				"rosaryBeadID": 227,
				"beadIndex": 2,
				"decadeIndex": 15,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 145,
				"messageIndex": 15,
				"loopBody": 1,
				"smallbeadPercent": 5,
				"mysteryPercent": 45
			}, {
				"rosaryBeadID": 228,
				"beadIndex": 2,
				"decadeIndex": 15,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 146,
				"messageIndex": 15,
				"loopBody": 1,
				"smallbeadPercent": 6,
				"mysteryPercent": 46
			}, {
				"rosaryBeadID": 229,
				"beadIndex": 2,
				"decadeIndex": 15,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 147,
				"messageIndex": 15,
				"loopBody": 1,
				"smallbeadPercent": 7,
				"mysteryPercent": 47
			}, {
				"rosaryBeadID": 230,
				"beadIndex": 2,
				"decadeIndex": 15,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 148,
				"messageIndex": 15,
				"loopBody": 1,
				"smallbeadPercent": 8,
				"mysteryPercent": 48
			}, {
				"rosaryBeadID": 231,
				"beadIndex": 2,
				"decadeIndex": 15,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 149,
				"messageIndex": 15,
				"loopBody": 1,
				"smallbeadPercent": 9,
				"mysteryPercent": 49
			}, {
				"rosaryBeadID": 232,
				"beadIndex": 2,
				"decadeIndex": 15,
				"mysteryIndex": 3,
				"prayerIndex": 4,
				"scriptureIndex": 150,
				"messageIndex": 15,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 50
			}, {
				"rosaryBeadID": 233,
				"beadIndex": 4,
				"decadeIndex": 15,
				"mysteryIndex": 3,
				"prayerIndex": 5,
				"scriptureIndex": 0,
				"messageIndex": 15,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 50
			}, {
				"rosaryBeadID": 234,
				"beadIndex": 4,
				"decadeIndex": 15,
				"mysteryIndex": 3,
				"prayerIndex": 6,
				"scriptureIndex": 0,
				"messageIndex": 15,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 50
			}, {
				"rosaryBeadID": 235,
				"beadIndex": 5,
				"decadeIndex": 0,
				"mysteryIndex": 5,
				"prayerIndex": 7,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 5,
				"mysteryPercent": 50
			}, {
				"rosaryBeadID": 236,
				"beadIndex": 5,
				"decadeIndex": 0,
				"mysteryIndex": 5,
				"prayerIndex": 8,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 10,
				"mysteryPercent": 50
			}, {
				"rosaryBeadID": 237,
				"beadIndex": 0,
				"decadeIndex": 0,
				"mysteryIndex": 4,
				"prayerIndex": 1,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 0,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 238,
				"beadIndex": 6,
				"decadeIndex": 0,
				"mysteryIndex": 0,
				"prayerIndex": 2,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 1,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 239,
				"beadIndex": 3,
				"decadeIndex": 0,
				"mysteryIndex": 0,
				"prayerIndex": 3,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 2,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 240,
				"beadIndex": 2,
				"decadeIndex": 0,
				"mysteryIndex": 0,
				"prayerIndex": 4,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 3,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 241,
				"beadIndex": 2,
				"decadeIndex": 0,
				"mysteryIndex": 0,
				"prayerIndex": 4,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 4,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 242,
				"beadIndex": 2,
				"decadeIndex": 0,
				"mysteryIndex": 0,
				"prayerIndex": 4,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 5,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 243,
				"beadIndex": 3,
				"decadeIndex": 0,
				"mysteryIndex": 0,
				"prayerIndex": 5,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 6,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 244,
				"beadIndex": 5,
				"decadeIndex": 16,
				"mysteryIndex": 4,
				"prayerIndex": 0,
				"scriptureIndex": 0,
				"messageIndex": 16,
				"loopBody": 0,
				"smallbeadPercent": 7,
				"mysteryPercent": 0
			}, {
				"rosaryBeadID": 245,
				"beadIndex": 3,
				"decadeIndex": 16,
				"mysteryIndex": 4,
				"prayerIndex": 3,
				"scriptureIndex": 0,
				"messageIndex": 16,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 1
			}, {
				"rosaryBeadID": 246,
				"beadIndex": 2,
				"decadeIndex": 16,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 151,
				"messageIndex": 16,
				"loopBody": 1,
				"smallbeadPercent": 1,
				"mysteryPercent": 1
			}, {
				"rosaryBeadID": 247,
				"beadIndex": 2,
				"decadeIndex": 16,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 152,
				"messageIndex": 16,
				"loopBody": 1,
				"smallbeadPercent": 2,
				"mysteryPercent": 2
			}, {
				"rosaryBeadID": 248,
				"beadIndex": 2,
				"decadeIndex": 16,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 153,
				"messageIndex": 16,
				"loopBody": 1,
				"smallbeadPercent": 3,
				"mysteryPercent": 3
			}, {
				"rosaryBeadID": 249,
				"beadIndex": 2,
				"decadeIndex": 16,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 154,
				"messageIndex": 16,
				"loopBody": 1,
				"smallbeadPercent": 4,
				"mysteryPercent": 4
			}, {
				"rosaryBeadID": 250,
				"beadIndex": 2,
				"decadeIndex": 16,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 155,
				"messageIndex": 16,
				"loopBody": 1,
				"smallbeadPercent": 5,
				"mysteryPercent": 5
			}, {
				"rosaryBeadID": 251,
				"beadIndex": 2,
				"decadeIndex": 16,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 156,
				"messageIndex": 16,
				"loopBody": 1,
				"smallbeadPercent": 6,
				"mysteryPercent": 6
			}, {
				"rosaryBeadID": 252,
				"beadIndex": 2,
				"decadeIndex": 16,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 157,
				"messageIndex": 16,
				"loopBody": 1,
				"smallbeadPercent": 7,
				"mysteryPercent": 7
			}, {
				"rosaryBeadID": 253,
				"beadIndex": 2,
				"decadeIndex": 16,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 158,
				"messageIndex": 16,
				"loopBody": 1,
				"smallbeadPercent": 8,
				"mysteryPercent": 8
			}, {
				"rosaryBeadID": 254,
				"beadIndex": 2,
				"decadeIndex": 16,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 159,
				"messageIndex": 16,
				"loopBody": 1,
				"smallbeadPercent": 9,
				"mysteryPercent": 9
			}, {
				"rosaryBeadID": 255,
				"beadIndex": 2,
				"decadeIndex": 16,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 160,
				"messageIndex": 16,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 10
			}, {
				"rosaryBeadID": 256,
				"beadIndex": 4,
				"decadeIndex": 16,
				"mysteryIndex": 4,
				"prayerIndex": 5,
				"scriptureIndex": 0,
				"messageIndex": 16,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 10
			}, {
				"rosaryBeadID": 257,
				"beadIndex": 4,
				"decadeIndex": 16,
				"mysteryIndex": 4,
				"prayerIndex": 6,
				"scriptureIndex": 0,
				"messageIndex": 16,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 10
			}, {
				"rosaryBeadID": 258,
				"beadIndex": 3,
				"decadeIndex": 17,
				"mysteryIndex": 4,
				"prayerIndex": 0,
				"scriptureIndex": 0,
				"messageIndex": 17,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 11
			}, {
				"rosaryBeadID": 259,
				"beadIndex": 3,
				"decadeIndex": 17,
				"mysteryIndex": 4,
				"prayerIndex": 3,
				"scriptureIndex": 0,
				"messageIndex": 17,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 11
			}, {
				"rosaryBeadID": 260,
				"beadIndex": 2,
				"decadeIndex": 17,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 161,
				"messageIndex": 17,
				"loopBody": 1,
				"smallbeadPercent": 1,
				"mysteryPercent": 11
			}, {
				"rosaryBeadID": 261,
				"beadIndex": 2,
				"decadeIndex": 17,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 162,
				"messageIndex": 17,
				"loopBody": 1,
				"smallbeadPercent": 2,
				"mysteryPercent": 12
			}, {
				"rosaryBeadID": 262,
				"beadIndex": 2,
				"decadeIndex": 17,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 163,
				"messageIndex": 17,
				"loopBody": 1,
				"smallbeadPercent": 3,
				"mysteryPercent": 13
			}, {
				"rosaryBeadID": 263,
				"beadIndex": 2,
				"decadeIndex": 17,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 164,
				"messageIndex": 17,
				"loopBody": 1,
				"smallbeadPercent": 4,
				"mysteryPercent": 14
			}, {
				"rosaryBeadID": 264,
				"beadIndex": 2,
				"decadeIndex": 17,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 165,
				"messageIndex": 17,
				"loopBody": 1,
				"smallbeadPercent": 5,
				"mysteryPercent": 15
			}, {
				"rosaryBeadID": 265,
				"beadIndex": 2,
				"decadeIndex": 17,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 166,
				"messageIndex": 17,
				"loopBody": 1,
				"smallbeadPercent": 6,
				"mysteryPercent": 16
			}, {
				"rosaryBeadID": 266,
				"beadIndex": 2,
				"decadeIndex": 17,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 167,
				"messageIndex": 17,
				"loopBody": 1,
				"smallbeadPercent": 7,
				"mysteryPercent": 17
			}, {
				"rosaryBeadID": 267,
				"beadIndex": 2,
				"decadeIndex": 17,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 168,
				"messageIndex": 17,
				"loopBody": 1,
				"smallbeadPercent": 8,
				"mysteryPercent": 18
			}, {
				"rosaryBeadID": 268,
				"beadIndex": 2,
				"decadeIndex": 17,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 169,
				"messageIndex": 17,
				"loopBody": 1,
				"smallbeadPercent": 9,
				"mysteryPercent": 19
			}, {
				"rosaryBeadID": 269,
				"beadIndex": 2,
				"decadeIndex": 17,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 170,
				"messageIndex": 17,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 20
			}, {
				"rosaryBeadID": 270,
				"beadIndex": 4,
				"decadeIndex": 17,
				"mysteryIndex": 4,
				"prayerIndex": 5,
				"scriptureIndex": 0,
				"messageIndex": 17,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 20
			}, {
				"rosaryBeadID": 271,
				"beadIndex": 4,
				"decadeIndex": 17,
				"mysteryIndex": 4,
				"prayerIndex": 6,
				"scriptureIndex": 0,
				"messageIndex": 17,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 20
			}, {
				"rosaryBeadID": 272,
				"beadIndex": 3,
				"decadeIndex": 18,
				"mysteryIndex": 4,
				"prayerIndex": 0,
				"scriptureIndex": 0,
				"messageIndex": 18,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 21
			}, {
				"rosaryBeadID": 273,
				"beadIndex": 3,
				"decadeIndex": 18,
				"mysteryIndex": 4,
				"prayerIndex": 3,
				"scriptureIndex": 0,
				"messageIndex": 18,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 21
			}, {
				"rosaryBeadID": 274,
				"beadIndex": 2,
				"decadeIndex": 18,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 171,
				"messageIndex": 18,
				"loopBody": 1,
				"smallbeadPercent": 1,
				"mysteryPercent": 21
			}, {
				"rosaryBeadID": 275,
				"beadIndex": 2,
				"decadeIndex": 18,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 172,
				"messageIndex": 18,
				"loopBody": 1,
				"smallbeadPercent": 2,
				"mysteryPercent": 22
			}, {
				"rosaryBeadID": 276,
				"beadIndex": 2,
				"decadeIndex": 18,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 173,
				"messageIndex": 18,
				"loopBody": 1,
				"smallbeadPercent": 3,
				"mysteryPercent": 23
			}, {
				"rosaryBeadID": 277,
				"beadIndex": 2,
				"decadeIndex": 18,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 174,
				"messageIndex": 18,
				"loopBody": 1,
				"smallbeadPercent": 4,
				"mysteryPercent": 24
			}, {
				"rosaryBeadID": 278,
				"beadIndex": 2,
				"decadeIndex": 18,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 175,
				"messageIndex": 18,
				"loopBody": 1,
				"smallbeadPercent": 5,
				"mysteryPercent": 25
			}, {
				"rosaryBeadID": 279,
				"beadIndex": 2,
				"decadeIndex": 18,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 176,
				"messageIndex": 18,
				"loopBody": 1,
				"smallbeadPercent": 6,
				"mysteryPercent": 26
			}, {
				"rosaryBeadID": 280,
				"beadIndex": 2,
				"decadeIndex": 18,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 177,
				"messageIndex": 18,
				"loopBody": 1,
				"smallbeadPercent": 7,
				"mysteryPercent": 27
			}, {
				"rosaryBeadID": 281,
				"beadIndex": 2,
				"decadeIndex": 18,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 178,
				"messageIndex": 18,
				"loopBody": 1,
				"smallbeadPercent": 8,
				"mysteryPercent": 28
			}, {
				"rosaryBeadID": 282,
				"beadIndex": 2,
				"decadeIndex": 18,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 179,
				"messageIndex": 18,
				"loopBody": 1,
				"smallbeadPercent": 9,
				"mysteryPercent": 29
			}, {
				"rosaryBeadID": 283,
				"beadIndex": 2,
				"decadeIndex": 18,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 180,
				"messageIndex": 18,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 30
			}, {
				"rosaryBeadID": 284,
				"beadIndex": 4,
				"decadeIndex": 18,
				"mysteryIndex": 4,
				"prayerIndex": 5,
				"scriptureIndex": 0,
				"messageIndex": 18,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 30
			}, {
				"rosaryBeadID": 285,
				"beadIndex": 4,
				"decadeIndex": 18,
				"mysteryIndex": 4,
				"prayerIndex": 6,
				"scriptureIndex": 0,
				"messageIndex": 18,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 30
			}, {
				"rosaryBeadID": 286,
				"beadIndex": 3,
				"decadeIndex": 19,
				"mysteryIndex": 4,
				"prayerIndex": 0,
				"scriptureIndex": 0,
				"messageIndex": 19,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 31
			}, {
				"rosaryBeadID": 287,
				"beadIndex": 3,
				"decadeIndex": 19,
				"mysteryIndex": 4,
				"prayerIndex": 3,
				"scriptureIndex": 0,
				"messageIndex": 19,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 31
			}, {
				"rosaryBeadID": 288,
				"beadIndex": 2,
				"decadeIndex": 19,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 181,
				"messageIndex": 19,
				"loopBody": 1,
				"smallbeadPercent": 1,
				"mysteryPercent": 31
			}, {
				"rosaryBeadID": 289,
				"beadIndex": 2,
				"decadeIndex": 19,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 182,
				"messageIndex": 19,
				"loopBody": 1,
				"smallbeadPercent": 2,
				"mysteryPercent": 32
			}, {
				"rosaryBeadID": 290,
				"beadIndex": 2,
				"decadeIndex": 19,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 183,
				"messageIndex": 19,
				"loopBody": 1,
				"smallbeadPercent": 3,
				"mysteryPercent": 33
			}, {
				"rosaryBeadID": 291,
				"beadIndex": 2,
				"decadeIndex": 19,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 184,
				"messageIndex": 19,
				"loopBody": 1,
				"smallbeadPercent": 4,
				"mysteryPercent": 34
			}, {
				"rosaryBeadID": 292,
				"beadIndex": 2,
				"decadeIndex": 19,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 185,
				"messageIndex": 19,
				"loopBody": 1,
				"smallbeadPercent": 5,
				"mysteryPercent": 35
			}, {
				"rosaryBeadID": 293,
				"beadIndex": 2,
				"decadeIndex": 19,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 186,
				"messageIndex": 19,
				"loopBody": 1,
				"smallbeadPercent": 6,
				"mysteryPercent": 36
			}, {
				"rosaryBeadID": 294,
				"beadIndex": 2,
				"decadeIndex": 19,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 187,
				"messageIndex": 19,
				"loopBody": 1,
				"smallbeadPercent": 7,
				"mysteryPercent": 37
			}, {
				"rosaryBeadID": 295,
				"beadIndex": 2,
				"decadeIndex": 19,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 188,
				"messageIndex": 19,
				"loopBody": 1,
				"smallbeadPercent": 8,
				"mysteryPercent": 38
			}, {
				"rosaryBeadID": 296,
				"beadIndex": 2,
				"decadeIndex": 19,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 189,
				"messageIndex": 19,
				"loopBody": 1,
				"smallbeadPercent": 9,
				"mysteryPercent": 39
			}, {
				"rosaryBeadID": 297,
				"beadIndex": 2,
				"decadeIndex": 19,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 190,
				"messageIndex": 19,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 40
			}, {
				"rosaryBeadID": 298,
				"beadIndex": 4,
				"decadeIndex": 19,
				"mysteryIndex": 4,
				"prayerIndex": 5,
				"scriptureIndex": 0,
				"messageIndex": 19,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 40
			}, {
				"rosaryBeadID": 299,
				"beadIndex": 4,
				"decadeIndex": 19,
				"mysteryIndex": 4,
				"prayerIndex": 6,
				"scriptureIndex": 0,
				"messageIndex": 19,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 40
			}, {
				"rosaryBeadID": 300,
				"beadIndex": 3,
				"decadeIndex": 20,
				"mysteryIndex": 4,
				"prayerIndex": 0,
				"scriptureIndex": 0,
				"messageIndex": 20,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 41
			}, {
				"rosaryBeadID": 301,
				"beadIndex": 3,
				"decadeIndex": 20,
				"mysteryIndex": 4,
				"prayerIndex": 3,
				"scriptureIndex": 0,
				"messageIndex": 20,
				"loopBody": 1,
				"smallbeadPercent": 0,
				"mysteryPercent": 41
			}, {
				"rosaryBeadID": 302,
				"beadIndex": 2,
				"decadeIndex": 20,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 191,
				"messageIndex": 20,
				"loopBody": 1,
				"smallbeadPercent": 1,
				"mysteryPercent": 41
			}, {
				"rosaryBeadID": 303,
				"beadIndex": 2,
				"decadeIndex": 20,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 192,
				"messageIndex": 20,
				"loopBody": 1,
				"smallbeadPercent": 2,
				"mysteryPercent": 42
			}, {
				"rosaryBeadID": 304,
				"beadIndex": 2,
				"decadeIndex": 20,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 193,
				"messageIndex": 20,
				"loopBody": 1,
				"smallbeadPercent": 3,
				"mysteryPercent": 43
			}, {
				"rosaryBeadID": 305,
				"beadIndex": 2,
				"decadeIndex": 20,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 194,
				"messageIndex": 20,
				"loopBody": 1,
				"smallbeadPercent": 4,
				"mysteryPercent": 44
			}, {
				"rosaryBeadID": 306,
				"beadIndex": 2,
				"decadeIndex": 20,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 195,
				"messageIndex": 20,
				"loopBody": 1,
				"smallbeadPercent": 5,
				"mysteryPercent": 45
			}, {
				"rosaryBeadID": 307,
				"beadIndex": 2,
				"decadeIndex": 20,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 196,
				"messageIndex": 20,
				"loopBody": 1,
				"smallbeadPercent": 6,
				"mysteryPercent": 46
			}, {
				"rosaryBeadID": 308,
				"beadIndex": 2,
				"decadeIndex": 20,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 197,
				"messageIndex": 20,
				"loopBody": 1,
				"smallbeadPercent": 7,
				"mysteryPercent": 47
			}, {
				"rosaryBeadID": 309,
				"beadIndex": 2,
				"decadeIndex": 20,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 198,
				"messageIndex": 20,
				"loopBody": 1,
				"smallbeadPercent": 8,
				"mysteryPercent": 48
			}, {
				"rosaryBeadID": 310,
				"beadIndex": 2,
				"decadeIndex": 20,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 199,
				"messageIndex": 20,
				"loopBody": 1,
				"smallbeadPercent": 9,
				"mysteryPercent": 49
			}, {
				"rosaryBeadID": 311,
				"beadIndex": 2,
				"decadeIndex": 20,
				"mysteryIndex": 4,
				"prayerIndex": 4,
				"scriptureIndex": 200,
				"messageIndex": 20,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 50
			}, {
				"rosaryBeadID": 312,
				"beadIndex": 4,
				"decadeIndex": 20,
				"mysteryIndex": 4,
				"prayerIndex": 5,
				"scriptureIndex": 0,
				"messageIndex": 20,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 50
			}, {
				"rosaryBeadID": 313,
				"beadIndex": 4,
				"decadeIndex": 20,
				"mysteryIndex": 4,
				"prayerIndex": 6,
				"scriptureIndex": 0,
				"messageIndex": 20,
				"loopBody": 1,
				"smallbeadPercent": 10,
				"mysteryPercent": 50
			}, {
				"rosaryBeadID": 314,
				"beadIndex": 5,
				"decadeIndex": 0,
				"mysteryIndex": 5,
				"prayerIndex": 7,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 5,
				"mysteryPercent": 50
			}, {
				"rosaryBeadID": 315,
				"beadIndex": 5,
				"decadeIndex": 0,
				"mysteryIndex": 5,
				"prayerIndex": 8,
				"scriptureIndex": 0,
				"messageIndex": 0,
				"loopBody": 0,
				"smallbeadPercent": 10,
				"mysteryPercent": 50
			}
		],
		"bead": [
			{
				"beadID": 0,
				"beadType": ""
			}, {
				"beadID": 1,
				"beadType": "string space"
			}, {
				"beadID": 2,
				"beadType": "small bead"
			}, {
				"beadID": 3,
				"beadType": "big bead"
			}, {
				"beadID": 4,
				"beadType": "bead space"
			}, {
				"beadID": 5,
				"beadType": "icon"
			}, {
				"beadID": 6,
				"beadType": "crusifix"
			}
		],
		"decade": [
	        {
	            "decadeID": 0,
	            "mysteryIndex": 0,
	            "decadeNo": 0,
	            "decadeName": "",
				"decadeInfo": "spiritual preparation",
				"infoRefference": ""
	        },
	        {
	            "decadeID": 1,
	            "mysteryIndex": 1,
	            "decadeNo": 1,
	            "decadeName": "The First Joyful Mystery: The Annunciation",
				"decadeInfo": "<p>Mary's humility is at the heart of the meditations on the Annunciation. Because Mary humbled herself God exalted her by choosing her to be the Mother of His Son. If you are to make progress in your spiritual life and your relationship with those you love, you must learn to imitate Mary's humility.</p>",
				"infoRefference": "<a href='http://www.how-to-pray-the-rosary-everyday.com/meditations-on-the-rosary.html' target='_blank'>link</a>"
	        },
	        {
	            "decadeID": 2,
	            "mysteryIndex": 2,
	            "decadeNo": 2,
	            "decadeName": "The Second Joyful Mystery: The Visitation",
				"decadeInfo": "<p>In this mystery Mary sets the example of neighborly love. Immediately after the angel told Mary she would be the Mother of Jesus, she went to help her cousin who was also expecting a baby. Mary's response to this great news was to disregard her own needs and share her joy with Elizabeth. You too must share your blessings and joys with those you love. You can start by sharing the Rosary with them.</p>",
				"infoRefference": "<a href='http://www.how-to-pray-the-rosary-everyday.com/meditations-on-the-rosary.html' target='_blank'>link</a>"
	        },
	        {
	            "decadeID": 3,
	            "mysteryIndex": 4,
	            "decadeNo": 3,
	            "decadeName": "The Third Joyful Mystery: The Nativity",
				"decadeInfo": "<p>While Mary and Joseph were in Bethlehem, no one would give them a comfortable place to stay. Jesus had to be born in a stable. Would you have invited them into your home? Have you made room for them in your heart and room for Jesus in your life? The best way to start is by making room for the Rosary in your day.</p>",
				"infoRefference": "<a href='http://www.how-to-pray-the-rosary-everyday.com/meditations-on-the-rosary.html' target='_blank'>link</a>"
	        },
	        {
	            "decadeID": 4,
	            "mysteryIndex": 4,
	            "decadeNo": 4,
	            "decadeName": "The Fourth Joyful Mystery: The Presentation of Jesus at the Temple",
				"decadeInfo": "This mystery shows the importance of being faithful to your duties. Keep your religious obligations without delay, just as Mary and Joseph did when they took the baby Jesus to the temple to offer Him to God as was the Jewish law. Learn to embrace your duties and fulfill them faithfully.</p>",
				"infoRefference": "<a href='http://www.how-to-pray-the-rosary-everyday.com/meditations-on-the-rosary.html' target='_blank'>link</a>"
	        },
	        {
	            "decadeID": 5,
	            "mysteryIndex": 5,
	            "decadeNo": 5,
	            "decadeName": "The Fifth Joyful Mystery: The Finding of Jesus at the Temple",
				"decadeInfo": "<p>Jesus, Mary and Joseph went to Jerusalem in observance of a religious celebration. This mystery teaches your family to live, work and pray together. Praying a family Rosary every day is a sure way of accomplishing this goal.</p>",
				"infoRefference": "<a href='http://www.how-to-pray-the-rosary-everyday.com/meditations-on-the-rosary.html' target='_blank'>link</a>"
	        },
	        {
	            "decadeID": 6,
	            "mysteryIndex": 1,
	            "decadeNo": 1,
	            "decadeName": "First Luminous Mystery: The Baptism in the Jordan",
				"decadeInfo": "<p>When Jesus was baptized He was instituting the sacrament of baptism. This sacrament washes away original sin from your soul and makes you a brother or sister of Jesus and a child of God. As a child of God you are an heir to heaven. To receive heaven as your reward you must make your life a reflection of Jesus' the way Mary did. To accomplish this you must study their lives.</p>",
				"infoRefference": "<a href='http://www.how-to-pray-the-rosary-everyday.com/meditations-on-the-rosary.html' target='_blank'>link</a>"
	        },
	        {
	            "decadeID": 7,
	            "mysteryIndex": 2,
	            "decadeNo": 2,
	            "decadeName": "Second Luminous Mystery: The wedding at Cana, when Christ manifested himself",
				"decadeInfo": "<p>Mary was not only present at Jesus' first miracle at the wedding feast at Cana; He preformed it at her request. Let this be a lesson to you. Mary is the perfect advocate and mother to you because Jesus fulfills every one of Mary's requests. Bring all your worries and concerns to her and she will present them to Jesus her Son on your behalf.</p>",
				"infoRefference": "<a href='http://www.how-to-pray-the-rosary-everyday.com/meditations-on-the-rosary.html' target='_blank'>link</a>"
	        },
	        {
	            "decadeID": 8,
	            "mysteryIndex": 3,
	            "decadeNo": 3,
	            "decadeName": "Third Luminous Mystery: The Proclamation of the Kingdom",
				"decadeInfo": "<p>This mystery which sets Jesus up as King of not only your heart but also of the entire world, begs you to be courageous enough to be a true follower of Jesus in both your personal and public life.</p>",
				"infoRefference": "<a href='http://www.how-to-pray-the-rosary-everyday.com/meditations-on-the-rosary.html' target='_blank'>link</a>"
	        },
	        {
	            "decadeID": 9,
	            "mysteryIndex": 4,
	            "decadeNo": 4,
	            "decadeName": "Fourth Luminous Mystery: The Transfiguration of our Lord",
				"decadeInfo": "<p>This mystery recalls Jesus being transfigured into a glorious state on Mount Tabor. It is a foreshadowing of the glory to come. Let it bring to your mind the glory that awaits you when you pass from this life. You must desire holiness, and you must learn to accept and make the necessary sacrifices to attain it. Remember, without the cross, there is no crown.</p>",
				"infoRefference": "<a href='http://www.how-to-pray-the-rosary-everyday.com/meditations-on-the-rosary.html' target='_blank'>link</a>"
	        },
	        {
	            "decadeID": 10,
	            "mysteryIndex": 5,
	            "decadeNo": 5,
	            "decadeName": "Fifth Luminous Mystery: The Last Supper, when our Lord gave us the Eucharist",
				"decadeInfo": "<p>At the Last Supper, Jesus instituted the Eucharist. When you receive Jesus in the Holy Eucharist a union between Him and you is created. This bond creates in you a holy life that is filled with peace because Jesus is the source of all holiness and the giver of all graces.</p>",
				"infoRefference": "<a href='http://www.how-to-pray-the-rosary-everyday.com/meditations-on-the-rosary.html' target='_blank'>link</a>"
	        },
	        {
	            "decadeID": 11,
	            "mysteryIndex": 1,
	            "decadeNo": 1,
	            "decadeName": "First Sorrowful Mystery: The Agony in the Garden",
				"decadeInfo": "<p>Jesus experienced great agony and showed you the way to confront your own sufferings. You must imitate Jesus and turn to God in prayer at these times. When you pray remember to be open to God's will for you even as you ask Him to relieve your sufferings just as Jesus did at Gethsemane.</p>",
				"infoRefference": "<a href='http://www.how-to-pray-the-rosary-everyday.com/meditations-on-the-rosary.html' target='_blank'>link</a>"
	        },
	        {
	            "decadeID": 12,
	            "mysteryIndex": 2,
	            "decadeNo": 2,
	            "decadeName": "Second Sorrowful Mystery: The Scourging At The Pillar",
				"decadeInfo": "<p>The whips that scourged Jesus were caused by our sins. With Jesus' scourging in mind commit yourself to never again offend God by keeping your thoughts, words and deeds pure.</p>",
				"infoRefference": "<a href='http://www.how-to-pray-the-rosary-everyday.com/meditations-on-the-rosary.html' target='_blank'>link</a>"
	        },
	        {
	            "decadeID": 13,
	            "mysteryIndex": 3,
	            "decadeNo": 3,
	            "decadeName": "Third Sorrowful Mystery: The Crowning with Thorns",
				"decadeInfo": "<p>When thinking of the terrible crown of thorns Jesus was forced to wear, keep in mind He wore this crown in expiation for the sins of thought. Keep your mind free from trouble. Do not worry endlessly or be anxious about anything. Keep your thoughts holy and fixed on Jesus and things that are not of this world.</p>",
				"infoRefference": "<a href='http://www.how-to-pray-the-rosary-everyday.com/meditations-on-the-rosary.html' target='_blank'>link</a>"
	        },
	        {
	            "decadeID": 14,
	            "mysteryIndex": 4,
	            "decadeNo": 4,
	            "decadeName": "Fourth Sorrowful Mystery: The Carrying of the Cross",
				"decadeInfo": "Jesus' patience is the focus of His agonizing way of the cross. Jesus embraced His cross because it was the will of God and the purpose of His mission to redeem fallen man. You must follow Jesus' example by embracing the trials and sufferings of your daily life and uniting them to His sufferings.",
				"infoRefference": "<a href='http://www.how-to-pray-the-rosary-everyday.com/meditations-on-the-rosary.html' target='_blank'>link</a>"
	        },
	        {
	            "decadeID": 15,
	            "mysteryIndex": 5,
	            "decadeNo": 5,
	            "decadeName": "Fifth Sorrowful Mystery: The Crucifixion of Our Lord",
				"decadeInfo": "<p>The crucifixion is Jesus' ultimate act of redemption. This act of redemption was necessary because God being a just God desired that mankind make reparation for the disobedience of Adam and Eve. Only man could repair for his sin. For this reason, God became man in the Person of Jesus and suffered and died on the cross. Jesus did this for you. In return, you must strive to increase in all the virtues and persevere in faith.</p>",
				"infoRefference": "<a href='http://www.how-to-pray-the-rosary-everyday.com/meditations-on-the-rosary.html' target='_blank'>link</a>"
	        },

	        {
	            "decadeID": 16,
	            "mysteryIndex": 1,
	            "decadeNo": 1,
	            "decadeName": "First Glorious Mystery: The Resurrection",
				"decadeInfo": "<p>Your faith in Jesus should be firmly founded in this mystery, Jesus' Resurrection. You must spread this faith by leading a holy life. Never let an opportunity pass when you can be an example of Jesus' love.</p>",
				"infoRefference": "<a href='http://www.how-to-pray-the-rosary-everyday.com/meditations-on-the-rosary.html' target='_blank'>link</a>"
	        },
	        {
	            "decadeID": 17,
	            "mysteryIndex": 2,
	            "decadeNo": 2,
	            "decadeName": "Second Glorious Mystery: The Ascension",
				"decadeInfo": "<p>Jesus' Ascension brings hope to those here on earth. Jesus ascended into heaven before the Apostles very eyes. Jesus is in heaven now waiting to greet you. You will find peace as you learn to embrace your crosses and eagerly await the day you will be united with Jesus and His Mother Mary and with all the angels and the saints.</p>",
				"infoRefference": "<a href='http://www.how-to-pray-the-rosary-everyday.com/meditations-on-the-rosary.html' target='_blank'>link</a>"
	        },
	        {
	            "decadeID": 18,
	            "mysteryIndex": 3,
	            "decadeNo": 3,
	            "decadeName": "Third Glorious Mystery: The Descent of the Holy Spirit",
				"decadeInfo": "<p>The Descent of the Holy Spirit should incite in you a deep love of God. Jesus sent the third Person of the Blessed Trinity, the Holy Spirit to guide and protect the Church and to pour out His gifts upon its members. Become familiar with these gifts and learn to use them in your own life, for your good and for the good of all those you love. Don't let these marvelous gifts go to waste. Thank God for loving you so much. Not only did He become Man to die for your sins, He also send His Spirit to guide and protect you and His Church.</p>",
				"infoRefference": "<a href='http://www.how-to-pray-the-rosary-everyday.com/meditations-on-the-rosary.html' target='_blank'>link</a>"
	        },
	        {
	            "decadeID": 19,
	            "mysteryIndex": 4,
	            "decadeNo": 4,
	            "decadeName": "Fourth Glorious Mystery: The Assumption",
				"decadeInfo": "<p>Jesus took Mary, body and soul up to Heaven where He had a place prepared for her. Mary had perfected all virtues and her life resembled the life of Jesus in all things. The more you practice the virtues the holier you will become and soon you too can make your life a reflection of Jesus'.</p>",
				"infoRefference": "<a href='http://www.how-to-pray-the-rosary-everyday.com/meditations-on-the-rosary.html' target='_blank'>link</a>"
	        },
	        {
	            "decadeID": 20,
	            "mysteryIndex": 5,
	            "decadeNo": 5,
	            "decadeName": "Fifth Glorious Mystery: The Coronation",
				"decadeInfo": "<p>Because Mary shared in all Jesus' sufferings and because her life so perfectly resembled His, she was rewarded and crowned Queen of heaven and earth. She is a good Queen who wishes to distribute the many graces Jesus has given her upon her children if they just ask.</p>",
				"infoRefference": "<a href='http://www.how-to-pray-the-rosary-everyday.com/meditations-on-the-rosary.html' target='_blank'>link</a>"
	        }
	    ],
		"mystery": [
			{
				"mysteryID": 0,
				"mysteryNo": 0,
				"mysteryName": "rosary preparation"
			},
			{
				"mysteryID": 1,
				"mysteryNo": 1,
				"mysteryName": "Joyful Mystery"
			},
			{
				"mysteryID": 2,
				"mysteryNo": 2,
				"mysteryName": "Luminous Mystery"
			},
			{
				"mysteryID": 3,
				"mysteryNo": 3,
				"mysteryName": "Sorrowful Mystery"
			},
			{
				"mysteryID": 4,
				"mysteryNo": 4,
				"mysteryName": "Glorious Mystery"
			},
			{
				"mysteryID": 5,
				"mysteryNo": 5,
				"mysteryName": "rosary conclusion"
			}
		],
		"book": [
			{
				"bookID": 0,
	            "bookName": "NAB Bible"
			},
			{
				"bookID": 1,
				"bookName": "Judith"
			},
			{
				"bookID": 2,
				"bookName": "Psalms"
			},
			{
				"bookID": 3,
				"bookName": "Proverbs"
			},
			{
				"bookID": 4,
				"bookName": "Songs a.ka. Ecclesiastes"
			},
			{
				"bookID": 5,
				"bookName": "Sirach"
			},
			{
				"bookID": 6,
				"bookName": "Isiah"
			},
			{
				"bookID": 7,
				"bookName": "Matthew"
			},
			{
				"bookID": 8,
				"bookName": "Mark"
			},
			{
				"bookID": 9,
				"bookName": "Luke"
			},
			{
				"bookID": 10,
				"bookName": "John"
			},
			{
				"bookID": 11,
				"bookName": "Acts"
			},
			{
				"bookID": 12,
				"bookName": "1 Corinthians"
			},
			{
				"bookID": 13,
				"bookName": "Revelations"
			},
			{
				"bookID": 14,
				"bookName": "Queenship of the B.V.M., Gradual",
				"library": "<a href='http://w2.vatican.va/content/pius-xii/en/encyclicals/documents/hf_p-xii_enc_11101954_ad-caeli-reginam.html' target='_blank'>AD CAELI REGINAM - ENCYCLICAL OF POPE PIUS XII, October 11, 1954 </a>"
			},
			{
				"bookID": 15,
				"bookName": "Oremus",
				"library": "<a href='http://www.oremus.org/liturgy/ccp/07mon.html' target='_blank'>Pentecost Alleluia</a>"
			}
		],
		"scripture": [
			{
				"scriptureID": 0,
	            "bookIndex": 0,
	            "chapterIndex": 0,
	            "verseIndex": 0,
	            "scriptureText": ""
			},
			{
				"scriptureID": 1,
				"bookIndex": 10,
				"chapterIndex": 1,
				"verseIndex": 1,
				"scriptureText": "In the beginning* was the Word, and the Word was with God, and the Word was God. - John 1:1"
			},
			{
				"scriptureID": 2,
				"bookIndex": 10,
				"chapterIndex": 1,
				"verseIndex": 2,
				"scriptureText": "He was in the beginning with God. - John 1:2"
			},
			{
				"scriptureID": 3,
				"bookIndex": 10,
				"chapterIndex": 1,
				"verseIndex": 3,
				"scriptureText": "All things came to be through him, and without him nothing came to be. What came to be - John 1:3"
			},
			{
				"scriptureID": 4,
				"bookIndex": 10,
				"chapterIndex": 1,
				"verseIndex": 4,
				"scriptureText": "through him was life, and this life was the light of the human race; - John 1:4"
			},
			{
				"scriptureID": 5,
				"bookIndex": 10,
				"chapterIndex": 1,
				"verseIndex": 5,
				"scriptureText": "the light shines in the darkness, and the darkness has not overcome it. - John 1:5"
			},
			{
				"scriptureID": 6,
				"bookIndex": 10,
				"chapterIndex": 1,
				"verseIndex": 6,
				"scriptureText": "A man named John was sent from God. - John 1:6"
			},
			{
				"scriptureID": 7,
				"bookIndex": 10,
				"chapterIndex": 1,
				"verseIndex": 7,
				"scriptureText": "He came for testimony, to testify to the light, so that all might believe through him. - John 1:7"
			},
			{
				"scriptureID": 8,
				"bookIndex": 10,
				"chapterIndex": 1,
				"verseIndex": 8,
				"scriptureText": "He was not the light, but came to testify to the light. - John 1:8"
			},
			{
				"scriptureID": 9,
				"bookIndex": 10,
				"chapterIndex": 1,
				"verseIndex": 9,
				"scriptureText": "The true light, which enlightens everyone, was coming into the world. - John 1:9"
			},
			{
				"scriptureID": 10,
				"bookIndex": 10,
				"chapterIndex": 1,
				"verseIndex": 10,
				"scriptureText": "He was in the world, and the world came to be through him, but the world did not know him. - John 1:10"
			},
			{
				"scriptureID": 11,
				"bookIndex": 10,
				"chapterIndex": 1,
				"verseIndex": 11,
				"scriptureText": "He came to what was his own, but his own people* did not accept him. - John 1:11"
			},
			{
				"scriptureID": 12,
				"bookIndex": 10,
				"chapterIndex": 1,
				"verseIndex": 12,
				"scriptureText": "But to those who did accept him he gave power to become children of God, to those who believe in his name, - John 1:12"
			},
			{
				"scriptureID": 13,
				"bookIndex": 10,
				"chapterIndex": 1,
				"verseIndex": 13,
				"scriptureText": "who were born not by natural generation nor by human choice nor by a man's decision but of God. - John 1:13"
			},
			{
				"scriptureID": 14,
				"bookIndex": 10,
				"chapterIndex": 1,
				"verseIndex": 14,
				"scriptureText": "And the Word became flesh and made his dwelling among us, and we saw his glory, the glory as of the Father's only Son, full of grace and truth. - John 1:14"
			},
			{
				"scriptureID": 15,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 26,
				"scriptureText": "In the sixth month, the angel Gabriel was sent from God to a town of Galilee called Nazareth - Luke 1:26"
			},
			{
				"scriptureID": 16,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 27,
				"scriptureText": "to a virgin betrothed to a man named Joseph, of the house of David, and the virgin's name was Mary - Luke 1:27"
			},
			{
				"scriptureID": 17,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 28,
				"scriptureText": "And coming to her, he said, \"Hail, favored one! The Lord is with you.\" - Luke 1:28"
			},
			{
				"scriptureID": 18,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 29,
				"scriptureText": "But she was greatly troubled at what was said and pondered what sort of greeting this might be. - Luke 1:29"
			},
			{
				"scriptureID": 19,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 30,
				"scriptureText": "Then the angel said to her, \"Do not be afraid, Mary, for you have found favor with God.\"- Luke 1:30"
			},
			{
				"scriptureID": 20,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 31,
				"scriptureText": "Behold, you will conceive in your womb and bear a son, and you shall name him Jesus. - Luke 1:31"
			},
			{
				"scriptureID": 21,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 32,
				"scriptureText": "He will be great and will be called Son of the Most High, and the Lord God will give him the throne of David his father, - Luke: 1:32"
			},
			{
				"scriptureID": 22,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 33,
				"scriptureText": "and he will rule over the house of Jacob forever, and of his kingdom there will be no end.\" - Luke 1:33"
			},
			{
				"scriptureID": 23,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 34,
				"scriptureText": "But Mary said to the angel, \"How can this be, since I have no relations with a man? - Luke 1: 34"
			},
			{
				"scriptureID": 24,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 35,
				"scriptureText": "And the angel said to her in reply, The holy Spirit will come upon you, and the power of the Most High will overshadow you. Therefore the child to be born will be called holy, the Son of God. - Luke 1: 35"
			},
			{
				"scriptureID": 25,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 36,
				"scriptureText": "And behold, Elizabeth, your relative, has also conceived a son in her old age, and this is the sixth month for her who was called barren; - Luke 1: 36"
			},
			{
				"scriptureID": 26,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 37,
				"scriptureText": "for nothing will be impossible for God.\" - Luke 1: 37"
			},
			{
				"scriptureID": 27,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 38,
				"scriptureText": "Mary said, Behold, I am the handmaid of the Lord. May it be done to me according to your word.\" Then the angel departed from her - Luke 1: 38"
			},
			{
				"scriptureID": 28,
				"bookIndex": 7,
				"chapterIndex": 1,
				"verseIndex": 20,
				"scriptureText": "Such was his intention when, behold, the angel of the Lord* appeared to him in a dream and said, \"Joseph, son of David, do not be afraid to take Mary your wife into your home. For it is through the holy Spirit that this child has been conceived in her. - Matthew 1:20"
			},
			{
				"scriptureID": 29,
				"bookIndex": 7,
				"chapterIndex": 1,
				"verseIndex": 21,
				"scriptureText": "She will bear a son and you are to name him Jesus,* because he will save his people from their sins.\" -  Matthew 1:21"
			},
			{
				"scriptureID": 30,
				"bookIndex": 7,
				"chapterIndex": 1,
				"verseIndex": 22,
				"scriptureText": "All this took place to fulfill what the Lord had said through the prophet: - Matthew 1:22"
			},
			{
				"scriptureID": 31,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 39,
				"scriptureText": "During those days Mary set out and traveled to the hill country in haste to a town of Judah, - Luke 1:39"
			},
			{
				"scriptureID": 32,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 40,
				"scriptureText": "where she entered the house of Zechariah and greeted Elizabeth. - Luke 1:40"
			},
			{
				"scriptureID": 33,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 41,
				"scriptureText": "When Elizabeth heard Mary's greeting, the infant leaped in her womb, and Elizabeth, filled with the holy Spirit, - Luke 1:41"
			},
			{
				"scriptureID": 34,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 42,
				"scriptureText": "cried out in a loud voice and said, \"Most blessed are you among women, and blessed is the fruit of your womb. - Luke 1:42"
			},
			{
				"scriptureID": 35,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 43,
				"scriptureText": "And how does this happen to me, that the mother of my Lordshould come to me? - Luke 1:43"
			},
			{
				"scriptureID": 36,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 44,
				"scriptureText": "For at the moment the sound of your greeting reached my ears, the infant in my womb leaped for joy. - Luke 1:44"
			},
			{
				"scriptureID": 37,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 45,
				"scriptureText": "Blessed are you who believed that what was spoken to you by the Lord would be fulfilled.\" - Luke 1:45"
			},
			{
				"scriptureID": 38,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 46,
				"scriptureText": "And Mary said: \"My soul proclaims the greatness of the Lord; - Luke 1:46"
			},
			{
				"scriptureID": 39,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 47,
				"scriptureText": "my spirit rejoices in God my savior. - Luke 1:47"
			},
			{
				"scriptureID": 40,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 48,
				"scriptureText": "For he has looked upon his handmaid's lowliness; behold, from now on will all ages call me blessed. - Luke 1:48"
			},
			{
				"scriptureID": 41,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 49,
				"scriptureText": "The Mighty One has done great things for me, and holy is his name. - Luke 1:49"
			},
			{
				"scriptureID": 42,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 50,
				"scriptureText": "His mercy is from age to age to those who fear him. - Luke 1:50"
			},
			{
				"scriptureID": 43,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 51,
				"scriptureText": "He has shown might with his arm, dispersed the arrogant of mind and heart. - Luke 1:51"
			},
			{
				"scriptureID": 44,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 52,
				"scriptureText": "He has thrown down the rulers from their thrones but lifted up the lowly. - Luke 1:52"
			},
			{
				"scriptureID": 45,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 53,
				"scriptureText": "The hungry he has filled with good things, the rich he has sent away empty. - Luke 1:53"
			},
			{
				"scriptureID": 46,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 54,
				"scriptureText": "He has helped Israel his servant, remembering his mercy, - Luke 1:54"
			},
			{
				"scriptureID": 47,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 55,
				"scriptureText": "according to his promise to our fathers, to Abraham and to his descendants forever.\" - Luke 1:55"
			},
			{
				"scriptureID": 48,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 56,
				"scriptureText": "Mary remained with her about three months and then returned to her home. - Luke 1:56"
			},
			{
				"scriptureID": 49,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 57,
				"scriptureText": "When the time arrived for Elizabeth to have her child she gave birth to a son. - Luke 1:57"
			},
			{
				"scriptureID": 50,
				"bookIndex": 9,
				"chapterIndex": 1,
				"verseIndex": 58,
				"scriptureText": "Her neighbors and relatives heard that the Lord had shown his great mercy toward her, and they rejoiced with her. - Luke 1:58"
			},
			{
				"scriptureID": 51,
				"bookIndex": 10,
				"chapterIndex": 1,
				"verseIndex": 23,
				"scriptureText": "He (John the Baptist) said: \"I am 'the voice of one crying out in the desert, \"Make straight the way of the Lord,\"' as Isaiah the prophet said.\" - John 1:23"
			},
			{
				"scriptureID": 52,
				"bookIndex": 8,
				"chapterIndex": 1,
				"verseIndex": 7,
				"scriptureText": "And this is what he (John the Baptist) proclaimed: \"One mightier than I is coming after me. I am not worthy to stoop and loosen the thongs of his sandals. - Mark 1:7"
			},
			{
				"scriptureID": 53,
				"bookIndex": 7,
				"chapterIndex": 3,
				"verseIndex": 11,
				"scriptureText": "I am baptizing you with water, for repentance, but the one who is coming after me is mightier than I. I am not worthy to carry his sandals. He will baptize you with the holy Spirit and fire. - Matthew 3:11"
			},
			{
				"scriptureID": 54,
				"bookIndex": 10,
				"chapterIndex": 1,
				"verseIndex": 29,
				"scriptureText": "The next day he saw Jesus coming toward him and said, \"Behold, the Lamb of God,* who takes away the sin of the world. - John 1:29"
			},
			{
				"scriptureID": 55,
				"bookIndex": 7,
				"chapterIndex": 3,
				"verseIndex": 13,
				"scriptureText": "Then Jesus came from Galilee to John at the Jordan to be baptized by him. - Matthew 3:13"
			},
			{
				"scriptureID": 56,
				"bookIndex": 7,
				"chapterIndex": 3,
				"verseIndex": 14,
				"scriptureText": "John tried to prevent him, saying, \"I need to be baptized by you, and yet you are coming to me?\" - Matthew 3:14"
			},
			{
				"scriptureID": 57,
				"bookIndex": 7,
				"chapterIndex": 3,
				"verseIndex": 15,
				"scriptureText": "Jesus said to him in reply, \"Allow it now, for thus it is fitting for us to fulfill all righteousness.\" Then he allowed him.  - Matthew 3:15"
			},
			{
				"scriptureID": 58,
				"bookIndex": 7,
				"chapterIndex": 3,
				"verseIndex": 16,
				"scriptureText": "After Jesus was baptized, he came up from the water and behold, the heavens were opened [for him], and he saw the Spirit of God descending like a dove [and] coming upon him. - Matthew 3:16"
			},
			{
				"scriptureID": 59,
				"bookIndex": 7,
				"chapterIndex": 3,
				"verseIndex": 17,
				"scriptureText": "And a voice came from the heavens, saying, \"This is my beloved Son,* with whom I am well pleased.\" - Matthew 3:17"
			},
			{
				"scriptureID": 60,
				"bookIndex": 8,
				"chapterIndex": 1,
				"verseIndex": 12,
				"scriptureText": "At once the Spirit drove him out into the desert / and he remained in the desert for forty days, tempted by Satan. He was among wild beasts, and the angels ministered to him. - Mark 1:12-13"
			},
			{
				"scriptureID": 61,
				"bookIndex": 10,
				"chapterIndex": 2,
				"verseIndex": 1,
				"scriptureText": "On the third day there was a wedding* in Cana* in Galilee, and the mother of Jesus was there. - John 2:1"
			},
			{
				"scriptureID": 62,
				"bookIndex": 10,
				"chapterIndex": 2,
				"verseIndex": 3,
				"scriptureText": "When the wine ran short, the mother of Jesus said to him, \"They have no wine.\" - John 2:3"
			},
			{
				"scriptureID": 63,
				"bookIndex": 10,
				"chapterIndex": 2,
				"verseIndex": 4,
				"scriptureText": "[And] Jesus said to her, \"Woman, how does your concern affect me? My hour has not yet come.\" - John 2:4"
			},
			{
				"scriptureID": 64,
				"bookIndex": 10,
				"chapterIndex": 2,
				"verseIndex": 5,
				"scriptureText": "His mother said to the servers, \"Do whatever he tells you.\" - John 2:5"
			},
			{
				"scriptureID": 65,
				"bookIndex": 10,
				"chapterIndex": 2,
				"verseIndex": 6,
				"scriptureText": "Now there were six stone water jars there for Jewish ceremonial washings,d each holding twenty to thirty gallons. - John 2:6"
			},
			{
				"scriptureID": 66,
				"bookIndex": 10,
				"chapterIndex": 2,
				"verseIndex": 7,
				"scriptureText": "Jesus told them, \"Fill the jars with water.\" So they filled them to the brim. - John 2:7"
			},
			{
				"scriptureID": 67,
				"bookIndex": 10,
				"chapterIndex": 2,
				"verseIndex": 8,
				"scriptureText": "Then he told them, \"Draw some out now and take it to the headwaiter.\" So they took it. - John 2:8"
			},
			{
				"scriptureID": 68,
				"bookIndex": 10,
				"chapterIndex": 2,
				"verseIndex": 9,
				"scriptureText": "And when the headwaiter tasted the water that had become wine, without knowing where it came from (although the servers who had drawn the water knew), the headwaiter called the bridegroom - John 2:9"
			},
			{
				"scriptureID": 69,
				"bookIndex": 10,
				"chapterIndex": 2,
				"verseIndex": 10,
				"scriptureText": "and said to him, \"Everyone serves good wine first, and then when people have drunk freely, an inferior one; but you have kept the good wine until now.\" - John 2:10"
			},
			{
				"scriptureID": 70,
				"bookIndex": 10,
				"chapterIndex": 2,
				"verseIndex": 11,
				"scriptureText": "Jesus did this as the beginning of his signs* in Cana in Galilee and so revealed his glory, and his disciples began to believe in him. - John 2:11"
			},
			{
				"scriptureID": 71,
				"bookIndex": 8,
				"chapterIndex": 1,
				"verseIndex": 14,
				"scriptureText": "After John had been arrested,* Jesus came to Galilee proclaiming the gospel of God: - Mark 1:14"
			},
			{
				"scriptureID": 72,
				"bookIndex": 10,
				"chapterIndex": 1,
				"verseIndex": 4,
				"scriptureText": "through him was life, and this life was the light of the human race; / the light shines in the darkness, and the darkness has not overcome it. - John 1:4-5"
			},
			{
				"scriptureID": 73,
				"bookIndex": 8,
				"chapterIndex": 1,
				"verseIndex": 15,
				"scriptureText": "\"This is the time of fulfillment. The kingdom of God is at hand. Repent, and believe in the gospel.\" - Mark 1:15"
			},
			{
				"scriptureID": 74,
				"bookIndex": 8,
				"chapterIndex": 2,
				"verseIndex": 2,
				"scriptureText": "Many gathered together so that there was no longer room for them, not even around the door, and he preached the word to them. - Mark 2:2"
			},
			{
				"scriptureID": 75,
				"bookIndex": 8,
				"chapterIndex": 2,
				"verseIndex": 4,
				"scriptureText": "Unable to get near Jesus because of the crowd, they opened up the roof above him. After they had broken through, they let down the mat on which the paralytic was lying. - Mark 2:4"
			},
			{
				"scriptureID": 76,
				"bookIndex": 8,
				"chapterIndex": 2,
				"verseIndex": 9,
				"scriptureText": "Which is easier, to say to the paralytic, 'Your sins are forgiven,' or to say, 'Rise, pick up your mat and walk'? - Mark 2:9"
			},
			{
				"scriptureID": 77,
				"bookIndex": 8,
				"chapterIndex": 2,
				"verseIndex": 10,
				"scriptureText": "But that you may know that the Son of Man has authority to forgive sins on earth\" / he said to the paralytic, \"I say to you, rise, pick up your mat, and go home.\" - Mark 2:10-11"
			},
			{
				"scriptureID": 78,
				"bookIndex": 7,
				"chapterIndex": 10,
				"verseIndex": 1,
				"scriptureText": "Then he summoned his twelve disciples* and gave them authority over unclean spirits to drive them out and to cure every disease and every illness. - Matthew 10:1"
			},
			{
				"scriptureID": 79,
				"bookIndex": 7,
				"chapterIndex": 10,
				"verseIndex": 5,
				"scriptureText": "Jesus sent out these twelve* after instructing them thus, \"Do not go into pagan territory or enter a Samaritan town. / As you go, make this proclamation: 'The kingdom of heaven is at hand.' - Matthew 10:5 & 7"
			},
			{
				"scriptureID": 80,
				"bookIndex": 10,
				"chapterIndex": 20,
				"verseIndex": 22,
				"scriptureText": "And when he had said this, he breathed on them and said to them, \"Receive the holy Spirit. / Whose sins you forgive are forgiven them, and whose sins you retain are retained.\" - John 20:22-23"
			},
			{
				"scriptureID": 81,
				"bookIndex": 7,
				"chapterIndex": 17,
				"verseIndex": 2,
				"scriptureText": "When he entered the house, the blind men approached him and Jesus said to them, \"Do you believe that I can do this?\" \"Yes, Lord,\" they said to him. - Luke 9:28"
			},
			{
				"scriptureID": 82,
				"bookIndex": 7,
				"chapterIndex": 17,
				"verseIndex": 2,
				"scriptureText": "And he was transfigured before them; his face shone like the sun and his clothes became white as light.  - Matthew 17:2"
			},
			{
				"scriptureID": 83,
				"bookIndex": 7,
				"chapterIndex": 17,
				"verseIndex": 3,
				"scriptureText": "And behold, Moses and Elijah appeared to them, conversing with him. - Matthew 17:3"
			},
			{
				"scriptureID": 84,
				"bookIndex": 9,
				"chapterIndex": 9,
				"verseIndex": 31,
				"scriptureText": "who appeared in glory and spoke of his exodus that he was going to accomplish in Jerusalem. - Luke 9:31"
			},
			{
				"scriptureID": 85,
				"bookIndex": 7,
				"chapterIndex": 17,
				"verseIndex": 4,
				"scriptureText": "Then Peter said to Jesus in reply, \"Lord, it is good that we are here. If you wish, I will make three tents* here, one for you, one for Moses, and one for Elijah.\" - Matthew 17:4"
			},
			{
				"scriptureID": 86,
				"bookIndex": 9,
				"chapterIndex": 9,
				"verseIndex": 34,
				"scriptureText": "While he was still speaking, a cloud came and cast a shadow over them, and they became frightened when they entered the cloud. - Luke 9:34"
			},
			{
				"scriptureID": 87,
				"bookIndex": 9,
				"chapterIndex": 9,
				"verseIndex": 35,
				"scriptureText": "Then from the cloud came a voice that said, \"This is my chosen Son; listen to him.\" - Luke 9:35"
			},
			{
				"scriptureID": 88,
				"bookIndex": 8,
				"chapterIndex": 9,
				"verseIndex": 8,
				"scriptureText": "Suddenly, looking around, they no longer saw anyone but Jesus alone with them. - Mark 9:8"
			},
			{
				"scriptureID": 89,
				"bookIndex": 8,
				"chapterIndex": 9,
				"verseIndex": 9,
				"scriptureText": "As they were coming down from the mountain, he charged them not to relate what they had seen to anyone, except when the Son of Man had risen from the dead. - Mark 9:9"
			},
			{
				"scriptureID": 90,
				"bookIndex": 8,
				"chapterIndex": 9,
				"verseIndex": 10,
				"scriptureText": "So they kept the matter to themselves, questioning what rising from the dead meant. - Mark 9:10"
			},
			{
				"scriptureID": 91,
				"bookIndex": 7,
				"chapterIndex": 26,
				"verseIndex": 17,
				"scriptureText": "On the first day of the Feast of Unleavened Bread,* the disciples approached Jesus and said, \"Where do you want us to prepare for you to eat the Passover?\" - Matthew 26:17"
			},
			{
				"scriptureID": 92,
				"bookIndex": 7,
				"chapterIndex": 26,
				"verseIndex": 18,
				"scriptureText": "He said, \"Go into the city to a certain man and tell him, 'The teacher says, \"My appointed time draws near; in your house I shall celebrate the Passover with my disciples.\" ' \" - Matthew 26:18"
			},
			{
				"scriptureID": 93,
				"bookIndex": 9,
				"chapterIndex": 22,
				"verseIndex": 14,
				"scriptureText": "When the hour came, he took his place at table with the apostles. / He said to them, \"I have eagerly desired to eat this Passover* with you before I suffer, - Luke 22:14-15"
			},
			{
				"scriptureID": 94,
				"bookIndex": 7,
				"chapterIndex": 26,
				"verseIndex": 21,
				"scriptureText": "And while they were eating, he said, \"Amen, I say to you, one of you will betray me.\" - Matthew 26:21"
			},
			{
				"scriptureID": 95,
				"bookIndex": 7,
				"chapterIndex": 26,
				"verseIndex": 25,
				"scriptureText": "Then Judas, his betrayer, said in reply, \"Surely it is not I, Rabbi?\" He answered, \"You have said so.\" - Matthew 26:25"
			},
			{
				"scriptureID": 96,
				"bookIndex": 7,
				"chapterIndex": 26,
				"verseIndex": 26,
				"scriptureText": "While they were eating, Jesus took bread, said the blessing, broke it, and giving it to his disciples said, \"Take and eat; this is my body.\" - Matthew 26:26"
			},
			{
				"scriptureID": 97,
				"bookIndex": 7,
				"chapterIndex": 26,
				"verseIndex": 27,
				"scriptureText": "Then he took a cup, gave thanks,* and gave it to them, saying, \"Drink from it, all of you, / for this is my blood of the covenant, which will be shed on behalf of many for the forgiveness of sins.  - Matthew 26:27-28"
			},
			{
				"scriptureID": 98,
				"bookIndex": 12,
				"chapterIndex": 11,
				"verseIndex": 26,
				"scriptureText": "For as often as you eat this bread and drink the cup, you proclaim the death of the Lord until he comes. - 1 Corinthians 11:26"
			},
			{
				"scriptureID": 99,
				"bookIndex": 10,
				"chapterIndex": 6,
				"verseIndex": 51,
				"scriptureText": "I am the living bread that came down from heaven; whoever eats this bread will live forever; and the bread that I will give is my flesh for the life of the world.\" - John 6:51"
			},
			{
				"scriptureID": 100,
				"bookIndex": 10,
				"chapterIndex": 6,
				"verseIndex": 54,
				"scriptureText": "'He who eats my flesh and drinks my blood has eternal life, and I will raise him at the last day.' - John 6:54"
			},
			{
				"scriptureID": 101,
				"bookIndex": 7,
				"chapterIndex": 26,
				"verseIndex": 36,
				"scriptureText": "Then Jesus went with them to a place called Gethsemane. / And he began to be sorrowful and troubled. - Matthew 26:36-37"
			},
			{
				"scriptureID": 102,
				"bookIndex": 7,
				"chapterIndex": 26,
				"verseIndex": 38,
				"scriptureText": "Then Jesus came with them to a place called Gethsemane,* and he said to his disciples, \"Sit here while I go over there and pray.\" / He took along Peter and the two sons of Zebedee,* and began to feel sorrow and distress. - Matthew 26:38"
			},
			{
				"scriptureID": 103,
				"bookIndex": 9,
				"chapterIndex": 22,
				"verseIndex": 41,
				"scriptureText": "After withdrawing about a stone's throw from them and kneeling, he prayed, - Luke 22:41"
			},
			{
				"scriptureID": 104,
				"bookIndex": 9,
				"chapterIndex": 22,
				"verseIndex": 42,
				"scriptureText": "saying, \"Father, if you are willing, take this cup away from me; still, not my will but yours be done.\" - Luke 22:42"
			},
			{
				"scriptureID": 105,
				"bookIndex": 9,
				"chapterIndex": 22,
				"verseIndex": 43,
				"scriptureText": "And to strengthen him an angel from heaven appeared to him. - Luke 22:43"
			},
			{
				"scriptureID": 106,
				"bookIndex": 9,
				"chapterIndex": 22,
				"verseIndex": 44,
				"scriptureText": "He was in such agony and he prayed so fervently that his sweat became like drops of blood falling on the ground.] - Luke 22:44 - Luke 22:44"
			},
			{
				"scriptureID": 107,
				"bookIndex": 9,
				"chapterIndex": 22,
				"verseIndex": 44,
				"scriptureText": "He was in such agony and he prayed so fervently that his sweat became like drops of blood falling on the ground.] - Luke 22:44"
			},
			{
				"scriptureID": 108,
				"bookIndex": 7,
				"chapterIndex": 26,
				"verseIndex": 40,
				"scriptureText": "When he returned to his disciples he found them asleep. He said to Peter, \"So you could not keep watch with me for one hour? - Matthew 26:40"
			},
			{
				"scriptureID": 109,
				"bookIndex": 7,
				"chapterIndex": 26,
				"verseIndex": 41,
				"scriptureText": "Watch and pray that you may not undergo the test.* The spirit is willing, but the flesh is weak.\" - Matthew 26:41"
			},
			{
				"scriptureID": 110,
				"bookIndex": 7,
				"chapterIndex": 26,
				"verseIndex": 41,
				"scriptureText": "Watch and pray that you may not undergo the test.* The spirit is willing, but the flesh is weak.\" - Matthew 26:41"
			},
			{
				"scriptureID": 111,
				"bookIndex": 8,
				"chapterIndex": 15,
				"verseIndex": 1,
				"scriptureText": "As soon as morning came, the chief priests with the elders and the scribes, that is, the whole Sanhedrin, held a council.* They bound Jesus, led him away, and handed him over to Pilate. / Pilate questioned him, \"Are you the king of the Jews?\"* He said to him in reply, \"You say so.\" - Mark 15:1-2"
			},
			{
				"scriptureID": 112,
				"bookIndex": 10,
				"chapterIndex": 18,
				"verseIndex": 36,
				"scriptureText": "Jesus answered, \"My kingdom does not belong to this world. If my kingdom did belong to this world, my attendants [would] be fighting to keep me from being handed over to the Jews. But as it is, my kingdom is not here.\" - John 18:36"
			},
			{
				"scriptureID": 113,
				"bookIndex": 10,
				"chapterIndex": 18,
				"verseIndex": 37,
				"scriptureText": "So Pilate said to him, \"Then you are a king?\" Jesus answered, \"You say I am a king.* For this I was born and for this I came into the world, to testify to the truth. Everyone who belongs to the truth listens to my voice.\" - John 18:37"
			},
			{
				"scriptureID": 114,
				"bookIndex": 10,
				"chapterIndex": 18,
				"verseIndex": 38,
				"scriptureText": "Pilate said to him, \"What is truth?\" When he had said this, he again went out to the Jews and said to them, \"I find no guilt in him. - John 18:38"
			},
			{
				"scriptureID": 115,
				"bookIndex": 9,
				"chapterIndex": 23,
				"verseIndex": 16,
				"scriptureText": "Therefore I shall have him flogged and then release him.\" / Then Pilate took Jesus and had him scourged. - Luke 23:16, John 19:1"
			},
			{
				"scriptureID": 116,
				"bookIndex": 6,
				"chapterIndex": 53,
				"verseIndex": 3,
				"scriptureText": "He was spurned and avoided by men, a man of suffering, knowing pain, Like one from whom you turn your face, spurned, and we held him in no esteem. - Isaiah 53:3"
			},
			{
				"scriptureID": 117,
				"bookIndex": 6,
				"chapterIndex": 3,
				"verseIndex": 7,
				"scriptureText": "Though harshly treated, he submitted and did not open his mouth; Like a lamb led to slaughter or a sheep silent before shearers, he did not open his mouth. - Isaiah 53:7"
			},
			{
				"scriptureID": 118,
				"bookIndex": 6,
				"chapterIndex": 53,
				"verseIndex": 5,
				"scriptureText": "But he was pierced for our sins, crushed for our iniquity. He bore the punishment that makes us whole, by his wounds we were healed. - Isaiah 53:5"
			},
			{
				"scriptureID": 119,
				"bookIndex": 6,
				"chapterIndex": 53,
				"verseIndex": 4,
				"scriptureText": "Yet it was our pain that he bore, our sufferings he endured. We thought of him as stricken, struck down by God* and afflicted, - Isaiah 53:4"
			},
			{
				"scriptureID": 120,
				"bookIndex": 6,
				"chapterIndex": 53,
				"verseIndex": 5,
				"scriptureText": "But he was pierced for our sins, crushed for our iniquity. He bore the punishment that makes us whole, by his wounds we were healed. - Isaiah 53:5"
			},
			{
				"scriptureID": 121,
				"bookIndex": 8,
				"chapterIndex": 15,
				"verseIndex": 16,
				"scriptureText": "The soldiers led him away inside the palace, that is, the praetorium, and assembled the whole cohort. / They clothed him in purple and, weaving a crown of thorns, placed it on him. / They stripped off his clothes and threw a scarlet military cloak* about him. - Mark 15:16-17, Matthew 27:28"
			},
			{
				"scriptureID": 122,
				"bookIndex": 7,
				"chapterIndex": 27,
				"verseIndex": 29,
				"scriptureText": "Weaving a crown out of thorns,* they placed it on his head, and a reed in his right hand. And kneeling before him, they mocked him, saying, \"Hail, King of the Jews!\" - Matthew 27:29"
			},
			{
				"scriptureID": 123,
				"bookIndex": 7,
				"chapterIndex": 27,
				"verseIndex": 29,
				"scriptureText": "Weaving a crown out of thorns,* they placed it on his head, and a reed in his right hand. And kneeling before him, they mocked him, saying, \"Hail, King of the Jews!\" - Matthew 27:29"
			},
			{
				"scriptureID": 124,
				"bookIndex": 7,
				"chapterIndex": 27,
				"verseIndex": 30,
				"scriptureText": "They spat upon him* and took the reed and kept striking him on the head. - Matthew 27:30"
			},
			{
				"scriptureID": 125,
				"bookIndex": 7,
				"chapterIndex": 27,
				"verseIndex": 24,
				"scriptureText": "When Pilate saw that he was not succeeding at all, but that a riot was breaking out instead, he took water and washed his hands in the sight of the crowd, saying, \"I am innocent of this man's blood. Look to it yourselves.\" - Matthew 27:24"
			},
			{
				"scriptureID": 126,
				"bookIndex": 10,
				"chapterIndex": 19,
				"verseIndex": 15,
				"scriptureText": "So Jesus came out, wearing the crown of thorns and the purple cloak. And he said to them, \"Behold, the man!\" - John 19:5"
			},
			{
				"scriptureID": 127,
				"bookIndex": 10,
				"chapterIndex": 19,
				"verseIndex": 15,
				"scriptureText": "They cried out, \"Take him away, take him away! Crucify him!\" Pilate said to them, \"Shall I crucify your king?\" The chief priests answered, \"We have no king but Caesar.\" - John 19:15"
			},
			{
				"scriptureID": 128,
				"bookIndex": 8,
				"chapterIndex": 15,
				"verseIndex": 14,
				"scriptureText": "Pilate said to them, \"Why? What evil has he done?\" They only shouted the louder, \"Crucify him.\" - Mark 15:14"
			},
			{
				"scriptureID": 129,
				"bookIndex": 10,
				"chapterIndex": 19,
				"verseIndex": 15,
				"scriptureText": "They cried out, \"Take him away, take him away! Crucify him!\" Pilate said to them, \"Shall I crucify your king?\" The chief priests answered, \"We have no king but Caesar.\" - John 19:15"
			},
			{
				"scriptureID": 130,
				"bookIndex": 8,
				"chapterIndex": 15,
				"verseIndex": 15,
				"scriptureText": "So Pilate, wishing to satisfy the crowd, released Barabbas to them and, after he had Jesus scourged, handed him over to be crucified. - Mark 15:15"
			},
			{
				"scriptureID": 131,
				"bookIndex": 9,
				"chapterIndex": 9,
				"verseIndex": 23,
				"scriptureText": "Then he said to all, \"If anyone wishes to come after me, he must deny himself and take up his cross daily* and follow me. - Luke 9:23"
			},
			{
				"scriptureID": 132,
				"bookIndex": 9,
				"chapterIndex": 9,
				"verseIndex": 23,
				"scriptureText": "Then he said to all, \"If anyone wishes to come after me, he must deny himself and take up his cross daily* and follow me. - Luke 9:23"
			},
			{
				"scriptureID": 133,
				"bookIndex": 10,
				"chapterIndex": 19,
				"verseIndex": 17,
				"scriptureText": "and carrying the cross himself* he went out to what is called the Place of the Skull, in Hebrew, Golgotha. - John 19:17"
			},
			{
				"scriptureID": 134,
				"bookIndex": 9,
				"chapterIndex": 23,
				"verseIndex": 26,
				"scriptureText": "As they led him away they took hold of a certain Simon, a Cyrenian, who was coming in from the country; and after laying the cross on him, they made him carry it behind Jesus. - Luke 23:26"
			},
			{
				"scriptureID": 135,
				"bookIndex": 7,
				"chapterIndex": 11,
				"verseIndex": 28,
				"scriptureText": "\"Come to me, all you who labor and are burdened,* and I will give you rest. - Matthew 11:28"
			},
			{
				"scriptureID": 136,
				"bookIndex": 7,
				"chapterIndex": 11,
				"verseIndex": 29,
				"scriptureText": "Take my yoke upon you and learn from me, for I am meek and humble of heart; and you will find rest for yourselves. - Matthew 11:29"
			},
			{
				"scriptureID": 137,
				"bookIndex": 7,
				"chapterIndex": 11,
				"verseIndex": 30,
				"scriptureText": "For my yoke is easy, and my burden light.\" - Matthew 11:30"
			},
			{
				"scriptureID": 138,
				"bookIndex": 9,
				"chapterIndex": 23,
				"verseIndex": 27,
				"scriptureText": "A large crowd of people followed Jesus, including many women who mourned and lamented him. - Luke 23:27"
			},
			{
				"scriptureID": 139,
				"bookIndex": 9,
				"chapterIndex": 23,
				"verseIndex": 28,
				"scriptureText": "Jesus turned to them and said, \"Daughters of Jerusalem, do not weep for me; weep instead for yourselves and for your children, - Luke 23:28"
			},
			{
				"scriptureID": 140,
				"bookIndex": 9,
				"chapterIndex": 23,
				"verseIndex": 31,
				"scriptureText": "for if these things are done when the wood is green what will happen when it is dry?\" - Luke 23:31"
			},
			{
				"scriptureID": 141,
				"bookIndex": 9,
				"chapterIndex": 23,
				"verseIndex": 33,
				"scriptureText": "When they came to the place called the Skull, they crucified him and the criminals there, one on his right, the other on his left. - Luke 23:33"
			},
			{
				"scriptureID": 142,
				"bookIndex": 9,
				"chapterIndex": 23,
				"verseIndex": 34,
				"scriptureText": "[Then Jesus said, \"Father, forgive them, they know not what they do.\"]* They divided his garments by casting lots. - Luke 23:34"
			},
			{
				"scriptureID": 143,
				"bookIndex": 9,
				"chapterIndex": 23,
				"verseIndex": 39,
				"scriptureText": "Now one of the criminals hanging there reviled Jesus, saying, \"Are you not the Messiah? Save yourself and us.\" / Let the Messiah, the King of Israel, come down now from the cross that we may see and believe.\" Those who were crucified with him also kept abusing him. - Luke 23:39, 42; Mark 15:32"
			},
			{
				"scriptureID": 144,
				"bookIndex": 9,
				"chapterIndex": 23,
				"verseIndex": 43,
				"scriptureText": "He replied to him, \"Amen, I say to you, today you will be with me in Paradise.\" - Luke 23:43"
			},
			{
				"scriptureID": 145,
				"bookIndex": 10,
				"chapterIndex": 19,
				"verseIndex": 25,
				"scriptureText": "Standing by the cross of Jesus were his mother and his mother's sister, Mary the wife of Clopas, and Mary of Magdala. - John 19:25"
			},
			{
				"scriptureID": 146,
				"bookIndex": 10,
				"chapterIndex": 19,
				"verseIndex": 26,
				"scriptureText": "JThen he said to the disciple, \"Behold, your mother.\" And from that hour the disciple took her into his home. - John 19:26"
			},
			{
				"scriptureID": 147,
				"bookIndex": 10,
				"chapterIndex": 19,
				"verseIndex": 27,
				"scriptureText": "Then he said to the disciple, \"Behold, your mother.\" And from that hour the disciple took her into his home. - John 19:27"
			},
			{
				"scriptureID": 148,
				"bookIndex": 9,
				"chapterIndex": 23,
				"verseIndex": 44,
				"scriptureText": "It was now about noon and darkness came over the whole land until three in the afternoon / And behold, the veil of the sanctuary was torn in two from top to bottom.* The earth quaked, rocks were split, - Luke 23:44; Matthew 27:51"
			},
			{
				"scriptureID": 149,
				"bookIndex": 9,
				"chapterIndex": 23,
				"verseIndex": 46,
				"scriptureText": "Jesus cried out in a loud voice, \"Father, into your hands I commend my spirit\"; and when he had said this he breathed his last. - Luke 23:46"
			},
			{
				"scriptureID": 150,
				"bookIndex": 10,
				"chapterIndex": 19,
				"verseIndex": 30,
				"scriptureText": "When Jesus had taken the wine, he said, \"It is finished.\" And bowing his head, he handed over the spirit. - John 19:30"
			},
			{
				"scriptureID": 151,
				"bookIndex": 10,
				"chapterIndex": 16,
				"verseIndex": 20,
				"scriptureText": "\"Truly, Truly, I say to you, / you will weep and lament, / but the world will rejoice; / you will be sorrowful, / but your sorrow will turn into joy.\" - John 16:20"
			},
			{
				"scriptureID": 152,
				"bookIndex": 10,
				"chapterIndex": 16,
				"verseIndex": 22,
				"scriptureText": "So you also are now in anguish. But I will see you again, and your hearts will rejoice, and no one will take your joy away from you. - John 16:22"
			},
			{
				"scriptureID": 153,
				"bookIndex": 9,
				"chapterIndex": 24,
				"verseIndex": 1,
				"scriptureText": "But at daybreak on the first day of the week they took the spices they had prepared and went to the tomb. - Luke 24:1"
			},
			{
				"scriptureID": 154,
				"bookIndex": 7,
				"chapterIndex": 28,
				"verseIndex": 2,
				"scriptureText": "And behold, there was a great earthquake; for an angel of the Lord descended from heaven, approached, rolled back the stone, and sat upon it. - Matthew 28:2"
			},
			{
				"scriptureID": 155,
				"bookIndex": 7,
				"chapterIndex": 28,
				"verseIndex": 5,
				"scriptureText": "Then the angel said to the women in reply, \"Do not be afraid! I know that you are seeking Jesus the crucified. - Matthew 28:5"
			},
			{
				"scriptureID": 156,
				"bookIndex": 9,
				"chapterIndex": 24,
				"verseIndex": 6,
				"scriptureText": "He is not here, but he has been raised.* Remember what he said to you while he was still in Galilee, - Luke 24:6"
			},
			{
				"scriptureID": 157,
				"bookIndex": 7,
				"chapterIndex": 28,
				"verseIndex": 7,
				"scriptureText": "Then go quickly and tell his disciples, 'He has been raised from the dead, and he is going before you to Galilee; there you will see him.' Behold, I have told you.\" - Matthew 28:7"
			},
			{
				"scriptureID": 158,
				"bookIndex": 8,
				"chapterIndex": 16,
				"verseIndex": 8,
				"scriptureText": "Then they went out and fled from the tomb, seized with trembling and bewilderment. They said nothing to anyone, for they were afraid. / Then they went away quickly from the tomb, fearful yet overjoyed, and ran to announce* this to his disciples. - Mark 16:8; Mt 28:8"
			},
			{
				"scriptureID": 159,
				"bookIndex": 10,
				"chapterIndex": 11,
				"verseIndex": 25,
				"scriptureText": "\"I am the resurrection and the life; / he who believes in me, / though he die, / yet shall he live.\" - John 11:25"
			},
			{
				"scriptureID": 160,
				"bookIndex": 10,
				"chapterIndex": 11,
				"verseIndex": 26,
				"scriptureText": "and everyone who lives and believes in me will never die. Do you believe this?\" - John 11:26"
			},
			{
				"scriptureID": 161,
				"bookIndex": 9,
				"chapterIndex": 24,
				"verseIndex": 50,
				"scriptureText": "Then he led them [out] as far as Bethany, raised his hands, and blessed them. - Luke 24:50"
			},
			{
				"scriptureID": 162,
				"bookIndex": 7,
				"chapterIndex": 28,
				"verseIndex": 18,
				"scriptureText": "Then Jesus approached and said to them, \"All power in heaven and on earth has been given to me. - Matthew 28:18"
			},
			{
				"scriptureID": 163,
				"bookIndex": 7,
				"chapterIndex": 28,
				"verseIndex": 19,
				"scriptureText": "Go, therefore,* and make disciples of all nations, baptizing them in the name of the Father, and of the Son, and of the holy Spirit, - Matthew 28:19"
			},
			{
				"scriptureID": 164,
				"bookIndex": 7,
				"chapterIndex": 28,
				"verseIndex": 19,
				"scriptureText": "Go, therefore,* and make disciples of all nations, baptizing them in the name of the Father, and of the Son, and of the holy Spirit, - Matthew 28:19"
			},
			{
				"scriptureID": 165,
				"bookIndex": 7,
				"chapterIndex": 28,
				"verseIndex": 20,
				"scriptureText": "teaching them to observe all that I have commanded you.* And behold, I am with you always, until the end of the age.\" - Matthew 28:20"
			},
			{
				"scriptureID": 166,
				"bookIndex": 8,
				"chapterIndex": 16,
				"verseIndex": 16,
				"scriptureText": "Whoever believes and is baptized will be saved; whoever does not believe will be condemned. - Mark 16:16"
			},
			{
				"scriptureID": 167,
				"bookIndex": 8,
				"chapterIndex": 16,
				"verseIndex": 16,
				"scriptureText": "Whoever believes and is baptized will be saved; whoever does not believe will be condemned. - Mark 16:16"
			},
			{
				"scriptureID": 168,
				"bookIndex": 7,
				"chapterIndex": 28,
				"verseIndex": 20,
				"scriptureText": "teaching them to observe all that I have commanded you.* And behold, I am with you always, until the end of the age.\" - Matthew 28:20"
			},
			{
				"scriptureID": 169,
				"bookIndex": 11,
				"chapterIndex": 1,
				"verseIndex": 9,
				"scriptureText": "When he had said this, as they were looking on, he was lifted up, and a cloud took him from their sight. - Acts 1:9"
			},
			{
				"scriptureID": 170,
				"bookIndex": 8,
				"chapterIndex": 16,
				"verseIndex": 19,
				"scriptureText": "So then the Lord Jesus, after he spoke to them, was taken up into heaven and took his seat at the right hand of God. - Mark 16:19"
			},
			{
				"scriptureID": 171,
				"bookIndex": 11,
				"chapterIndex": 2,
				"verseIndex": 1,
				"scriptureText": "When the time for Pentecost was fulfilled, they were all in one place together. - Acts 2:1"
			},
			{
				"scriptureID": 172,
				"bookIndex": 11,
				"chapterIndex": 2,
				"verseIndex": 2,
				"scriptureText": "And suddenly there came from the sky a noise like a strong driving wind,* and it filled the entire house in which they were. - Acts 2:2"
			},
			{
				"scriptureID": 173,
				"bookIndex": 11,
				"chapterIndex": 2,
				"verseIndex": 3,
				"scriptureText": "Then there appeared to them tongues as of fire,* which parted and came to rest on each one of them. - Acts 2:3"
			},
			{
				"scriptureID": 174,
				"bookIndex": 11,
				"chapterIndex": 2,
				"verseIndex": 4,
				"scriptureText": "And they were all filled with the holy Spirit and began to speak in different tongues,* as the Spirit enabled them to proclaim. / both Jews and converts to Judaism, Cretans and Arabs, yet we hear them speaking in our own tongues of the mighty acts of God.\" - Acts 2:4,11"
			},
			{
				"scriptureID": 175,
				"bookIndex": 11,
				"chapterIndex": 2,
				"verseIndex": 5,
				"scriptureText": "Now there were devout Jews from every nation under heaven staying in Jerusalem. - Acts 2:5"
			},
			{
				"scriptureID": 176,
				"bookIndex": 11,
				"chapterIndex": 2,
				"verseIndex": 14,
				"scriptureText": "Then Peter stood up with the Eleven, raised his voice, and proclaimed to them, \"You who are Jews, indeed all of you staying in Jerusalem. Let this be known to you, and listen to my words. - Acts 2:14"
			},
			{
				"scriptureID": 177,
				"bookIndex": 11,
				"chapterIndex": 2,
				"verseIndex": 38,
				"scriptureText": "Peter [said] to them, \"Repent and be baptized,* every one of you, in the name of Jesus Christ for the forgiveness of your sins; and you will receive the gift of the holy Spirit. - Acts 2:38"
			},
			{
				"scriptureID": 178,
				"bookIndex": 11,
				"chapterIndex": 2,
				"verseIndex": 41,
				"scriptureText": "Those who accepted his message were baptized, and about three thousand persons were added that day. - Acts 2:41"
			},
			{
				"scriptureID": 179,
				"bookIndex": 15,
				"chapterIndex": 0,
				"verseIndex": 0,
				"scriptureText": "Send forth your Spirit, and they shall be created;/ and you shall renew the face of the earth. - Pentecost Alleluia"
			},
			{
				"scriptureID": 180,
				"bookIndex": 15,
				"chapterIndex": 0,
				"verseIndex": 0,
				"scriptureText": "Come, Holy Spirit, fill the hearts of your faithful;/ and kindle in them the fire of your love. - Pentecost Alleluia"
			},
			{
				"scriptureID": 181,
				"bookIndex": 4,
				"chapterIndex": 2,
				"verseIndex": 10,
				"scriptureText": "My lover speaks and says to me, \"Arise, my friend, my beautiful one, and come! - Songs 2:10"
			},
			{
				"scriptureID": 182,
				"bookIndex": 4,
				"chapterIndex": 2,
				"verseIndex": 11,
				"scriptureText": "For see, the winter is past, the rains are over and gone. - Songs 2:11"
			},
			{
				"scriptureID": 183,
				"bookIndex": 4,
				"chapterIndex": 2,
				"verseIndex": 14,
				"scriptureText": "My dove in the clefts of the rock, in the secret recesses of the cliff, Let me see your face, let me hear your voice, For your voice is sweet, and your face is lovely.\" - Songs 2:14"
			},
			{
				"scriptureID": 184,
				"bookIndex": 13,
				"chapterIndex": 11,
				"verseIndex": 19,
				"scriptureText": "Then God's temple in heaven was opened, and the ark of his covenant could be seen in the temple. There were flashes of lightning, rumblings, and peals of thunder, an earthquake, and a violent hailstorm. - Revelations 11:19"
			},
			{
				"scriptureID": 185,
				"bookIndex": 13,
				"chapterIndex": 12,
				"verseIndex": 1,
				"scriptureText": "A great sign appeared in the sky, a woman* clothed with the sun, with the moon under her feet, and on her head a crown of twelve stars. - Revelations 12:1"
			},
			{
				"scriptureID": 186,
				"bookIndex": 13,
				"chapterIndex": 12,
				"verseIndex": 1,
				"scriptureText": "A great sign appeared in the sky, a woman* clothed with the sun, with the moon under her feet, and on her head a crown of twelve stars. 12:1"
			},
			{
				"scriptureID": 187,
				"bookIndex": 2,
				"chapterIndex": 45,
				"verseIndex": 13,
				"scriptureText": "honor him, daughter of Tyre. Then the richest of the people will seek your favor with gifts. / All glorious is the king's daughter as she enters, her raiment threaded with gold; - Psalm 45:13-14"
			},
			{
				"scriptureID": 188,
				"bookIndex": 1,
				"chapterIndex": 13,
				"verseIndex": 18,
				"scriptureText": "Then Uzziah said to her, \"Blessed are you, daughter, by the Most High God, above all the women on earth; and blessed be the Lord God, the creator of heaven and earth, who guided your blow at the head of the leader of our enemies. - Judith 13:18"
			},
			{
				"scriptureID": 189,
				"bookIndex": 1,
				"chapterIndex": 13,
				"verseIndex": 19,
				"scriptureText": "Your deed of hope will never be forgotten by those who recall the might of God. - Judith 13:19"
			},
			{
				"scriptureID": 190,
				"bookIndex": 1,
				"chapterIndex": 15,
				"verseIndex": 9,
				"scriptureText": "When they came to her, all with one accord blessed her, saying: \"You are the glory of Jerusalem! You are the great pride of Israel! You are the great boast of our nation! - Judith 15:9"
			},
			{
				"scriptureID": 191,
				"bookIndex": 4,
				"chapterIndex": 6,
				"verseIndex": 10,
				"scriptureText": "Who is this that looks forth like the dawn, / fair as the moon, / bright as the sun?\" - Songs 6:10"
			},
			{
				"scriptureID": 192,
				"bookIndex": 5,
				"chapterIndex": 50,
				"verseIndex": 7,
				"scriptureText": "Like sun shining upon the temple of the King, like a rainbow appearing in the cloudy sky; / Like blossoms on the branches in springtime, like a lily by running waters; Like a green shoot on Lebanon in summer, - Sirach 50:7-8"
			},
			{
				"scriptureID": 193,
				"bookIndex": 4,
				"chapterIndex": 2,
				"verseIndex": 1,
				"scriptureText": "I am a flower of Sharon, a lily of the valleys. - Songs 2:1"
			},
			{
				"scriptureID": 194,
				"bookIndex": 5,
				"chapterIndex": 24,
				"verseIndex": 4,
				"scriptureText": "In the heights of heaven I dwelt, and my throne was in a pillar of cloud. / Before all ages, from the beginning, he created me, and through all ages I shall not cease to be. - Sirach 24:4,9"
			},
			{
				"scriptureID": 195,
				"bookIndex": 5,
				"chapterIndex": 24,
				"verseIndex": 19,
				"scriptureText": "Come to me, all who desire me, and be filled with my fruits. - Sirach 24:19"
			},
			{
				"scriptureID": 196,
				"bookIndex": 5,
				"chapterIndex": 24,
				"verseIndex": 17,
				"scriptureText": "I bud forth delights like a vine; my blossoms are glorious and rich fruit. / You will remember me as sweeter than honey, better to have than the honeycomb. - Sirach 24:17,20"
			},
			{
				"scriptureID": 197,
				"bookIndex": 3,
				"chapterIndex": 8,
				"verseIndex": 32,
				"scriptureText": "Now, children, listen to me; happy are they who keep my ways. / Listen to instruction and grow wise, do not reject it! - Proverbs 8:32-33"
			},
			{
				"scriptureID": 198,
				"bookIndex": 3,
				"chapterIndex": 8,
				"verseIndex": 34,
				"scriptureText": "Happy the one who listens to me, attending daily at my gates, keeping watch at my doorposts; - Proverbs 8:34"
			},
			{
				"scriptureID": 199,
				"bookIndex": 3,
				"chapterIndex": 8,
				"verseIndex": 35,
				"scriptureText": "For whoever finds me finds life, and wins favor from the LORD; - Proverbs 8:35"
			},
			{
				"scriptureID": 200,
				"bookIndex": 14,
				"chapterIndex": 0,
				"verseIndex": 0,
				"scriptureText": "Hail, Queen of mercy, protect us from the enemy,/ and receive us at the hour of death. - Queenship of the B.V.M., Gradual"
			}
		],
		"message": [
			{
				"messageID": 0,
				"mesageText": ""
			},
			{
				"messageID": 1,
				"mesageText": "Fruit of the Mystery: Humility"
			},
			{
				"messageID": 2,
				"mesageText": "Fruit of the Mystery: Love of Neighbour"
			},
			{
				"messageID": 3,
				"mesageText": "Fruit of the Mystery: Poverty (poor in spirit), Detachment from the things of the world, Contempt of Riches, Love of the Poor"
			},
			{
				"messageID": 4,
				"mesageText": "Fruit of the Mystery: Purity, Obedience"
			},
			{
				"messageID": 5,
				"mesageText": "Fruit of the Mystery: True Wisdom and True Conversion, Piety, Joy of Finding Jesus"
			},
			{
				"messageID": 6,
				"mesageText": "Fruit of the Mystery: Openness to the Holy Spirit"
			},
			{
				"messageID": 7,
				"mesageText": "Fruit of the Mystery: To Jesus through Mary"
			},
			{
				"messageID": 8,
				"mesageText": "Fruit of the Mystery: Repentance, Trust in God"
			},
			{
				"messageID": 9,
				"mesageText": "Fruit of the Mystery: Desire for Holiness"
			},
			{
				"messageID": 10,
				"mesageText": "Fruit of the Mystery: Eucharistic Adoration, Active Participation at Mass"
			},
			{
				"messageID": 11,
				"mesageText": "Fruit of the Mystery: Contrition, Conformity to the Will of God"
			},
			{
				"messageID": 12,
				"mesageText": "Fruit of the Mystery: Purity, Mortification"
			},
			{
				"messageID": 13,
				"mesageText": "Fruit of the Mystery: Moral Courage"
			},
			{
				"messageID": 14,
				"mesageText": "Fruit of the Mystery: Patience"
			},
			{
				"messageID": 15,
				"mesageText": "Fruit of the Mystery: Salvation, Self-Denial"
			},
			{
				"messageID": 16,
				"mesageText": "Fruit of the Mystery: Faith"
			},
			{
				"messageID": 17,
				"mesageText": "Fruit of the Mystery: Hope, Desire for Heaven"
			},
			{
				"messageID": 18,
				"mesageText": "Fruit of the Mystery: Wisdom, Love of God"
			},
			{
				"messageID": 19,
				"mesageText": "Fruit of the Mystery: Devotion to Mary"
			},
			{
				"messageID": 20,
				"mesageText": "Fruit of the Mystery: Eternal Happiness"
			}
		],
		"prayer": [
			{
				"prayerID": 0,
				"prayerName": "",
				"prayerText": "..."
			},
			{
				"prayerID": 1,
				"prayerName": "Sign of the Cross",
				"prayerText": "IN THE NAME of the Father, and of the Son, and of the Holy Spirit. Amen. (As you say this, with your right hand touch your forehead when you say Father, touch your breastbone when you say Son, touch your left shoulder when you say Holy, and touch your right shoulder when you say Spirit.)"
			},
			{
				"prayerID": 2,
				"prayerName": "Apostle's Creed",
				"prayerText": "I BELIEVE IN GOD, the Father almighty, Creator of Heaven and earth. And in Jesus Christ, His only Son, our Lord, Who was conceived by the Holy Spirit, born of the Virgin Mary, suffered under Pontius Pilate; was crucified, died, and was buried. He descended into Hell. The third day He rose again from the dead. He ascended into Heaven, and sits at the right hand of God,the Father almighty. He shall come again to judge the living and the dead. I believe in the Holy Spirit, the holy Catholic Church, the communion of saints, the forgiveness of sins, the resurrection of the body, and life everlasting. Amen"
			},
			{
				"prayerID": 3,
				"prayerName": "Our Father",
				"prayerText": "OUR FATHER, Who art in Heaven, hallowed be Thy Name. Thy kingdom come, Thy will be done on earth as it is in Heaven. Give us this day our daily bread, and forgive us our trespasses, as we forgive those who trespass against us. And lead us not into temptation, but deliver us from evil. Amen."
			},
			{
				"prayerID": 4,
				"prayerName": "Hail Mary",
				"prayerText": "HAIL MARY, full of grace, the Lord is with thee. Blessed art thou among women, and blessed is the fruit of thy womb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen."
			},
			{
				"prayerID": 5,
				"prayerName": "Glory Be",
				"prayerText": "GLORY BE to the Father, and to the Son, and to the Holy Spirit. As it was in the beginning is now, and ever shall be, world without end. Amen."
			},
			{
				"prayerID": 6,
				"prayerName": "Fatima Prayer",
				"prayerText": "O MY JESUS, forgive us our sins, save us from the fires of Hell; lead all souls to Heaven, especially those in most need of Thy mercy. Amen."
			},
			{
				"prayerID": 7,
				"prayerName": "Hail Holy Queen",
				"prayerText": "HAIL HOLY QUEEN, mother of mercy; our life, our sweetness, and our hope. To thee do we cry, poor banished children of Eve. To thee do we send up our sighs, mourning and weeping in this vale of tears. Turn, then, most gracious advocate, thine eyes of mercy toward us. And after this, our exile, show unto us the blessed fruit of thy womb, Jesus. O clement, O loving, O sweet Virgin Mary. Pray for us, O holy Mother of God, that we may be made worthy of the promises of Christ. Amen."
			},
			{
				"prayerID": 8,
				"prayerName": "O God",
				"prayerText": "O GOD, WHOSE only-begotten Son by His life, death and resurrection, has purchased for us the rewards of eternal life; grant, we beseech Thee, that by meditating upon these mysteries of the Most Holy Rosary of the Blessed Virgin Mary, we may imitate what they contain and obtain what they promise, through the same Christ our Lord. Amen. Pour forth we beseech Thee, O Lord, Thy grace into our hearts, that we to whom the incarnation of Christ, Thy Son, was made known by the message of an angel, may by His passion and cross be brought to the glory of His resurrection, through the same Christ Our Lord. Amen."
			},
	        {
	            "prayerID": 10,
	            "prayerName": "Nicene Creed",
	            "prayerText": "I believe in one God the Father almighty, maker of heaven and earth of all things visible and invisible. I believe in one Lord Jesus Christ, the Only-begotten Son of God, born of the Father before all ages. God from God, Light from Light, true God from true God, begotten, not made, consubstantial with the Father; through Him all things were made. For us men and for our salvation He came down from heaven, and by the Holy Ghost was incarnate of the Virgin Mary, and became man. For our sake He was crucified under Pontius Pilate, He suffered death and was buried, and rose again on the third day in accordance with the Scriptures. He ascended into heaven and is seated at the right hand of the Father. He will come again in glory to judge the living and the dead. His kingdom will have no end. I believe in the Holy Ghost, the Lord, the giver of life who proceeds from the Father and the Son, who with the Father and the Son is adored and glorified, who has spoken through the prophets. I believe in one, holy, catholic, and apostolic Church. I confess one baptism for the forgiveness of sins. I look forward to the resurrection of the dead and the life of the world to come. Amen."
	        }
		]
	}


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
		49: 0,
		50: 79,
		51: 158,
		52: 237,
		48: mysteryOfDay(),
		261: navFwd(accumulatorInput),	## rt arrow
		260: navRev(accumulatorInput),	## lt arrow
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

	centerText(1, maxX, "python-curses")
	screen.addstr(3, 2, "About:", lblUnderline)
	leftJustifyText(5, "A CLI scriptural Rosary using Python and Curses")
	leftJustifyText(6, "by Mezcel, https://github.com/mezcel/python-curses.git")

	screen.addstr(8, 2, "Display:", lblUnderline)
	leftJustifyText(10, "Dynamic resize primarily works on Linux style POSIX terminal types like WSL, Xterm or xfce4-terminal, ect." )
	leftJustifyText(11, "Current display: (" + str(maxX) + "x, " + str(maxY) + "y)." + " | Minimum display: (140x, 40y)" )
	screen.addstr(13, 2, "Instructions:", lblUnderline)
	leftJustifyText(15, "The first mystery defaults to the mystery of the day." )
	leftJustifyText(16, "Reset to a desired mystery. Number Keys (0-4) correspond with: Daily, Joy, Luminous, Sorrow, & Glory." )
	leftJustifyText(17, "Press the right/left arrow keys to navigate forward/reverse." )
	leftJustifyText(18, "Press Q to quit." )

	centerText(maxY - 1, maxX, "(press any key to continue)")
	screen.getch()

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
			and myKeyPress != 48
		): ## rt/lt keys
			screen.erase()
			lblUnderline = curses.A_UNDERLINE
			aboutScreen(lblUnderline)

## Run

if __name__ == '__main__':

	initDisplay()
	myMain()
