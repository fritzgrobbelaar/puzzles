import cleaninput
from datetime import datetime
from collections import defaultdict
from itertools import repeat
listOfText_Puzzle = cleaninput.getfileInputLinesAsList('input15.txt')


input_sample = '''rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'''.split('\n')


input = listOfText_Puzzle
#input = input_sample

boxes = []
for i in range(256):
    boxes.append([{}, []])

input = input[0]
rows = []
for row in input.split(','):
    rows.append(row)

def calculateOne(currentValue, newChar):
    currentValue += ord(newChar)
    #print(f'{currentValue=} 1')
    currentValue = currentValue*17
    #print(f'{currentValue=} position 2')

    currentValue = currentValue % 256
    #print(f'{currentValue=} 3')

    return currentValue

assert calculateOne(0, 'H') == 200

def getBoxNumber(label):

    currentValue = 0
    for char in label:
        currentValue = calculateOne(currentValue, char)
    #print(f'{("").join(row)} {currentValue}')
    return currentValue

assert getBoxNumber('cm') == 0

def updateBoxes(row):
    label = row.split('=')[0]
    label = label.split('-')[0]
    
    boxNr = getBoxNumber(label)
    print(f'{boxNr=}')
    box = boxes[boxNr]
    if '=' in row:
        if label in box[0]:
            i = box[0][label]
            boxes[boxNr][1][i] = row
            print(f'Found {label=} in {box=}')
        else:

            boxes[boxNr][1].append(row)
            boxes[boxNr][0][label] = len(boxes[boxNr][1])-1
            
            print(f'Added {row=} to end of start of {boxNr=} {box=}')
    if '-' in row:
        if label not in box[0]:
            return
        i = box[0][label]
        boxes[boxNr][1][i] = None
        del box[0][label]

def updateBoxesAfter():
    for i,box in enumerate(boxes):
        newBox = [{},[]]
        for j, row in enumerate(box[1]):
            if row != None:
                newBox[1].append(row)
                label = row.split('=')[0]
                label = label.split('-')[0]
                newBox[0][label] = len(newBox[1])-1
        #print('newBox',newBox)
        boxes[i] = newBox
    
def printBoxes():
    print('\n--started printing boxes')

    for i,box in enumerate(boxes):
        if box[0] != {}:
            print(f' {i} {box}')
    print('completed printing boxes')

print('')

total = 0
for i, row in enumerate(rows):
    updateBoxes(row)

printBoxes()
updateBoxesAfter()
printBoxes()

def getFocusPower():
    total = 0
    for i,box in enumerate(boxes):
        for j, row in enumerate(box[1]):
            focalPower=int(row.split('=')[1])
            print(f'focal power {focalPower=}')
            newValue = (i+1)*(1+j)*focalPower
            total += newValue
            print(f'{total=} {newValue=}')
    return total

print('total', getFocusPower())
