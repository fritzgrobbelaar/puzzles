sampleText = '''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''

with open('input_4.txt', 'r') as handle:
 text = handle.read()

#Comment to test
#text = sampleText

rows = text.split('\n')
rows = [list(row) for row in rows]
print(f'{rows=}')
i_limit = len(rows[0])-1
j_limit = len(rows)-1

bigTotal = 0
total = None
while True:
    if total == None:
        total = 0
    elif total == 0:
        break
    bigTotal += total
    total = 0
    for j, row in enumerate(rows):
        for i, value in enumerate(row):
            #print(f'\nChecking {i=}, {j=}, {value=}')
            if value == ".":
                continue
            countRolls = 0
            good = True
            
            for i_near in [-1, 0, 1]:
                for j_near in [-1, 0, 1]:
                    if i_near == 0 and j_near == 0:
                        continue
                    pointi = i + i_near
                    pointj = j + j_near
                    
                    if pointi < 0 or pointi > i_limit:
                        continue
                    if pointj < 0 or pointj > j_limit:
                        continue
                    #print(f'-- Checking near {i=} {j=} {pointi=}, {pointj=} {rows[pointj][pointi]}')
                    if rows[pointj][pointi] == "@":
                        #print(f'Found a roll at {pointi=}, {pointj=} near for {i=}, {j=}')
                        countRolls += 1
                    if countRolls > 3:
                        #print(f'Break as we found {countRolls=} near at {i+i_near=}, {j+j_near=}')
                        good= False
            if good:
               # print(f'--- Hooray - good one at {i=}, {j=}')
                rows[j][i] = "."
                total += 1


print(f'{bigTotal=}')
