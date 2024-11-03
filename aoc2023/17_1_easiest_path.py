
import cleaninput
from text_grid import findLocationsOfLetters

listOfText_Puzzle = cleaninput.getfileInputLinesAsList('input17.txt')

listOfText_Sample1='''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533'''.split('\n')

raw_grid = listOfText_Puzzle
raw_grid = listOfText_Sample1

height = len(raw_grid)
width = len(raw_grid[0])

def getWeight(x,y):
    weight=int(raw_grid[y][x])
    #print(f'Returning {weight=} for {x=} {y=}')
    return weight

records = {}
keysToNavigate = []
x=0
y=0
p='>0'
key = (x,y,p)
keysToNavigate.append(key)
records[key] = 0
results = []
stepCounter = 0
while keysToNavigate:
    stepCounter +=1
    nextKeys = []
    print(f'\nStarted {keysToNavigate=} {records=}')
    for key in keysToNavigate:
        #print(f'Processing {key=}')
        x=key[0]
        y=key[1]
        p=key[2]

        if (x < 0) or (y < 0) or x > (width-1) or (y > width-1):
            print(f'Off grid {key=}')
            continue

        if (x == width -1) and (y == height -1):
            results.append(records[key])
            print(f'Reached the end {key=}')
            continue

        curWeight = records[key]
        print(f'-- Navigating {key=} {records[key]}')
        for direc in ['>', '<', '^', 'v']:

            if direc == '>':
                if (p[0] != '<') and (p != '>3'): # can go right
                    if p[0] == '>':
                        newp = p[0] + str(int(p[1])+1)
                    else:
                        newp = '>1'
                    nextKey = (x+1, y, newp)
                    print(f'Adding {direc} {nextKey=}')
                else:
                    print(f'Not going {direc} {key=}')
                    continue
                    
            if direc == '<':
                if (p[0] != '>') and (p != '<3'): # can go left
                    if p[0] == '<':
                        newp = p[0] + str(int(p[1])+1)
                    else:
                        newp = '<1'
                    nextKey = (x-1, y, newp)
                    print(f'Adding {direc} {nextKey=}')
                else:
                    print(f'Not going {direc} {key=}')
                    continue
                
            if direc == 'v':
                if (p[0] != '^') and (p != 'v3'): # can go down
                    if p[0] == 'v':
                        newp = p[0] + str(int(p[1])+1)
                    else:
                        newp = 'v1'
                    nextKey = (x, y+1, newp)
                    print(f'Adding {direc} {nextKey=}')
                else:
                    print(f'Not going {direc} {key=}')
                    continue

            if direc == '^':
                if (p[0] != 'v') and (p != '^3'): # can go down
                    if p[0] == '^':
                        newp = p[0] + str(int(p[1])+1)
                    else:
                        newp = '^1'
                    nextKey = (x, y-1, newp)
                    print(f'Adding {direc} {nextKey=}')
                else:
                    print(f'Not going {direc} {key=}')
                    continue

            newWeight = curWeight + getWeight(x,y)
            if nextKey in records:
                oldWeight = records[nextKey]
                if newWeight >= oldWeight:


                    continue
            records[nextKey] = newWeight
            nextKeys.append(nextKey)
    keysToNavigate=nextKeys
    if stepCounter == 3:
        break

