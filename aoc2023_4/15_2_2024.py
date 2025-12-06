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

<^^>>>vv<v>>v<<'''.split('\n')

sample = '''#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^'''.split('\n')

sample = '''##############
##.......#..##
##..........##
##......[]..##
##...[].....##
##...[][]...##
##..........##
##..[][][]..##
##..........##
##...[].[]..##
##..........##
##....[]....##
##..........##
##.....@....##

^^^^^^^'''.split('\n')

sample='''##.....@....##
##..........##
##....[]....##
##..........##
##...[].[]..##
##..........##
##..[][][]..##
##..........##
##...[][]...##
##......[]..##
##...[].....##
##..........##
##.......#..##
##..........##
##############

vvvvvvv'''.split('\n')


sample='''#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^'''.split('\n')

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

#The plan
# Read instructions carefully
# Create a new method - move boxes pyramid - which takes map, boxes pyramid - direction
# boxes pyramid is a list of lists of coordinates - x first, y second
# the attempted move itself - split off in a new method (advantage is that it can take direction as argument - and lessen bugs with switching up/down)
# create a very good test case


def printMap(map):
    # print('map print',steps)
    for j, row in enumerate(map):
        printRow = []
        for i, value in enumerate(row):
            printRow.append(value)
        print('print', ''.join(printRow))


printMap(theMap)


def scaleMap(theMap):
    for y, row in enumerate(theMap):
        newRow = []
        for x, value in enumerate(row):
            if value == '#':
                value = newRow.append('#')
                value = newRow.append('#')
            if value == '.':
                newRow.append('.')
                newRow.append('.')
            if value == 'O':
                newRow.append('[')
                newRow.append(']')
            if value == '@':
                newRow.append('@')
                newRow.append('.')
        theMap[y] = newRow

scaleMap(theMap)
printMap(theMap)


def getStartPosition(theMap):
    for y, row in enumerate(theMap):
        for x, value in enumerate(row):
            if value == '@':
                return (x, y)


robotPosition = getStartPosition(theMap)
print(f'Start position calculated {''.join(moves)=}, {robotPosition=}')

def moveBoxesPyramid(theMap, boxesPyramid, direction):
    boxesPyramid.reverse()
    print(f'Moving {boxesPyramid}')
    for coordinates in boxesPyramid:
        coordinates = list(set(coordinates))
        for coordinate in coordinates:
            x = coordinate[0]
            y = coordinate[1]

            if direction == 'up':
                newY = y-1
            else:
                newY = y+1
            item = theMap[y][x]
            if theMap[newY][x] != '.':
                printMap(theMap)

                print(f'something bad is about to happen {newY=} {x=} {coordinate=} found {theMap[newY][x]=}')
                raise ValueError('Moving to a non-empty block')
            theMap[newY][x] = item
            theMap[y][x] = '.'
    return theMap

#moveBoxesPyramid(theMap,[[(5,3),(6,3)],[]], 'down')

printMap(theMap)


