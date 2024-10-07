from text_grid import findLocationsOfLetters, navigatePipesAndCountLength

grid = '''.....
.S-7.
.|.|.
.L-J.
.....'''.split('\n')
assert findLocationsOfLetters(grid, ['S']) == [(1, 1)]
print('success')

print(navigatePipesAndCountLength(grid, (1, 1)))