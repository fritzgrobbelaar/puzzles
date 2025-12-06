import cleaninput

listOfText = cleaninput.getfileInputLinesAsList('input2_2024.txt')

sample = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 2 3 7 8
1 2 4 7 8 11 14 17
1 3 6 7 9'''.split('\n')

#listOfText = sample

total = 0
for i, row in enumerate(listOfText):
    #print(f'\n#### Processing {row=}')

    rowIn = row.split()
    row = []
    for value in rowIn:
        row.append(int(value))

    originalRow = row[:]
    addOne = False
    for removeOne in range(len(row)+1):
        row = originalRow[:]
        if removeOne != len(row):
            row.pop(removeOne)
        #print(f'{row=}')
        incr = True
        decr = True
        prevValue = row[0]
        #print(f'\n#### Processing {row=}')
        for value in row[1:]:
            if (abs(value-prevValue))==0:
                print('jump too small')
                incr=False
                decr=False
            if (abs(value-prevValue))>3:
                incr=False
                decr=False
            if value > prevValue:
                decr = False
            if value < prevValue:
                incr = False
            prevValue=value
        if incr or decr:
            addOne=True

    if addOne:
        print(f'Success {originalRow=}')
        total = total + 1
    else:
        print(f'Fail {originalRow=}')

print(f'{total=}')
