import cleaninput, re
from collections import deque
from operator import itemgetter, attrgetter
from functools import cmp_to_key

listOfText1 = cleaninput.getfileInputLinesAsList('input5_1_2024.txt')
listOfText2 = cleaninput.getfileInputLinesAsList('input5_2_2024.txt')

sample1 = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13'''.split('\n')

sample2= '''75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''.split('\n')

#listOfText1 = sample1
#listOfText2 = sample2

sequence = {}
for row in listOfText1:
    row = row.split('|')
    key = row[0]
    value = row[1]
    if key not in sequence.keys():
        sequence[key] = set()
    sequence[key].add(value)
print(f'{sequence=}')

def sortFunc(key,key2):
    if key in sequence.keys():
        if key2 in sequence[key]:
            return -1
    return 0

def fixOrder(row):
    print('Sorting row', row)
    row.sort(key=cmp_to_key(sortFunc))
    print('sorted row', row)
    return row
    # newRow = []
    # print(f'Fixing {row=}')
    # for value in row:
    #     location = len(newRow)
    #     if value in sequence.keys():
    #         laterList = sequence[value]
    #     for i,newRowValue in enumerate(newRow):
    #         if newRowValue in laterList:
    #             location=i-1
    #             print(f'Adding {value=} to {i=} in {newRow=}')
    #             break
    #
    #     newRow = newRow[:location] + [value] + newRow[location:]
    #     print(f'{newRow=}')
    # return newRow


#assert ['61','29','13'] == fixOrder(['61','13','29'])
#assert ['97','75','47','61','53'] == fixOrder(['75','97','47','61','53'])
#assert ['97','75','47','29','13'] == fixOrder(['97','13','75','29','47'])


total = 0
#listOfText2 = ['75,97,47,61,53']
#listOfText2 = ['75,47,61,53,29']
for row in listOfText2:
    print(f'Processing {row=}')
    row = row.split(',')
    badRow = False
    for i, value in enumerate(row):
        if i == 0:
            continue
        #print('checking i')

        if badRow:
            break
        if value in sequence.keys():

            print(f'Checking row {value=} to see if {sequence[value]=} is found in {row[:i]=} {row=}')
            for later in sequence[value]:
                if later in row[:i]:
                    print(f'Invalid row as for {value=} {later=} is found in {row[:i]=} {row=}')
                    badRow=True
                    continue
        else:
            pass
            #print(f'{value=} not found in {sequence.keys()=}')

    print(f'{badRow=} {row=}')
    if badRow:
        newRow = fixOrder(row)
        print('adding',int(row[int(len(row)/2)]))
        total = total + int(row[int(len(row)/2)])


print(f'{total=}')
