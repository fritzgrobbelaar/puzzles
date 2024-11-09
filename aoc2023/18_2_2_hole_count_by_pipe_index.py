import cleaninput
from text_grid import countDotsSurroundedByPipes

listOfText_Puzzle = cleaninput.getfileInputLinesAsList('input18.txt')

listOfText_Sample1 = '''R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)'''.split('\n')

listOfText_Sample2 = '''L 6 (#70c710)
D 5 (#0dc571)
R 2 (#5713f0)
D 2 (#d2c081)
L 2 (#59c680)
D 2 (#411b91)
R 5 (#8ceee2)
U 2 (#caa173)
R 1 (#1b58a2)
U 2 (#caa171)
L 2 (#7807d2)
U 3 (#a77fa3)
R 2 (#015232)
U 2 (#7a21e3)'''.split('\n')

listOfText = listOfText_Puzzle
listOfText = listOfText_Sample1
# listOfText = listOfText_Sample2

grid = []


def printAndBuildGrid(points):
    # print('\n-- print grid')
    minX = 0
    maxX = 0
    minY = 0
    maxY = 0
    for point in points:
        x = point[0]
        y = point[1]
        if x < minX:
            minX = x
        if x > maxX:
            maxX = x
        if y < minY:
            minY = y
        if y > maxY:
            maxY = y
    width = maxX - minX
    height = maxY - minY
    grid = []
    print(f'\nprint grid old {height=} {width=}')
    for i in range(height + 1):
        row = []
        for j in range(width + 1):
            row.append('.')
        grid.append(row)

    for point in points:
        y = point[1] - minY
        x = point[0] - minX
        p = point[2]
        grid[y][x] = p

    for row in grid:
        print(''.join(row))
    return grid


def getGridFull(listOfText, approachingStartDirection, firstElbow):
    elbows = {}
    points = []
    point = (0, 0)
    points.append(point)
    prevD = approachingStartDirection
    for row in listOfText:
        x = point[0]
        y = point[1]
        rowList = row.split(' ')
        d = rowList[0]
        dis = int(rowList[1])

        for i in range(dis):
            if i == 0:
                if d == 'R':
                    if prevD == 'U':
                        p = 'F'
                    else:
                        p = 'L'
                elif d == 'L':
                    if prevD == 'U':
                        p = '7'
                        # print(f'Adding 7 at {x=} {y=} {row=} {d=} {prevD=}')
                    elif prevD == 'D':
                        p = 'J'
                    else:
                        raise ValueError('this is unexpected')

                elif d == 'U':
                    if prevD == 'L':
                        p = 'L'
                    else:
                        p = 'J'

                elif d == 'D':
                    if prevD == 'L':
                        p = 'F'
                    else:
                        p = '7'

            elif (d == 'R') or (d == 'L'):
                p = '-'
            elif (d == 'U') or (d == 'D'):
                p = '|'
            if d == 'R':
                x += 1
            if d == 'L':
                x -= 1
            if d == 'D':
                y += 1
            if d == 'U':
                y -= 1
            point = (x, y)
            prevD = d
            points[-1] = points[-1][0], points[-1][1], p
            points.append(point)

    points[-1] = points[-1][0], points[-1][1], firstElbow  # Remember to check starting condition
    return points, elbows


def getGridEfficient(listOfText):
    elbows = {}
    points = []
    point = (0, 0)
    points.append(point)
    prevD = listOfText[-1][0]
    for row in listOfText:
        x = point[0]
        y = point[1]
        rowList = row.split(' ')
        d = rowList[0]
        dis = int(rowList[1])

        if d == 'R':
            if prevD == 'U':
                p = 'F'
            else:
                p = 'L'
        elif d == 'L':
            if prevD == 'U':
                p = '7'
                # print(f'Adding 7 at {x=} {y=} {row=} {d=} {prevD=}')
            elif prevD == 'D':
                p = 'J'
            else:
                raise ValueError('this is unexpected')

        elif d == 'U':
            if prevD == 'L':
                p = 'L'
            else:
                p = 'J'

        elif d == 'D':
            if prevD == 'L':
                p = 'F'
            else:
                p = '7'

        elif (d == 'R') or (d == 'L'):
            p = '-'
        elif (d == 'U') or (d == 'D'):
            p = '|'
        if d == 'R':
            x += dis
        if d == 'L':
            x -= dis
        if d == 'D':
            y += dis
        if d == 'U':
            y -= dis
        point = (x, y)
        prevD = d
        points[-1] = points[-1][0], points[-1][1], p
        points.append(point)
    points.pop(-1)
    return points


