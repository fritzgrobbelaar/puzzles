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

sample = '''Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176'''.split('\n')

sampleCornerCase = '''Button A: X+1, Y+2
Button B: X+2, Y+4
Prize: X=12748, Y=12176'''.split('\n')


listOfText = sample


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
            rowDict[name][distance[0]]= int(distance[1])#+10000000000000
    else:
        rowDict['Button A']['cost'] = 3
        rowDict['Button B']['cost'] = 1
        listOfMachines.append(rowDict)
        rowDict = {}

def location(prize, cheapButton, expensiveButton, cheapButtonPresses, expensiveButtonPresses):
    prizeX = prize['X']
    prizeY = prize['Y']
    print(f'{prize=}, {cheapButton}, {cheapButtonPresses=}, cxt={cheapButton['X'] * cheapButtonPresses} cyt={cheapButton['Y'] * cheapButtonPresses}, {expensiveButton} {expensiveButtonPresses=} ext={expensiveButton['X'] * expensiveButtonPresses} eyt={expensiveButton['Y'] * expensiveButtonPresses}'
          f' xtotal={(cheapButton['X'] * cheapButtonPresses) + (expensiveButton['X'] * expensiveButtonPresses)} '
          f'ytotal={(cheapButton['Y'] * cheapButtonPresses) + (expensiveButton['Y'] * expensiveButtonPresses)}')
    if (cheapButton['X'] * cheapButtonPresses) + (expensiveButton['X'] * expensiveButtonPresses) > prizeX:
        print('too high X - switching', (cheapButton['X'] * cheapButtonPresses) + (expensiveButton['X'] * expensiveButtonPresses), f'{prizeX=}')
        return 'tooHigh'
    if (cheapButton['Y'] * cheapButtonPresses) + (expensiveButton['Y'] * expensiveButtonPresses) > prizeY:
        print('too high Y - switching', (cheapButton['Y'] * cheapButtonPresses) + (expensiveButton['Y'] * expensiveButtonPresses), f'{prizeY=}')
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

    limit =  cheapButton['X']*expensiveButton['X'] + cheapButton['Y'] * expensiveButton['Y']

    cheapButtonPresses = int(machine['Prize']['X']/cheapButton['X'])
    expensiveButtonPresses = 0
    #print(f'{cheapButtonPresses=}')
    limitCount = 0
    while location(machine['Prize'], cheapButton, expensiveButton, cheapButtonPresses, expensiveButtonPresses) != 'inSync':
        limitCount += 1
        if cheapButtonPresses == 0:
            print('Reached cheap button presses to 0')
            break
        if limitCount > limit:
            print(f'{limit=} reached - stopping search')

            print(f'{machine['Prize']}, {cheapButton}, {cheapButtonPresses=}, {cheapButton['X'] * cheapButtonPresses} {cheapButton['Y'] * cheapButtonPresses}, {expensiveButton} {expensiveButtonPresses=} {expensiveButton['X'] * expensiveButtonPresses} {expensiveButton['Y'] * expensiveButtonPresses}'
                  f' {(cheapButton['X'] * cheapButtonPresses) + (expensiveButton['X'] * expensiveButtonPresses)} '
                  f'{(cheapButton['Y'] * cheapButtonPresses) + (expensiveButton['Y'] * expensiveButtonPresses)}')
            break
        cheapButtonPresses = cheapButtonPresses-1
        while location(machine['Prize'], cheapButton, expensiveButton, cheapButtonPresses, expensiveButtonPresses) == 'tooLow':
            expensiveButtonPresses += 1

    print(f'Status report  {expensiveButtonPresses=} {expensiveButtonCost=} {cheapButtonPresses=}  {cheapButtonCost=}')
    #print(location(machine['Prize'], cheapButton, expensiveButton, cheapButtonPresses, expensiveButtonPresses) )
    if location(machine['Prize'], cheapButton, expensiveButton, cheapButtonPresses, expensiveButtonPresses) != 'inSync':
        #print('Not found')
        return 0
    return expensiveButtonPresses*expensiveButtonCost + cheapButtonPresses * cheapButtonCost

def calculateCostAlgebra(machine):
    print(f'\nNew logic: {machine=}')

    priceAX = machine['Button A']['X']/machine['Button A']['cost']
    priceBX = machine['Button B']['X']/machine['Button B']['cost']
    prize = machine['Prize']
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

    Xpz = prize['X']
    Ypz = prize['Y']
    X_1 = cheapButton['X']
    Y_1 = cheapButton['Y']
    X_2 = expensiveButton['X']
    Y_2 = expensiveButton['Y']

    if X_1/X_2 == Y_1/Y_2:
        raise Exception('We have a corner case')

    P_2 = (Y_1*Ypz - X_1*Xpz)/(X_2*Y_1-X_1*Y_2)

    P_1 = (Xpz-P_2*Y_2)/Y_1

    print(f'Starting point must be close to {P_1=} {P_2=} {P_2*X_2=} {P_2*Y_2=} {P_1*X_1+P_2*X_2} {P_1*Y_1+P_2*Y_2}')
    limit =  cheapButton['X']*expensiveButton['X'] + cheapButton['Y'] * expensiveButton['Y']
    cheapButtonPresses = int(P_1)
    expensiveButtonPresses = int(P_2) - cheapButton['X']*expensiveButton['X'] + cheapButton['Y'] * expensiveButton['Y']
    if expensiveButtonPresses > 0:
        expensiveButtonPresses=0
    # #print(f'{cheapButtonPresses=}')
    limitCount = 0
    while location(machine['Prize'], cheapButton, expensiveButton, cheapButtonPresses, expensiveButtonPresses) != 'inSync':
        limitCount += 1
        if cheapButtonPresses == 0:
            print('Reached cheap button presses to 0')
            break
        if limitCount > limit:
            print(f'{limit=} reached - stopping search')

            print(f'{machine['Prize']}, {cheapButton}, {cheapButtonPresses=}, {cheapButton['X'] * cheapButtonPresses} {cheapButton['Y'] * cheapButtonPresses}, {expensiveButton} {expensiveButtonPresses=} {expensiveButton['X'] * expensiveButtonPresses} {expensiveButton['Y'] * expensiveButtonPresses}'
                  f' {(cheapButton['X'] * cheapButtonPresses) + (expensiveButton['X'] * expensiveButtonPresses)} '
                  f'{(cheapButton['Y'] * cheapButtonPresses) + (expensiveButton['Y'] * expensiveButtonPresses)}')
            break
        cheapButtonPresses = cheapButtonPresses-1
        while location(machine['Prize'], cheapButton, expensiveButton, cheapButtonPresses, expensiveButtonPresses) == 'tooLow':
            expensiveButtonPresses += 1
    #
    # #print(f'Status report  {expensiveButtonPresses=} {expensiveButtonCost=} {cheapButtonPresses=}  {cheapButtonCost=}')
    # #print(location(machine['Prize'], cheapButton, expensiveButton, cheapButtonPresses, expensiveButtonPresses) )
    # if location(machine['Prize'], cheapButton, expensiveButton, cheapButtonPresses, expensiveButtonPresses) != 'inSync':
    #     #print('Not found')
    #     return 0
    return expensiveButtonPresses*expensiveButtonCost + cheapButtonPresses * cheapButtonCost



for i,machine in enumerate(listOfMachines):
    print(f'{total=} {i=}')
    print(f'Original',calculateCost(machine))
    total += calculateCostAlgebra(machine)

print(f'{total=}')







