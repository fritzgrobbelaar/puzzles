import cleaninput
from datetime import datetime
from functools import cmp_to_key

listOfText = cleaninput.getfileInputLinesAsList('input10_2024.txt')

sample = '''.....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9....'''.split('\n')

sample = '''..90..9
...1.98
...2..7
6543456
765.987
876....
987....'''.split('\n')

sample = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''.split('\n')


#listOfText = sample

listOfLists = []
total = 0
for row in listOfText:
    listOfLists.append(list(row))

def printMap(map, steps):
    #print('map print',steps)
    for j, row in enumerate(map):
        printRow = []
        for i,value in enumerate(row):
            found=False
            for h,steprow in enumerate(steps):
                for step in steprow:
                    if j == step[0] and i == step[1]:
                        #print(f'map print {i=} {j=} {step=}')
                        printRow.append(str(h))
                        found=True
                        break
            if not found:
                printRow.append('.')
     #   print('map print',''.join(printRow))

def validateStep(height, step, map):
    maxI = len(map[0]) - 1
    maxJ = len(map[1]) - 1
    if step[0] < 0:
        #print(f'too left, {step=}')
        return False
    if step[1] < 0:
        #print(f'too up, {step=}')
        return False

    if step[0] > maxI:
       # print(f'too right, {step=}')
        return False

    if step[1] > maxJ:
      #  print(f'too below, {step=}')
        return False
    if not str(height) == map[step[1]][step[0]]:
     #   print(f'wrong height {height=} {map[step[1]][step[0]]=}')
        return False
    #print(f'seems good {step=} {height=}')
    return True


def calculateTrailHeads(x, y, map):
    steps = [[(x, y)]]

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for height in range(1, 10):
        steps.append([])
        for step in steps[-2]:
            #print(f'\n{step=} {height=} {steps=}')
            stepI = step[0]
            stepJ = step[1]
            for direction in directions:
                newStep = (stepI + direction[0], stepJ + direction[1])
                #print(f'{newStep=}')
                if validateStep(height, newStep, map):
                    steps[-1].append(newStep)
        #steps[-1] = list(set(steps[-1]))
        #print(f'{steps=}')
        printMap(map, steps)
    return len(steps[-1])


#assert 1 == calculateTrailHeads(0, 0, listOfLists)

for y, row in enumerate(listOfLists):
    print(f'{total=} {row=} {y=}')
    for x,value in enumerate(row):
        if value == '0':
            #print(f'{total=} {row=} {x=} {y=}')
            total += calculateTrailHeads(x, y, listOfLists)

print(f'{total=}')
