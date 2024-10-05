""" Input Examples:
Map:
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)

Ghost map:
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
"""
from datetime import datetime
import math


def getMapInfo(input):
    mapInfo = input[2:]
    mapDict = {}

    for i, row in enumerate(mapInfo):
        row = row.replace(' ', '').replace('(', '').replace(')', '').replace('\n', '').replace('\r', '')
        if not row:
            continue
        key_values = row.split('=')
        key = key_values[0]
        values = key_values[1].split(',')
        mapDict[key] = {'L': values[0], 'R': values[1]}
    mapDict['entryPoint'] = 'AAA'
    mapDict['exitPoint'] = 'ZZZ'
    return mapDict


def convertMapInfoToGhostEntriesAndExits(mapDict):
    mapDict['entryPoints'] = []
    mapDict['exitPoints'] = []
    del mapDict['entryPoint']
    del mapDict['exitPoint']
    for key in mapDict.keys():
        if key[-1] == 'A':
            mapDict['entryPoints'].append(key)
        elif key[-1] == 'Z':
            mapDict['exitPoints'].append(key)
    return mapDict


def navigateToZZZ(leftRight, mapDict):
    print('---- navigate to ZZZ ----', leftRight, mapDict, '\n')
    leftRight = list(leftRight * 1000000)
    key = mapDict['entryPoint']
    for i, leftRight in enumerate(leftRight):
        if key == mapDict['exitPoint']:
            break
        keyOld = key[:]
        key = mapDict[key][leftRight]
        if i < 100:
            print(i, 'jump', leftRight, 'from ', keyOld, 'to', key)
    else:
        raise ValueError('value not found in iterations: ' + str(i))
    return i


def navigateToZ_Ghost(leftRightFull, mapDict, checkUniqueNess=False, maxIterations=100000000000):
    print('---- navigate to Z$ ----', leftRightFull, mapDict, '\n')
    keys = mapDict['entryPoints']
    exitpoints = set(mapDict['exitPoints'])
    print('exitpoints:', exitpoints)
    lenKeys = len(keys)
    uniqueSteps = set()
    leftRightLen = len(leftRightFull)
    print('left right len', leftRightLen)
    jumpCount = 0

    keys = ['PQB', 'LGL', 'FVP', 'FRJ', 'KSV', 'LXM']
    startIteration = 5960000

    previousDateTime = datetime.now()
    for j in range(startIteration, maxIterations):
        for i, leftRight in enumerate(leftRightFull):
            if j % 10000 == 0:
                if i == 0:
                    print(f'Dumping info: {i=}, {j=}, {keys=}, {j*leftRightLen+i=}', 'Jump count: ', j, round(j / maxIterations * 100, 2), '% at', datetime.now(),
                          datetime.now() - previousDateTime)
                    previousDateTime = datetime.now()
            if keys[0] in exitpoints and \
                    keys[1] in exitpoints and \
                    keys[2] in exitpoints and \
                    keys[3] in exitpoints and \
                    keys[4] in exitpoints and \
                    keys[5] in exitpoints:
                    return j,i
            keys = [
                mapDict[keys[0]][leftRight],
                mapDict[keys[1]][leftRight],
                mapDict[keys[2]][leftRight],
                mapDict[keys[3]][leftRight],
                mapDict[keys[4]][leftRight],
                mapDict[keys[5]][leftRight]
            ]
    else:
        print(f'Dumping info: {j=}, {i=}, {jumpCount=}, {keys=}')
        raise ValueError('value not found in iterations: ' + str(g))
    return i + g * len(leftRightFull)
