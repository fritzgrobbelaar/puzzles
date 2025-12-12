import cleaninput, copy
from datetime import datetime
from functools import cmp_to_key
import math
from datetime import datetime
import itertools
global listOfText

sample='''0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2'''.split('\n')

extracases = '''
'''

test=False
if test:
    listOfText = sample
else:
    listOfText = cleaninput.getfileInputLinesAsList('input_12.txt')

print(f'{sample=}')
print(f'{listOfText=}')

#listOfText = [row.split(' ') for row in listOfText]

shapes = {}
areas = []
shapesNr = None
for row in listOfText:
    print(f'{row=}')
    if row.strip() == "" and shape:
        shapes[shapesNr] = [shape]
        shape = None
        shapesNr = None
    elif row[1] == ':':
        shape = []
        shapesNr = row[0]
    elif row.startswith('.') or row.startswith('#'):
        shape.append(row)
    elif 'x' in row:
        areas.append(row)
        

print(f'{shapes=}')
print(f'{areas=}')

def printShapes(shapes):
    print('\n-- Print shapes --')
    keys = sorted(shapes.keys())
    for key in keys:
        print(f'{key=}')
        for shape in shapes[key]:
            for row in shape:
                print(''.join(row))
            print('')

print(f'before {shapes=}')
def flipVertically(shapes):
    keys = sorted(shapes.keys())
    for key in keys:
        shapesCopy = copy.deepcopy(shapes[key])
        for shape in shapesCopy:
            shapeReversed = list(reversed(shape))
            if shapeReversed not in shapes[key]:
                shapes[key].append(shapeReversed)
    return shapes

def flipHorizontally(shapes):
    keys = sorted(shapes.keys())
    for key in keys:
        shapesCopy = copy.deepcopy(shapes[key])
        for shape in shapesCopy:
            shapeReversed = []
            for row in shape:
                shapeReversed.append(''.join(list(reversed(row))))
            #print(f'checking in flipH if {shapeReversed=} found in {shapes[key]=}')
            if shapeReversed not in shapes[key]:
                shapes[key].append(shapeReversed) 
    return shapes

def numberShapes(shapes):
    keys = sorted(shapes.keys())
    for key in keys:
        for j,shape in enumerate(shapes[key]):
            for i, row in enumerate(shape):
                shapes[key][j][i] = shapes[key][j][i].replace('#',key)
    return shapes


shapes = numberShapes(shapes)


assert 1 == len(flipHorizontally({'5': [['###', '.#.', '###']]})['5'])
assert 1 == len(flipVertically({'5': [['###', '.#.', '###']]})['5'])

def rotate(shapes):
    keys = sorted(shapes.keys())
    for key in keys:
        shapesCopy = copy.deepcopy(shapes[key])
        for shape in shapesCopy:
            shapeReversed = [list(row) for row in zip(*shape[::-1])]
            shapeReversed = [''.join(row) for row in shapeReversed]
            #print(f'checking in rotate if {shapeReversed=} found in {shapes[key]=}')
            
            if shapeReversed not in shapes[key]:
                shapes[key].append(shapeReversed) 
    return shapes

shapes = numberShapes(shapes)
print(f'\n\nafter rotation {shapes=}')

if test:
    assert 2 == len(rotate({'5': [['###', '.#.', '###']]})['5'])
    shapes = rotate(shapes)
    #print(f'\n\nafter rotation {shapes=}')
    assert 2 == len(shapes['5'])
    #printShapes(shapes)
    shapes = flipVertically(shapes)
    #print(f'\n\nafter flipV {shapes=}')
    assert 2 == len(shapes['5'])
    #printShapes(shapes)
    shapes = flipHorizontally(shapes)
    #print(f'\n\nafter flipH {shapes=}')
    assert 2 == len(shapes['5'])
    #printShapes(shapes)


def printGrid(grid):
    print('\n\n---- grid ---')
    for row in grid:
        print(''.join(row))
    


def weighShapesByOpenAreaRightBottom(shapes):
    """
    Return list of lists - example list [6, '3', 1]
    example list - [weight, presentKey, present index in present key list]
"""
    presentWeights = []
    for key in shapes.keys():
        for z,shape in enumerate(shapes[key]):
            presentWeight = 0
            for j, row in enumerate(shape):
                for i, value in enumerate(row):
                    if value == '.':
                        presentWeight += i+j
            presentWeights.append([presentWeight,key,z])
    presentWeights.sort()
    presentWeights = list(reversed(presentWeights))
    return presentWeights
presentWeightsRightBottom = weighShapesByOpenAreaRightBottom(shapes)
print(f'{presentWeightsRightBottom=}')

def tryAndFitPresent(grid, presentShape, upperLeftPoint):
    grid = copy.deepcopy(grid[:])
    originalGrid = copy.deepcopy(grid[:])

    upperLeftPointY = upperLeftPoint[0]
    upperLeftPointX = upperLeftPoint[1]
    for y, row in enumerate(presentShape):
        for x, value in enumerate(row):
            gridValue = grid[upperLeftPointY + y][upperLeftPointX + x]
            if gridValue == '.':
                grid[upperLeftPointY + y][upperLeftPointX + x] = value
            elif  value == '.':
                pass
            else:
                return False
    #print('\noriginal grid')
    #printGrid(originalGrid)
    #print(f'after trying to fit and succeeding - returning grid {presentShape=} {upperLeftPoint=}')
    #printGrid(grid)
    #print('returning this grid')
    return grid

