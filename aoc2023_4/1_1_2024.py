import cleaninput

listOfText = cleaninput.getfileInputLinesAsList('input1_2024.txt')

sample = '''3   4
4   3
2   5
1   3
3   9
3   3'''.split('\n')

#listOfText=sample


print(f'listOfText')

total = 0
left = []
right = []

for i, row in enumerate(listOfText):
    print(f'{row=}')
    l,r = row.split()
    left.append(l)
    right.append(r)

left.sort()
right.sort()
total = 0
for i,l in enumerate(left):
    r=right[i]
    print(f'{l=} {r=}')
    total = total + abs(int(l)-int(r))

    # for character in row:
    #     if character.isdigit():
    #         first = character
    #         break
    #
    # reversed = list(row)
    # reversed.reverse()
    # for character in reversed:
    #     if character.isdigit():
    #         last = character
    #         break
    # total = total + int(first + last)
    # print('row:', i, first + last, 'total:', total)
print(f'{total=}')