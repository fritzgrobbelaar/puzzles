import cleaninput, copy
from text_grid import countDotsSurroundedByPipes

listOfText_Puzzle = cleaninput.getfileInputLinesAsList('input18.txt')

sample1 = '''R 6 (#70c710)
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
U 2 (#7a21e3)'''

listOfText_Sample1 = sample1.split('\n')

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
listOfText1 = listOfText_Sample1
listOfText4 = listOfText_Sample2
listOfText3 = sample1.replace('D', 'u').replace('U', 'D').replace('u', 'U').split('\n')
listOfText = (sample1
              .replace('D', 'l')
              .replace('U', 'r')
              .replace('R', 'u')
              .replace('L', 'd')
              .replace('d', 'D')
              .replace('u', 'U')
              .replace('r', 'R')
              .replace('l', 'L').split('\n'))

listOfText = (sample1
               .replace('U', 'l')
               .replace('D', 'r')
               .replace('R', 'u')
               .replace('L', 'd')
               .replace('d', 'D')
               .replace('u', 'U')
               .replace('r', 'R')
               .replace('l', 'L').split('\n'))


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


def captureBoundaryConditionOld(fullRow, inside):
    start = None
    addAmount = 0
    xS = []
    for elbowFR in fullRow:
        elX = elbowFR[0]
        xS.append(elX)
    for array in inside:
        xS.append(array[0])
        xS.append(array[1])
    xS = list(set(xS))
    xS.sort()
    start = None
    for x in xS:
        if start is None:
            start = x
        else:
            addAmount += x - start + 1
            start = None
    print(f'** Capturing boundary condition {fullRow=} {inside=} {addAmount=}')
    return addAmount


def captureBoundaryCondition(prevInside, inside):
    print(f'Processing boundary condition {prevInside=} {inside=}')
    addAmount = 0
    arrays = prevInside + inside
    arrays.sort()
    nonOverlappingArrays = [copy.deepcopy(arrays[0])]
    for array in arrays[1:]:
        if (array[0] > nonOverlappingArrays[-1][1]) or (array[0] < nonOverlappingArrays[-1][0]):
            nonOverlappingArrays.append(array)
        elif array[1] > nonOverlappingArrays[-1][1]:
            nonOverlappingArrays[-1][1] = array[1]
        else:
            pass

    for array in nonOverlappingArrays:
        addAmount += array[1] - array[0] + 1

    print(f'** Capturing boundary condition {prevInside=} {inside=} {nonOverlappingArrays=} {addAmount=}')
    return addAmount


inside = [[-6, -1]]
prevInside = [[-4, 0]]
assert 10 == captureBoundaryCondition(prevInside=[[-9, -0], [-5, -3]], inside=[])
assert 9 == captureBoundaryCondition(prevInside=[[-9, -7], [-5, 0]], inside=[])


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
    prevInside = []
    inside.sort()
    startHeight = elbows[0][1]
    for elbow in elbows:
        print(f'\nProcessing {elbow=}. {inside=} {partialArray=}')
        x = elbow[0]
        y = elbow[1]
        p = elbow[2]
        if y != startHeight:
            heightDistance = y - startHeight
            if includeBoundary:
                boundaryAdd = 1
            for insideArray in inside:
                addAmount = (insideArray[1] - insideArray[0] + boundaryAdd) * (heightDistance - 1)
                print(f'\n** Capturing ( {insideArray=}+ {boundaryAdd})*{(heightDistance - 1)} {addAmount=}')
                points += addAmount
            addAmount = captureBoundaryCondition(prevInside, inside)
            points += addAmount
            print(f'** Capturing boundary {addAmount=} totalPoints: {points}')
            startHeight = y
            prevInside = copy.deepcopy(inside)

        insideCopy = copy.deepcopy(inside)
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
                    print(f'Array is no longer b {insideArray=} {partialArray=}')
                    inside.remove(insideArray)
                    if x == iStart:
                        partialArray[1] = insideArray[1]
                        print(f'Array is now broken a {partialArray=}')
                        break
                    else:
                        partialArray[0] = insideArray[0]

                elif p == 'F':
                    if x == iStart:
                        inside.remove(insideArray)
                        insideArray[1] = x
                        inside.append(insideArray)
                        partialArray[0] = x
                        print(f'Updated 1 {inside=} - expecting partialArray to be dropped soon')
                    else:
                        print(f'Updating end of array')
                        # if inside == [[-9,0]]:
                        #     pass
                        #     raise Exception ('todo')
                        partialArray[1] = insideArray[1]
                        inside.remove(insideArray)
                        insideArray[1] = x
                        inside.append(insideArray)
                        print(f'Updated 2 {inside=} - expecting partialArray to be dropped soon')
                elif p == '7':
                    if partialArray[0] == None:
                        partialArray = x
                        inside.append(partialArray)
                break
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
                elif partialArray == [None, None]:
                    partialArray[1] = None
                else:
                    partialArray = [None, None]
            elif p == 'L':
                if partialArray[0] != None and partialArray[1] == None:
                    pass
                elif partialArray == [None, None]:
                    partialArray = [x,None]
                if partialArray[1] != None:
                    print(f'Array is no longer 3 {insideArray=}')
                    partialArray[1] = insideArray[1]
                    print(f'Array is now broken 2 {partialArray=}')
                    partialArray = [insideArray[0], None]


    print(f'{topLeftCorner=} {bottomRightCorner=} {points=}\n')
    addAmount = captureBoundaryCondition(prevInside, inside)
    points += addAmount
    print(f'** Capturing final boundary  {addAmount=} totalPoints: {points}')
    print('returning points:', points)
    return points


points, elbows = getGridFull(listOfText, approachingStartDirection='U', firstElbow='L')
grid = printAndBuildGrid(points)

elbowsNew = getGridEfficient(listOfText)
points = countDotsSurroundedByPipesByElbow(elbowsNew)
print('points', points)

print(f'{elbowsNew=}')
