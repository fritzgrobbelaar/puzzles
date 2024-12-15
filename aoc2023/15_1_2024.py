import cleaninput
from datetime import datetime
from functools import cmp_to_key

listOfText = cleaninput.getfileInputLinesAsList('input15_2024.txt')

sample = '''##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^'''.split('\n')

sample = '''########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>'''.split('\n')
#>>v
#v<v>>v<<

listOfText = sample
theMap = []
moves = []

mapComplete = False
listOfLists = []
total = 0
for row in listOfText:
    if row == '':
        mapComplete = True
    elif not mapComplete:
        theMap.append(list(row))
    else:
        moves.extend(list(row))

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

def printMap(map):
    #print('map print',steps)
    for j, row in enumerate(map):
        printRow = []
        for i,value in enumerate(row):



                printRow.append(value)
        print('print',''.join(printRow))

printMap(theMap)

def getStartPosition(theMap):
    for y, row in enumerate(theMap):
        for x, value in enumerate(row):
            if value == '@':
                return (x,y)

robotPosition = getStartPosition(theMap)
print(f'{''.join(moves)=}, {robotPosition=}')

def calculateMove(theMap, robotPosition, move):
    robotX = robotPosition[0]
    robotY = robotPosition[1]

    if move == '^':
        for y in range(robotY-1,-1,-1):
            item = theMap[y][robotX]
            print(f'Perhaps we can move {item=}, {robotPosition=} {move=} {y=}')
            if item == '#':
                print(f'Blockage was reached before any work was done')
                return theMap, robotPosition
            if item == '.':
                print(f'We can move to {item=}, {robotPosition=} {move=} {y=}')
                robotPosition = robotX, robotY-1
                for newY in range(y, robotY, 1):
                    item = theMap[newY+1][robotX]
                    print(f'Moving {item=}, {robotPosition=} {move=} {y=}')
                    theMap[newY][robotX] = item
                    theMap[newY+1][robotX] = '.'
                return theMap, robotPosition

    if move == '<':
        for x in range(robotX-1,-1,-1):
            item = theMap[x][robotY]
            print(f'Perhaps we can move {item=}, {robotPosition=} {move=} {x=}')
            if item == '#':
                print(f'Blockage was reached before anx work was done')
                return theMap, robotPosition
            if item == '.':
                print(f'We can move to {item=}, {robotPosition=} {move=} {x=}')
                robotPosition = robotY, robotX-1
                for newX in range(x, robotX, 1):
                    item = theMap[newX+1][robotY]
                    print(f'Moving {item=}, {robotPosition=} {move=} {x=}')
                    theMap[newX][robotY] = item
                    theMap[newX+1][robotY] = '.'
                return theMap, robotPosition

    if move == '>':
        for x in range(robotX+1,1000,1):
            item = theMap[x][robotY]
            print(f'Perhaps we can move {item=}, {robotPosition=} {move=} {x=}')
            if item == '#':
                print(f'Blockage was reached before anx work was done')
                return theMap, robotPosition
            if item == '.':
                print(f'We can move to {item=}, {robotPosition=} {move=} {x=}')
                robotPosition = robotY, robotX-1
                for newX in range(x, robotX, 1):
                    item = theMap[newX+1][robotY]
                    print(f'Moving {item=}, {robotPosition=} {move=} {x=}')
                    theMap[newX][robotY] = item
                    theMap[newX+1][robotY] = '.'
                return theMap, robotPosition


    return theMap, robotPosition

for i,move in enumerate(moves):
    print(f'\nNew move starts {move=}')
    theMap, robotPosition = calculateMove(theMap, robotPosition, move)
    printMap(theMap)

exit()




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
                if calculateStep(height, newStep, map):
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
