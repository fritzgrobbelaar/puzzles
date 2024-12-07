import cleaninput
from datetime import datetime
listOfText = cleaninput.getfileInputLinesAsList('input7_2024.txt')

sample = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''.split('\n')

#listOfText = sample

listOfLists = []
total = 0
for row in listOfText:
    row = row.replace(':', '')
    oldRow = row.split(' ')
    row = [int(value) for value in oldRow]

    listOfLists.append(list(row))

    expectedValue = row[0]
    print(f'{expectedValue=}')
    combinedValues = [[row[1]]]
    print(f'{combinedValues=}')
    for value in row[2:]:
        print(f'{combinedValues=} {value=}')
        combinedValuesNew = []
        for combinedValue in combinedValues[-1]:
            combinedValuesNew.append(combinedValue*value)
            combinedValuesNew.append(combinedValue+value)
            combinedValuesNew.append(int(str(combinedValue)+str(value)))
        combinedValues.append(combinedValuesNew)
    if expectedValue in combinedValues[-1]:
        print(f'{expectedValue=} found in {combinedValues[-1]=}')
        total += expectedValue
    else:
        print(f'{expectedValue=} not found in {combinedValues[-1]=}')

print('total', total)


