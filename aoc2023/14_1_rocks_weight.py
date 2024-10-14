import cleaninput
from datetime import datetime
from collections import defaultdict
from itertools import repeat
listOfText_Puzzle = cleaninput.getfileInputLinesAsList('input14.txt')


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

input = listOfText_Puzzle
#input = input_sample


rows = []
for row in input:
    rows.append(list(row))

def printBlock(block):
    print()
    for row in block:
        print(''.join(row))

def tiltNorth(rows):
    rows = list(map(list, zip(*rows)))

    for i,row in enumerate(rows):
        stringRow = ''.join(row)
        splitRow = stringRow.split('#')
        sortedShortStrings = []
        for shortString in splitRow:
            #print(f'{shortString=} {shortString.count("O")=}  {shortString.count(".")=}')
            sortedShortStrings.append('O'*shortString.count("O") + '.'*shortString.count("."))
        rows[i] = list('#'.join(sortedShortStrings)    )

    rows = rows = list(map(list, zip(*rows)))
    return rows

def tiltSouth(rows):
    rows = list(map(list, zip(*rows)))


    for i,row in enumerate(rows):
        stringRow = ''.join(row)
        splitRow = stringRow.split('#')
        sortedShortStrings = []
        for shortString in splitRow:
            #print(f'{shortString=} {shortString.count("O")=}  {shortString.count(".")=}')
            sortedShortStrings.append('.'*shortString.count(".")+'O'*shortString.count("O"))
        rows[i] = list('#'.join(sortedShortStrings)    )

    rows = rows = list(map(list, zip(*rows)))
    return rows

def tiltEast(rows):

    for i,row in enumerate(rows):
        stringRow = ''.join(row)
        splitRow = stringRow.split('#')
        sortedShortStrings = []
        for shortString in splitRow:
           # print(f'{shortString=} {shortString.count("O")=}  {shortString.count(".")=}')
            sortedShortStrings.append('.'*shortString.count(".")+'O'*shortString.count("O"))
        rows[i] = list('#'.join(sortedShortStrings)    )

    return rows

def tiltWest(rows):

    for i,row in enumerate(rows):
        stringRow = ''.join(row)
        splitRow = stringRow.split('#')
        sortedShortStrings = []
        for shortString in splitRow:
            #print(f'{shortString=} {shortString.count("O")=}  {shortString.count(".")=}')
            sortedShortStrings.append('O'*shortString.count("O") + '.'*shortString.count("."))
        rows[i] = list('#'.join(sortedShortStrings)    )

    return rows

storeStates = {}
frequency = None
for i in range(200):
    rows = tiltNorth(rows)
    rows = tiltWest(rows)
    rows = tiltSouth(rows)
    rows = tiltEast(rows)
    dictKey = tuple([tuple(row) for row in rows])
    
    if dictKey not in storeStates:
        storeStates[dictKey]= []
    else:
        print('frequency', i-storeStates[dictKey][0],' at iteration', i)
        if frequency == None:
            frequency = i-storeStates[dictKey][0]
    storeStates[dictKey].append(i)
    if frequency and (1000_000_000-i-1) % frequency == 0:
    #if frequency and (20-i) % frequency == 0:
    
        print('cycle is in sync at', i)
        break

print('storeStates',storeStates.values())
printBlock(rows)

def calculateLoad(rows):
    rows = rows = list(map(list, zip(*rows)))

    length = len(rows[0])
    total = 0
    for i, row in enumerate(rows):
        for j, value in enumerate(row):
            if value == 'O':
                total += length-j
    return total

print('total', calculateLoad(rows))
