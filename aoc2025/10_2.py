import cleaninput
from datetime import datetime
from functools import cmp_to_key
import math
from datetime import datetime
import itertools
import pprint
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
    #print(f'{switches=}')
    referencesCount = []
    for j in range(len(switches[0])):
        referencesCount.append([0,j,[]])
    for i,switch in enumerate(switches):
        for j, value in enumerate(switch):
            referencesCount[j][0] += value
            if value == 1:
                referencesCount[j][2].append(i)
    referencesCount.sort()
    #print(f'{referencesCount}')
    return referencesCount

assert [[1, 1, [2]], [1, 2, [0]], [3, 0, [0, 1, 2]]] == getStateIDsFromLeastReferenced(switches=[(1,0,1),(1,0,0), (1,1,0)])
assert [[2, 1, [0, 2]], [2, 2, [0, 3]], [4, 0, [0, 1, 2, 3]]] == getStateIDsFromLeastReferenced(switches=[(1,1,1),(1,0,0),(1,1,0),(1,0,1)]) 


def getListOfOptions(remainingCount, switchIDs):
   # print(f'\ngetListOfOptions received {remainingCount} {switchIDs=}')
    switchID = switchIDs[0]
    remainingIDs = switchIDs[1:]
    if not remainingIDs:
     #   print(f'no remainingIDs found {switchIDs=}')
        return [{switchID:remainingCount}]
    iterations = []
    for i in range(remainingCount+1):
        recurseAnswer = getListOfOptions(remainingCount - i, remainingIDs)
        #print(f'got recurseAnswer {recurseAnswer=}. Need to add switchID {switchID=} with count {i=}')
        localAnswer = {switchID: i}
       # print(f'local answer is {localAnswer=}')
        addedAnswer = {**localAnswer,**{'more': recurseAnswer}}
        #print(f'combined {addedAnswer=} after adding {localAnswer=} to {recurseAnswer=}')
        iterations.append(addedAnswer)
        
    #print(f'returning iterations {iterations=}')
    return iterations


def getListOfValidSwitchConfigurations(endState, switches, leastReferencedDigit):
    """
    input:
        endState - example: (52,23,12)
        switches - example: [(1,1,1),(1,0,0),(1,1,0),(1,0,1)]
        leastReferencedDigitAndSwitches - example:
        - [switchesCount, endStateReferenceIndex, switches
            [2, 1, [0, 2]]
            returns [{0: 3}]
        
        example2 input: (3,4,5), [(1,0,1), (0,1,1), (1,1,0)], [3,0,[0,1,2]]
        example2 explanation: - we're targetting the first endState digit of 0, value 3 using all combinations of switches listed [0,1,2]
        example2 output: [{0: 0,
  'more': [{1: 0, 'more': [{2: 3}]},
           {1: 1, 'more': [{2: 2}]},
           {1: 2, 'more': [{2: 1}]},
           {1: 3, 'more': [{2: 0}]}]},
 {0: 1,
  'more': [{1: 0, 'more': [{2: 2}]},
           {1: 1, 'more': [{2: 1}]},
           {1: 2, 'more': [{2: 0}]}]},
 {0: 2, 'more': [{1: 0, 'more': [{2: 1}]}, {1: 1, 'more': [{2: 0}]}]},
 {0: 3, 'more': [{1: 0, 'more': [{2: 0}]}]}]
            
    returns: validStatesForIndex
    """
   #print(f'--\n\nStart get list {leastReferencedDigit=}')
    leastReferencedDigitId = leastReferencedDigit[1]
    leastReferencedSwitchesUsed = leastReferencedDigit[2]
    targetingCount = endState[leastReferencedDigitId]
    options = getListOfOptions(targetingCount, leastReferencedSwitchesUsed)
    #print(f'\n options=\n')
    #pprint.pprint(options)
    return options
        

