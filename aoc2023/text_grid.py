def findLocationsOfLetters(grid, symbols):
    symbolLocations = []
    symbols = set(symbols)
    for i, row in enumerate(grid):
        for j, letter in enumerate(row):
            if letter in symbols:
                symbolLocations.append((i, j))
    return symbolLocations


def getNextLocationPipes(grid, currentLocation):
    width = len(grid[0])
    height = len(grid)

    def getChar(location):
        return grid[location[0]][location[1]]

    i = currentLocation[0]
    j = currentLocation[1]

    def def_above(i, j):
        return (i - 1, j)

    def def_to_right(i, j):
        return (i, j + 1)

    def def_to_left(i, j):
        return (i, j - 1)

    def def_below(i, j):
        return (i + 1, j)

    above = def_above(*currentLocation)
    to_right = def_to_right(*currentLocation)
    to_left = def_to_left(*currentLocation)
    below = def_below(*currentLocation)

    options = {
        'S': [above, to_right, to_left, below],
        'L': [above, to_right],
        '-': [to_left, to_right],
        'F': [to_right, below],
        'J': [above, to_left],
        '|': [above, below],
        '7': [to_left, below]
    }

    next_options = {
        'S': [def_above, def_to_right, def_to_left, def_below],
        'L': [def_above, def_to_right],
        '-': [def_to_left, def_to_right],
        'F': [def_to_right, def_below],
        'J': [def_above, def_to_left],
        '|': [def_above, def_below],
        '7': [def_to_left, def_below],
        '.': [],
        '*': []
    }

    for (i, j) in [above, to_right, to_left, below]:
        for k, direction in enumerate(options[getChar(currentLocation)]):
            i = direction[0]
            j = direction[1]
            if (i < 0) or (j < 0):
                pass
            elif (i > width) or (j > height):
                pass
            symbol = getChar((i, j))
            for next_option in next_options[symbol]:
                if currentLocation == next_option(i, j):
                    return (i, j)


def navigatePipesAndCountLength(grid, startLocation):
    print('\n\n-----Starting \n', grid, '\n', startLocation)

    nextLocation = startLocation[:]
    count = 0
    while nextLocation != None:
        count = count + 1
        oldLocation = nextLocation
        nextLocation = getNextLocationPipes(grid, nextLocation)
        print(nextLocation)
        grid[oldLocation[0]][oldLocation[1]] = '*'
        if count > 100000:
            raise Exception('Soft Limit reached', count)
    return count / 2


def countDotsSurroundedByPipes(originalGrid):
    print('originalGrid:\n', originalGrid)

    for row in originalGrid:
        print(''.join(row))
    tiles = 0
    openCharacter = None
    flip = False
    for i, row in enumerate(originalGrid):
        print('i', row)
        inside = False
        for j, value in enumerate(row):
            print(f'{inside=}')
            flip = False
            if inside and value == '.':
                tiles += 1

            if value == '|':
                flip = True
            elif value == 'F':
                openCharacter = None
                if value == 'J':
                    flip = False
                else:
                    flip = True
            elif openCharacter == 'L':
                openCharacter = None
                if value == '7':
                    flip = False
                else:
                    flip = True
            elif value in ['F', 'L']:
                print('setting open character because of ', f'{value}')
                openCharacter = value
                flip = True
            if flip:
                if inside:
                    inside = False
                else:
                    inside = True
    return tiles
