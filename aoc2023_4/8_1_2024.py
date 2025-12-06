import cleaninput
from datetime import datetime
listOfText = cleaninput.getfileInputLinesAsList('input8_2024.txt')

sample = '''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............'''.split('\n')

#The plan:
# Create a dictionary of letters with indexes of their locations
# for each two of these (iterate over the list) - subtract to find the diff - subtract diff from first & add to second - check if on map
# the end
# work in listOfText

#listOfText = sample

indexes = {}
total = 0
for j,row in enumerate(listOfText):
    for i,value in enumerate(row):
        if value not in indexes.keys():
            indexes[value] = []
        if value != '.':
            indexes[value].append((i,j))

print(f'{indexes=}')

def onMap(res):
    if res[0] >= 0 and res[0] < len(row) and  res[1] >= 0 and res[1] < len(listOfText):
    #    print(f'onMap {res=}')
        return True
   # print(f'offMap {res=}')
    return False

resLocations = set()
total = 0
for key in indexes.keys():
    locations = indexes[key]
    for k,startValue in enumerate(locations):
         for l, nextValue in enumerate(locations[k+1:]):

            one = startValue
            two = nextValue

            diff = one[0] - two[0], one[1]-two[1]


            res1 = one[0] + diff[0], one[1] + diff[1]
            res2 = two[0] - diff[0], two[1] - diff[1]
            resLocations.add(res1)
            resLocations.add(res2)
            #print(f'Checking {key=} {one=} {two=} {res1=} {res2=}')
for res in resLocations:

    if onMap(res):
        total += 1



    #     combinedValuesNew = []
    #     for combinedValue in combinedValues[-1]:
    #         combinedValuesNew.append(combinedValue*value)
    #         combinedValuesNew.append(combinedValue+value)
    #         combinedValuesNew.append(int(str(combinedValue)+str(value)))
    #     combinedValues.append(combinedValuesNew)
    # if expectedValue in combinedValues[-1]:
    #     #print(f'{expectedValue=} found in {combinedValues[-1]=}')
    #     total += expectedValue

print('total', total)


