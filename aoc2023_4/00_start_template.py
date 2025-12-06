import cleaninput
from datetime import datetime
from functools import cmp_to_key

listOfText = cleaninput.getfileInputLinesAsList('input14_2024.txt')

sample = '''.....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9....'''.split('\n')


#listOfText = sample

listOfLists = []
total = 0
for row in listOfText:
    listOfLists.append(list(row))

sequence = {}
def sortFunc(key,key2):
    if key in sequence.keys():
        if key2 in sequence[key]:
            return -1
    return 0

def fixOrder(row):
    print('Sorting row', row)
    row.sort(key=cmp_to_key(sortFunc))
    print('sorted row', row)
    return row

def printMap(map, steps):
    #print('map print',steps)
    for j, row in enumerate(map):
        printRow = []
        for i,value in enumerate(row):
            found=False
            for h,steprow in enumerate(steps):
                for step in steprow:
                    if j == step[0] and i == step[1]:
                        #print(f'map print {i=} {j=} {step=}')
                        printRow.append(str(h))
                        found=True
                        break
            if not found:
                printRow.append('.')
     #   print('map print',''.join(printRow))

def calculateStep(robot, roomX, roomY):
    newX = robot['v'][0] + robot['p'][0]
    newY = robot['v'][1] + robot['p'][1]
    #print(f'\nCalculated{newX=} {newY=}')

    maxX = roomX - 1
    maxY = roomY - 1
    if newX < 0:
        newX = roomX + newX
    #   print(f'too left, {newX=}')
    elif newX > maxX:
        #  print(f'too right, {newX=}')
        newX = newX - roomX

    if newY < 0:
        #        print(f'too up, {newY=}')
        newY = roomY + newY

    elif newY > maxY:
        # print(f'too below, {newY=}')
        newY = newY - roomY

    newPosition = (newX, newY)
    #print(f'{newPosition=}')

    robot['p'] = newPosition
    #printMap(roomX, roomY, [robot])

    return robot


def calculateTrailHeads(x, y, map):
    steps = [[(x, y)]]

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for height in range(1, 10):
        steps.append([])
        for step in steps[-2]:
            #print(f'\n{step=} {height=} {steps=}')
            stepI = step[0]
            stepJ = step[1]
            for direction in directions:
                newStep = (stepI + direction[0], stepJ + direction[1])
                #print(f'{newStep=}')
                if validateStep(height, newStep, map):
                    steps[-1].append(newStep)
        #steps[-1] = list(set(steps[-1]))
        #print(f'{steps=}')
        printMap(map, steps)
    return len(steps[-1])


#assert 1 == calculateTrailHeads(0, 0, listOfLists)

for y, row in enumerate(listOfLists):
    print(f'{total=} {row=} {y=}')
    for x,value in enumerate(row):
        if value == '0':
            #print(f'{total=} {row=} {x=} {y=}')
            total += calculateTrailHeads(x, y, listOfLists)

print(f'{total=}')
