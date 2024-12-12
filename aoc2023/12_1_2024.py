import cleaninput
from datetime import datetime
from functools import cmp_to_key
import copy
listOfText = cleaninput.getfileInputLinesAsList('input12_2024.txt')

sample = '''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE'''.split('\n')



#listOfText = sample

listOfLists = []
total = 0
for row in listOfText:
    listOfLists.append(list(row))

knownRegions = set()
def printMap(map, knownRegions):
    print('\nmap print', knownRegions)
    for y, row in enumerate(map):
        printRow = []
        for x,value in enumerate(row):
            if (x,y) in knownRegions:
                printRow.append('#')
            else:
                printRow.append('.')
        print('map print',''.join(printRow))

def validateStep(letter, step, map):
    maxX = len(map[0]) - 1
    maxY = len(map[1]) - 1
    if step in knownRegions:
        return False
    if step[0] < 0:
        #print(f'too left, {step=}')
        return False
    if step[1] < 0:
        #print(f'too up, {step=}')
        return False

    if step[0] > maxX:
        # print(f'too right, {step=}')
        return False

    if step[1] > maxY:
        #  print(f'too below, {step=}')
        return False
    if not letter == map[step[1]][step[0]]:
        #   print(f'wrong {letter=}=} {map[step[1]][step[0]]=}')
        return False
    #print(f'seems good {step=} {letter=}')
    return True

#assert False == validateStep('B', (0,0), listOfLists)
#assert True == validateStep('A', (0,0), listOfLists)

def calculateFenceLength(region):
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    fenceLength = 0
    for point in region:
        for direction in directions:
            if (point[0] + direction[0], point[1] + direction[1]) not in region:
                fenceLength += 1
    return fenceLength

assert 10 == calculateFenceLength([(3, 2), (3, 3), (2, 1), (2, 2)])

printMap(listOfLists, knownRegions)
def calculateRegion(x, y, map):

    region = [[(x, y)]]
    knownRegions.add((x,y))
    currentRegion = set()
    currentRegion.add((x,y))
    regionTotal = 0

    letter = listOfLists[y][x]
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    fenceLength = 0
    allCalculationsExhausted = False
    while region[-1] != []:
        #print(f'\n While loop {region[-1]=}')
        region.append([])
        for step in copy.deepcopy(region[-2]):


            #print(f'Taking a step {step=} {letter=} {region=}')
            stepX = step[0]
            stepY = step[1]
            for direction in directions:
                newStep = (stepX + direction[0], stepY + direction[1])
                #print(f'{newStep=}')
                if validateStep(letter, newStep, map):
                    #print(f'Adding {newStep=} to {region=}')
                    region[-1].append(newStep)
                    knownRegions.add(newStep)
                    currentRegion.add(newStep)

            #steps[-1] = list(set(steps[-1]))
            print(f'{region=}')

    fenceLength = calculateFenceLength(currentRegion)
    print(f'Region calculated completely regionSize is {len(currentRegion)=} {currentRegion=} {letter=}')
    printMap(map, knownRegions)
    return fenceLength*len(currentRegion)


#assert 1 == calculateTrailHeads(0, 0, listOfLists)

for y, row in enumerate(listOfLists):
    print(f'{total=} {y=}')
    for x,value in enumerate(row):
        if (x,y) not in knownRegions:
            #print(f'{total=} {row=} {x=} {y=}')
            total += calculateRegion(x, y, listOfLists)

print(f'{total=}')
