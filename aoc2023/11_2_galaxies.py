import cleaninput
from text_grid import findLocationsOfLetters

listOfText_Puzzle = cleaninput.getfileInputLinesAsList('aoc2023/input11.txt')
#

total = 0
for i in range(500):
    for j in range(i):
        total = total + 1
print('total:', total)

listOfText_Sample1 = '''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....'''.split('\n')

raw_grid = listOfText_Puzzle
scaledRows = []
scaledColumns = []
grid = []
for i, row in enumerate(raw_grid):
    row = list(row)
    if set(row) == set(['.']):
        scaledRows.append(i)
    else:
        print(' not fonud', set(row))
    grid.append(row)
transposed_grid = list(map(list, zip(*grid)))

grid = []
for i, row in enumerate(transposed_grid):
    row = list(row)
    if set(row) == set(['.']):
        scaledColumns.append(i)
    grid.append(row)
grid = list(map(list, zip(*grid)))

print('scaledRows & colmns', scaledRows, scaledColumns)

locations = []
for i, row in enumerate(grid):
    for j, value in enumerate(row):
        if value == '#':
            locations.append((i, j))

for row in grid:
    print(''.join(row))

print(locations)

totalDistance = 0
count = 0
scalingAddition = 999999
for i, location in enumerate(locations):
    for j in range(i + 1, len(locations)):
        #print('Comparing', locations[i] , ' and ', locations[j])
        count += 1
        totalDistance += abs(locations[i][0] - locations[j][0]) + abs(locations[i][1] - locations[j][1])
        #print('comparing rows', locations[i][0] , locations[j][0])
        #print('comparing columns', locations[i][1] , locations[j][1])
        for column in scaledColumns:
            if ((column < locations[i][1]) and (column > locations[j][1])) or (
                    (column > locations[i][1]) and (column < locations[j][1])):
                totalDistance += scalingAddition
                #print("Adding column scaling column due to empty column", column,  'which is between', locations[i][1], 'and', locations[j][1])
        for row in scaledRows:
            if ((row < locations[i][0]) and (row > locations[j][0])) or (
                    (row > locations[i][0]) and (row < locations[j][0])):
                totalDistance += scalingAddition
                #print("Adding row scaling due to empty row", row, 'which is between', locations[i][0], 'and', locations[j][0])

print('scaledRows', scaledRows, scaledColumns)
print('count', count)
print('distances', totalDistance)
