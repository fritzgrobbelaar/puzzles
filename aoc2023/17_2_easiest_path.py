
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

listOfText_Sample2='''111111111111
999999999991
999999999991
999999999991
999999999991'''.split('\n')

raw_grid = listOfText_Puzzle
#raw_grid = listOfText_Sample1
#raw_grid = listOfText_Sample2

height = len(raw_grid)
width = len(raw_grid[0])

def getWeight(x,y):
    weight=int(raw_grid[y][x])
    #print(f'Returning {weight=} for {x=} {y=}')
    return weight

def printNextKeys(keys,chars=3):
    grid = []
    
    for i,row in enumerate(raw_grid):
        newRow = []
        for value in row:
            newRow.append('.'*chars)
        grid.append(newRow)

    for key in keys:
        x=key[0]
        y=key[1]
        p=key[2]
        grid[y][x] = (p+' ')[:chars]
        

    print('\n')
    for row in grid:
        if chars == 3:
            print(' '.join(row))
        else:
            print(''.join(row))

    for key in keys:
        x=key[0]
        y=key[1]
        p=key[2]
        if chars == 3:
            grid[y][x] = str(records[key]).zfill(3)[:chars]
        else:
            grid[y][x] = str(records[key])[:chars]
        
    print('\n')
    for row in grid:
        if chars == 3:
            print(' '.join(row))
        else:
            print(''.join(row))
        
records = {(0,0,'>0'):0}
keysToNavigate = []
x=0
y=0
p='>0'
key = (x,y,p)
keysToNavigate.append(key)
printNextKeys(keysToNavigate)

records[key] = 0
results = []
stepCounter = 0
while keysToNavigate:
    stepCounter +=1
    nextKeys = []
    #printNextKeys(keysToNavigate)
    #print(f'\nStarted {keysToNavigate=} {records=}')
    for key in keysToNavigate:
        #print(f'Processing {key=}')
        x=key[0]
        y=key[1]
        p=key[2]


        curWeight = records[key]
        #print(f'-- Navigating {key=} {records[key]}')

        cd = p[0]
        cc = int(p[1:])

        if (x == width -1) and (y == height -1):
            if (cc >=4) and (cc <= 10):
                print(f'Success. Reached the end {key=} {records[key]=}')
                results.append(records[key])
            else:
                print(f'Failed. Reached the end, but overrunning {key=} {records[key]=}')
            continue
        
        for direc in ['>', '<', '^', 'v']:

            if direc == '>':
                if (cd != '<') and (((cd == direc) and cc < 10) or (cd in ['^','v'] and cc >= 4 and cc <= 10)): # can go right
                    if cd == '>':
                        newp = cd + str(cc+1)
                    else:
                        newp = '>1'
                    nextKey = (x+1, y, newp)
                else:
                    #print(f'Not going {direc} {key=}')
                    continue
                    
            if direc == '<':
                if (cd != '>') and (((cd == direc) and cc < 10) or (cd in ['^','v'] and cc >= 4 and cc <= 10)): # can go left
                    if cd == '<':
                        newp = cd + str(cc+1)
                    else:
                        newp = '<1'
                    nextKey = (x-1, y, newp)
                    
                else:
                    #print(f'Not going {direc} {key=}')
                    continue
                
            if direc == 'v':
                if (cd != '^') and (((cd == direc) and cc < 10) or (cd in ['>','<'] and cc >= 4 and cc <= 10)): # can go down
                    if cd == 'v':
                        newp = cd + str(cc+1)
                    else:
                        newp = 'v1'
                    nextKey = (x, y+1, newp)
                else:
                    #print(f'Not going {direc} {key=}')
                    continue

            if direc == '^':
                if (cd != 'v') and (((cd == direc) and cc < 10) or (cd in ['>','<'] and cc >= 4 and cc <= 10)): # can go up
                    if cd == '^':
                        newp = cd + str(cc+1)
                    else:
                        newp = '^1'
                    nextKey = (x, y-1, newp)
                else:
                    #print(f'Not going {direc} {key=}')
                    continue

            nx=nextKey[0]
            ny=nextKey[1]
            if (nx< 0) or (ny < 0) or nx > (width-1) or (ny > height-1):
                #print(f'Off grid {nextKey=}')
                continue

            newWeight = curWeight + getWeight(nextKey[0],nextKey[1])
            if nextKey in records:
                oldWeight = records[nextKey]
                if newWeight >= oldWeight:
                    #print(f'Too heavy going {direc} {key=} {newWeight=} {oldWeight=}')
                    continue
            records[nextKey] = newWeight
            #print(f'Adding {direc} {nextKey=} {newWeight=}')
            nextKeys.append(nextKey)
    keysToNavigate=nextKeys
    print('stepCounter',stepCounter)
    if stepCounter == 1000:
        break
    if stepCounter %50 == 0:
        printNextKeys(keysToNavigate,1)

printNextKeys(keysToNavigate,1)
print(results)
print(min(results))
#1165 is too high
