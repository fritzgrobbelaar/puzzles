sampleText = '''
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  '''

#response = requests.get('https://adventofcode.com/2025/day/1/input')
with open('6_1.txt', 'r') as handle:
 text = handle.read()

from functools import cache
#comment to run
#text = sampleText
rows = text.split('\n')
rows = [row for row in rows if row.strip() != ""]

splitIndexes = []

for i,value in enumerate(rows[0]):
    if value == " ":
       for row in rows[1:-1]: 
            if row[i] == " ":
                pass
                #print(f'{i=} is still looking good')
            else:
                #print(f'{i=} is no good')
                break
       else:
            splitIndexes.append(i)
splitIndexes.append(len(rows[0]))

print(f'{splitIndexes=}')

for i,row in enumerate(rows):
    prevIndex = 0
    newRow = []
    for indexBreak in splitIndexes:
        #print(f'{prevIndex=} {indexBreak=} {row[prevIndex:indexBreak]=}')
        newValue = list(row[prevIndex:indexBreak])
        newValue = reversed(newValue)
        newValue = "".join(newValue)
        newRow.append(newValue)
        prevIndex = indexBreak+1
    rows[i] = newRow
    #print(f'{newRow=}')

rows = list(map(list, zip(*rows)))
rows = reversed(rows)
total = 0
for row in rows:
    #print(f'Processing {row=}')
    newRow = []
    for i in range(len(row[0])):
        newNumber = ""
        for value in row[:-1]:
            newNumber += value[i:i+1].strip()
        newRow.append(int(newNumber))
    #print(f'Processing {newRow=}')
    newRow

    if row[-1].strip() == '+':
        subTotal = 0
        for value in newRow:
            subTotal += value
    else:
        subTotal = 1
        for value in newRow:
            subTotal *= value
    total += subTotal
    #print(f'{subTotal=}')     

print(f'{total=}')