def calculateMove(theMap, robotPosition, move):
    robotX = robotPosition[0]
    robotY = robotPosition[1]

    if move == '^':
        boxesPyramid = [[(robotPosition)]]
        for y in range(robotY - 1, -1, -1):
            boxesPyramid.append([])
            for coordinate in boxesPyramid[-2]:
                x = coordinate[0]
                item = theMap[y][x]
                #print(f'Perhaps we can move {item=}, {robotPosition=} {move=} {y=}')
                if item == '#':
                    print(f'Blockage was reached before any work was done')
                    return theMap, robotPosition
                elif item == '.':
                    pass
                    #print(f'No blockage here {item=}, {robotPosition=} {move=} {y=}')
                elif item == '[':
                    boxesPyramid[-1].append((x,y))
                    boxesPyramid[-1].append((x+1,y))
                elif item == ']':
                    boxesPyramid[-1].append((x,y))
                    boxesPyramid[-1].append((x-1,y))
            if boxesPyramid[-1] == []:
                robotPosition = robotX, robotY - 1
                theMap = moveBoxesPyramid(theMap, boxesPyramid, 'up')
                return theMap, robotPosition

    if move == 'v':
        boxesPyramid = [[(robotPosition)]]
        for y in range(robotY+1,1000, 1):
            boxesPyramid.append([])
            for coordinate in boxesPyramid[-2]:
                x = coordinate[0]
                item = theMap[y][x]
                #print(f'Perhaps we can move {item=}, {robotPosition=} {move=} {y=}')
                if item == '#':
                    print(f'Blockage was reached before any work was done')
                    return theMap, robotPosition
                elif item == '.':
                    pass
                    #print(f'No blockage here {item=}, {robotPosition=} {move=} {y=}')
                elif item == '[':
                    boxesPyramid[-1].append((x,y))
                    boxesPyramid[-1].append((x+1,y))
                elif item == ']':
                    boxesPyramid[-1].append((x,y))
                    boxesPyramid[-1].append((x-1,y))
            if boxesPyramid[-1] == []:
                robotPosition = robotX, robotY + 1
                theMap = moveBoxesPyramid(theMap, boxesPyramid, 'down')
                return theMap, robotPosition

    if move == 'oldDown':
        for y in range(robotY, 1000, 1):
            item = theMap[y][robotX]
            print(f'Perhaps we can move {item=}, {robotPosition=} {move=} {y=}')
            if item == '#':
                print(f'Blockage was reached before anx work was done')
                return theMap, robotPosition
            if item == '.':
                print(f'We can move to {item=}, {robotPosition=} {move=} {y=}, {robotY}')
                robotPosition = robotX, robotY + 1
                for newY in range(y, robotY, -1):
                    item = theMap[newY - 1][robotX]
                    print(f'Moving {item=}, {robotPosition=} {move=} {y=} to {newY=} from {newY-1=}')
                    theMap[newY][robotX] = item
                    theMap[newY - 1][robotX] = '.'
                return theMap, robotPosition



    if move == '<':
        for x in range(robotX - 1, -1, -1):
            item = theMap[robotY][x]
        #    print(f'Perhaps we can move {item=}, {robotPosition=} {move=} {x=} {robotY=}')
            if item == '#':
        #        print(f'Blockage was reached before anx work was done')
                return theMap, robotPosition
            if item == '.':
        #       print(f'We can move to {item=}, {robotPosition=} {move=} {x=}')
                robotPosition = robotX - 1, robotY
                for newX in range(x, robotX, 1):
                    item = theMap[robotY][newX + 1]
         #           print(f'Moving {item=}, {robotPosition=} {move=} {x=}')
                    theMap[robotY][newX] = item
                    theMap[robotY][newX + 1] = '.'
                return theMap, robotPosition

    if move == '>':
        for x in range(robotX, 1000, 1):
            item = theMap[robotY][x]
      #      print(f'Perhaps we can move {item=}, {robotPosition=} {move=} {x=}')
            if item == '#':
       #         print(f'Blockage was reached before anx work was done')
                return theMap, robotPosition
            if item == '.':
      #          print(f'We can move to {item=}, {robotPosition=} {move=} {x=}, {robotX}')
                robotPosition = robotX + 1, robotY
                for newX in range(x, robotX, -1):
                    item = theMap[robotY][newX - 1]
        #            print(f'Moving {item=}, {robotPosition=} {move=} {x=} to {newX=} from {newX-1=}')
                    theMap[robotY][newX] = item
                    theMap[robotY][newX - 1] = '.'
                return theMap, robotPosition


    return theMap, robotPosition

print(f' before {moves=}')
for i, move in enumerate(moves):
    print(f'\nNew move starts {move=}')
    theMap, robotPosition = calculateMove(theMap, robotPosition, move)
    printMap(theMap)

def calculateTotal(theMap):
    total = 0
    for y, row in enumerate(theMap):
        print(f'{total=} {row=} {y=}')
        for x, value in enumerate(row):
            if value == '[':
                total += 100 * y + x
    return total

total = calculateTotal(theMap)
print(f'{total=}')
