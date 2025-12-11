import cleaninput
from datetime import datetime
from functools import cmp_to_key
import math
from datetime import datetime
import itertools
global listOfText

sample='''
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out'''.split('\n')

test=False
if test:
    listOfText = sample
else:
    listOfText = cleaninput.getfileInputLinesAsList('input_11.txt')

#print(f'{listOfText=}\n')
listOfText = [item for item in listOfText if item.strip() != '']
listOfText = [row.split(' ') for row in listOfText]

nodeDicts = {}
for row in listOfText:
    nodeDicts[row[0][:-1]] = row[1:]

global cache
cache = {}
def calculatePaths(input_step):
    #print(f'\n Calculate paths for {input_step=}')
    if input_step in cache.keys():
        return cache[input_step]
    elif input_step == 'out':
        return 1
    elif input_step not in nodeDicts.keys():
        print(f'this is weird - {input_step=} was never found')
        return 0
    else:
        totalPaths = 0
        for output_step in nodeDicts[input_step]:
            totalPaths += calculatePaths(output_step)
        #print(f'Steps found {input_step=} {totalPaths=}')
        cache[input_step] = totalPaths
        return totalPaths
countPaths = calculatePaths('you')
print(f'{countPaths=}')
