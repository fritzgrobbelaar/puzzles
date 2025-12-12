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

test=True
if test:
    listOfText = sample
else:
    listOfText = cleaninput.getfileInputLinesAsList('input_12.txt')

#print(f'{listOfText=}\n')
listOfText = [row.split(' ') for row in listOfText]

shapes = {}
areas = []
shapesNr = None
for row in sample:
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

for area in areas:
    area = area.split(':')
    grid = area[0]
    presents = area[1][1:].split(' ')
    print(f'{presents=} should fit into {grid=}')

print('-- the end --')
