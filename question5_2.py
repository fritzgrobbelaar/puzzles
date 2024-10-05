with open('input5.txt') as handle:
    text=handle.readlines()

text_='''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''.split('\n')

mapNameList = []
envMap = {}
for row in text[2:]:
    row = row.replace('\n','')
    print('row:',row)
    if row.endswith('map:'):
        currentMapName = row.replace(' map:','')
        mapNameList.append(currentMapName)
        envMap[currentMapName] = {}
        envMap[currentMapName]['destinationStart'] = []
        envMap[currentMapName]['sourceStart'] = []
        envMap[currentMapName]['range'] = []

    else:
        values = row.split()
        if len(values) == 0:
            print('row:',row)
            continue
        envMap[currentMapName]['destinationStart'].append(int(values[0]))
        envMap[currentMapName]['sourceStart'].append(int(values[1]))
        envMap[currentMapName]['range'].append(int(values[2]))



def getNewMapRange(origin, originEnd, sourceStart, destinationStart, rangeEnv):
    found=False
    sourceStart = int(sourceStart)
    destinationStart = int(destinationStart)
    rangeEnv = int(rangeEnv)
    newOrigin = origin
    newOriginEnd = originEnd
    offset = destinationStart-sourceStart
    sourceEnd = sourceStart + rangeEnv
    print(f'Searching 1: {origin=} {originEnd=} {sourceStart=} {sourceEnd=} {destinationStart=} {offset=} {rangeEnv=}')
    if originEnd < sourceStart:   # no hope for match
        print(f'not found 1')
        return origin, originEnd, False
    elif origin > sourceEnd: # no hope for a match
        print(f'not found 2')
        return origin, originEnd, False


    if origin < sourceStart:
        origin = sourceStart + offset
    else:
        origin = origin + offset

    if originEnd < sourceEnd:
        originEnd = originEnd + offset
    else:
        originEnd = sourceEnd + offset

    print(f'Returning found: {origin=} {originEnd=}')
    return origin, originEnd, True

print('\n--------- starting unit test ------')
#   origin, originEnd, sourceStart, destinationStart, rangeEnv, expectedOrigin, expectedOriginEnd, expectedFound
unitTests = [
    [0,     0,         1,           1,                0,         0,              0,                False],  # below
    [2,     3,         4,           1,                10,        2,              3,                False],  # above
    [22,    33,        4,           1,                10,        22,             33,               False],  # above
    [10,    50,        21,          31,               11,        31,             42,                True],  # origin consumes source completely
    [30,    40,        21,          31,               100,       40,             50,                True]   # source consumes origin completely
]

for i, unitTest in enumerate(unitTests):
    origin, originEnd, found = getNewMapRange(*tuple(unitTest[0:5]))
    assert unitTest[-3] == origin
    assert unitTest[-2] == originEnd
    assert unitTest[-1] == found
    print(f'Test {i} passed')
print('------------------completed unit tests')

lowestLocation = 9999999999999
seedList = text[0][6:].split()
print('seedList',seedList)
seeds = []
for i in range(0,len(seedList),2):
    print('entered for loop')
    seeds.append((seedList[i],seedList[i+1]))
print('seeds',seeds)

for seed in seeds:
    origin = int(seed[0])
    originEnd = origin + int(seed[1])
    print('\n ######## seed in for-loop:', seed)
    totalLocation = 0
    originOptionsList = [origin]
    originEndOptionsList = [originEnd]
    for mapName in mapNameList:
        resultOptionsList = []
        resultEndOptionsList = []
        print("\n starting with map", mapName)
        for j, origin in enumerate(originOptionsList):
            originEnd = originEndOptionsList[j]
            for i, sourceStart in enumerate(envMap[mapName]['sourceStart']):
                print('map count ', i)
                destinationStart = envMap[mapName]['destinationStart'][i]
                rangeEnv = envMap[mapName]['range'][i]
                originReturned, originEndReturned, found = getNewMapRange(origin, originEnd, sourceStart, destinationStart, rangeEnv)
                if found:
                    resultOptionsList.append(originReturned)
                    resultEndOptionsList.append(originEndReturned)
            else:
                print(f'not found - keeping {mapName=} {origin=}, {originEnd=}')
        if resultOptionsList:
            originOptionsList = resultOptionsList
            originEndOptionsList = resultEndOptionsList
    for origin in originOptionsList:
        if origin < lowestLocation:
            lowestLocation = origin
print('lowestLocation:', lowestLocation)

