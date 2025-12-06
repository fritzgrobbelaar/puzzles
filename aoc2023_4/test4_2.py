with open('input4.txt') as handle:
    text=handle.readlines()

text_='''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''.split('\n')

multipliersList = []

winningsList = []
total = 0
for row in text:
    print(row)
    info = row.split(':')[1]
    left, right = info.split('|')
    numbers1= set(left.split())
    addRowWinnings = 0
    for number in right.split():
        if number in numbers1:
            print('found', number)
            if not addRowWinnings:
                addRowWinnings = 1
            else:
                addRowWinnings = addRowWinnings+1
    winningsList.append(addRowWinnings)

#    1 TC 2
# 4 1+0+0+0+0  0   0  1
# 2 1+1+0+0+0  0   0  2
# 2 1+1+2+0+0  4   4 + 2*2 = 8
# 1 1+1+2+4+0      4 + 2*2 + 1*4= 
# 0 1+1+0+4+8
# 0 1+0+0+0+0
print(f'{winningsList=}')

total = 0
cardsCountList = [1]*len(winningsList)
for i, matchingCount in enumerate(winningsList):
    cardsCount = cardsCountList[i]
    for j in range(1, 1+ matchingCount):
        updateIndex = i + j
        cardsCountList[updateIndex] += cardsCount
        print(f'{i=} {updateIndex=}' ,cardsCountList)
    total = total + cardsCount
    
print('total:', total)
