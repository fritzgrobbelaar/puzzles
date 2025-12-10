import cleaninput
from datetime import datetime
from functools import cmp_to_key
import math
import itertools
global listOfText
listOfText = cleaninput.getfileInputLinesAsList('input_10.txt')

sample='''[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}'''.split('\n')

extracases = '''
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
[...#..#.#.] (0,3,8) (4,6,7,9) (1,2,4,5,6,7) (1,2,3,5,6) (7) (0,2,4,5,7) (1,2,5,6,9) (1,2,5,6,7,8,9) (6,9) (2,3,5,8,9) (0,1,2,5,8,9) (0,1,5) (4,9) {48,42,54,27,48,66,42,67,50,68}
[#.##] (3) (0,1) (1,2,3) (0,2,3) (0,2) {197,187,34,33}
'''

test=True
if test:
    listOfText = sample
#print(f'{listOfText=}\n')
listOfText = [item for item in listOfText if item.strip() != '']
listOfText = [row.split(' ') for row in listOfText]

def sortSwitches(switches):
    withSizes= []
    for switch in switches:
        withSizes.append([len(switch),switch])
    withSizes.sort()
    switches = [withSize[1] for withSize in withSizes]
    
    return switches
    
assert ['(0,4)', '(2,3)',  '(0,1,2)','(0,2,3,4)',  '(1,2,3,4)',] == sortSwitches(['(0,2,3,4)' ,'(2,3)', '(0,4)' ,'(0,1,2)' ,'(1,2,3,4)'])

def parseSwitches(listOfStrings):
    listOfTuples = []
    for switch in listOfStrings:
        switch = switch[1:-1]
        switch = switch.split(',')
        switch = [int(switchItem) for switchItem in switch]
        listOfTuples.append(tuple(switch))
    #print(f'{listOfTuples=}')
    return listOfTuples
        
assert [(1,2,3,4), (0,2,3,4), (0,1,2), (2,3), (0,4)] == parseSwitches(['(1,2,3,4)', '(0,2,3,4)', '(0,1,2)', '(2,3)', '(0,4)'])

def getLength(switches):
    highestValue = 0
    for switch in switches:
        for switchItem in switch:
            if switchItem > highestValue:
                highestValue = switchItem
    return highestValue+1
    
def convertSwitches(switches, state):
    newSwitches = []
    originalState = state
    for switch in switches:
        state = originalState[:]
        for switchValue in switch:
            state[switchValue] = 1
        newSwitches.append(tuple(state))
        #print(f'{state=}')
    #print(f'{newSwitches=}')
    return newSwitches
        
assert [(0, 1, 1, 1, 1), (1, 0, 1, 1, 1), (1, 1, 1, 0, 0), (0, 0, 1, 1, 0), (1, 0, 0, 0, 1)] == convertSwitches([(1,2,3,4), (0,2,3,4), (0,1,2), (2,3), (0,4)], [0,0,0,0,0])
    
def compareState(endState,state):
    #print('compareState', endState,state)
    if endState == state:
        #print('return matched')
        return 'matched'
    for i, valueEnd in enumerate(endState):
        valueState = state[i]
        if valueState > valueEnd:
           # print('return too high')
            return 'too high'
    #print('return too low')
    return 'too low'
    
assert 'matched' == compareState(endState=(2,3), state=(2,3))
assert 'too high' == compareState(endState=(2,3), state=(2,4))
assert 'too high' == compareState(endState=(2,3), state=(3,1))
assert 'too low' == compareState(endState=(2,3), state=(1,2))
assert 'too low' == compareState(endState=(2,3), state=(2,2))

def calculateNewState(state, switchesCounters, switches):
   # print(f'\n{switchesCounters=}')
    #print(f'\nCalculate new state from: {state=} {iteration=} {switches=}')
    for i, it in enumerate(switchesCounters):
        if it == 0:
            continue
        switch = switches[i]
        for j,value in enumerate(state):
            state[j] += it*switch[j]
    #print(f'Returning {state=} {iteration=}, {switchesCounters=}')
    return state

