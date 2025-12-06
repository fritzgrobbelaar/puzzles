from lib import cleaninput

listOfText = cleaninput.getfileInputLinesAsList('aoc2023/input1_numbers_in_text.txt')

total = 0
for i, row in enumerate(listOfText):
    print('row:', row)
    first = ''
    last = ''

    for character in row:
        if character.isdigit():
            first = character
            break

    reversed = list(row)
    reversed.reverse()
    for character in reversed:
        if character.isdigit():
            last = character
            break
    total = total + int(first + last)
    print('row:', i, first + last, 'total:', total)
