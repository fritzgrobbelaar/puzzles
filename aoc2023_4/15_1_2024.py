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

sample2 = '''########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<'''.split('\n')

#

#listOfText = sample
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
        #print('print',''.join(printRow))

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
            item = theMap[robotY][x]
            print(f'Perhaps we can move {item=}, {robotPosition=} {move=} {x=} {robotY=}')
            if item == '#':
                print(f'Blockage was reached before anx work was done')
                return theMap, robotPosition
            if item == '.':
                print(f'We can move to {item=}, {robotPosition=} {move=} {x=}')
                robotPosition = robotX-1, robotY
                for newX in range(x, robotX, 1):
                    item = theMap[robotY][newX+1]
                    print(f'Moving {item=}, {robotPosition=} {move=} {x=}')
                    theMap[robotY][newX] = item
                    theMap[robotY][newX+1] = '.'
                return theMap, robotPosition

    if move == '>':
        for x in range(robotX,1000,1):
            item = theMap[robotY][x]
            print(f'Perhaps we can move {item=}, {robotPosition=} {move=} {x=}')
            if item == '#':
                print(f'Blockage was reached before anx work was done')
                return theMap, robotPosition
            if item == '.':
                print(f'We can move to {item=}, {robotPosition=} {move=} {x=}, {robotX}')
                robotPosition = robotX+1,robotY
                for newX in range( x,robotX,  -1):
                    item = theMap[robotY][newX-1]
                    print(f'Moving {item=}, {robotPosition=} {move=} {x=} to {newX=} from {newX-1=}')
                    theMap[robotY][newX] = item
                    theMap[robotY][newX-1] = '.'
                return theMap, robotPosition

    if move == 'v':
        for y in range(robotY,1000,1):
            item = theMap[y][robotX]
            print(f'Perhaps we can move {item=}, {robotPosition=} {move=} {y=}')
            if item == '#':
                print(f'Blockage was reached before anx work was done')
                return theMap, robotPosition
            if item == '.':
                print(f'We can move to {item=}, {robotPosition=} {move=} {y=}, {robotY}')
                robotPosition = robotX,robotY+1
                for newY in range( y,robotY,  -1):
                    item = theMap[newY-1][robotX]
                    print(f'Moving {item=}, {robotPosition=} {move=} {y=} to {newY=} from {newY-1=}')
                    theMap[newY][robotX] = item
                    theMap[newY-1][robotX] = '.'
                return theMap, robotPosition


    return theMap, robotPosition

for i,move in enumerate(moves):
    print(f'\nNew move starts {move=}')
    theMap, robotPosition = calculateMove(theMap, robotPosition, move)
    printMap(theMap)

total = 0
for y, row in enumerate(theMap):
    print(f'{total=} {row=} {y=}')
    for x,value in enumerate(row):
        if value == 'O':
            total += 100*y + x

print(f'{total=}')