#assert str(([24,56,45], [1])) ==  #str(calculateNewState([23,56,45], [1], (1,0,0)], switchesCounters = [0]))
#assert str(([22,56,45], [2])) ==  str(calculateNewState([23,56,45], [-1], [(1,0,0)], switchesCounters = [3]))
#assert str(([24, 56, 45],  [11,0])) ==  str(calculateNewState([23,56,45], [1,0], [(1,0,0), (1,1,0)], switchesCounters = [10,0]))
#assert str(([23, 55, 0], [5,7,6])) ==  str(calculateNewState([23,56,0], [0,1,-1], [(1,0,1),(1,0,0), (1,1,0)], switchesCounters = [5,6,7]))

def tensIncrease(switchesCounters):
    #print(f'Increasing {switchesCounters=} by tens')
    length = len(switchesCounters)
    value = 0
    for i in range(length-1, -1, -1):
        value = switchesCounters[i]
     #   print(f'Checking position {i} with value {value} {switchesCounters=}')
        if value == 0:
            pass
        else:
            if i == 0:
                raise Exception('bad things')
            #print(f'adding to position {i=}')
            switchesCounters[i-1] += 1
            switchesCounters[i] = 0
            break
    #print(f'Returning {switchesCounters=}')
    return switchesCounters
assert [1,1,0] == tensIncrease([1,0,1])
assert [2,0,0] == tensIncrease([1,1,0])
#assert 'bad things' == tensIncrease([1,0,0])


def getLowestIteration(row):
    print('\n\n ---- New row --',row)
    endState = row[-1]
    endState = list(parseSwitches([endState])[0])
    print(f'{endState=}')
    switches = row[1:-1]
    switches = sortSwitches(switches)
    switches = parseSwitches(switches)
    length = len(endState) 
    state = [0]*length
    originalState = state[:]
    switches = convertSwitches(switches, state[:])
    switchesCounters = [0]*len(switches)
    print(f'{switches=}')
    counter = 1
    
    lastResult = 'too low'
    while lastResult != 'matched':
       # print(f'{switchesCounters=} {state=} {lastResult=}')
        lastResult = compareState(endState,state)
        if lastResult == 'matched':
            resultCounter = sum(switchesCounters)
            print(f'Returning {resultCounter=}')
            return resultCounter
        if lastResult == 'too low':
        #    print(f'Too low - increasing last switch {switchesCounters} to {switchesCounters[-1]+1}')
            switchesCounters[-1] += 1
        elif lastResult == 'too high':
            switchesCounters = tensIncrease(switchesCounters)
        state = calculateNewState(originalState[:], switchesCounters, switches)
    raise Exception('should not reach here')

print('\n-------------------------\n')
assert 1 == getLowestIteration(row=['[.##.]', '(1)', '(2,1)', '(1,2,3)', '{0,1,1,1}'])
assert 2 == getLowestIteration(row=['[.##.]', '(1)', '(2,1)', '{0,2,0,0}'])
assert 2 == getLowestIteration(row=['[.##.]', '(1)', '(2,1)', '(3,2,1)', '{0,2,0,0}'])
assert 3 == getLowestIteration(row=['[.##.]', '(2)', '(1,2)', '(3,2,1)', '{0,2,3,0}'])
assert 2 == getLowestIteration(row=['[.##.]', '(1)', '{0,2,0,0}'])
assert 10 == getLowestIteration(row=['[.##.]', '(3)', '(1,3)', '(2)', '(2,3)', '(0,2)', '(0,1)', '{3,5,4,7}'])
print('\n-------------------------\n\n\n\n -- the real deal ----\n')

totalCounter = 0
for row in listOfText:
    print(f'\n ------------\n{row=}')
    counter = getLowestIteration(row)
    totalCounter += counter
    
print(f'{totalCounter=}')
