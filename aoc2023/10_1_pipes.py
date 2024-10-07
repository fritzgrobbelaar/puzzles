from lib import cleaninput
from lib.text_grid import findLocationsOfLetters

listOfText_Puzzle = cleaninput.getRowsOfNumbersLists('aoc2023\\input10.txt')

listOfText_Sample='''.....
.S-7.
.|.|.
.L-J.
.....'''.split('\n')
listOfText_Sample = cleaninput.convertRowsOfTextToRowsOfNumbers(listOfText_Sample)

text = listOfText_Sample


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