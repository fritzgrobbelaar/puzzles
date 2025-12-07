import cleaninput
from datetime import datetime
from functools import cmp_to_key

listOfText = cleaninput.getfileInputLinesAsList('input_7.txt')

sample='''.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............'''.split('\n')

#listOfText = sample

listOfLists = []
beams = set()
total = 0
for row in listOfText:
    for i,value in enumerate(row):
        if value == 'S':
            beams.add(i)
            continue
        else:
            pass
            #print(f'{value=}')
        if value == '^' and i in beams:
            beams.add(i-1)
            beams.add(i+1)
            beams.remove(i)
            total += 1
    #print('f{beams=}')


print(f'{total=}')

