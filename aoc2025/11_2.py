import cleaninput
from datetime import datetime
from functools import cmp_to_key
import math
from datetime import datetime
import itertools
global listOfText
import copy
sample='''svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
'''.split('\n')

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
def calculatePaths(input_step,trackDac):
    #print(f'\n Calculate paths for {input_step=} {trackDac=}')
    trackDac = copy.deepcopy(trackDac)
    if input_step == 'fft':
        trackDac['fft'] = 1
    if input_step == 'dac':
        trackDac['dac'] = 1
        
    if input_step + str(trackDac) in cache.keys():
        return cache[input_step+ str(trackDac)]
    elif input_step == 'out':
        if trackDac['dac'] == 1 and trackDac['fft'] == 1:
        #if 'dac' in paths and 'fft' in paths:
                return 1
        else:
            return 0
    elif input_step not in nodeDicts.keys():
        print(f'this is weird - {input_step=} was never found')
        return 0
    else:
        totalPaths = 0
        for output_step in nodeDicts[input_step]:
            totalPaths += calculatePaths(output_step, trackDac)
        #print(f'Steps found {input_step=} {totalPaths=}')
        cache[input_step + str(trackDac)] = totalPaths
        return totalPaths
trackDac = {}
trackDac['fft'] = 0
trackDac['dac'] = 0
countPaths = calculatePaths('svr', trackDac)
print(f'{countPaths=}')
