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


rules = {
    '0': '1',
    'even': '*2' + 'engraved',
    'else': '*2024'
}

def blink(stones):
    #print(f'\n Before iteration {stones=}')
    stonesOriginal = copy.deepcopy(stones)
    arrayJump = 0
    for i,value in enumerate(stonesOriginal):
        i = i + arrayJump
       # print(f'Processing {value=}')
        if value == 0:
            valueArray = [1]
        elif len(str(value)) %2 == 0:
            valueString = str(value)
            arrayLengthHalf = int(len(valueString)/2)
            valueArray = [int(valueString[:arrayLengthHalf]), int(valueString[arrayLengthHalf:])]
            arrayJump += 1
        else:
            valueArray = [value *2024]
       # print(f'{stones=} {i=}')
      #  print(f'{stones[:i]=} + {valueArray=} + {stones[i+1:]=} {i=}')
        stones = stones[:i] + valueArray + stones[i+1:]

     #   print(f'After iteration {stones=}')
    #print(f'After blink {stones=}')
    return stones

#assert [253000, 1, 7] == blink(stones)

for i in range(25):
    print('Processing iteration', i, datetime.datetime.now())
    stones = blink(stones)

#print(f'{stones=}')
print(f'{len(stones)=}')
