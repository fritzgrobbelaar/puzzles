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

test=True
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
print(areas[0])


def doesWormIntersectArea(area): #limitation is that 1-in & out does not work
    global listOfText
    corner_x_1 = int(area[3][0])
    corner_x_2 = int(area[4][0])
    corner_y_1 = int(area[3][1])
    corner_y_2 = int(area[4][1])
    low_corner_x = min(corner_x_1, corner_x_2)
    high_corner_x = max(corner_x_1, corner_x_2)
    low_corner_y = min(corner_y_1, corner_y_2)
    high_corner_y = max(corner_y_1, corner_y_2)
    prevPoint = listOfText[0]
    x_2 = int(prevPoint[0])
    y_2 = int(prevPoint[1])
    for i, point in enumerate(listOfText):
        print(f'{point=}')
        print(f'{low_line_x=} {low_corner_x=} {high_line_x=} {low_corner_x=}')
        x_1 = int(point[0])
        y_1 = int(point[1])
        low_line_x = min(x_1, x_2)
        low_line_y = min(y_1, y_2)
        high_line_x = max(x_1, x_2)
        high_line_y = max(y_1, y_2)
        if low_line_y == high_line_y:
            
            if (low_line_x < low_corner_x) and (high_line_x > low_corner_x):
                print('intersect x found')
                return True
            if (high_line_x > high_corner_x) and (low_line_x < high_corner_x):
                print('intersectx found')
                return True
        if low_line_x == high_line_x:
            if (low_line_y < low_corner_y) and (high_line_y > low_corner_y):
                print('intersect y found')
                return True
            if (high_line_y > high_corner_y) and (low_line_y < high_corner_y):
                print('intersect y found')
                return True    
        
    return False

for area in areas:
    if not doesWormIntersectArea(area):
        print(f'answer found {area=}')
        break
    


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
