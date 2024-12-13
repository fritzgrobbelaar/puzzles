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

sampleBad = '''Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176'''.split('\n')

sampleCornerCase = '''Button A: X+1, Y+2
Button B: X+2, Y+4
Prize: X=12748, Y=12176'''.split('\n')

sample1='''Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400'''.split('\n')

sampleCC='''Button A: X+36, Y+42
Button B: X+16, Y+97
Prize: X=4444, Y=12313'''.split('\n')

sampleGoodBig='''Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176'''.split('\n')

#{'Button A': {'X': 36, 'Y': 42, 'cost': 3}, 'Button B': {'X': 16, 'Y': 97, 'cost': 1}, 'Prize': {'X': 10000000004444, 'Y': 10000000012313}}

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
            rowDict[name][distance[0]]= int(distance[1]) +10000000000000
    else:
        rowDict['Button A']['cost'] = 3
        rowDict['Button B']['cost'] = 1
        listOfMachines.append(rowDict)
        rowDict = {}

def location(prize, P1Button, P2Button, P1ButtonPresses, P2ButtonPresses):
    prizeX = prize['X']
    prizeY = prize['Y']
#   print(f'{prize=}, {P1Button=}, {P1ButtonPresses=}, cxt={P1Button['X'] * P1ButtonPresses} cyt={P1Button['Y'] * P1ButtonPresses}, {P2Button=} {P2ButtonPresses=} ext={P2Button['X'] * P2ButtonPresses} eyt={P2Button['Y'] * P2ButtonPresses}'
#        f' xtotal={(P1Button['X'] * P1ButtonPresses) + (P2Button['X'] * P2ButtonPresses)} '
#        f'ytotal={(P1Button['Y'] * P1ButtonPresses) + (P2Button['Y'] * P2ButtonPresses)}')
    if (P1Button['X'] * P1ButtonPresses) + (P2Button['X'] * P2ButtonPresses) > prizeX:
#        print('too high X - switching', (P1Button['X'] * P1ButtonPresses) + (P2Button['X'] * P2ButtonPresses), f'{prizeX=}')
        return 'tooHigh'
    if (P1Button['Y'] * P1ButtonPresses) + (P2Button['Y'] * P2ButtonPresses) > prizeY:
#        print('too high Y - switching', (P1Button['Y'] * P1ButtonPresses) + (P2Button['Y'] * P2ButtonPresses), f'{prizeY=}')
        return 'tooHigh'
    if (P1Button['X'] * P1ButtonPresses) + (P2Button['X'] * P2ButtonPresses) == prizeX and (P1Button['Y'] * P1ButtonPresses) + (P2Button['Y'] * P2ButtonPresses) == prizeY:
#        print('------whoop whoop ------ we found the right one!')
        return 'inSync'
    return 'tooLow'

#assert 'tooHigh' == location({'X': 7870, 'Y': 6450}, {'X': 17, 'Y': 86, 'cost': 3},{'X': 84, 'Y': 37, 'cost': 1}, 10000, 10000 )
#assert 'tooHigh' == location({'X': 7870, 'Y': 6450}, {'X': 17, 'Y': 86, 'cost': 3},{'X': 84, 'Y': 37, 'cost': 1}, 1, 10000 )
#assert 'tooHigh' == location({'X': 7870, 'Y': 6450}, {'X': 17, 'Y': 86, 'cost': 3},{'X': 84, 'Y': 37, 'cost': 1}, 10000, 1 )
#assert 'tooLow' == location({'X': 7870, 'Y': 6450}, {'X': 17, 'Y': 86, 'cost': 3},{'X': 84, 'Y': 37, 'cost': 1}, 1, 1 )
#assert 'inSync' == location({'X': 8400, 'Y': 5400}, {'X': 94, 'Y': 34, 'cost': 3},{'X': 22, 'Y': 67, 'cost': 1}, 80, 40 )

