import cleaninput
from datetime import datetime
from functools import cmp_to_key
listOfText = cleaninput.getfileInputLinesAsList('input10_2024.txt')

sample = '''2333133121414131402'''.split('\n')

listOfText = sample

listOfLists = []
total = 0
for row in listOfText:
    listOfLists.append(list(row))

for i, row in enumerate(listOfLists):
    total += 1
print(f'{total=}')

