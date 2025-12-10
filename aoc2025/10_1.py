import cleaninput
from datetime import datetime
from functools import cmp_to_key
import math
import itertools
global listOfText
listOfText = cleaninput.getfileInputLinesAsList('input_10.txt')

sample='''[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
'''.split('\n')

test=True
if test:
    listOfText = sample
print(f'{listOfText=}\n')

listOfText = [row.split(' ') for row in listOfText]

def convertValueToBinary(value, length):
    print(f'converting to binary {value=} {length=}')
    value = value[1:-1]
    value= value.split(',')
    longestString = ['.']*length
    for digit in value:
        longestString[int(digit)] = '#'
    string = ''.join(longestString)

    return string

assert  '...#' == convertValueToBinary('(3)',4)
assert  '0b10' == convertValueToBinary('(3)',5)
assert  '0b101' == convertValueToBinary('(2,0)',3)
assert  '0b101' == convertValueToBinary('(3,1)',4)

def convertEndState(endState):
    print(f'{endState=}')
    endState = endState[1:-1]
    endState = endState.replace('.','0').replace('#','1')
    endState = '0b' + endState\

    endState = bin(int(endState, 2))
    print(f'Returning {endState=}')
    return endState

assert '0b100' == convertEndState('[.#..]')

for row in listOfText:
    endState = row[0]
    switches = row[1:-1]

    combs = [list(x) for x in itertools.permutations(switches, len(switches))]
    combs = [com for com in combs if len(com) == len(switches)]
    print(f'{len(combs)=}')
    for comb in combs:
        for value in comb:
            convertValueToBinary(value,len(switches)-2)
        break
    break

exit()
from itertools import permutations

my_list = ['A', 'B', 'C']
all_perms = []
for r in range(1, len(my_list) + 1):
    for perm in permutations(my_list, r):
        all_perms.append(perm)

print(all_perms)

a="0011101"
b="1011100"

#print('{y=int(a,2) ^ int(b,2)}'.format(a))
print('a {}'.format(a))
print('b {}'.format(b))
y=int(a,2) ^ int(b,2)
print('y {0:b}'.format(y))
#drawScaledArea(listOfText, scale)
print('- the end')
