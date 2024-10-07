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


assert findLocationsOfLetters(grid, ['S']) == [(1, 1)]

count = navigatePipesAndCountLength(grid, (1, 1))
assert 4 == count



