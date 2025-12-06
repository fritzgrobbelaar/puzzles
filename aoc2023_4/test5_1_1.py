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
    print('row:',row)
    if row.endswith('map:\n'):
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

lowestLocation = 9999999999999
seedList = text[0][6:].split()

for seed in seeds:
    origin = int(seed)
    print('seed:', seed)
    totalLocation = 0
    for mapName in mapNameList:
        for i, sourceStart in enumerate(envMap[mapName]['sourceStart']):
            destinationStart = envMap[mapName]['destinationStart'][i]
            rangeEnv = envMap[mapName]['range'][i]
            if (origin >= sourceStart) and (origin < sourceStart + rangeEnv):
                
                print(f'adding destination found {mapName=} {origin=}, {sourceStart=} {rangeEnv=} ',mapName, origin)
                origin = destinationStart  - (sourceStart - origin)
                print('new origin:', origin)
                break

        else:
            print(f'not found - keeping {mapName=} {origin=}, {sourceStart=} {rangeEnv=}')
    if origin < lowestLocation:
        lowestLocation = origin
print(envMap)
print(mapNameList)
print('lowestLocation:',lowestLocation)
