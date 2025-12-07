import cleaninput
from datetime import datetime
from functools import cmp_to_key

listOfText = cleaninput.getfileInputLinesAsList('input16_2024.txt')

sample='''###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############'''.split('\n')

listOfText = sample

listOfLists = []
total = 0
for row in listOfText:
    listOfLists.append(list(row))


def printMap(map, steps):
    #print('map print',steps)
    for j, row in enumerate(map):
        printRow = []
        for i,value in enumerate(row):
            found=False
            for h,steprow in enumerate(steps):
                for step in steprow:
                    #print(f'map print {i=} {j=} {step=}')
                    if j == step[1] and i == step[0]:
                       # print(f'map print {i=} {j=} {step=}')
                        printRow.append('0')
                        #printRow.append(str(h))
                        found=True
                        break
            if not found:
                printRow.append(value)
        print('map print',''.join(printRow))
    print()

def findStart(listOfLists):
    for j, row in enumerate(listOfLists):
        for i, value in enumerate(row):
            if value == 'S':
                start=(i,j)
                return start

def validateStep(step, map):
    printMap(map, [[step]])

    maxI = len(map[0]) - 1
    maxJ = len(map[1]) - 1
    if step[0] < 0:
        #print(f'too left, {step=}')
        return False
    if step[1] < 0:
        #print(f'too up, {step=}')
        return False

    if step[0] > maxI:
       # print(f'too right, {step=}')
        return False

    if step[1] > maxJ:
      #  print(f'too below, {step=}')
        return False
    if map[step[0]][ step[1]] == '#':
        return False
    #print(f'seems good {step=} {height=}')
    return True


def calculateTrailHeads(x, y, map):
    steps = [[(x, y)]]
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    for direction in directions:
        newStep = (x + direction[0], y + direction[1])
        if validateStep(newStep, map):
            steps[-1].append(newStep)
        steps[-1] = list(set(steps[-1]))
        #print(f'{steps=}')
    return len(steps[-1])


#assert 1 == calculateTrailHeads(0, 0, listOfLists)
start=findStart(listOfLists)
print(f'{start=}')

steps = [start]
counter = 0
while counter < 3:
    counter = counter + 1
    for step in steps:
        steps = calculateTrailHeads(step[0],step[1],listOfLists)
printMap(listOfLists, [[start]])

printMap(listOfLists, steps)
exit()
for y, row in enumerate(listOfLists):
    print(f'{total=} {row=} {y=}')
    for x,value in enumerate(row):
        if value == '0':
            #print(f'{total=} {row=} {x=} {y=}')
            total += calculateTrailHeads(x, y, listOfLists)

print(f'{total=}')
