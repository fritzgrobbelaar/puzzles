import cleaninput
from datetime import datetime
from functools import cmp_to_key
import math
from datetime import datetime
import itertools
global listOfText
import copy
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


def getStateIDsFromLeastReferenced(switches):
    """
    referencesCount first & id second. Example:
    input: [(1,0,1),(1,0,0), (1,1,0)]
    returns: [[1,1],[1,2],[2,0]]

    input: [(1,0,1),(1,0,0),(1,1,0),(1,0,1)]
    returns: [[1,2],[2,2],[4,0]]
    """
    print(f'{switches=}')
    referencesCount = []
    for j in range(len(switches[0])):
        referencesCount.append([0,j,[]])
    for i,switch in enumerate(switches):
        for j, value in enumerate(switch):
            referencesCount[j][0] += value
            if value == 1:
                referencesCount[j][2].append(i)
    referencesCount.sort()
    print(f'{referencesCount}')
    return referencesCount

assert [[1, 1, [2]], [1, 2, [0]], [3, 0, [0, 1, 2]]] == getStateIDsFromLeastReferenced(switches=[(1,0,1),(1,0,0), (1,1,0)])
assert [[2, 1, [0, 2]], [2, 2, [0, 3]], [4, 0, [0, 1, 2, 3]]] == getStateIDsFromLeastReferenced(switches=[(1,1,1),(1,0,0),(1,1,0),(1,0,1)]) 


def getListOfOptions(remainingCount, switchIDs):
    print(f'\ngetListOfOptions received {remainingCount} {switchIDs=}')
    switchID = switchIDs[0]
    remainingIDs = switchIDs[1:]
    if not remainingIDs:
        print(f'no remainingIDs found {switchIDs=}')
        return [{'switchID':switchID, 'count':remainingCount}]
    iterations = []
    for i in range(remainingCount):
        iterations.append( [{'switchID':switchID, 'count':i},getListOfOptions(remainingCount - i, remainingIDs)])
    return iterations


def getListOfValidSwitchConfigurations(endState, switches, leastReferencedDigit):
    """
    input:
        endState - example: (52,23,12)
        switches - example: [(1,1,1),(1,0,0),(1,1,0),(1,0,1)]
        leastReferencedDigitAndSwitches - example:
        - [switchesCount, endStateReferenceIndex, switches
            [2, 1, [0, 2]]

    returns: validStatesForIndex
    """
    print(f'Start get list {leastReferencedDigit=}')
    leastReferencedDigitId = leastReferencedDigit[1]
    leastReferencedSwitchesUsed = leastReferencedDigit[2]
    targetingCount = endState[leastReferencedDigitId]
    options = getListOfOptions(targetingCount, leastReferencedSwitchesUsed)
    print(f'{options=}')
    return options
        
    

assert [{'switchID': 0, 'count': 3}] == getListOfValidSwitchConfigurations((3,4,3,3), [(1,1,1,1), (0,1,0,0)], [1,0,[0]])
print('test passed')
getListOfValidSwitchConfigurations((3,4,5), [(1,0,1), (0,1,1), (1,1,0)], [3,0,[0,1,2]])



