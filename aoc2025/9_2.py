import cleaninput
from datetime import datetime
from functools import cmp_to_key
import math
global listOfText
listOfText = cleaninput.getfileInputLinesAsList('input_9.txt')

sample='''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''.split('\n')

test = True
if test:
    listOfText = sample
    scale=1
else:
    scale=1000
listOfText = [row.split(',') for row in listOfText]
print(f'{abs(-2)=}')

areas = []
for i,row1 in enumerate(listOfText):
    #print(f'{i=} {row1=}')
    for j in range(i+1, len(listOfText)):
        x_1 = int(row1[0])
        y_1 = int(row1[1])
        row2 = listOfText[j]
        x_2 = int(row2[0])
        y_2 = int(row2[1])
        #print(f'{i=} {j=} {(abs(x_1-x_2)+1)=} {(abs(y_1-y_2)+1)=}')
        area = (abs(x_1-x_2)+1)*(abs(y_1-y_2)+1)
        areas.append([area,i,j,row1,row2])
    #print(areas)
areas.sort()
areas = list(reversed(areas))
print('We now have areas from largest to smallest. Largest first: ',areas[0])


def doesLinesIntersect(verticalLine, horizontalLine):
    if test:
        print(f'{verticalLine=} {horizontalLine=}')
    if  verticalLine['x'] < horizontalLine['x_max'] and \
        verticalLine['x'] > horizontalLine['x_min'] and \
        horizontalLine['y'] < verticalLine['y_max'] and \
        horizontalLine['y'] > verticalLine['y_min']:
            if test:
                print('------ intersection found')
            return True
    #print('no intersection found')
    return False

assert False == doesLinesIntersect(verticalLine={'x' : 4, 'y_min' :3, 'y_max' :10}, horizontalLine={'y' : 6, 'x_min' : 10, 'x_max' : 300})
assert True == doesLinesIntersect(verticalLine={'x' : 15, 'y_min' :3, 'y_max' :10}, horizontalLine={'y' : 6, 'x_min' : 10, 'x_max' : 300})
assert False == doesLinesIntersect(verticalLine={'x' : 6, 'y_min' : 10, 'y_max' : 300}, horizontalLine={'y' : 4, 'x_min' :3, 'x_max' :10}, )
assert True == doesLinesIntersect(verticalLine={'x' : 6, 'y_min' : 10, 'y_max' : 300}, horizontalLine={'y' : 15, 'x_min' :3, 'x_max' :10})
assert True == doesLinesIntersect(verticalLine={'x': 11, 'y_min': 3, 'y_max': 7}, horizontalLine={'y': 4, 'x_min': 5, 'x_max': 12})

def doesSegmentIntersectArea(area,  low_line_x, high_line_x, low_line_y, high_line_y):
        corner_x_1 = int(area[3][0])
        corner_x_2 = int(area[4][0])
        corner_y_1 = int(area[3][1])
        corner_y_2 = int(area[4][1])
        low_corner_x = min(corner_x_1, corner_x_2)
        high_corner_x = max(corner_x_1, corner_x_2)
        low_corner_y = min(corner_y_1, corner_y_2)
        high_corner_y = max(corner_y_1, corner_y_2)        
        #print(f'\nRectangle: {low_corner_x=} {high_corner_x=} {low_corner_y=} {high_corner_y=}')
        if test: 
            print(f'\nline: {low_line_x=} {high_line_x=} {low_line_y=} {high_line_y=}')
        if low_line_y == high_line_y: # y is the same - worm travels horizontally
            if test:
                print('checking worm horizontal')
            rectangleLeft_verticalLine = {'x': low_corner_x, 'y_min': low_corner_y, 'y_max': high_corner_y}
            rectangleRight_verticalLine = {'x': high_corner_x, 'y_min': low_corner_y, 'y_max': high_corner_y}
            worm_horizontalLine = {'y': low_line_y, 'x_min':low_line_x, 'x_max' : high_line_x}
            if doesLinesIntersect(rectangleLeft_verticalLine, worm_horizontalLine):
                if test:
                    print('intersect left found')
                return True
            elif doesLinesIntersect(rectangleRight_verticalLine, worm_horizontalLine):
                if test:
                    print('intersect right found')
                return True
        if low_line_x == high_line_x: # worm travels vertically
            if test:
                print('checking worm vertical')
            rectangleBottom_horizontalLine = {'y': low_corner_y, 'x_min': low_corner_x, 'x_max': high_corner_x}
            rectangleTop_horizontalLine = {'y': high_corner_y, 'x_min': low_corner_x, 'x_max': high_corner_x}
            worm_vertical = {'x': low_line_x, 'y_min': low_line_y, 'y_max': high_line_y}
            if doesLinesIntersect(verticalLine = worm_vertical, horizontalLine=rectangleBottom_horizontalLine):
                if test:
                    print('intersect bottom found')
                return True
                
            if doesLinesIntersect(verticalLine = worm_vertical, horizontalLine=rectangleTop_horizontalLine):
                if test:
                    print('intersect top found')
                return True    
        if test:
            print(f'no intersection found {area=} {low_line_x=}, {high_line_x=}, {low_line_y=}, {high_line_y=}')

assert True == doesSegmentIntersectArea(area=[50, 2, 6, ['11', '7'], ['2', '3']],  low_line_x=5, high_line_x=12, low_line_y=4, high_line_y=4)


def doesWormIntersectArea(area): #limitation is that 1-in & out does not work
    global listOfText
    print('\n ### Now starting with area: ', area)
    prevPoint = listOfText[-1]

    for i, point in enumerate(listOfText):
        x_2 = int(prevPoint[0])
        y_2 = int(prevPoint[1])
        x_1 = int(point[0])
        y_1 = int(point[1])
        low_line_x = min(x_1, x_2)
        low_line_y = min(y_1, y_2)
        high_line_x = max(x_1, x_2)
        high_line_y = max(y_1, y_2)
        if doesSegmentIntersectArea(area, low_line_x, high_line_x, low_line_y, high_line_y):
            return True
        prevPoint = point
    return False


for area in areas:
    if not doesWormIntersectArea(area):
        print(f'answer found {area=}')
        break
else:
    print('no answer found')
    


def drawScaledArea(listOfText, scale=1):
    grid = []
    print('\n')
    for i in range(20):
        row = []
        for j in range(20):
            row.append('.')
        grid.append(row)

    x_2 = int(int(listOfText[-1][0])/scale)
    y_2 = int(int(listOfText[-1][1])/scale)
    for z,row in enumerate(listOfText):
        y_1=int(int(row[1])/scale)
        x_1=int(int(row[0])/scale)
        grid[y_1][x_1] = '#'

        if x_1 == x_2:
                for y in range (min(y_1,y_2),max(y_1,y_2)):
                    grid[y][x_1] = '#'
                    print(f'{y=} {x_1=}')
        else:
                for x in range(min(x_1, x_2), max(x_1, x_2)):
                    grid[y_1][x] = '#'
                    print(f'{y_1=} {x=}')
        x_2 = x_1
        y_2 = x_1
    for row in grid:
        print(''.join(row))


#drawScaledArea(listOfText, scale)
print('- the end')

# 2451913560 is too high
