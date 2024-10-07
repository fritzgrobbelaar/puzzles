from lib import cleaninput
from lib.text_grid import findLocationsOfLetters

listOfText_Puzzle = cleaninput.getfileInputLinesAsList('aoc2023\\input10.txt')

listOfText_Sample='''.....
.S-7.
.|.|.
.L-J.
.....'''.split('\n')

raw_grid = listOfText_Puzzle

from lib.text_grid import findLocationsOfLetters, navigatePipesAndCountLength

grid = []
for row in raw_grid:
    grid.append(list(row))

count = navigatePipesAndCountLength(grid,  findLocationsOfLetters(grid, ['S']) [0])
print('count:', count)