def calculateCost(machine):
    print(f'\n{machine=}')
    priceAX = machine['Button A']['X']/machine['Button A']['cost']
    priceBX = machine['Button B']['X']/machine['Button B']['cost']

    if priceAX < priceBX:
        print(f"Cheapest Button is {machine['Button A']=}")
        cheapButton = machine['Button A']
        expensiveButton = machine['Button B']
        cheapButtonCost = 3
        expensiveButtonCost = 1
    else:
        print(f"Cheapest Button is {machine['Button B']=}")
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

        if cheapButtonPresses == 0:
            print('Reached cheap button presses to 0')
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
        print(f'Cheapest  Button {priceAX}')
        P1Button = machine['Button A']
        P2Button = machine['Button B']
        P1ButtonCost = 3
        P2ButtonCost = 1
    else:
        P1Button = machine['Button B']
        P2Button = machine['Button A']
        P1ButtonCost = 1
        P2ButtonCost = 3

    print(f'{P1Button=} {P2Button=}')

    Xpz = prize['X'] 
    Ypz = prize['Y']
    X_1 = P1Button['X']
    Y_1 = P1Button['Y']
    X_2 = P2Button['X']
    Y_2 = P2Button['Y']

    if X_1/X_2 == Y_1/Y_2:
        raise Exception('We have a corner case')

    P_2 = (Y_1*Xpz - X_1*Ypz)/(X_2*Y_1-X_1*Y_2)

    P_1 = (Ypz-P_2*Y_2)/Y_1

    print(f'Starting point must be close to {P_1=} {P_2=} {P_2*X_2=} {P_2*Y_2=} {P_1*X_1+P_2*X_2=} {P_1*Y_1+P_2*Y_2=}')
    if (P_1 < -1000) or (P_2 < - 100):
        print("This is just a bad spot to start")
        return 0

    limit = X_1
    
    P2ButtonPressesStart = int(P_2) - X_2
    if P2ButtonPressesStart < 0:
        P2ButtonPressesStart=0
    P2ButtonPresses = P2ButtonPressesStart
    # #print(f'{P1ButtonPresses=}')

    P1ButtonPresses = int(P_1)+1
    #testing
    #P1ButtonPresses=42
    #limit=10

    limitCount = 0
    while location(machine['Prize'], P1Button, P2Button, P1ButtonPresses, P2ButtonPresses) != 'inSync':
        P2ButtonPresses = P2ButtonPressesStart
        limitCount += 1

        if P1ButtonPresses <= 0:
            print('Reached P1 button presses to 0')
            return 0
        if limitCount > limit:


#            print(f'{machine['Prize']}, {P1Button}, {P1ButtonPresses=}, {P1Button['X'] * P1ButtonPresses} {P1Button['Y'] * P1ButtonPresses}, {P2Button} {P2ButtonPresses=} {P2Button['X'] * P2ButtonPresses} {P2Button['Y'] * P2ButtonPresses}'
#                  f' {(P1Button['X'] * P1ButtonPresses) + (P2Button['X'] * P2ButtonPresses)} '
#                  f'{(P1Button['Y'] * P1ButtonPresses) + (P2Button['Y'] * P2ButtonPresses)}')
            print(f'Status report  {P2ButtonPresses=}  {P1ButtonPresses=} ')
            print(f'{limit=} reached - stopping search - returning 0')
            return 0
        P1ButtonPresses = P1ButtonPresses-1
        while location(machine['Prize'], P1Button, P2Button, P1ButtonPresses, P2ButtonPresses) == 'tooLow':
            P2ButtonPresses += 1

        #print(f'Lets drop one P1 button press {P1ButtonPresses=}')
    #
    print(f'Status report  {P2ButtonPresses=}  {P1ButtonPresses=} ')
    # #print(location(machine['Prize'], P1Button, P2Button, P1ButtonPresses, P2ButtonPresses) )
    if location(machine['Prize'], P1Button, P2Button, P1ButtonPresses, P2ButtonPresses) != 'inSync':
        print('Not found')
        return 0
    answer = P2ButtonPresses*P2ButtonCost + P1ButtonPresses * P1ButtonCost
    print('Returning', answer)
    return answer



for i,machine in enumerate(listOfMachines):
    print(f'{total=} {i=}')
#    original = calculateCost(machine)
#    print(f'Original',original)
    new = calculateCostAlgebra(machine)
#    if new != original:
#        raise ValueError(f'{new=} does not match {original=}')
    total += new

print(f'{total=}')







