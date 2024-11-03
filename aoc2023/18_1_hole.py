import cleaninput
from text_grid import countDotsSurroundedByPipes

listOfText_Puzzle = cleaninput.getfileInputLinesAsList('input18.txt')

listOfText_Sample1 = '''R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)'''.split('\n')

listOfText_Sample2 = '''L 6 (#70c710)
D 5 (#0dc571)
R 2 (#5713f0)
D 2 (#d2c081)
L 2 (#59c680)
D 2 (#411b91)
R 5 (#8ceee2)
U 2 (#caa173)
R 1 (#1b58a2)
U 2 (#caa171)
L 2 (#7807d2)
U 3 (#a77fa3)
R 2 (#015232)
U 2 (#7a21e3)'''.split('\n')

listOfText = listOfText_Puzzle
#listOfText = listOfText_Sample1
#listOfText = listOfText_Sample2

grid = []


def printGrid(points):
    print('\n-- print grid')
    minX = 0
    maxX = 0
    minY = 0
    maxY = 0
    for point in points:
        x = point[0]
        y = point[1]
        if x < minX:
            minX = x
        if x > maxX:
            maxX = x
        if y < minY:
            minY = y
        if y > maxY:
            maxY = y
    width = maxX - minX
    height = maxY - minY
    grid = []
    print(f'{height=} {width=}')
    for i in range(height + 1):
        row = []
        for j in range(width + 1):
            row.append('.')
        grid.append(row)

    for point in points:
        y = point[1] - minY
        x = point[0] - minX
        p = point[2]
        grid[y][x] = p

    print('-- print grid2')
    for row in grid:
        print(''.join(row))
    return grid


elbows = {}
points = []
point = (0, 0)
points.append(point)
prevD = 'U'
for row in listOfText:
    x = point[0]
    y = point[1]
    rowList = row.split(' ')
    d = rowList[0]
    dis = int(rowList[1])

    for i in range(dis):
        if i == 0:
            if d == 'R':
                if prevD == 'U':
                    p = 'F'
                else:
                    p = 'L'
            elif d == 'L':
                if prevD == 'U':
                    p = '7'
                    print(f'Adding 7 at {x=} {y=} {row=} {d=} {prevD=}')
                elif prevD == 'D':
                    p = 'J'
                else:
                    raise ValueError('this is unexpected')

            elif d == 'U':
                if prevD == 'L':
                    p = 'L'
                else:
                    p = 'J'

            elif d == 'D':
                if prevD == 'L':
                    p = 'F'
                else:
                    p = '7'

        elif (d == 'R') or (d == 'L'):
            p = '-'
        elif (d == 'U') or (d == 'D'):
            p = '|'
        if d == 'R':
            x += 1
        if d == 'L':
            x -= 1
        if d == 'D':
            y += 1
        if d == 'U':
            y -= 1
        point = (x, y)
        prevD = d
        points[-1] = points[-1][0], points[-1][1], p
        points.append(point)

points[-1] = points[-1][0], points[-1][1], 'F' #Remember to check starting condition

print(points)
grid = printGrid(points)

totalInside = countDotsSurroundedByPipes(grid)
print(f'{totalInside=}')
print('elbows', elbows)
print(len(points))
print('set', len(set(points))) # should be one less
print('totalInside', totalInside + len(set(points)))
