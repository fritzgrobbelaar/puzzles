with open('input2.txt') as handle:
    text = handle.readlines()

total = 0
for i, row in enumerate(text):
    row = row.replace('\\n', '')
    maxCount = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    gameNumber = int(row.split(':')[0].split(' ')[1])
    print('\ngameNumber:', gameNumber, 'row:', row)
    numbersFull = row.split(':')[1]
    numbers = numbersFull.split(';')
    rowBad = False
#    print('numbers:', numbers)
    for number in numbers:

        fewValues = number.split(',')
        for oneValue in fewValues:
            oneValue = oneValue[1:]
            value, key = oneValue.split(' ')
            key = key.strip()
            value = int(value)
            if value > maxCount[key]:
                print('increase value:', gameNumber, key.strip(), value)
                maxCount[key] = value
    power = maxCount['red']*maxCount['green']*maxCount['blue']
    print('gameNumber row score:', gameNumber, f'{maxCount=}', f'{power=}')
    total = total + power
print('total:', total)
