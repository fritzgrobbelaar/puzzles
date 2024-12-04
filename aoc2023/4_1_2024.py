import cleaninput, re

listOfText = cleaninput.getfileInputLinesAsList('input4_2024.txt')

sample = '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'''.split('\n')

listOfText = sample




total = 0
for i, row in enumerate(listOfText):
    print(f'\n#### Processing {row=}')

        print(f'{match=}')
        match = match.replace('mul(', '')
        match = match.replace(')', '')
        matches = match.split(',')
        print(f'{matches=}')
        total += int(matches[0])*int(matches[1])

print(f'{total=}')
