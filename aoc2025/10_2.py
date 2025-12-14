import cleaninput
from datetime import datetime
from functools import cmp_to_key
import math
from datetime import datetime
import itertools
import pprint
global listOfText
global switches
import copy
listOfText = cleaninput.getfileInputLinesAsList('input_10.txt')

sample='''
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
[..####.] (0,2,4,6) (0,1,2,3,5) (0,1,2,3,6) (1,4) (0,5) (2,3,5) (3,6) (0,4) {40,25,40,35,11,33,20}
[#...#] (2,4) (2,3) (0,2) (0,1,2) (0,4) {196,6,193,3,14}
[###.] (1,2,3) (0,1,2) {189,191,191,2}
[.#..##.##] (0,1,2,6,8) (1,2,4,6,7) (2,5) (0,1,8) (0,1,2,6,7) (0,2,4,7) (0,1,3,4,5,6,8) {60,49,46,18,45,18,45,38,30}
[.###.##] (0,2,4) (0,1,3,4,5,6) (1,3,4,5,6) (1,4,5) (1,3,6) {177,195,15,190,195,180,190}
[#.##.] (1,2) (0,1,2,3) (1,3,4) (1,2,3,4) (0,1,4) (0,4) (2,3) {46,67,40,39,47}
[....#..] (0,3,5) (0,1,2,3) (0,6) (1,5) (0,1,2,4,6) (0,1,3,4) (2,5,6) {55,32,12,33,22,30,23}

'''.split('\n')

#6.3 seconds
sample_speedtest='''
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
[..####.] (0,2,4,6) (0,1,2,3,5) (0,1,2,3,6) (1,4) (0,5) (2,3,5) (3,6) (0,4) {40,25,40,35,11,33,20}
[#...#] (2,4) (2,3) (0,2) (0,1,2) (0,4) {196,6,193,3,14}
[###.] (1,2,3) (0,1,2) {189,191,191,2}
[.#..##.##] (0,1,2,6,8) (1,2,4,6,7) (2,5) (0,1,8) (0,1,2,6,7) (0,2,4,7) (0,1,3,4,5,6,8) {60,49,46,18,45,18,45,38,30}
[.###.##] (0,2,4) (0,1,3,4,5,6) (1,3,4,5,6) (1,4,5) (1,3,6) {177,195,15,190,195,180,190}
[#.##.] (1,2) (0,1,2,3) (1,3,4) (1,2,3,4) (0,1,4) (0,4) (2,3) {46,67,40,39,47}
[....#..] (0,3,5) (0,1,2,3) (0,6) (1,5) (0,1,2,4,6) (0,1,3,4) (2,5,6) {55,32,12,33,22,30,23}
'''


extracases = '''

[...#..#.#.] (0,3,8) (4,6,7,9) (1,2,4,5,6,7) (1,2,3,5,6) (7) (0,2,4,5,7) (1,2,5,6,9) (1,2,5,6,7,8,9) (6,9) (2,3,5,8,9) (0,1,2,5,8,9) (0,1,5) (4,9) {48,42,54,27,48,66,42,67,50,68}
[#.##] (3) (0,1) (1,2,3) (0,2,3) (0,2) {197,187,34,33}
'''

test=False
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
def calculateNewState(state, switchesCounters):
    global cache
    global swiches
    
    #print(f'Calculating new state from {state=} and {switches=} with {switchesCounters=}')
    for i, it in enumerate(switchesCounters):
        if it == 0:
            continue
        switch = switches[i]
        for j,value in enumerate(state):
            state[j] += it*switch[j]
    #print(f'Returning {state=}')
    return state
switches=[(1,0,0)]
assert [1,0,0] ==  calculateNewState([0,0,0], switchesCounters = [1])
switches=[(1,0,0)]
assert [3,0,0] ==  calculateNewState([0,0,0], switchesCounters = [3])
switches= [(1,0,0), (1,1,0)]
assert [10,0,0] ==  calculateNewState([0,0,0], switchesCounters = [10,0])
switches= [(1,0,1),(1,0,0), (1,1,0)]
assert [18, 7, 5] ==  (calculateNewState([0,0,0],switchesCounters = [5,6,7]))


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


