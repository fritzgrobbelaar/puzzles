import cleaninput
from datetime import datetime
from functools import cmp_to_key
import math
import itertools
global listOfText
listOfText = cleaninput.getfileInputLinesAsList('input_10.txt')

sample='''[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
[...#..#.#.] (0,3,8) (4,6,7,9) (1,2,4,5,6,7) (1,2,3,5,6) (7) (0,2,4,5,7) (1,2,5,6,9) (1,2,5,6,7,8,9) (6,9) (2,3,5,8,9) (0,1,2,5,8,9) (0,1,5) (4,9) {48,42,54,27,48,66,42,67,50,68}
[#.##] (3) (0,1) (1,2,3) (0,2,3) (0,2) {197,187,34,33}
'''.split('\n')

extracases = '''
'''

test=False
if test:
    listOfText = sample
#print(f'{listOfText=}\n')
listOfText = [item for item in listOfText if item.strip() != '']
listOfText = [row.split(' ') for row in listOfText]

def convertValueToBinary(value, length):
    #print(f'converting to binary {value=} {length=}')
    value = value[1:-1]
    value= value.split(',')
    longestString = ['.']*length
    for digit in value:
        try:
            longestString[int(digit)] = '#'
        except IndexError:
            print('something went wrong',length, value)
            raise
    string = ''.join(longestString)
    #print(f'returning {string=}')
    return string

assert  '...#' == convertValueToBinary('(3)',4)
assert  '...#.' == convertValueToBinary('(3)',5)
assert  '#.#' == convertValueToBinary('(2,0)',3)
assert  '.#.#' == convertValueToBinary('(3,1)',4)

def convertEndState(endState):
    endState = endState[1:-1]
    return endState

assert '.#..' == convertEndState('[.#..]')

def flipSwitches(switches, flips):
    if len(switches) != len(flips):
        raise ValueError(' lengths should be the same')
    newList = []
    for i,value in enumerate(switches):
        value2 = flips[i]
        if value == value2:
            newList.append('.')
        else:
            newList.append('#')
    return ''.join(newList)


assert '....' == flipSwitches('....','....')
assert '..#.' == flipSwitches('..#.','....')
assert '..#.' == flipSwitches('....','..#.')
assert '#..#' == flipSwitches('...#','#...')
assert '#..#' == flipSwitches('.#.#','##..')

def calculateFewestPresses(endState, switches, permutationLimit):
    fewestPresses = 100000
    for comb in itertools.permutations(switches, permutationLimit):
        state = '.'*len(endState)
        for i,value in enumerate(comb):
            if i+1 >= fewestPresses:
                #print('already reached')
                break
            flips = convertValueToBinary(value,len(endState))
            state = flipSwitches(state, flips)
            #print(f'comparing {state=} {endState=}')
            if state == endState:
                fewestPresses = i+1
                #print(f'found one - breaking {comb=} {fewestPresses=}')
    return fewestPresses

fewestPressesTotal = 0

for row in listOfText:
    endState = convertEndState(row[0])
    switches = row[1:-1]
    #print(f'\n{len(switches)=} {row=}')

    for limit in [5, 6, 7]:
        fewestPresses = calculateFewestPresses(endState, switches, min(limit,len(switches)))
        if fewestPresses != 100000:
            break
        print('failed to calculate on', limit)
    else:
        print('failed to calculate')
    #print(f'{fewestPresses=} for {row=}')
    fewestPressesTotal += fewestPresses
print(f'{fewestPressesTotal=}')
#484 is too high
