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


def blink(stones):
    #print(f'\n Before iteration {stones=}')
    #stonesOriginal = copy.deepcopy(stones)

    for i,value in enumerate(stones):
    #    print(f'Processing {value=}')
        if type(value) == list:
            valueArray = blink(value)
        elif value == 0:
            valueArray = [1]
        elif len(str(value)) %2 == 0:
            valueString = str(value)
            arrayLengthHalf = int(len(valueString)/2)
            valueArray = [int(valueString[:arrayLengthHalf]), int(valueString[arrayLengthHalf:])]
        else:
            valueArray = [value *2024]
      #  print(f'{stones=} {i=}')
        stones[i] = valueArray
     #   print(f'After iteration {stones=}')
    #print(f'After blink {stones=}')
    return stones

#assert [[253000], [1, 7]] == blink(stones)

def count(stones):
    total = 0
    for stoneList in stones:
        if type(stoneList)== list:
            total += count(stoneList)
        else:
            total += 1
    return total

for i in range(25):
    print('Processing iteration', i+1, datetime.datetime.now())
    stones = blink(stones)

total = count(stones)

#print(f'{stones=}')
print(f'{total=}')
