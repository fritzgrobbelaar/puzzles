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

    def getChar(grid, location):
        return grid[location[0]][location[1]]

    i = currentLocation[0]
    j = currentLocation[1]
    above = (i, j - 1)
    to_right = (i + 1, j)
    to_left = (i - 1, j)
    below = (i, j + 1)

    options = {'S': [above, to_right, to_left, below],
               'L': [above, to_right],
               '-': [to_left, to_right],
               'F': [to_right, to_left],
               'J': [above, to_left],
               '|': [above, below],
               '7': [to_left, below]
               }

    for (i, j) in [above, to_right, to_left, below]:
        if (i < 0) or (j < 0):
            pass
        elif (i > width) or (j > height):
            pass
        aboveSymbol = above(*currentLocation)
        if grid[above[0]][above[1]] in ['F', '|', '7']:
            return grid, above(currentLocation)


def navigatePipesAndCountLength(grid, startLocation):
    return getNextLocationPipes(grid, startLocation)
