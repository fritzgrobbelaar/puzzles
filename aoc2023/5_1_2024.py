import cleaninput, re

listOfText = cleaninput.getfileInputLinesAsList('input5_2024.txt')

sample = '''..X...
.SAMX.
.A..A.
XMAS.S
.X....'''.split('\n')

listOfText = sample

total = 0
for row in listOfText:
    print(''.join(row))

print(f'{total=}')
