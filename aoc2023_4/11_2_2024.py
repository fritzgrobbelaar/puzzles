import cleaninput
from datetime import datetime
from functools import cmp_to_key
import datetime
import copy
listOfText = cleaninput.getfileInputLinesAsList('input11_2024.txt')



sample = '''125 17'''.split('\n')
#sample = '''0 1 10 99 999'''.split('\n')

#listOfText = sample

listOfLists = []
total = 0
for row in listOfText:
    listOfLists.append(row.split())

stones = listOfLists[0]

stones = [int(value) for value in stones]
#stones = [[stone] for stone in stones]

rules = {
    '0': '1',
    'even': '*2' + 'engraved',
    'else': '*2024'
}

lookupDict= {}

def rule(value):
    if value == 0:
        valueArray = [1]
    elif len(str(value)) %2 == 0:
        valueString = str(value)
        arrayLengthHalf = int(len(valueString)/2)
        valueArray = [int(valueString[:arrayLengthHalf]), int(valueString[arrayLengthHalf:])]
    else:
        valueArray = [value *2024]
    return valueArray

def navigateTree(number, depthRemaining):
    key = (number, depthRemaining)
    #print(f'{key=}')
    if key in lookupDict.keys():
        return lookupDict[key]
    elif depthRemaining == 0:
        return 1
    else:
        depthRemaining = depthRemaining - 1
        valueArray = rule(number)
        total = 0
        for value in valueArray:
            newAnswer = navigateTree(value, depthRemaining)
            lookupDict[(value, depthRemaining)] = newAnswer
            total = total + newAnswer
        return total


totalDepth = 75
total = 0
for stone in stones:
    print('\n\nProcessing stone',stone,  '  at ', datetime.datetime.now(), 'depth', totalDepth)
    total += navigateTree(stone, totalDepth)

print(f'{total=}')
