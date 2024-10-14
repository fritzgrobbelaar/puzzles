import cleaninput
from datetime import datetime
from collections import defaultdict
from itertools import repeat
listOfText_Puzzle = cleaninput.getfileInputLinesAsList('input13.txt')


input_sample = '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....'''.split('\n')

input = input_sample

rows = []
for row in input:
    rows.append(list(row))
rows = list(map(list, zip(*rows)))

def printBlock(block):
    print()
    for row in block:
        print(''.join(row))

printBlock(rows)

for i,row in enumerate(rows):
    stringRow = ''.join(row)
    splitRow = stringRow.split('#')
    sortedShortStrings = []
    for shortString in splitRow:
        print(f'{shortString=} {shortString.count("O")=}  {shortString.count(".")=}')
        sortedShortStrings.append('O'*shortString.count("O") + '.'*shortString.count("."))
    rows[i] = '#'.join(sortedShortStrings)    
        
printBlock(rows)
length = len(rows[0])
total = 0
for i, row in enumerate(rows):
    for j, value in enumerate(row):
        if value == 'O':
            total += length-j
print('total:',total)
