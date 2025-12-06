import cleaninput
import sys

sys.setrecursionlimit(10000)

from collections import defaultdict

listOfText_Puzzle = cleaninput.getfileInputLinesAsList('input16.txt')

listOfText_Sample1 = r'''.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....'''.split('\n')

raw_grid = listOfText_Puzzle
#raw_grid = listOfText_Sample1

height = len(raw_grid)
width = len(raw_grid[0])

gridRecord = []
def clearGridRecords():
    gridRecord = []
    for row in raw_grid:
        newRow = []
        for value in range(width):
            newRow.append(set())
        gridRecord.append(newRow)
    return gridRecord

gridRecord = clearGridRecords()
print(gridRecord)

def printGrid(grid):
  #  print('printing grid')
    for row in grid:
        pass
       # print(''.join(row))


def printGridRecord():
   # print('printing grid record:')
    count = 0
    for row in gridRecord:
        printRow = []
        for value in row:
            value = list(value)
            if len(value) == 0:
                printRow.append('.')
            elif len(value) > 1:
                printRow.append(str(len(value)))
                count += 1
            else:
                printRow.append(value[0])
                count += 1
        #print(''.join(printRow))
    return count


def calculate(point, lightDirection):
    y = point[0]
    x = point[1]
    if (x < 0) or (x > width - 1) or (y < 0) or (y > height - 1):
        # print(f'off grid {y=} {x=} {lightDirection}')
        return

    if lightDirection in gridRecord[y][x]:
        # print(f'Already been here', point, lightDirection)
        return
    value = raw_grid[point[0]][point[1]]
    #print(f'=Calculating {point} {lightDirection} {value=}')
    gridRecord[y][x].add(lightDirection)

    if lightDirection in ('>', '<') and value == '|':
        newPoint = (y - 1, x)
        calculate(newPoint, '^')
        newPoint = (y + 1, x)
        calculate(newPoint, 'v')
    elif lightDirection in ('v', '^') and value == '-':
        calculate((y, x - 1), '<')
        calculate((y, x + 1), '>')
    elif lightDirection == '>' and value in ('.', '-'):
        calculate((y, x + 1), lightDirection)
    elif lightDirection == '<' and value in ('-', '.'):
        calculate((y, x - 1), '<')
    elif lightDirection == '^' and value in ('.', '|'):
        calculate((y - 1, x), '^')
    elif lightDirection == 'v' and value in ('.', '|'):
        calculate((y + 1, x), lightDirection)

    elif lightDirection == '>' and value == '/':
        calculate((y - 1, x), '^')
    elif lightDirection == '>' and value == '\\':
        calculate((y + 1, x), 'v')
    elif lightDirection == '^' and value == '\\':
        calculate((y, x - 1), '<')
    elif lightDirection == '^' and value == '/':
        calculate((y, x + 1), '>')

    elif lightDirection == '<' and value == '/':
        calculate((y + 1, x), 'v')
    elif lightDirection == '<' and value == '\\':
        calculate((y - 1, x), '^')

    elif lightDirection == 'v' and value == '\\':
        calculate((y, x + 1), '>')
    elif lightDirection == 'v' and value == '/':
        calculate((y, x - 1), '<')

    else:
        print(f'Unknown condition {point=} {lightDirection=}, {value=}')


maxTotal = 0
for i in range(width):
#if False:
    gridRecord = clearGridRecords()

    calculate((0, i), 'v')
    value = printGridRecord()
    if value > maxTotal:
        maxTotal = value
    gridRecord = clearGridRecords()

    calculate((height - 1, i), '^')
    value = printGridRecord()
    if value > maxTotal:
        maxTotal = value


for i in range(height):
#if False:
    gridRecord = clearGridRecords()
    calculate((i, 0), '>')
    value = printGridRecord()
    if value > maxTotal:
        maxTotal = value
    gridRecord = clearGridRecords()

    calculate((i, width - 1), '<')
    value = printGridRecord()
    if value > maxTotal:
        maxTotal = value


printGrid(raw_grid)

total = printGridRecord()

print('maxTotal', maxTotal)
