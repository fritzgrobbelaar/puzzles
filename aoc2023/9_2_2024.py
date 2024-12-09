import copy

import cleaninput
from datetime import datetime
from functools import cmp_to_key
listOfText = cleaninput.getfileInputLinesAsList('input9_2024.txt')

sample = '''2333133121414131402'''.split('\n')
#sample = '''12345'''.split('\n')
#sample = '''432111'''.split('\n')
#sample='''4321114116413220541570577'''.split('\n')

#listOfText = sample

line = listOfText[0]
lineList = list(line)

newLine = []
emptySizeIndex = []
unProcessedDiscUsageIndex = []
for i, value in enumerate(lineList):
    if i%2 == 0:
        unProcessedDiscUsageIndex.append({'index': len(newLine), 'size': int(value), 'name': int(i / 2)})
        newLine.extend([str(int(i/2))]*int(value))
    else:
        emptySizeIndex.append( {'index':len(newLine), 'size':int(value)})
        #emptySizeIndex.append((len(newLine), int(value)))
        newLine.extend(['.']*int(value))


lineList = newLine

print(f'{''.join(lineList)} {emptySizeIndex=} {unProcessedDiscUsageIndex=}')

print(f'{len(lineList)=}')
print(f'Fixed up {emptySizeIndex=}')
print(f'{unProcessedDiscUsageIndex=}')
print(f'{''.join(newLine)}')
upToDateDiscUsageIndex = copy.deepcopy(unProcessedDiscUsageIndex)
for valueListIndex in range(len(unProcessedDiscUsageIndex) - 1, 0, -1):
    value = unProcessedDiscUsageIndex[valueListIndex]

#   print(f'\nBefore iteration of {value=} {upToDateDiscUsageIndex=}')
#   print(f'Before iteration of {value=}  {emptySizeIndex=}')
#   print(f'Before iteration of {value=} {unProcessedDiscUsageIndex=}')

    valueLocationIndex = value['index']
    valueSize = value['size']
    valueFileIndex = value['name']


    emptySpaceListIndex = 0
    emptySpaceLocationIndex = emptySizeIndex[emptySpaceListIndex]['index']
    emptySpaceSize = emptySizeIndex[emptySpaceListIndex]['size']
    while (emptySpaceLocationIndex < valueLocationIndex) and (emptySpaceSize < valueSize):
         #print(f'{emptySpaceListIndex=} did not find space large enough {valueSize=} in small space available {emptySpaceSize=} at {emptySizeIndex[emptySpaceListIndex]['index']}')
         emptySpaceListIndex += 1
         emptySpaceSize = emptySizeIndex[emptySpaceListIndex]['size']
         emptySpaceLocationIndex = emptySizeIndex[emptySpaceListIndex]['index']

    if emptySpaceListIndex == len(emptySizeIndex)-1:
       # print('Ran out of empty space for indexed item', emptySpaceListIndex)
        continue

   # print(f'Found index of first empty space big enough index {emptySpaceLocationIndex=}, {emptySpaceSize=} {valueLocationIndex=}')
    if valueLocationIndex <= emptySpaceLocationIndex:
  #      print(f'Continue as we cannot move items at  {valueLocationIndex=} to empty space with larger index {emptySpaceListIndex=}')
        continue
    emptySpaceLocationIndex = emptySizeIndex[emptySpaceListIndex]['index']
    for i in range(valueSize):
        lineList[emptySpaceLocationIndex+i] = lineList[valueLocationIndex+i]
        lineList[valueLocationIndex+i] = '.'

    originalNewIndex = emptySizeIndex[emptySpaceListIndex]['index']
    emptySizeIndex[emptySpaceListIndex]['size'] = emptySizeIndex[emptySpaceListIndex]['size'] - valueSize
    emptySizeIndex[emptySpaceListIndex]['index'] = emptySizeIndex[emptySpaceListIndex]['index'] + valueSize


    movedItem = unProcessedDiscUsageIndex.pop(valueListIndex)

    upToDateDiscUsageIndex.remove(movedItem)

    for m, valueNewDisc in enumerate(upToDateDiscUsageIndex):

        if originalNewIndex < valueNewDisc['index']:
            movedItem = {'index':originalNewIndex, 'size':movedItem['size'], 'name':movedItem['name']}
            upToDateDiscUsageIndex = upToDateDiscUsageIndex[:m] + [movedItem] + upToDateDiscUsageIndex[m:]
            break
    else:
   #     print('item never moved - lets add it to the end')
        movedItem = {'index':originalNewIndex, 'size':movedItem['size'], 'name':movedItem['name']}
        upToDateDiscUsageIndex = upToDateDiscUsageIndex + [movedItem]

 #   print(f'After iteration of {value=} {upToDateDiscUsageIndex=}')
 #   print(f'After iteration of {value=}  {emptySizeIndex=}')
 #   print(f'After iteration of {value=} {unProcessedDiscUsageIndex=}')
#
 #   print(f'{''.join(newLine)}')


def getChecksum(lineList):
    total = 0
    for i, value in enumerate(lineList):
        if value != '.':
            total += i*int(value)
    return total

def getChecksum2(newDiscSizeIndex):
    total = 0
    for disc in newDiscSizeIndex:
        start = disc['index']
        size = disc['size']
        id = disc['name']
        for i in range(size):
            total += (start+i)*int(id)
    return total

print(f'checksum2 ', getChecksum2(upToDateDiscUsageIndex))
print(f'checksum ', getChecksum(lineList))

# too low 95479
#also too low 6333626232522
#also too low 6333644568623
#what about   8478907259440 # also bad - can retry at 07:24
# also bad 8531943982710 - can retry at 08:00