def flattenListOfValidSwitchConfigurations(listOfValidSwitchConfigurations):
    """
    input:
        listOfValidSwitchConfigurations - example:
        - [{0: 0,
            'more': [{1: 0, 'more': [{2: 3}]},
                     {1: 1, 'more': [{2: 2}]},
                     {1: 2, 'more': [{2: 1}]},
                     {1: 3, 'more': [{2: 0}]}]},
           {0: 1,
            'more': [{1: 0, 'more': [{2: 2}]},
                     {1: 1, 'more': [{2: 1}]},
                     {1: 2, 'more': [{2: 0}]}]},
           {0: 2, 'more': [{1: 0, 'more': [{2: 1}]}, {1: 1, 'more': [{2: 0}]}]},
           {0: 3, 'more': [{1: 0, 'more': [{2: 0}]}]}]

    output:
        flattenedListOfValidSwitchConfigurations - example:
        - [{0: 0,1:0,2:3},
           {0: 0,1:1,2:2},
           {0: 0,1:2,2:1},
           {0: 0,1:3,2:0},
           {0: 1,1:0,2:2},
           {0: 1,1:1,2:1},
           {0: 1,1:2,2:0},
           {0: 2,1:0,2:1},
           {0: 2,1:1,2:0},
           {0: 3,1:0,2:0}]
        """
    flattenedListOfValidSwitchConfigurations = []
    def recurse(currentDict, accumulatedDict):
        for key in currentDict:
            if key == 'more':
                for moreDict in currentDict['more']:
                    recurse(moreDict, accumulatedDict)
            else:
                accumulatedDict[key] = currentDict[key]
        if 'more' not in currentDict:
            flattenedListOfValidSwitchConfigurations.append(accumulatedDict.copy())
    
    for validSwitchConfiguration in listOfValidSwitchConfigurations:
        recurse(validSwitchConfiguration, {})

    return flattenedListOfValidSwitchConfigurations

assert [{0: 3}] == getListOfValidSwitchConfigurations((3,4,3,3), [(1,1,1,1), (0,1,0,0)], [1,0,[0]])
expectedResult = [{0: 0,
  'more': [{1: 0, 'more': [{2: 3}]},
           {1: 1, 'more': [{2: 2}]},
           {1: 2, 'more': [{2: 1}]},
           {1: 3, 'more': [{2: 0}]}]},
 {0: 1,
  'more': [{1: 0, 'more': [{2: 2}]},
           {1: 1, 'more': [{2: 1}]},
           {1: 2, 'more': [{2: 0}]}]},
 {0: 2, 'more': [{1: 0, 'more': [{2: 1}]}, {1: 1, 'more': [{2: 0}]}]},
 {0: 3, 'more': [{1: 0, 'more': [{2: 0}]}]}]

actualResult = getListOfValidSwitchConfigurations((3,4,5), [(1,0,1), (0,1,1), (1,1,0)], [3,0,[0,1,2]]) #can't be a valid test case as switch 1 never references endState[0]
assert expectedResult == actualResult
answer = flattenListOfValidSwitchConfigurations(expectedResult)
expectedFlattendResult = [
    {0: 0, 1: 0, 2: 3},
    {0: 0, 1: 1, 2: 2},
    {0: 0, 1: 2, 2: 1},
    {0: 0, 1: 3, 2: 0},
    {0: 1, 1: 0, 2: 2},
    {0: 1, 1: 1, 2: 1}, 
    {0: 1, 1: 2, 2: 0},
    {0: 2, 1: 0, 2: 1}, 
    {0: 2, 1: 1, 2: 0}, 
    {0: 3, 1: 0, 2: 0}
]
assert expectedFlattendResult == answer
#print(f'\nflattened answer=\n {answer=}')
def flattenFurther(switches, listOfDictionariesThatSetsAnEndStateToZero):
    print(f'\nFurther flattening {switches=}, {listOfDictionariesThatSetsAnEndStateToZero=}')
    newList = []
    for dictItem in listOfDictionariesThatSetsAnEndStateToZero:
        newEntry = [0]*len(switches)
        #print(f'flattening {dictItem=}')
        for key in dictItem:
            newEntry[key] = dictItem[key]
        newList.append(newEntry)
    for entry in newList:
        if len(entry) != len(switches):
            raise Exception(f'flattenFurther generated entry of incorrect length {entry=} {switches=}') 
    print('returning', newList)
    return newList  

expectedFlattenedFurtherResult = [
    [0,0,3],
    [0,1,2],
    [0,2,1],
    [0,3,0],
    [1,0,2],
    [1,1,1],
    [1,2,0],
    [2,0,1],
    [2,1,0],
    [3,0,0]
]
listOfDictionariesThatSetsOneEndStateToZero = expectedFlattendResult
assert expectedFlattenedFurtherResult == flattenFurther( [(0,0,1), (1,1,0)], expectedFlattendResult)

