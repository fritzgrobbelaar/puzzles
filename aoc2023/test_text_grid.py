from text_grid import findLocationsOfLetters, navigatePipesAndCountLength

raw_grid = '''..F7.
.FJ|.
SJ.L7
|F--J
LJ...'''.split('\n')

grid = []
for row in raw_grid:
    grid.append(list(row))

count = navigatePipesAndCountLength(grid,  findLocationsOfLetters(grid, ['S']) [0])
print('count:', count)
assert 8 == count





raw_grid = '''-L|F7
7S-7|
L|7||
-L-J|
L|-JF'''.split('\n')

grid = []
for row in raw_grid:
    grid.append(list(row))

count = navigatePipesAndCountLength(grid,  findLocationsOfLetters(grid, ['S']) [0])
print('count:', count)
assert 4 == count




print('success')

raw_grid = '''.....
.S-7.
.|.|.
.L-J.
.....'''.split('\n')

grid = []
for row in raw_grid:
    grid.append(list(row))
import copy
originalGrid = copy.deepcopy(grid)
print('originalGrid 1 ', originalGrid)
assert findLocationsOfLetters(grid, ['S']) == [(1, 1)]

count = navigatePipesAndCountLength(grid, (1, 1))
assert 4 == count

def countDots(grid, originalGrid):
    print('grid\n', grid, 'originalGrid:\n',originalGrid)
    tiles = 0
    for i,row in enumerate(grid):
        inside = False
        for j,value in enumerate(row):
            if value == '.' and inside:
                tiles += 1
                print(row, value,i,j, originalGrid[i][j])
            elif value == None and originalGrid[i][j] != '-':
                print('flipping', i, j, originalGrid[i][j])
                if inside:
                    inside = False
                else:
                    inside = True
    return tiles


print('grid',grid)
print('count:', countDots(grid, originalGrid))

grid = '''S-7
|.|
L-J'''
