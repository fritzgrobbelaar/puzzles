import cleaninput
from datetime import datetime
from functools import cmp_to_key
global output
listOfText = cleaninput.getfileInputLinesAsList('input14_2024.txt')
roomX = 101
roomY = 103

output = ''

sample = '''p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3'''.split('\n')

#sample = '''p=2,4 v=2,-3'''.split('\n')
#sample = '''p=0,0 v=-1,-1'''.split('\n')
sample2 = '''p=0,0 v=1,1
p=1,0 v=1,1
p=1,1 v=1,1
p=0,1 v=1,1'''.split('\n')

sample = '''p=0,0 v=0,0
p=1,0 v=0,0
p=2,0 v=0,0
p=3,0 v=0,0
p=4,0 v=0,0
p=5,0 v=0,0
p=6,0 v=0,0
p=7,0 v=0,0'''.split('\n')




roomXSample = 11
roomYSample = 7

#listOfText = sample
#roomX = roomXSample
#roomY = roomYSample

listOfLists = []
total = 0

robots = []
for row in listOfText:
    #    print(f'{row=}')
    row = row.split(' ')
    position = row[0].split('=')[1].split(',')
    velocity = row[1].split('=')[1].split(',')
   # print(f'{position=}')
    position = int(position[0]), int(position[1])
    velocity = int(velocity[0]), int(velocity[1])

    robots.append({'p':position, 'v':velocity, 'cycle': 0})

#print(f'{robots=}')

def printMap(roomX, roomY, robots, consecutiveCount=0, cycleCount=0):
    global output
    #output += '\n'

    locations = {}
    horizontals = {}
    for robot in robots:
        x = robot['p'][0]
        y = robot['p'][1]
        if robot['p'] not in locations.keys():
            locations[robot['p']] = 0
        locations[robot['p']] += 1
        if y not in horizontals:
            horizontals[y] = []
        horizontals[y].append(x)

    found = False
    #print(f'{horizontals=}')
    for horizontal in horizontals.values():
        horizontal.sort()
        #print(f'{horizontal=}')
        count = 0
        for i,value in enumerate(horizontal[:-1]):
            #print(f'Comparing {value+1=} {horizontal[i+1]=}')
            if value+1 == horizontal[i+1]:
                count +=1
        if count > consecutiveCount:
            #print('seems to match')
            found = True
    if (not found) and (cycleCount not in [0,1,2]):
        return

    output = output + '\n' + str(cycleCount)
    for y in range(roomY):
        printRow = []
        for x in range(roomX):
            if (x,y) in locations:
                printRow.append(str(locations[(x,y)]))
            else:
                printRow.append('.')
        #print(''.join(printRow))
        output += '\n'
        output += ''.join(printRow)
        #output.append()

#printMap(roomX, roomY, robots)


def calculateStep(robot, roomX, roomY):
    newX = robot['v'][0] + robot['p'][0]
    newY = robot['v'][1] + robot['p'][1]
    #print(f'\nCalculated{newX=} {newY=}')

    maxX = roomX - 1
    maxY = roomY - 1
    if newX < 0:
        newX = roomX + newX
     #   print(f'too left, {newX=}')
    elif newX > maxX:
      #  print(f'too right, {newX=}')
        newX = newX - roomX

    if newY < 0:
#        print(f'too up, {newY=}')
        newY = roomY + newY

    elif newY > maxY:
       # print(f'too below, {newY=}')
        newY = newY - roomY

    newPosition = (newX, newY)
    #print(f'{newPosition=}')

    robot['p'] = newPosition
    #printMap(roomX, roomY, [robot])

    return robot


cycles = 10000
for i in range(cycles):
    #global output
    #output += '\n'
    #output += str(i+1)
    print('Starting cycle', i+1)
    for j, robot in enumerate(robots):
        robots[j] = calculateStep(robot, roomX, roomY)

    printMap(roomX, roomY, robots, consecutiveCount=10, cycleCount=i+1)

def calculateTotal(robots):
    midX = int(roomX/2)
    midY = int(roomY/2)
    print(f'{midX=} {roomX=}')
    leftTop = 0
    rightTop = 0
    leftBottom = 0
    rightBottom = 0
    for robot in robots:
        p = robot['p']
        x = p[0]
        y = p[1]
        if x<midX and y< midY:
            leftTop += 1
        if x>midX and y< midY:
            rightTop += 1
        if x<midX and y> midY:
            leftBottom += 1
        if x>midX and y> midY:
            rightBottom += 1

    print(f'{leftTop=} {rightTop=} {leftBottom=} {rightBottom}')
    return leftTop*rightTop*leftBottom*rightBottom
total = calculateTotal(robots)
print(f'{total=}')

with open('../../picture.txt', 'w') as handle:
    handle.write(output)