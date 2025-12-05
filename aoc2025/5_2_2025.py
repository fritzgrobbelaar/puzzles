sampleText = '''
3-5
10-14
16-20
12-18

1
5
8
11
17
32'''

#response = requests.get('https://adventofcode.com/2025/day/1/input')
with open('input_5.txt', 'r') as handle:
 text = handle.read()

from functools import cache
#comment to run
#text = sampleText
rows = text.split('\n')


products = []
freshRanges = []
for row in rows:
    if '-' in row:
        row = row.split('-')
        freshRanges.append([int(row[0]), int(row[1])])

def SimplifyRanges(ranges):
    newRanges = []
    for i, oldRange in enumerate(ranges):
        for j, newRange in enumerate(newRanges):
            if (oldRange[0] >= newRange[0] and oldRange[0] <= newRange[1]) or (oldRange[1] >= newRange[0] and oldRange[1] <= newRange[1]):
                newRanges[j][0] = min(oldRange[0], newRange[0])
                newRanges[j][1] = max(oldRange[1], newRange[1])
                break
            elif (newRange[0] >= oldRange[0] and newRange[0] <= oldRange[1]) or (newRange[1] >= oldRange[0] and newRange[1] <= oldRange[1]):
                newRanges[j][0] = min(oldRange[0], newRange[0])
                newRanges[j][1] = max(oldRange[1], newRange[1])
                break
                
        else:
            #print('not found')
            newRanges.append(oldRange)
    #print(newRanges)
    return newRanges

assert [[10,14]] == SimplifyRanges([[10, 14]])
assert [[10,14]] == SimplifyRanges([[10, 14],[11,13]])
assert [[10,14]] == SimplifyRanges([[11,13],[10, 14]])

print(f'{freshRanges=}')
previousCountFreshRanges = None

while previousCountFreshRanges != len(freshRanges):
    previousCountFreshRanges = len(freshRanges)
    freshRanges = SimplifyRanges(freshRanges)
    #print(f'{freshRanges=}')

freshRanges = SimplifyRanges(freshRanges)


#print(f'{freshRanges=}')
counter = 0
for freshRange in freshRanges:
    counter = counter + freshRange[1] - freshRange[0] + 1
print(f'{counter=}')
#365011257653806 is too high