expectedResult = [{0: 0, 'more': [{2: 3}]},
 {0: 1, 'more': [{2: 2}]},
 {0: 2, 'more': [{2: 1}]},
 {0: 3, 'more': [{2: 0}]}]
actualResult = getListOfValidSwitchConfigurations((3,4,5), [(1,0,1), (0,1,1), (1,1,0)], [3,0,[0,2]])
assert expectedResult == actualResult

answer = flattenListOfValidSwitchConfigurations(expectedResult)
#print(f'\nflattened answer=\n {answer=}')

def zeroEndStateDigitWithMultipleSwitchesLockedIn(endState, switches, validSwitchConfigurations,leastReferencedSwitchesUsed):
    """
    input:
        endState - example: (3,4,5)
        switches - example: [(1,1,1),(1,0,0),(1,1,0),(1,0,1)]
        validSwitchConfigurations - example:
        - [
            [0,0,3],
            [0,1,2],
            [0,2,1],
            [0,3,0],
            [1,0,2],
            [1,1,1],
            [1,2,0],
            [2,0,1],
            [2,1,0],
            [3,0,0]
        ]
    output:
        [(0,2,2), (0,0,3)], [(0,1,3), 1,0,2]]
        """
    print(f'\n\nStarting zeroEndStateDigitWithMultipleSwitchesLockedIn with \n{endState=} \n{switches=} \n{validSwitchConfigurations=} \n{leastReferencedSwitchesUsed=}')

    listOfValidStates = []
    for validSwitchConfiguration in validSwitchConfigurations:
        print(f'\nProcessing validSwitchConfiguration {validSwitchConfiguration=}')
        switchConfig = tuple(validSwitchConfiguration)
        newEndState = list(endState)
        for switchID, switchCount in enumerate(switchConfig):
            switch = switches[switchID]
            for j, switchValue in enumerate(switch):
                newEndState[j] -= switchCount*switchValue
        #print(f'Generated newEndState {newEndState=}')
        listOfValidStates.append([tuple(newEndState), switchConfig])
    #print('Returning listOfValidStates')
    #pprint.pprint(listOfValidStates)
    return listOfValidStates
    

testCaseValidSwitchConfigurations = [
            [0,0,3],
            [1,0,2],
            [2,0,1],
            [3,0,0]
        ]

answer = zeroEndStateDigitWithMultipleSwitchesLockedIn(endState=(3,4,5), switches=[(1,0,1), (0,1,1), (1,1,0)], validSwitchConfigurations=testCaseValidSwitchConfigurations, leastReferencedSwitchesUsed=[2,0,[0,2]])
expectedAnswer = [
     [(0,2,2), [(0,1,1)], {(1,0,1): 0, (1,1,0): 3}],
     [(0,1,3), [(0,1,1)], {(1,0,1): 0, (1,1,0): 3}]
    ]

def getLowestIteration(row):
    now = datetime.now()
    nowString = datetime.strftime(datetime.now(),'%Y:%m:%d %H:%M:%S')
    print(f'\n\n ---- New row -- {nowString=}\n',row)
    endState = row[-1]
    endState = list(parseSwitches([endState])[0])
    print(f'{endState=}')
    switches = row[1:-1]
    switches = parseSwitches(switches)
    switches = convertSwitches(switches, [0]*len(endState))
    print('switches parsed=',switches)
    stateIDs = getStateIDsFromLeastReferenced(switches)

    for stateID in stateIDs:
        switchConfigs = getListOfValidSwitchConfigurations(endState, switches, stateID)
        print(f'{switchConfigs=}')
        flatten1edSwitchConfigs = flattenListOfValidSwitchConfigurations(switchConfigs)
        print(f'{flatten1edSwitchConfigs=}')
        furtherFlattenedSwitchConfigs = flattenFurther(endState, flatten1edSwitchConfigs)
        print(f'{furtherFlattenedSwitchConfigs=}')
        raise ValueError(' this does not look right')
        zeroEndStateDigitWithMultipleSwitchesLockedIn(endState, switches, furtherFlattenedSwitchConfigs,stateID)
        print(f'{zeroEndStateDigitWithMultipleSwitchesLockedIn}')

        exit()

    print(f'{stateIDs=}')
    

answer = getLowestIteration(listOfText[0])
print(f'Final answer: {answer}')