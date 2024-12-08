import cleaninput
from datetime import datetime
listOfText = cleaninput.getfileInputLinesAsList('input8_2024.txt')

sample1 = '''............
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

sample = '''............
........0...
.....0......
............
............
............
............
............
............
............
............
............'''.split('\n')

#The plan:
# Create a dictionary of letters with indexes of their locations
# for each two of these (iterate over the list) - subtract to find the diff - subtract diff from first & add to second - check if on map
# the end
# work in listOfText

#listOfText = sample1

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
     #   print(f'onMap {res=}')
        return True
    #print(f'offMap {res=}')
    return False

def getHighResDiff(diff):
    for i in range(20,1,-1):
        if diff[0] % i == 0 and diff [1] % i == 0:
            diff = diff[0]/i, diff[1]/i
    return diff

assert (1,2) == getHighResDiff((1,2))
assert (1,2) == getHighResDiff((10,20))

resLocations = set()
total = 0
for key in indexes.keys():
    locations = indexes[key]
    for k,startValue in enumerate(locations):
         for l, nextValue in enumerate(locations[k+1:]):
            one = startValue
            two = nextValue
            resLocations.add(one)
            resLocations.add(two)

            diff = one[0] - two[0], one[1]-two[1]
            diff = getHighResDiff(diff)

            res1 = one[0] + diff[0], one[1] + diff[1]
            resLocations.add(res1)
            while onMap(res1):
                res1 = res1[0] + diff[0], res1[1] + diff[1]
                #print(f'checking loc 1 {res1=}')
                resLocations.add(res1)

            res1 = one[0] - diff[0], one[1] - diff[1]
            resLocations.add(res1)
            while onMap(res1):
                res1 = res1[0] - diff[0], res1[1] - diff[1]
                #print(f'checking loc 2 {res1=}')
                resLocations.add(res1)
            #print(f'Checking {key=} {one=} {two=} {diff=} {sorted(resLocations)=}')

def printMap(listOfText, resLocations):
    for j, row in enumerate(listOfText):
        printRow = []
        for i,value in enumerate(row):
            if (i,j) in resLocations:
                printRow.append('#')
            else:
                printRow.append('.')
        print(''.join(printRow))

for res in resLocations:
    if onMap(res):
        total += 1

#print(f'{resLocations=}')
printMap(listOfText, resLocations)


print('total', total)


