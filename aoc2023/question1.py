with open('input.txt') as handle:
    text = handle.readlines()

total = 0
for i,row in enumerate(text):
    print('row:', row)
    first = ''
    last = ''

    for character in row:
        if character.isdigit():
            first=character
            break

    reversed = list(row)
    reversed.reverse()
    print('row:', row,'reversed:', reversed)
    for character in reversed:
        if character.isdigit():
            last=character
            break
    print('first:',first,'last:', last)
    total = total + int(first + last)
    print('row:', i, first + last, 'total:', total)


