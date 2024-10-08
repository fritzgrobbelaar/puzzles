
import cleaninput
from text_grid import findLocationsOfLetters

listOfText_Puzzle = cleaninput.getfileInputLinesAsList('aoc2023/input11.txt')
#

total = 0
for i in range(500):
    for j in range(i):
        total = total + 1
print('total:', total)

listOfText_Sample1='''...#......
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

grid = []
for row in raw_grid:
    row = list(row)
    if set(row) == set(['.']):
        grid.append(row)
    else:
        print(' not fonud', set(row))
    grid.append(row)
transposed_grid = list(map(list, zip(*grid)))

grid = []
for row in transposed_grid:
    row = list(row)
    if set(row) == set(['.']):
        grid.append(row)
    grid.append(row)
grid = list(map(list, zip(*grid)))

locations = []
for i,row in enumerate(grid):
    for j, value in enumerate(row):
        if value == '#':
            locations.append((i,j))

for row in grid:
    print(''.join(row))

print(locations)

totalDistance = 0
count = 0
for i,location in enumerate(locations):
    for j in range(i+1, len(locations)):
        #print('from',i, locations[i] ,' to ', j,locations[j])
        count +=1
        totalDistance += abs(locations[i][0]-locations[j][0]) + abs(locations[i][1]-locations[j][1])
        #print('locations ',locations[i][0]-locations[j][0], locations[i][0],locations[j][0])
print('count',count)
print('distances', totalDistance)