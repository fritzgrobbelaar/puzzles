def getMapInfo(input):
    textRowNumber = {}
    mapInfo = input[2:]
    mapDict = {}

    for i, row in enumerate(mapInfo):

        row = row.replace(' ', '').replace('(', '').replace(')', '')
        key_values = row.split('=')
        key = key_values[0]
        values = key_values[1].split(',')
        mapDict[key] = {'L': values[0], 'R': values[1]}
    mapDict['entryPoint'] = 'AAA'
    mapDict['exitPoint'] = 'ZZZ'
    return mapDict

def navigateToZZZ(leftRight, mapDict):
    print('---- navigate to ZZZ ----', leftRight, mapDict, '\n')
    leftRight = list(leftRight*1000000)
    key = mapDict['entryPoint']
    for i, leftRight in enumerate(leftRight):
        if key == mapDict['exitPoint']:
            break
        keyOld = key[:]
        key = mapDict[key][leftRight]
        if i < 100:
            print(i, 'jump', leftRight, 'from ', keyOld, 'to', key)
    else:
        raise ValueError('value not found in iterations: ' + str(i))
    return i