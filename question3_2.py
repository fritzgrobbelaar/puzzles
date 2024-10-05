import re

with open('input3.txt') as handle:
    text = handle.readlines()

print(text[0])
print(text[-1])

text_sample= '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''.split()

gearLocations = []
for i, row in enumerate(text):
    row = row.strip()
    rowSymbols = []
    for j, letter in enumerate(row):
        if letter == '*':
            rowSymbols.append(j)
    gearLocations.append(rowSymbols)
print('gearLocations', gearLocations)

gears = {}

total = 0
for i, row in enumerate(text):
    row = row.replace('\\n', '')
    numberStart = None
    matchedSets = re.finditer('\d+', row)
    for numberMatch in matchedSets:
        alreadyMatched = False
        for location in range(numberMatch.span()[0], numberMatch.span()[1]):
            if alreadyMatched:
                continue
            symbolRows = []
            offset = -1
            if i != 0:
                symbolRows.append(gearLocations[i - 1])
            else:
                offset = 0
            symbolRows.append(gearLocations[i])
            if i != len(text)-1:
                symbolRows.append(gearLocations[i + 1])
            for k, symbolLocationRow in enumerate(symbolRows):
                for symbolLocation in symbolLocationRow:
                    if abs(symbolLocation - location) < 2:
                        number = int(numberMatch.group(0))
                        key = (i+k+offset, symbolLocation)
                        print('Match found because digit at:', i, location, ' touches gear at ', key,
                              symbolLocation, ' the number is:', number, 'new total:')

                        if key not in gears.keys():
                            gears[key] = []
                        gears[key].append(number)

                        alreadyMatched = True
                        break
total = 0
for key in gears.keys():
    if len(gears[key]) == 2:
        total = total + gears[key][0]*gears[key][1]

print('total:',total)