def getFlatListOfOptionsNoEmpty(remainingCount, switchIDs):
    #print(f'\ngetListOfOptions received {remainingCount=} {switchIDs=}')
    switchID = switchIDs[0]
    remainingIDs = switchIDs[1:]
    if not remainingIDs:
#        print(f'no remainingIDs found {switchIDs=}')
        return [[remainingCount]]
    iterations = []
    for i in range(remainingCount+1):
        recurseAnswers = getFlatListOfOptionsNoEmpty(remainingCount - i, remainingIDs)
        #print(f'got recurseAnswer {recurseAnswers=}. Need to add switchID {switchID=} with count {i=}')
        localAnswer = [i]
       # print(f'local answer is {localAnswer=}')
        addedAnswers = []
        for recurseAnswer in recurseAnswers:
      #      print(f'processing {recurseAnswer=}')
     #       print(f'processing {recurseAnswer[0]=}')
            if type(recurseAnswer[0]) == int:
                addedAnswers.append(localAnswer+recurseAnswer)
            else:
                addedAnswers.append(localAnswer+recurseAnswer[0])
        
        #print(f'combined {addedAnswers=} after adding {localAnswer=} to {recurseAnswer=}')
        iterations.extend(addedAnswers)
        
    #print(f'returning iterations {iterations=}')
    return iterations

def getFlatListOfOptions(remainingCount, switchIDs):
    #print(f'\n\n\nStaring processing {remainingCount=} {switchIDs=}')
    flatListOfOptionsNoEmpty = getFlatListOfOptionsNoEmpty(remainingCount, switchIDs)
  #  print(f'\n\n -- ## -- Converting {flatListOfOptionsNoEmpty=} {switchIDs=} by ensuring the 0 values are added properly based on switches length')
    referencedSwitchIDs = switchIDs
    flatListOfOptions = []
    for row in flatListOfOptionsNoEmpty:
        newRow = []
        for i in range(len(switches)):
            if i not in referencedSwitchIDs:
                newRow.append(0)
            else:
                switchIndex = referencedSwitchIDs.index(i)
                newRow.append(row[switchIndex])
        flatListOfOptions.append(newRow)
  #  print(f' returning {flatListOfOptions=}')
    return flatListOfOptions
            

def getFlatListOfValidSwitchConfigurations(endState, leastReferencedDigit):
    """
    input:
        endState - example: (52,23,12)
        switches - example: [(1,1,1),(1,0,0),(1,1,0),(1,0,1)]
        leastReferencedDigitAndSwitches - example:
        - [switchesCount, endStateReferenceIndex, switches
            [2, 1, [0, 2]]
            returns [[3]]
        
        example2 input: (3,4,5), [(1,0,1), (0,1,1), (1,1,0)], [3,0,[0,1,2]]
        example2 explanation: - we're targetting the first endState digit of 0, value 3 using all combinations of switches listed [0,1,2]
        example2 output: [
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
    returns: validStatesForIndex
    """
    global switches
   # print(f'--\n\nStart get list {endState=} {leastReferencedDigit=}')
    leastReferencedDigitId = leastReferencedDigit[1]
    leastReferencedSwitchesUsed = leastReferencedDigit[2]
    targetingCount = endState[leastReferencedDigitId]
    options = getFlatListOfOptions(targetingCount, leastReferencedSwitchesUsed)
  #  print(f'\n Returning {options=}\n')
    #pprint.pprint(options)
    return options


expectedAnswer = [[0, 0, 2], [1, 0, 1], [2, 0, 0]]
switches=[(1, 0, 1), (0, 1, 1), (1,1,1)]
leastReferencedDigit=[2, 0, [0,2]]
endState = [2,10,3]
assert expectedAnswer == getFlatListOfValidSwitchConfigurations(endState=endState, leastReferencedDigit=leastReferencedDigit)


