sampleText = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32'''

#response = requests.get('https://adventofcode.com/2025/day/1/input')
with open('input_5.txt', 'r') as handle:
 text = handle.read()

from functools import cache
#comment to run
#text = sampleText
rows = text.split('\n')

products = []
freshRanges = []
for row in rows:
    if '-' in row:
        row = row.split('-')
        freshRanges.append([int(row[0]), int(row[1])])
    elif row.strip() != '':
        products.append(int(row))

#print(f'{freshRanges=}')
#print(f'{products=}')
counter = 0
for product in products:
    for range in freshRanges:
        if product >= range[0] and product <= range[1]:
            counter +=1
            break
        else:
            pass
            #print(f'{product=} not in {range=} {product >= range[0]=} {product <= range[1]=}')
print(f'{counter=}')
