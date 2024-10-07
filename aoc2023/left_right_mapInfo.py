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
        row = row.replace(' ', '').replace('(', '').replace(')', '').replace('\n','').replace('\r','')
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
    leftRight = list(leftRight*1000000)
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

def navigateToZ_Ghost(leftRightFull, mapDict, checkUniqueNess = False):
    print('---- navigate to Z$ ----', leftRightFull, mapDict, '\n')
    keys = mapDict['entryPoints']
    uniqueSteps = set()
    jumpCount = 0
    maxIterations = 10000000
    previousDateTime = datetime.now()
    for g in range(maxIterations):
        if jumpCount < 1000:
            print(f'Jumping from last {leftRightFull[-2:]} to first again {leftRightFull[:2]}')
        for h,leftRight in enumerate(leftRightFull):
            for i, leftRight in enumerate(leftRight):
                if jumpCount % 1000000 == 0:
                    print('Jump count: ', jumpCount, round(g/maxIterations*100,2), '% at', datetime.now(), datetime.now() - previousDateTime)
                    previousDateTime = datetime.now()
                for key in keys:
                    if key[-1] != 'Z':
                        if jumpCount < 100:
                            print('Found key that does not end on Z', key)
                        break
                else:
                    return jumpCount
                jumpCount += 1
                keysOld = keys[:]
                keys = []
                for key in keysOld:
                    keys.append(mapDict[key][leftRight])
                if checkUniqueNess:
                    tupleKeys = tuple(keys + [h])
                    if tupleKeys in uniqueSteps:
                        raise ValueError("We've been here before: " + str(tupleKeys), str(uniqueSteps)[:1000])
                    uniqueSteps.add(tupleKeys)
                if jumpCount < 100:
                    print(jumpCount, 'jump', leftRight, 'from ', keysOld, 'to', keys)
    else:
        raise ValueError('value not found in iterations: ' + str(g))
    return i + g*len(leftRightFull)

def getfirstHitsAndFrequencies(leftRightFull, mapDict, checkUniqueNess = False):
    print('---- navigate to Z$ ----', leftRightFull, mapDict, '\n')
    keys = mapDict['entryPoints']
    uniqueSteps = set()
    jumpCount = 0
    maxIterations = 10000000
    previousDateTime = datetime.now()
    firstHits = []
    for key in keys:
        firstHits.append([])
    for g in range(maxIterations):
        # if jumpCount < 1000:
        #     print(f'Jumping from last {leftRightFull[-2:]} to first again {leftRightFull[:2]}')
        for h,leftRight in enumerate(leftRightFull):
            for i, leftRight in enumerate(leftRight):
                if jumpCount % 1000000 == 0:
                    print('Jump count: ', jumpCount, round(g/maxIterations*100,2), '% at', datetime.now(), datetime.now() - previousDateTime)
                    previousDateTime = datetime.now()
                for i, key in enumerate(keys):
                    if key[-1] == 'Z':
                        firstHits[i].append(jumpCount)

                jumpCount += 1
                keysOld = keys[:]
                keys = []
                for key in keysOld:
                    keys.append(mapDict[key][leftRight])
                for i,key in enumerate(keys):
                    if len(firstHits[i]) < 4:
                        break
                else:
                    return firstHits
    else:
        raise ValueError('value not found in iterations: ' + str(g))
    return i + g*len(leftRightFull)

def syncTwoCycles(start1, start2, frequency1, frequency2):
    print(f'Syncing {start1=} {start2=} {frequency1=} {frequency2=}')
    number = frequency1
    while number % frequency2 != 0:
        number += frequency1
    frequency = number

    for i in range(100):
        if ((start1 - start2) % frequency2 == 0) and (start1 >= start2):
            break
        start1 += frequency1
    print(f'Completed sync {start1=} {frequency=}')
    return start1, frequency


def calculateAnswerFromFirstHits(firstHits):
    frequencies = []
    starts = []
    for firstHit in firstHits:
        frequencies.append(firstHit[-1] - firstHit[-2])
        starts.append(firstHit[0])
    start1 = starts[0]
    frequency1 = frequencies[0]
    print(starts, frequencies)
    for i, startItem in enumerate(starts[1:]):
        start1, frequency1 = syncTwoCycles(start1, startItem, frequency1, frequencies[i+1])

    return start1, frequency1
