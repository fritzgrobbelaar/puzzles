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
'''.split('\n')

test=False
if test:
    listOfText = sample
print(f'{listOfText=}\n')
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

fewestPressesTotal = 0

for row in listOfText:
    endState = convertEndState(row[0])
    switches = row[1:-1]

    combs = [list(x) for x in itertools.permutations(switches, len(switches))]
    combs = [com for com in combs if len(com) == len(switches)]
    print(f'{len(combs)=}')
    fewestPresses = 100000
    for comb in combs:
        state = '.'*len(endState)
        for i,value in enumerate(comb):
            if i+1 == fewestPresses:
                #print('already reached')
                break
            flips = convertValueToBinary(value,len(endState))
            state = flipSwitches(state, flips)
            #print(f'comparing {state=} {endState=}')
            if state == endState:
                print(f'found one - breaking {comb=}')
                fewestPresses = i+1
    print(f'{fewestPresses=} for {row=}')
    fewestPressesTotal += fewestPresses
print(f'{fewestPressesTotal=}')