expectedAnswer = [[0, 0, 0, 0, 0, 29], [1, 0, 0, 0, 0, 28], [2, 0, 0, 0, 0, 27], [3, 0, 0, 0, 0, 26], [4, 0, 0, 0, 0, 25], [5, 0, 0, 0, 0, 24], [6, 0, 0, 0, 0, 23], [7, 0, 0, 0, 0, 22], [8, 0, 0, 0, 0, 21], [9, 0, 0, 0, 0, 20], [10, 0, 0, 0, 0, 19], [11, 0, 0, 0, 0, 18], [12, 0, 0, 0, 0, 17], [13, 0, 0, 0, 0, 16], [14, 0, 0, 0, 0, 15], [15, 0, 0, 0, 0, 14], [16, 0, 0, 0, 0, 13], [17, 0, 0, 0, 0, 12], [18, 0, 0, 0, 0, 11], [19, 0, 0, 0, 0, 10], [20, 0, 0, 0, 0, 9], [21, 0, 0, 0, 0, 8], [22, 0, 0, 0, 0, 7], [23, 0, 0, 0, 0, 6], [24, 0, 0, 0, 0, 5], [25, 0, 0, 0, 0, 4], [26, 0, 0, 0, 0, 3], [27, 0, 0, 0, 0, 2], [28, 0, 0, 0, 0, 1], [29, 0, 0, 0, 0, 0]]
switches=[(1, 0, 0, 0, 0, 1), (0, 1, 1, 1, 1, 1), (0, 1, 0, 1, 1, 1), (0, 0, 0, 1, 1, 0), (0, 0, 1, 1, 0, 1), (1, 1, 1, 0, 0, 1)]
leastReferencedDigit=[2, 0, [0, 5]]
endState = [29, 40, 23, 42, 39, 52]
assert expectedAnswer == getFlatListOfValidSwitchConfigurations(endState=endState, leastReferencedDigit=leastReferencedDigit)

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

switches = [(1,1,1,1), (0,1,0,0)]
assert [[3,0]] == getFlatListOfValidSwitchConfigurations((3,4,3,3), [1,0,[0]])


#print(f'\nflattened answer=\n {answer=}')
def flattenFurther(listOfDictionariesThatSetsAnEndStateToZero):
    #print(f'\nFurther flattening {switches=}, {listOfDictionariesThatSetsAnEndStateToZero=}')
    #pprint.pprint(listOfDictionariesThatSetsAnEndStateToZero)
    global switches
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
    #print('returning', newList)
    return newList  
switches = [(1,0,1), (0,1,1)]
assert [[0, 3], [1, 2], [2, 1], [3, 0]] == getFlatListOfValidSwitchConfigurations((3,4,3,3), [1,0,[0,1]])

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
switches = [(1,0,1), (0,1,1), (1,1,0)]
actual = getFlatListOfValidSwitchConfigurations((3,4,5), [3,0,[0,1,2]])
assert actual == expectedFlattenedFurtherResult

switches = [(1,0,1), (0,1,1), (1,1,0)]



def zeroEndStateDigitWithMultipleSwitchesLockedIn(endState, validSwitchConfigurations,leastReferencedSwitchesUsed):
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
    #print(f'\n\nStarting zeroEndStateDigitWithMultipleSwitchesLockedIn with \n{endState=} \n{switches=} \n{validSwitchConfigurations=} \n{leastReferencedSwitchesUsed=}')
    global switches 
    listOfValidStates = []
    for validSwitchConfiguration in validSwitchConfigurations:
        #print(f'Processing {endState=} {switches=} {leastReferencedSwitchesUsed=} {validSwitchConfiguration=}')
        allPositive=True
        switchConfig = tuple(validSwitchConfiguration)
        newEndState = list(endState)
        for switchID, switchCount in enumerate(switchConfig):
            switch = switches[switchID]
            for j, switchValue in enumerate(switch):
            
                newEndState[j] -= switchCount*switchValue
                if newEndState[j] < 0:
                    allPositive= False
                    break
        #print(f'Generated newEndState {newEndState=}')
        if allPositive:
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
switches = [(1,0,1), (0,1,1), (1,1,0)]
answer = zeroEndStateDigitWithMultipleSwitchesLockedIn(endState=(3,4,5), validSwitchConfigurations=testCaseValidSwitchConfigurations, leastReferencedSwitchesUsed=[2,0,[0,2]])
expectedAnswer = [
     [(0,2,2), [(0,1,1)], {(1,0,1): 0, (1,1,0): 3}],
     [(0,1,3), [(0,1,1)], {(1,0,1): 0, (1,1,0): 3}]
    ]