def countDotsSurroundedByPipesByElbow(elbows, includeBoundary=True):
    from math import inf

    # sort elbows from top to bottom and then left to right:
    elbows.sort(key=lambda x: (x[1], x[0]))
    print('\nSorted elbows:\n', elbows)
    points = 0
    topLeftCorner = elbows[0]
    bottomRightCorner = elbows[-1]
    partialArray = [None, None]
    inside = []
    fullRow = []
    inside.sort()
    startHeight = elbows[0][1]
    for elbow in elbows:
        print(f'\nProcessing {elbow=}. {inside=} {partialArray=}')
        x = elbow[0]
        y = elbow[1]
        if y != startHeight:
            heightDistance = y - startHeight
            if includeBoundary:
                boundaryAdd = 1
            for insideArray in inside:
                addAmount = (insideArray[1] - insideArray[0] + boundaryAdd) * (heightDistance - 1)
                print(f'\n** Capturing ( {insideArray=}+ {boundaryAdd})*{(heightDistance - 1)} {addAmount=}')
                points += addAmount

            start = None
            addAmount = 0
            for elbowFR in fullRow:
                elX = elbowFR[0]
                if start == None:
                    start = elX
                else:
                    addAmount += elX - start + 1
                    # print('Boundary condition - adding ', addAmount)
            points += addAmount
            print(f'** Capturing boundary condition {fullRow} {addAmount=} {points=} \n')
            startHeight = y
            fullRow = []

        p = elbow[2]
        insideCopy = inside[:]
        for insideArray in insideCopy:
            iStart = insideArray[0]
            iEnd = insideArray[1]
            if (x >= iStart) and (x <= iEnd):
                print(f' {x=} is in {iStart=} of {insideArray=} {elbow=}')
                if p == 'J':

                    if partialArray[0] != None:
                        partialArray[1] = insideArray[1]
                        inside.remove(insideArray)
                        inside.append(partialArray)
                        partialArray = [None, None]
                        print(f'Updated {inside=}')
                        break
                    else:
                        print(f'what to do {inside=} {elbow=} {partialArray=}')
                        raise Exception('what to do')

                elif p == 'L':
                    print(f'Array is no longer {insideArray=}')
                    inside.remove(insideArray)
                    if x == iStart:
                        partialArray[1] = insideArray[1]
                        print(f'Array is now broken {partialArray=}')
                        break
                    else:
                        partialArray[0] = insideArray[0]

                elif p == 'F':
                    if x == iStart:
                        inside.remove(insideArray)
                        insideArray[1] = x
                        inside.append(insideArray)
                        partialArray[0] = x
                        print(f'Updated {inside=} - expecting partialArray to be dropped soon')
                    else:
                        print(f'Updating end of array')
                        partialArray[0] = x
                        inside.remove(insideArray)
                        insideArray[1] = x
                        inside.append(insideArray)
                        print(f'Updated {inside=} - expecting partialArray to be dropped soon')
                else:
                    print(f' - 2 I have no idea whot to do with {elbow=} matching inside')
                    raise ('fix me 2')

        else:
            if p == 'F':
                print(f'Setting start of partial Array')
                partialArray[0] = x
            elif p == '7':
                print('Fixing partial array', partialArray)
                if partialArray[1] == None:
                    partialArray[1] = x
                else:
                    partialArray[0] = x
                inside.append(partialArray)
                print(f'{inside=}')
                partialArray = [None, None]
            elif p == 'J':
                print('entered with the J')
                if (partialArray[0] != None) and (partialArray[1] == None):
                    partialArray[0] = None
                    print('still being processed')
                elif (partialArray[0] == None) and (partialArray[1] == None):
                    partialArray[1] = None
        fullRow.append(elbow)
    print(f'{topLeftCorner=} {bottomRightCorner=} {points=}\n')
    print('returning points:', points)
    exit()
    return points


points, elbows = getGridFull(listOfText, approachingStartDirection='U', firstElbow='F')
grid = printAndBuildGrid(points)

elbowsNew = getGridEfficient(listOfText)
countDotsSurroundedByPipesByElbow(elbowsNew)

print(f'{elbowsNew=}')

# print('points=',points)

totalInside = countDotsSurroundedByPipes(grid)
print(f'{totalInside=}')
print('elbows', elbows)
print(len(points))
print('set', len(set(points)))  # should be one less
print('totalInside', totalInside + len(set(points)))
