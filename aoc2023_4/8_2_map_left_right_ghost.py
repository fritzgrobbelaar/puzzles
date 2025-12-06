from lib.left_right_mapInfo import *
from lib import cleaninput
from datetime import datetime
started = datetime.now()

input1 = '''LR

            11A = (11B, XXX)
            11B = (XXX, 11Z)
            11Z = (11B, XXX)
            22A = (22B, XXX)
            22B = (22C, 22C)
            22C = (22Z, 22Z)
            22Z = (22B, 22B)
            XXX = (XXX, XXX)'''.split('\n')

fileInput = cleaninput.getfileInputLinesAsList('aoc2023\\input8_map_left_right.txt')
print("Read file at", datetime.now())
listOfText = fileInput
#listOfText = input1
actualMap = getMapInfo(listOfText)
ghostMap = convertMapInfoToGhostEntriesAndExits(actualMap)
firstHits = getfirstHitsAndFrequencies(listOfText[0], ghostMap)
print('firstHits:', firstHits)
syncedNumber, frequency = calculateAnswerFromFirstHits(firstHits)
print('syncedNumber:', syncedNumber)
print('endend', datetime.now(), started, datetime.now() - started)