def removeDuplicateReferencedLockedInSwitchesFromSubsequentStateIDs(stateIDs):
    referencedSwitches = set()
    validStateIDs = []
    for stateID in stateIDs:
        switchIdList = stateID[2]
        allValid = True
        newSwitchIdList = []
        for switchId in switchIdList:
            
            if switchId not in referencedSwitches:
                newSwitchIdList.append(switchId)

        if newSwitchIdList:
            stateID[2] = newSwitchIdList
            validStateIDs.append(stateID)
            referencedSwitches = referencedSwitches.union(list(switchIdList))
    #print(f'Returning valid & distinct {validStateIDs=}')
    return validStateIDs

assert [[2,1,[5,4]]] == removeDuplicateReferencedLockedInSwitchesFromSubsequentStateIDs([[2,1,[5,4]]])
assert [[2,1,[5,4]]] == removeDuplicateReferencedLockedInSwitchesFromSubsequentStateIDs([[2,1,[5,4]], [3,4,[4]]])
assert [[2,1,[5,4]],[3,4,[2]]] == removeDuplicateReferencedLockedInSwitchesFromSubsequentStateIDs([[2,1,[5,4]],[3,4,[2,4]]])

def getValidSolutions(stateIDs, targetState):
    #print(f'\n\n -- getValidSolutions {stateIDs=}, {targetState=} {switches=}')
    global switches
    if stateIDs == []:
     #   print('Nothing found')
        return None
        #return [targetState, [0]*len(switches)]
    stateID = stateIDs[0]
    remainingStateIDs = stateIDs[1:]
        
    referencedSwitches = set(stateID[2])

    furtherFlattenedSwitchConfigs_Optimized = getFlatListOfValidSwitchConfigurations(targetState, stateID)

    validStatesWithEndStateDigitZeroed = zeroEndStateDigitWithMultipleSwitchesLockedIn(targetState, furtherFlattenedSwitchConfigs_Optimized,stateID)
    
    printString = ''
    for validState in validStatesWithEndStateDigitZeroed:
        #print(f'  targetState={targetState} {stateID=} {switches=} {validState=}')
        pass


    validStates = []
    for validState in validStatesWithEndStateDigitZeroed:
        if list(validState[0]) == [0]*len(targetState):
         #   print(f'*******hooray - we found one - no need to process further - whoop whoop {stateID=} {remainingStateIDs=} {targetState=} {switches=} answer={sum(validState[1])=}')
            validStates.append(validState)
        else:
            #print(f'before diving deeper, we have a {validState=}')
            recursiveValidSolutions = getValidSolutions(remainingStateIDs, validState[0])
            if recursiveValidSolutions == None:
                continue
          #  print(f'can I simply add or extend {validState=} and {recursiveValidSolutions=}')
            flatRecursiveValidSolutions = []
            for recursiveValidSolution in recursiveValidSolutions:
           #     print(f'{recursiveValidSolution=}')
                combinedValidState = []
                for i, value in enumerate(validState[1]):
                    combinedValidState.append(validState[1][i] + recursiveValidSolution[1][i])

      #          print(f'can I simply add or extend {validState=} and {recursiveValidSolution=}')
     #           print(f'planning to send back: {recursiveValidSolution[0]} {combinedValidState}')
                validStates.append([recursiveValidSolution[0],combinedValidState])

    #print(f'{stateIDs=}')
    #print(f'Returning {validStates=}')
    return validStates

#def processAndFlattenSolutions(validSolutions):

