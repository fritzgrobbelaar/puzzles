import cleaninput, re
from collections import deque
from operator import itemgetter, attrgetter
from functools import cmp_to_key

listOfText = cleaninput.getfileInputLinesAsList('input6_2024.txt')

sample = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29'''.split('\n')

listOfText = sample

total = 0
for row in listOfText:
    print(f'{row=}')
    total += 1
print(f'{total=}')
