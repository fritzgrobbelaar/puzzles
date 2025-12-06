import cleaninput
from datetime import datetime
from collections import defaultdict
from itertools import repeat
listOfText_Puzzle = cleaninput.getfileInputLinesAsList('input15.txt')


input_sample = '''rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'''.split('\n')


input = listOfText_Puzzle
#input = input_sample

input = input[0]
rows = []
for row in input.split(','):
    rows.append(list(row))


def calculateOne(currentValue, newChar):
    currentValue += ord(newChar)
    #print(f'{currentValue=} 1')
    currentValue = currentValue*17
    #print(f'{currentValue=} position 2')

    currentValue = currentValue % 256
    #print(f'{currentValue=} 3')

    return currentValue

assert calculateOne(0, 'H') == 200

def calculate(row):
    currentValue = 0
    for char in row:
        currentValue = calculateOne(currentValue, char)
    return currentValue

assert calculate('HASH') == 52

total = 0
for i, row in enumerate(rows):
    total += calculate(row)

print('total', total)
