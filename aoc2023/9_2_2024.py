import copy

import cleaninput
from datetime import datetime
from functools import cmp_to_key
listOfText = cleaninput.getfileInputLinesAsList('input9_2024.txt')

sample = '''2333133121414131402'''.split('\n')
#sample = '''12345'''.split('\n')

#listOfText = sample

line = listOfText[0]
lineList = list(line)

newLine = []
emptySizeIndex = []
discSizeIndex = []
for i, value in enumerate(lineList):
    if i%2 == 0:
        discSizeIndex.append((len(newLine), int(value),int(i/2)))
        newLine.extend([str(int(i/2))]*int(value))
    else:
        emptySizeIndex.append([len(newLine), int(value)])
        #emptySizeIndex.append((len(newLine), int(value)))
        newLine.extend(['.']*int(value))


lineList = newLine

print(f'{''.join(lineList)} {emptySizeIndex=} {discSizeIndex=}')

emI = 0
print(f'{len(lineList)=}')
print(f'Fixed up {emptySizeIndex=}')
print(f'{discSizeIndex=}')
print(f'{''.join(newLine)}')
newDiscSizeIndex = copy.deepcopy(discSizeIndex)
for valI in range(len(discSizeIndex)-1,0,-1):
    #print(f'{valI=} {emI=}, {''.join(lineList)=}')
    value = discSizeIndex[valI]
    emI = 0
    while (emI < len(emptySizeIndex)-1) and (emptySizeIndex[emI][1] < value[1]):
     #   print(f'{emI=} did not find space large enough {emptySizeIndex[emI][1]=} in small space available {value[1]=}')
        emI += 1

    if emI == len(emptySizeIndex)-1:
        #print('Ran out of empty space for indexed item', emI)
        continue

    #print(f'Found index of first empty space big enough index {emptySizeIndex[emI][0]=}, space size {emptySizeIndex[emI][1]=}')
    if valI < emI:
        #print(f'Continue {emI=} {valI=}')
        continue
 #   print(f'Swopping {emI=} {valI=} {lineList[emI]=} {lineList[valI]=}')
    for i in range(value[1]):
        lineList[emptySizeIndex[emI][0]+i] = lineList[discSizeIndex[valI][0]+i]
        lineList[discSizeIndex[valI][0]+i] = '.'
    originalNewIndex = emptySizeIndex[emI][0]
    emptySizeIndex[emI][1] = emptySizeIndex[emI][1] - value[1]
    emptySizeIndex[emI][0] = emptySizeIndex[emI][1] + value[1]+1

    movedItem = discSizeIndex.pop(valI)

    newDiscSizeIndex.remove(movedItem)

    #print(f'Before the move {newDiscSizeIndex=}')
    for m, valueNewDisc in enumerate(newDiscSizeIndex):

        #print(f'Comparing {originalNewIndex=} with {valueNewDisc[0]=}')
        if originalNewIndex < valueNewDisc[0]:
            #print(f'Moving to index {originalNewIndex=} {m=} {movedItem=}', (originalNewIndex), movedItem[1], movedItem[2])
            movedItem = (originalNewIndex), movedItem[1], movedItem[2]
            newDiscSizeIndex = newDiscSizeIndex[:m] + [movedItem] + newDiscSizeIndex[m:]
            break
    # print(f'After the move {newDiscSizeIndex=}')
    # print(f'Fixed up {emptySizeIndex=}')
    # print(f'Fixed up {discSizeIndex=}')
    #
    # print(f'{''.join(newLine)}')


def getChecksum(lineList):
    total = 0
    for i, value in enumerate(lineList):
        if value != '.':
            total += i*int(value)
    return total

def getChecksum2(newDiscSizeIndex):
    total = 0
    for disc in newDiscSizeIndex:
        start = disc[0]
        size = disc[1]
        id = disc[2]

        for i in range(size):
            total += (start+i)*int(id)
    return total

print('checksum2', getChecksum2(newDiscSizeIndex))
print('checksum', getChecksum(lineList))

# too low 95479
#also too low 6333626232522