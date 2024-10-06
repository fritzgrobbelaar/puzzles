from lib import cleaninput
from lib.number_pattern import extrapolatePattern

listOfText_Puzzle = cleaninput.getRowsOfNumbersLists('aoc2023\\input9.txt')

listOfText_Sample='''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''.split('\n')
listOfText_Sample = cleaninput.convertRowsOfTextToRowsOfNumbers(listOfText_Sample)

listOfText = listOfText_Sample

print(listOfText)

exit()

for row in text:
    print(row)
    info = row.split(':')[1]
    left, right = info.split('|')
    numbers1= set(left.split())
    addRowWinnings = 0
    for number in right.split():
        if number in numbers1:
            print('found', number)
            if not addRowWinnings:
                addRowWinnings = 1
            else:
                addRowWinnings = addRowWinnings*2
    total = total+addRowWinnings
print('total:', total)
