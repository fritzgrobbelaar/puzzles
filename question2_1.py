with open('input2.txt') as handle:
    text = handle.readlines()

maxCount = {
    'red':   12,
    'green': 13,
    'blue': 14
}

total = 0
for i, row in enumerate(text):
    row = row.replace('\\n','')
    maxBlue = 0
    maxGreen = 0
    maxRed = 0
    gameNumber = int(row.split(':')[0].split(' ')[1])
    print('\ngameNumber:',gameNumber, 'row:', row)
    numbersFull = row.split(':')[1]
    numbers = numbersFull.split(';')
    rowBad = False
    print('numbers:', numbers)
    for number in numbers:

        fewValues = number.split(',')
        for oneValue in fewValues:
            oneValue = oneValue[1:]
            value,key = oneValue.split(' ')
            if int(value) > maxCount[key.strip()]:
                print('bad row:', gameNumber, key.strip(), value)
                rowBad = True
                break
    if not rowBad:
        print('good row:', gameNumber)
        total = total + gameNumber
print('total:', total)