gridSample = '''000.........
000.........
0...........
............
............'''.split('\n')
gridSample = [list(row) for row in gridSample]
expectedGrid = '''00099.......
00099.......
0.999.......
............
............'''.split('\n')
expectedGrid = [list(row) for row in expectedGrid]
assert expectedGrid == tryAndFitPresent(grid=gridSample, presentShape=['.99', '.99', '999'], upperLeftPoint=(0, 2))

def placeShapeThatFitsWithMostOpenAtBottom(grid, weightedPresents, upperLeftPoint):
    
    for weightedPresent in weightedPresents:
        presentShape= shapes[weightedPresent[1]][weightedPresent[2]]
        #print(f'Trying pt={upperLeftPoint} {presentShape=} from {weightedPresent=}  ')                     
        answer = tryAndFitPresent(grid, presentShape, upperLeftPoint)
        if answer != False:
            grid = answer
            
            grid, correctPresent = grid, int(weightedPresent[1])
            if test:
                print('successfully placed present')
                printGrid(grid)
            return grid, correctPresent
    #print(f'failed to fit present {grid=} lastPresentShape={presentShape}, {upperLeftPoint=}')
    #printGrid(grid)
    return False


gridSample = '''....
....
....
....'''
gridSample = gridSample.split('\n')
gridSample = [list(row) for row in gridSample]
printGrid(gridSample)
weightedPresents = [[7, '0', 5], [7, '0', 0], [6, '3', 1]]
if test:
    grid, presentSelected = placeShapeThatFitsWithMostOpenAtBottom(gridSample, weightedPresents,(0,0))
#printGrid(grid)

def parseArea(area):
    area = area.split(':')
    gridDimensions = area[0]
    gridDimensions = gridDimensions.split('x')
    gridDimensions = [int(dim) for dim in gridDimensions]
    grid = []
    for y in range(gridDimensions[1]):
        grid.append(['.']*gridDimensions[0])
    presents = area[1][1:].split(' ')
    presents = [int(present) for present in presents]
    print(f'{presents=}')
    return grid, presents, gridDimensions

testArea = parseArea('2x3: 0 0 0 0 2 0')
printGrid(testArea[0])
assert testArea[1] == [0,0,0,0,2,0]
assert testArea[0] == [['.','.'],['.','.'],['.','.']]

print('\n\n --- tests completed - starting the real deal --- \n')
answers = []
for areaCount,area in enumerate(areas):
    print(f'\n\n -- Starting brand new area{areaCount=} {area=}')
    grid, presents,gridDimensions = parseArea(area)

    iterationCounter = 0
    iterationLimit = 100
    endOfGridReached = False
    # while presents != [0,0,0,0,0,0]:
        # for present in presents:
            # if present < 0:
                # raise ValueError('something went wrong - you cannot place presents you dont have')
        # iterationCounter += 1
        # if iterationCounter >  iterationLimit:
            # print(f'{iterationLimit=} reached')
            # print('not found, ')
            # answers.append(['presents remaining- iteration limit reached: ',presents, grid])
            
    weightedPresents = []
    for weightedPresent in presentWeightsRightBottom:
        presentKey = int(weightedPresent[1])
        if presents[presentKey] != 0:
            weightedPresents.append(weightedPresent)
        # successfullyPlaced = False
    for y in range(gridDimensions[1] -2):
        for x in range(gridDimensions[0]-2):
            answer = placeShapeThatFitsWithMostOpenAtBottom(grid, weightedPresents, (y,x))
            if answer == False:
                #print(f'Failed to place anything at {(y,x)} {gridDimensions=} ')
                continue
            else:
                grid, presentSelected = answer
                presents[presentSelected] = presents[presentSelected] -1
                successfullyPlaced = True
                weightedPresents = []
                for weightedPresent in presentWeightsRightBottom:
                    presentKey = int(weightedPresent[1])
                    if presents[presentKey] != 0:
                        weightedPresents.append(weightedPresent)

    note=f'{areaCount=} of {len(areas)=} {datetime.now()=}'
    print(f'\n\n{note}')
    if presents == [0,0,0,0,0,0]:
        print('placed all')
        printGrid(grid)
        answer = [True, 'successfully placed all - original request:', area, grid]
    else:
        print('failed to place all')
        print(presents)
        printGrid(grid)
        answer = [False, sum(presents), 'failed to placed all - original request:', area, f'{presents=}' ,grid]
    answers.append(answer)
    with open('tracking.txt', 'a') as handle:
        handle.write('\n' + str(note) + str(answer))

for answer in answers:
    print('answer - :',answer, printGrid(answer[-1]))
print(f'-- the end -- {answers=}')
summary = [True if answer[0] is True else answer[1] for answer in answers]
successfulPlacements = [True if answer is True else 0 for answer in summary]

print(f'-- the end -- {summary=}')
print(f'-- the end -- {sum(successfulPlacements)=}')

