import cleaninput
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
raw_grid = listOfText_Sample1
height = len(raw_grid)
width = len(raw_grid[0])
gridRecord = []
for row in raw_grid:
    newRow = []
    for value in range(width):
        newRow.append(set())
    gridRecord.append(newRow)


def printGrid(grid):
    print('printing grid')
    for row in grid:
        print(''.join(row))


def printGridRecord(grid):
    print('printing grid record:')
    for row in grid:
        printRow = []
        for value in row:
            value = list(value)
            if len(value) == 0:
                printRow.append('.')
            elif len(value) > 1:
                printRow.append(len(value))
            else:
                printRow.append(value[0])
        print(''.join(printRow))


def calculate(point, lightDirection):
    print(f'=Calculating {point} {lightDirection}')
    if lightDirection in gridRecord[point[0]][point[1]]:
        print(f'Already been here', point, lightDirection)
        return
    value = raw_grid[point[0]][point[1]]
    print(f'Found {value} at {point}')
    y = point[0]
    x = point[1]
    gridRecord[y][x].add(lightDirection)
    if lightDirection == '>' and value == '.':
        if x == width - 1:
            print(f'Beam left to the right, {point=} {lightDirection=} ')
            return
        nextPoint = (y, x + 1)
        calculate(nextPoint, lightDirection)
    elif lightDirection in ('>', '<') and value == '|':
        if y == 0:
            newPoint = (y + 1, x)
            calculate(newPoint, 'v')
        elif y == height - 1:
            newPoint = (y - 1, x)
            calculate(newPoint, 'v')
        else:
            newPoint = (y - 1, x)
            calculate(newPoint, 'v')
            newPoint = (y + 1, x)
            calculate(newPoint, 'v')
    elif lightDirection == 'v' and value == '.':
        if y == height - 1:
            return
        calculate((y + 1, x), lightDirection)
    elif lightDirection in ('v', '^') and value == '-':
        if x == 0:
            newPoint = (y, x+1)
            calculate(newPoint, '>')
        elif y == width - 1:
            newPoint = (y, x-1)
            calculate(newPoint, '<')
        else:
            newPoint = (y, x-1)
            calculate(newPoint, '<')
            newPoint = (y, x+1)
            calculate(newPoint, '>')
    elif lightDirection == '>' and value == '-':
        pass

        print(f'Unknown condition {point=} {lightDirection}')


calculate((0, 0), '>')

printGrid(raw_grid)
printGridRecord(gridRecord)
