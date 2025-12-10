import cleaninput
from datetime import datetime
from functools import cmp_to_key
import math
from datetime import datetime
import itertools
global listOfText
listOfText = cleaninput.getfileInputLinesAsList('input_10.txt')

sample='''
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
[..####.] (0,2,4,6) (0,1,2,3,5) (0,1,2,3,6) (1,4) (0,5) (2,3,5) (3,6) (0,4) {40,25,40,35,11,33,20}
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
    return newSwitches
        
assert [(0, 1, 1, 1, 1), (1, 0, 1, 1, 1), (1, 1, 1, 0, 0), (0, 0, 1, 1, 0), (1, 0, 0, 0, 1)] == convertSwitches([(1,2,3,4), (0,2,3,4), (0,1,2), (2,3), (0,4)], [0,0,0,0,0])
    
def compareState(endState,state):
    #print('compareState', endState,state)
    if endState == state:
        #print('return matched')
        return 0
    for i, valueEnd in enumerate(endState):
        valueState = state[i]
        if valueState > valueEnd:
            #print(f'return too high {endState=} {state=} ')
            return 1
    #print('return too low')
    return -1
    
assert 0 == compareState(endState=(2,3), state=(2,3))
assert 1 == compareState(endState=(2,3), state=(2,4))
assert 1 == compareState(endState=(2,3), state=(3,1))
assert -1 == compareState(endState=(2,3), state=(1,2))
assert -1 == compareState(endState=(2,3), state=(2,2))
global cache
def calculateNewState(state, switchesCounters, switches):
    global cache
    
    #print(f'Calculating new state from {state=} and {switches=} with {switchesCounters=}')
    for i, it in enumerate(switchesCounters):
        if it == 0:
            continue
        switch = switches[i]
        for j,value in enumerate(state):
            state[j] += it*switch[j]
    #print(f'Returning {state=}')
    return state

assert [1,0,0] ==  calculateNewState([0,0,0], switchesCounters = [1], switches=[(1,0,0)])
assert [3,0,0] ==  calculateNewState([0,0,0], switchesCounters = [3], switches=[(1,0,0)])
assert [10,0,0] ==  calculateNewState([0,0,0], switchesCounters = [10,0], switches= [(1,0,0), (1,1,0)])
assert [18, 7, 5] ==  (calculateNewState([0,0,0],switchesCounters = [5,6,7], switches= [(1,0,1),(1,0,0), (1,1,0)]))


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
    if sum(switchesCounters) == 0:
        raise Exception ('something bad happened - all switchesCounters adds to 0')
    return switchesCounters
assert [1,1,0] == tensIncrease([1,0,1])
assert [2,0,0] == tensIncrease([1,1,0])
#assert 'bad things' == tensIncrease([1,0,0])

def validateSwitchesCountersStandAChance(endState,switches, switchesCounters):
    combined = [0]*len(endState)
    for i,value in enumerate(switchesCounters):
        if value == 0:
            continue
        combined = [a+b for a, b in zip(combined, switches[i])]
    for i, value in enumerate(combined):
        if value == 0 and endState[i]!=0:
            print('no way its gonna work')
            return False
    return True
            

assert False == validateSwitchesCountersStandAChance((4,9),[(0,1),(1,0)], [0,1])
assert False == validateSwitchesCountersStandAChance((4,9),[(0,1),(1,0)], [1,0])
assert True == validateSwitchesCountersStandAChance((4,9),[(0,1),(1,0)], [1,1])
print('new assertions pass')
def getLowestIteration(row):
    global cache
    cache = {}
    now = datetime.now()
    nowString = datetime.strftime(datetime.now(),'%Y:%m:%d %H:%M:%S')
    print(f'\n\n ---- New row -- {nowString=}\n',row)
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
    justOneIncrement = [0]*len(switches)
    justOneIncrement[-1] = 1
    print(f'{switches=}')
    counter = 1
    iterCounter = 0
    switchesCounters[-1] = 1
    state = calculateNewState(originalState[:], switchesCounters, switches)
    now2 = datetime.now()
    lastResult = 'too low'
    while lastResult != 'matched':
        print(f'{switchesCounters=}')
        iterCounter += 1
        if iterCounter % 1000000 == 0:
            itertime = datetime.now() - now2
            print(f'processing iterCounter, {iterCounter=} {switchesCounters=} {itertime=}')
            now2 = datetime.now()
        lastResult = compareState(endState,state)
        if lastResult == 0:
            resultCounter = sum(switchesCounters)
            timeDelta = datetime.now()-now
            print(f'Returning {resultCounter=} after {timeDelta=}')
            return resultCounter
        if not validateSwitchesCountersStandAChance(endState, switches, switchesCounters):
            iterCounter += 1
            if iterCounter % 1000000 == 0:
                itertime = datetime.now() - now2
                print(f'While iterCounter, {iterCounter=} {switchesCounters=} {itertime=}')
            switchesCounters = tensIncrease(switchesCounters)
            switchesCounters[-1] += 1
            state = calculateNewState(originalState[:], switchesCounters, switches)
            continue
        if lastResult == -1:
        #    print(f'Too low - increasing last switch {switchesCounters} to {switchesCounters[-1]+1}')
            switchesCounters[-1] += 1
            state = calculateNewState(state, justOneIncrement, switches)
        elif lastResult == 1:
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
    counter = getLowestIteration(row)
    totalCounter += counter
    
print(f'{totalCounter=}')
