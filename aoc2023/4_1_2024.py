import cleaninput, re

listOfText = cleaninput.getfileInputLinesAsList('input4_2024.txt')

sample = '''..X...
.SAMX.
.A..A.
XMAS.S
.X....'''.split('\n')

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

listOfText = sample2

def getDiagonal(listOfText):
    listOfLists = []
    for row in listOfText:
        listOfLists.append(list(row))
    diagonal = []
    for i, row in enumerate(listOfLists):
        for j, value in enumerate(row):
            rowNum = i + j
            if len(diagonal) <= rowNum:
                diagonal.append([])
            diagonal[rowNum].append(value)
    diagStrings = []
    for row in diagonal:
        diagStrings.append(''.join(row))
    #print(f'{diagStrings=}')
    return diagStrings

assert getDiagonal(['123',
'234',
'345']) == ['1',
'22',
'333',
'44',
'5']

def printList(listOfText):
    print('-- ListOfText --')
    for row in listOfText:
        print(''.join(row))

def count(listOfText):

    total = 0
    for row in listOfText:
        total = total + len(re.findall('XMAS', row))
    return total

assert 2 == count('''MXMAS
MMMMXMAS'''.split('\n'))

def getReversed(listOfText):
    reversed = []
    for row in listOfText:
        rev = list(row)
        rev.reverse()
        reversed.append(''.join(rev))
    return reversed

def getTransposed(listOfText):
    listOfLists = []
    for row in listOfText:
        listOfLists.append(row)
    listOfLists =  list(map(list, zip(*listOfLists)))
    listOfText = []
    for row in listOfLists:
        listOfText.append(''.join(row))
    return listOfText

print('point 1')
printList(listOfText)
total = count(listOfText)
print(f'{total=}') # 3
diag = getDiagonal(listOfText)
printList(diag)
total += count(diag)
print(f'{total=}') #4

listOfText = getReversed(listOfText)
print('\n\n --- point 2') # 6
printList(listOfText)
total += count(listOfText)
print(f'{total=}')
diag = getDiagonal(listOfText)
printList(diag)
total += count(diag)
print(f'{total=}')

listOfText = getTransposed(listOfText)
print('\n\n --- point 3')
printList(listOfText)
total += count(listOfText)
print(f'{total=}') # should be 8 - is 8
diag = getDiagonal(listOfText)
printList(diag)
total += count(diag)
print(f'{total=}') # should be 12 - is 12

listOfText = getReversed(listOfText)
print('\n\n --- point 4')
printList(listOfText)
total += count(listOfText)
print(f'{total=}') # should be 14 - is 14
diag = getDiagonal(listOfText)
printList(diag)
total += count(diag)

print(f'{total=}')