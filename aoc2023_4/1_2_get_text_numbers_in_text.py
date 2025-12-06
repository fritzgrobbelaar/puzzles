with open('input1_numbers_in_text.txt') as handle:
    text = handle.readlines()

numberStrings = {
    'one':   '1',
    'two':   '2',
    'three': '3',
    'four':  '4',
    'five':  '5',
    'six':   '6',
    'seven': '7',
    'eight': '8',
    'nine':  '9'
}

total = 0
for i, row in enumerate(text):
    print('\ni:',i, 'row:', row)
    first = None
    last = None

    for i,character in enumerate(row):
        partialString = row[i:]
        if character.isdigit():
            last=character
            if first == None:
                first = character

        for numberString in numberStrings.keys():
            if partialString.startswith(numberString):
                digit = numberStrings[numberString]
                print('found, ',numberString,'row:', i)
                if first == None:
                    first=digit
                last=digit
    if first != None:
        print('first:', first, 'last:', last)
        total = total + int(first + last)
        print('row:', i, first + last, 'total:', total)
