
import cleaninput
from text_grid import findLocationsOfLetters

listOfText_Puzzle = cleaninput.getfileInputLinesAsList('input10.txt')

listOfText_Sample1='''.....
.S-7.
.|.|.
.L-J.
.....'''.split('\n')

listOfText_Sample2='''...........
.S--------7.
.|.F-----7|.
.|.|.....||.
.|.|.....||.
.|.L-7.F-J|.
.|...|.|..|.
.L---J.L--J.
............'''

listOfText_Sample3='''.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
'''

listOfText_Sample4='''FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L'''

raw_grid = listOfText_Sample4.split('\n')



from text_grid import findLocationsOfLetters, navigatePipesAndCountLength

grid = []
for row in raw_grid:
    grid.append(list(row))
import copy
originalGrid = copy.deepcopy(grid)

count = navigatePipesAndCountLength(grid,  findLocationsOfLetters(grid, ['S']) [0])
print('count:', count)


def countDots(grid, originalGrid):
    print('grid\n', grid)
    for row in grid:
        print(''.join(row))
    print('originalGrid:\n',originalGrid)

    for row in originalGrid:
        print(''.join(row))
    tiles = 0
    openCharacter = None
    flip = False
    for i,row in enumerate(grid):
        inside = False
        for j,value in enumerate(row):
            originalValue = originalGrid[i][j]
            if inside and value != '*':
                tiles += 1
                print('adding a tile', row, value,i,j, originalGrid[i][j])
            elif value == '*' and originalValue not in ['-']:
                print('evaluating', originalValue)
                if originalValue == '|':
                    flip = True
                elif openCharacter == 'F':
                    openCharacter = None
                    if originalValue == 'J':
                        print('do not flip, F, J')
                        flip = False
                    else:
                        flip = True
                elif openCharacter == 'L':
                    openCharacter = None
                    if originalValue == '7':
                        print('do not flip - L, 7')
                        flip = False
                    else:
                        print('flip - L, not 7', originalValue)
                        flip = True
                else:
                    openCharacter = originalValue
                    flip = True
                    print('setting openCharacter to ', openCharacter)
                if flip:
                    print('flipping', i, j, originalGrid[i][j])
                    if inside:
                        inside = False
                    else:
                        inside = True
                        
    return tiles


print('count:', countDots(grid, originalGrid))