def estimateCalculationSize(row):
    endState = row[-1]
    endState = list(parseSwitches([endState])[0])
    #print(f'{endState=}')
    switches = row[1:-1]
    switches = parseSwitches(switches)
    switches = convertSwitches(switches, [0]*len(endState))
    originalSwitches = copy.deepcopy(switches)
    stateIDs = getStateIDsFromLeastReferenced(switches)
    stateIDs = removeDuplicateReferencedLockedInSwitchesFromSubsequentStateIDs(stateIDs)
    return endState[stateIDs[0][1]] ** len(stateIDs[0][2])
    

def getLowestIteration(row):
    endState = row[-1]
    global switches
    endState = list(parseSwitches([endState])[0])
    #print(f'{endState=}')
    switches = row[1:-1]
    switches = parseSwitches(switches)
    switches = convertSwitches(switches, [0]*len(endState))
    originalSwitches = copy.deepcopy(switches)
    print('switches parsed=',switches)
    stateIDs = getStateIDsFromLeastReferenced(switches)
    stateIDs = removeDuplicateReferencedLockedInSwitchesFromSubsequentStateIDs(stateIDs)
    validSolutions = getValidSolutions(stateIDs, targetState=endState)
    #def processAndFlattenSolutions(validSolutions)
    print(f'at the end of the row, we found {validSolutions=}')
    #pprint.pprint(validSolutions)
    minNumberUsed = 10000
    for validSolution in validSolutions:
        sumUsed = sum(validSolution[1])
        if minNumberUsed > sumUsed:
            minNumberUsed = sumUsed
    print(f'{minNumberUsed=} for {row=}')
    return minNumberUsed


#Test case from prod with unknown answer - but it failed, so need to fix logic
getLowestIteration(['[..##..]', '(0,5)', '(1,2,3,4,5)', '(1,3,4,5)', '(3,4)', '(2,3,5)', '(0,1,2,5)', '{29,40,23,42,39,52}'])

assert 17 == getLowestIteration( ['[###.]', '(1,3)', '(0,1,2)', '{0,17,0,17}'])
assert 20 == getLowestIteration(['[#.##]', '(1,2,3)', '(0,2,3)', '{12,8,20,20}'])
assert 10 == getLowestIteration(['[.##.]', '(3)', '(1,3)', '(2)', '(2,3)', '(0,2)', '(0,1)', '{3,5,4,7}'])

assert 12 == getLowestIteration(['[...#.]', '(0,2,3,4)', '(2,3)', '(0,4)', '(0,1,2)', '(1,2,3,4)', '{7,5,12,7,2}'])
assert 11 == getLowestIteration( ['[.###.#]', '(0,1,2,3,4)', '(0,3,4)', '(0,1,2,4,5)', '(1,2)', '{10,11,11,5,10,5}'])

total = 0
sizeEstimate = []
for i,row in enumerate(listOfText):
    now = datetime.now()
    nowString = datetime.strftime(datetime.now(),'%Y:%m:%d %H:%M:%S')    
    number = estimateCalculationSize(row)
    sizeEstimate.append([number, i])

print(f'\n\n\n\n\n ######### -------- Calculation size estimates ------- ######## {nowString=}\n')
sizeEstimate.sort()
for row in sizeEstimate:
    print(row)

import sys
try:
    startNumber = int(sys.argv[1])
except IndexError as e:
    print('no command line argument - starting at 0')
    startNumber = 0
listOfText = listOfText[startNumber:]
now = datetime.now()
startString = datetime.strftime(datetime.now(),'%Y%m%d %H%M%S')    

total = 0
for i,row in enumerate(listOfText):
    now = datetime.now()
    nowString = datetime.strftime(datetime.now(),'%Y:%m:%d %H:%M:%S')    
    with open(f'trackingfile_{startNumber}_{startString}.txt', 'a') as handle:
        handle.write(f'Starting {nowString} {i=} {row=}  \n ')
    print(f'\n\n\n\n\n ######### -------- Processing {i=} of {len(listOfText)=} ------- ######## {nowString=}\n',row)
    number = getLowestIteration(row)
    print(f'received {number=}')
    sizeEstimate.append([number, i])
    #total += number
    with open(f'trackingfile_{startNumber}_{startString}.txt', 'a') as handle:
        handle.write(f'{startNumber+i=} {number=}  {row=} {nowString} \n ')
    total += number

print(f'{total=}')
