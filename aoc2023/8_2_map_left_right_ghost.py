from lib.left_right_mapInfo import *
from lib import cleaninput
from datetime import datetime

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
actualMap = getMapInfo(listOfText)
print("Got actual Map at", datetime.now())
ghostMap = convertMapInfoToGhostEntriesAndExits(actualMap)
print("Converted Map at", datetime.now())
pathsCount = navigateToZ_Ghost(listOfText[0], ghostMap, checkUniqueNess=False)
#gave up on 42000000
print('Result:', pathsCount)