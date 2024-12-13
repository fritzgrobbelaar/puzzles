import cleaninput
from datetime import datetime
from functools import cmp_to_key
import copy
listOfText = cleaninput.getfileInputLinesAsList('input13_2024.txt')

sample = '''Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279'''.split('\n')


#listOfText = sample


listOfText.append('')
listOfMachines = []
total = 0
rowDict = {}
for row in listOfText:
#    print(f'{row=}')
    if row.startswith('Button'):
        row = row.split(':')
        buttonName = row[0]
        distances = row[1].split(',')
 #       print(f'{row=} {distances=}')
        rowDict[buttonName] = {}
        for distance in distances:
            distance = distance.strip().split('+')
            rowDict[buttonName][distance[0]] = int(distance[1])
    elif row.startswith('Prize'):
        row = row.split(':')
        name = row[0]
        distances = row[1].split(',')
        rowDict[name] = {}
        for distance in distances:
            distance = distance.strip().split('=')
            rowDict[name][distance[0]]= int(distance[1])
    else:
        rowDict['Button A']['cost'] = 3
        rowDict['Button B']['cost'] = 1
        listOfMachines.append(rowDict)
        rowDict = {}

def location(prize, cheapButton, expensiveButton, cheapButtonPresses, expensiveButtonPresses):
    prizeX = prize['X']
    prizeY = prize['Y']
    if (cheapButton['X'] * cheapButtonPresses) + (expensiveButton['X'] * expensiveButtonPresses) > prizeX:
        return 'tooHigh'
    if (cheapButton['Y'] * cheapButtonPresses) + (expensiveButton['Y'] * expensiveButtonPresses) > prizeY:
        return 'tooHigh'
    if (cheapButton['X'] * cheapButtonPresses) + (expensiveButton['X'] * expensiveButtonPresses) == prizeX and (cheapButton['Y'] * cheapButtonPresses) + (expensiveButton['Y'] * expensiveButtonPresses) == prizeY:
        return 'inSync'
    return 'tooLow'

assert 'tooHigh' == location({'X': 7870, 'Y': 6450}, {'X': 17, 'Y': 86, 'cost': 3},{'X': 84, 'Y': 37, 'cost': 1}, 10000, 10000 )
assert 'tooHigh' == location({'X': 7870, 'Y': 6450}, {'X': 17, 'Y': 86, 'cost': 3},{'X': 84, 'Y': 37, 'cost': 1}, 1, 10000 )
assert 'tooHigh' == location({'X': 7870, 'Y': 6450}, {'X': 17, 'Y': 86, 'cost': 3},{'X': 84, 'Y': 37, 'cost': 1}, 10000, 1 )
assert 'tooLow' == location({'X': 7870, 'Y': 6450}, {'X': 17, 'Y': 86, 'cost': 3},{'X': 84, 'Y': 37, 'cost': 1}, 1, 1 )
assert 'inSync' == location({'X': 8400, 'Y': 5400}, {'X': 94, 'Y': 34, 'cost': 3},{'X': 22, 'Y': 67, 'cost': 1}, 80, 40 )

def calculateCost(machine):
    print(f'\n{machine=}')
    priceAX = machine['Button A']['X']/machine['Button A']['cost']
    priceBX = machine['Button B']['X']/machine['Button B']['cost']

    if priceAX < priceBX:
        print(f'Cheapest Button {priceAX}')
        cheapButton = machine['Button A']
        expensiveButton = machine['Button B']
        cheapButtonCost = 3
        expensiveButtonCost = 1
    else:
        cheapButton = machine['Button B']
        expensiveButton = machine['Button A']
        cheapButtonCost = 1
        expensiveButtonCost = 3

    print(f'{cheapButton=} {expensiveButton=}')

    cheapButtonPresses = int(machine['Prize']['X']/cheapButton['X'])
    expensiveButtonPresses = 0
    #print(f'{cheapButtonPresses=}')
    while location(machine['Prize'], cheapButton, expensiveButton, cheapButtonPresses, expensiveButtonPresses) != 'inSync':
        if cheapButtonPresses == 0:
            print('Reached cheap button presses to 0')
            break
        cheapButtonPresses = cheapButtonPresses-1
        while location(machine['Prize'], cheapButton, expensiveButton, cheapButtonPresses, expensiveButtonPresses) == 'tooLow':
            expensiveButtonPresses += 1

    #print(f'Status report  {expensiveButtonPresses=} {expensiveButtonCost=} {cheapButtonPresses=}  {cheapButtonCost=}')
    #print(location(machine['Prize'], cheapButton, expensiveButton, cheapButtonPresses, expensiveButtonPresses) )
    if location(machine['Prize'], cheapButton, expensiveButton, cheapButtonPresses, expensiveButtonPresses) != 'inSync':
        #print('Not found')
        return 0
    return expensiveButtonPresses*expensiveButtonCost + cheapButtonPresses * cheapButtonCost




for i,machine in enumerate(listOfMachines):
    print(f'{total=} {i=}')
    total += calculateCost(machine)

print(f'{total=}')








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


