import cleaninput
from datetime import datetime
from functools import cmp_to_key
import math
import itertools
global listOfText
listOfText = cleaninput.getfileInputLinesAsList('input_10.txt')

sample='''[.##.] (1) {0,2,0,0}
'''.split('\n')

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
    switches = list(reversed(switches))
    
    return switches
    
assert ['(1,2,3,4)', '(0,2,3,4)', '(0,1,2)', '(2,3)', '(0,4)'] == sortSwitches(['(0,2,3,4)' ,'(2,3)', '(0,4)' ,'(0,1,2)' ,'(1,2,3,4)'])

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
    if endState == state:
        return 'matched'
    for i, valueEnd in enumerate(endState):
        valueState = state[i]
        if valueState > valueEnd:
            return 'too high'
    return 'too low'
    
assert 'matched' == compareState(endState=(2,3), state=(2,3))
assert 'too high' == compareState(endState=(2,3), state=(2,4))
assert 'too high' == compareState(endState=(2,3), state=(3,1))
assert 'too low' == compareState(endState=(2,3), state=(1,2))
assert 'too low' == compareState(endState=(2,3), state=(2,2))

def calculateNewState(state, iteration, switches):
    print(f'\n{state=} {iteration=} {switches=}')
    for i, it in enumerate(iteration):
        if it == 0:
            continue
        switch = switches[i]
        print(f' {it} multiply {switch=} to {state=}')
        for j,value in enumerate(state):
            state[j] += it*switch[j]
    print(f'Returning {state=} {iteration=} {switches=}')
    return state
    
assert [24,56,45] ==  calculateNewState([23,56,45], [1], [(1,0,0)])
assert [22,56,45] ==  calculateNewState([23,56,45], [-1], [(1,0,0)])
assert [24, 56, 45] ==  calculateNewState([23,56,45], [1,0], [(1,0,0), (1,1,0)])
assert [23, 55, 0] ==  calculateNewState([23,56,0], [0,1,-1], [(1,0,1),(1,0,0), (1,1,0)])

def calculateNextIteration(iteration, state, lastResult):
    if lastResult == 'too low':
        return iteration
    elif lastResult == 'matched':
        raise Exception('could have been done already')
    else:  # careful binary logic
        
    
assert [1,0,0] == calculateNextIteration([1,0,0], [23,56,45], 'too low')
assert [1,0,0] == calculateNextIteration([10,57,0], [11,5,5], 'too high')

for row in listOfText:
    print(f'\n {row=}')
    endState = row[-1]
    endState = parseSwitches([endState])[0]
    print(f'{endState=}')
    switches = row[1:-1]
    switches = sortSwitches(switches)
    switches = parseSwitches(switches)
    length = len(endState) 
    state = [0]*length
    switches = convertSwitches(switches, state[:])
    
    iteration = [0]*len(switches)
    iteration[0] = 1
    lastResult = 'too low'
    while lastResult != 'matched':
        print(f'{iteration=} {state=} {lastResult=}')
        iteration = calculateNextIteration(iteration, state, lastResult)
        state = calculateNewState(state, iteration, switches)
        lastResult = compareState(endState,state)
    
    print(f'{switches=} {length=} {state=}')
    
