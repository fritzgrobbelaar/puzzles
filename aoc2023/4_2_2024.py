import cleaninput, re

listOfText = cleaninput.getfileInputLinesAsList('input4_2024.txt')

sample = '''M.S
.A.
M.S'''.split('\n')

sample2='''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''.split('\n')

#listOfText = sample2

searchBlock1 = sample = '''M.M
.A.
S.S'''.split('\n')

searchBlock2 = sample = '''S.M
.A.
S.M'''.split('\n')

searchBlock3 = sample = '''M.S
.A.
M.S'''.split('\n')

searchBlock4 = sample = '''S.S
.A.
M.M'''.split('\n')

def printBlock(block):
 for row in block:
     print(row)

total = 0
for i in range(len(listOfText)-2):
    print('\n\n ----- ### --- new row')
    for j in range(len(listOfText[0])-2):
        block = listOfText[i][j:j+3], listOfText[i+1][j:j+3], listOfText[i+2][j:j+3]
        print('printing block:')
        printBlock(block)
        for k,searchBlock in enumerate([searchBlock1, searchBlock2, searchBlock3, searchBlock4]):
            if searchBlock[0][0] == block[0][0] and \
                searchBlock[0][2] == block[0][2] and \
                searchBlock[1][1] == block[1][1] and \
                searchBlock[2][0] == block[2][0] and \
                searchBlock[2][2] == block[2][2]:
                print('matched', k)
                #printBlock(searchBlock)
                total += 1
                print(f'{total=}')
            else:
                print('unmatched', k)
                #printBlock(searchBlock)

print(f'{total=}')
#1784 is too low