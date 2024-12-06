import cleaninput
from datetime import datetime
listOfText = cleaninput.getfileInputLinesAsList('input6_2024.txt')


sample = '''...........
...#.......
#<.........
..#........'''.split('\n')

sample = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''.split('\n')

#listOfText = sample

listOfLists = []
for row in listOfText:
    listOfLists.append(list(row))

distinctPositions = set()
distinctPositionsAndDirection = set()

def printMap(listOfLists, distinctPositionsAndDirection, distinctPositions):
    for j, row in enumerate(listOfLists):
        newRow = []
        for i,value in enumerate(row):
            if (i,j) in distinctPositions:
                newRow.append('0')
            else:
                newRow.append(value)
        #print(''.join(newRow))

def findStart(listOfLists):
    for j, row in enumerate(listOfLists):
        for i, value in enumerate(row):
            if value not in ('.', '#'):
                return i, j, value

#assert (4, 6, '^') == findStart(listOfLists)
start = findStart(listOfLists)

print("Starting at", datetime.now())
timeStart = datetime.now()

while start not in distinctPositionsAndDirection:
    distinctPositionsAndDirection.add(start)
    i=start[0]
    j=start[1]
    direction=start[2]
    distinctPositions.add((i, j))
    #print(f'{sorted(list(distinctPositionsAndDirection))=}')
    #print(f'{distinctPositions=}')

    if direction == '^':
        if j == 0:
     #       print(f'Left Map above due to {j=}, {distinctPositionsAndDirection=}')
            break
        else:
            valueAbove = listOfLists[j-1][i]
            if valueAbove == '#':
           #     print('turning right 5')
                direction = '>'
              #  i = i + 1
            else:
                j = j-1

    elif direction == '<':
        if i == 0:
          #  print(f'Left Map on left due to {i=}, {distinctPositionsAndDirection=}')
            break
        else:
            valueLeft = listOfLists[j][i-1]
            if valueLeft == '#':
         #       print('turning up 3')
                direction = '^'
              #  j = j - 1
            else:
                i = i-1

    elif direction == 'v':
        #print(f'{j=} {len(listOfLists)=}')
        #print(f'{j=} {len(row)=}')
        if j == len(listOfLists)-1:
            #print(f'Left Map below due to {j=}, {distinctPositionsAndDirection=}')
            break
        else:
            valueBelow = listOfLists[j+1][i]
            if valueBelow == '#':
             #   print('turning right 1')
                direction = '<'
                #i = i - 1
            else:
                j = j+1

    elif direction == '>':
        if i == len(row)-1:
            #print(f'Left Map on right due to {i=}, {distinctPositionsAndDirection=}')
            break
        else:
            valueRight = listOfLists[j][i+1]
            if valueRight == '#':
      #          print('turning down 2')
                direction = 'v'
                #j = j + 1
            else:
                i = i+1

    start=(i,j,direction)
    printMap(listOfLists, distinctPositionsAndDirection, distinctPositions)

print(sorted(list(distinctPositions)))
print(f'{distinctPositionsAndDirection=}')

print(f'{len(distinctPositions)=}')

print('reached the end at', datetime.now(), 'it took', datetime.now() - timeStart)