import cleaninput
from datetime import datetime
from functools import cmp_to_key
import datetime
import copy
listOfText = cleaninput.getfileInputLinesAsList('input12_2024.txt')



sample = '''125 17'''.split('\n')
#sample = '''0 1 10 99 999'''.split('\n')

listOfText = sample

listOfLists = []
total = 0
for row in listOfText:
    listOfLists.append(row.split())

print(f'{listOfLists=}')

def count(stones):
    total = 0
    for stoneList in stones:
        if type(stoneList)== list:
            total += count(stoneList)
        else:
            total += 1
    return total

total = count(listOfLists)

print(f'{total=}')
