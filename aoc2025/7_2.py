import cleaninput,copy
from datetime import datetime
from functools import cmp_to_key

listOfText = cleaninput.getfileInputLinesAsList('input_7.txt')

sample='''.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............'''.split('\n')

#listOfText = sample
global totalScenarios
totalScenarios = 1
def addRow(beams: set, row, multiplier):
    global totalScenarios
    #print(f'{beams=}')
    scenarios = [beams]
    for i, value in enumerate(row):
        if value == '^':
            newScenarios = []
            for beams in scenarios:
                if i in beams:
                        beams.remove(i)
                        beams1 = copy.deepcopy(beams)
                        beams2 = copy.deepcopy(beams)
                        beams1.add((i-1))
                        newScenarios.append(beams1)
                        beams2.add((i+1))

                        newScenarios.append(beams2)
                        #print(f'{scenarios=} just split {multiplier=}')
                        totalScenarios += multiplier
                else:
                    newScenarios.append(beams)
            scenarios = newScenarios
    #print(f'{scenarios=}')
    return scenarios
def combineScenarios(scenarios):
    distinctScenarios = []
    for i,scenario in enumerate(scenarios):
        for j,distinctScenario in enumerate(distinctScenarios):
            if scenario[0] == distinctScenario[0]:
                distinctScenarios[j][1] += scenario[1]
                break
        else:
            distinctScenarios.append(scenario)
    print(f'Returning {distinctScenarios=}')
    return distinctScenarios

def addMultipleScenarioRow(scenarios: list, row: str):
    newScenarios = []
    for beamSet, multiplier in scenarios:
        newRow = addRow(beamSet, row, multiplier)
        newRow = [[item, multiplier] for item in newRow]
        newScenarios.extend(newRow)
    newScenarios = combineScenarios(newScenarios)
    print(f'returning {newScenarios=} {totalScenarios=} \n')
    return newScenarios       


assert [{1}, {3}] == addRow(beams={2}, row='..^..',multiplier=1)
assert [{2}] == addRow(beams={2}, row='.......',multiplier=1)
assert [[{1},1], [{3},1]] == addMultipleScenarioRow([[{2},1]], row='..^..')
assert [[{1,4},1], [{3,4},1]] == addMultipleScenarioRow([[{2,4},1]], row='..^..')
totalScenarios = 1
assert [[{1,4},2], [{3,4},2]] == addMultipleScenarioRow([[{2,4},2]], row='..^..')
assert totalScenarios == 3
assert [[{1,4},1], [{3,4},1]] == addMultipleScenarioRow([[{1,4},1], [{3,4},1]], row='........^')
assert [[{1,3},1], [{1,5},1], [{3},1],[{3,5},1]] == addMultipleScenarioRow([[{2,4},1]], row='..^.^.')

assert [[{1,4},1], [{3,4},1]] == combineScenarios([[{1,4},1], [{3,4},1]])

assert [[{1,4},3], [{3,4},1]] == combineScenarios([[{1,4},1], [{3,4},1], [{1,4},1], [{1,4},1]])
assert [[{1,4},3], [{3,4},1]] == combineScenarios([[{1,4},1], [{3,4},1], [{1,4},2]])

print(f'{totalScenarios=}')
totalScenarios = 1
#raise Exception('end reached')
scenarios = []
for j,row in enumerate(listOfText):
    print(f'Processing {j=} of {len(listOfText)=}')
    for i,value in enumerate(row):
        
        if scenarios == [] and value == 'S':
            scenarios = [[{i},1]]
            continue
    scenarios = addMultipleScenarioRow(scenarios, row)


print(f'{totalScenarios=}')

