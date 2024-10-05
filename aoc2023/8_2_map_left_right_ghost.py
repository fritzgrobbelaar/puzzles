from left_right_mapInfo import *
import cleaninput
from datetime import datetime

input1 = '''LR

            11A = (11B, XXX)
            11B = (XXX, 11Z)
            11Z = (11B, XXX)
            22A = (22B, XXX)
            22B = (22C, 22C)
            22C = (22Z, 22Z)
            22Z = (22B, 22B)
            XXX = (XXX, XXX)'''.split('\n')

fileInput = cleaninput.getfileInputLinesAsList('aoc2023\\input8_map_left_right.txt')
print("Read file at", datetime.now())
listOfText = fileInput
actualMap = getMapInfo(listOfText)
print("Got actual Map at", datetime.now())
ghostMap = convertMapInfoToGhostEntriesAndExits(actualMap)
print("Converted Map at", datetime.now())
pathsCount = navigateToZ_Ghost(listOfText[0], ghostMap, checkUniqueNess=False)
#gave up on 42000000
#Tested 279 000 000 - 11% answer is 'too low'
#Tested 2709000000 - too low
# Busy  449860000
#       1132780000
# Giving up on:

#Dumping info: i=0, j=17850000, keys=['PKB', 'MTG', 'JVT', 'XPS', 'SFD', 'DQR'], j*leftRightLen+i=4837350000 Jump count:  17850000 0.02 % at 2024-10-05 16:06:07.274159 0:00:01.243992
#Dumping info: i=0, j=17860000, keys=['TJP', 'QFR', 'DJG', 'VMD', 'SDS', 'SGJ'], j*leftRightLen+i=4840060000 Jump count:  17860000 0.02 % at 2024-10-05 16:06:08.488163 0:00:01.213002
#Dumping info: i=0, j=17870000, keys=['NQH', 'CBH', 'QNP', 'LKG', 'BXR', 'GJQ'], j*leftRightLen+i=4842770000 Jump count:  17870000 0.02 % at 2024-10-05 16:06:09.784161 0:00:01.293999
#Dumping info: i=0, j=17880000, keys=['RXF', 'LBT', 'NSR', 'DHK', 'BGT', 'TCH'], j*leftRightLen+i=4845480000 Jump count:  17880000 0.02 % at 2024-10-05 16:06:11.021158 0:00:01.235995
#Dumping info: i=0, j=17890000, keys=['DND', 'JVH', 'HHJ', 'JLS', 'VBJ', 'PDC'], j*leftRightLen+i=4848190000 Jump count:  17890000 0.02 % at 2024-10-05 16:06:12.265158 0:00:01.242997
#Dumping info: i=0, j=17900000, keys=['DBD', 'VDN', 'KBC', 'LQP', 'FXS', 'SNQ'], j*leftRightLen+i=4850900000 Jump count:  17900000 0.02 % at 2024-10-05 16:06:13.568160 0:00:01.302001

print('Result:', pathsCount)