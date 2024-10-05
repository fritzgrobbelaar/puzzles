import re

with open('input3.txt') as handle:
    text = handle.readlines()

print(text[0])
print(text[-1])

text_3= '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''.split()

symbolLocations = []
for i, row in enumerate(text):
    row = row.strip()
    rowSymbols = []
    for j, letter in enumerate(row):
        #    print('i', i, j, letter, letter.isdigit(), letter != '.')
        if letter != '.' and not letter.isdigit():
            rowSymbols.append(j)
    symbolLocations.append(rowSymbols)
print('symbolLocations', symbolLocations)

total = 0
for i, row in enumerate(text):
    row = row.replace('\\n', '')
    numberStart = None
    matchedSets = re.finditer('\d+', row)
    for numberMatch in matchedSets:
        #print(numberMatch, row)
        alreadyMatched = False
        for location in range(numberMatch.span()[0], numberMatch.span()[1]):
            if alreadyMatched:
                continue
#            print('i', i, location)
            symbolRows = []
            if i != 0:
                symbolRows.append(symbolLocations[i - 1])
            symbolRows.append(symbolLocations[i])
            if i != len(text)-1:
                symbolRows.append(symbolLocations[i + 1])
            for k, symbolLocationRow in enumerate(symbolRows):
                for symbolLocation in symbolLocationRow:
                    if abs(symbolLocation - location) < 2:
                        number = int(numberMatch.group(0))
                        total = total + number
                        print('Match found because digit at:', i, location, ' matches symbol at location', k,
                              symbolLocation, ' adding:', number, 'new total:', total)

                        alreadyMatched = True
                        break
print('total:',total)