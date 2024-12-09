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
for i, value in enumerate(lineList):
    if i%2 == 0:
        newLine.extend([str(int(i/2))]*int(value))
    else:
        newLine.extend(['.']*int(value))

lineList = newLine

emI = 0
print(f'{len(lineList)=}')
for valI in range(len(lineList)-1,0,-1):
 #   print(f'{valI=} {emI=}, {lineList=}')
    value = lineList[valI]
    if value == '.':
        continue

    while lineList[emI] != '.':
        print(f'{emI=} {lineList[emI]=}')
        emI += 1
    if valI < emI:
        print(f'Breaking {emI=} {valI=}')
        break
 #   print(f'Swopping {emI=} {valI=} {lineList[emI]=} {lineList[valI]=}')
    lineList[emI] = value
    lineList[valI] = '.'

print(f'{''.join(newLine)}')



def getChecksum(lineList):
    total = 0
    for i, value in enumerate(lineList):
        if value != '.':
            total += i*int(value)
    return total

print('checksum', getChecksum(lineList))

