from left_right_mapInfo import *
import cleaninput

input1 = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)'''.split('\n')

input2 = '''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)'''.split('\n')

listOfText = cleaninput.getfileInputLinesAsList('aoc2023\\input8_map_left_right.txt')
input = listOfText
leftRight = input[0]

actualMap1 = getMapInfo(input)
jumps = navigateToZZZ(input[0], actualMap1)
print('Result:', jumps)