sampleText = '''123 328  51 64 
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

products = []
freshRanges = []
for i,row in enumerate(rows):
    row = row.split()
    if i != len(rows) - 1:
        row =  [int(value) for value in row]
    rows[i] = row

rows = list(map(list, zip(*rows)))
total = 0
for row in rows:
    
    if row[-1] == '+':
        subTotal = 0
        for value in row[:-1]:
            subTotal += value
    else:
        subTotal = 1
        for value in row[:-1]:
            subTotal *= value
    total += subTotal
    print(f'{subTotal=}')     

print(f'{total=}')
