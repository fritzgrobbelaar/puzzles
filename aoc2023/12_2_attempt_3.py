import cleaninput
from datetime import datetime
from collections import defaultdict
from itertools import repeat

listOfText_Puzzle = cleaninput.getfileInputLinesAsList('input12.txt')

input_sample = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''.split('\n')

# input_sample='''?###???????? 3,2,1'''.split('\n')
# input_sample='''?###???.???###???? 3,2,1,3'''.split('\n')
input_sample = '''?###???????? 3,2,1'''.split('\n')

rows = input_sample


# rows= listOfText_Puzzle

def calculate(row, ids):
    print('\nstarting with ', row, ids)
    permutations = {}
    permutations[(0, 0)] = 1

    for character in row:
        next = []
        for key in permutations.keys():
            permutation_count = permutations[key]
            group_id, group_amount = key
            if character in ['.', '?']:
                if group_amount == 0: # Starting condition
                    next.append((group_id, group_amount, permutation_count))
                elif group_amount == ids[group_id]:
                    next.append((group_id + 1, 0, permutation_count))
            if character in ['?', '#']:
                if group_id < len(ids):
                    print("not yet counter more groups than we have ids for")
                    if group_amount < ids[group_id]:
                        print(f'Not yet overrun the target as {group_amount} is less than {ids[group_id]} {ids} {group_id}')
                        next.append((group_id, group_amount + 1, permutation_count))

        permutations = {}
        for group_id, group_amount, permutation_count in next:
            if (group_id, group_amount) not in permutations.keys():
                permutations[(group_id, group_amount)] = 0
            permutations[(group_id, group_amount)] += permutation_count

    def is_valid(group_id, group_amount):
        if group_id == len(ids):
            return True
        if (group_id == len(ids) - 1 and group_amount == ids[group_id]):
            return True
        return False

    sum = 0
    print(f'By the end {permutations=}')
    for key, value in permutations.items():
        print(f'{key=} {value=}')
        if is_valid(key[0], key[1]):
            sum += value
    print('returning', sum)
    return sum


finalTotal = 0
start = datetime.now()
for i, row in enumerate(rows):
    print('processing row:', row)
    row, ids = row.split(' ')
    row = row  # + '?' + row #+'?' + row+'?' + row+'?' + row
    ids = ids.split(',')
    ids = [int(id) for id in ids]
    result = calculate(row, ids)
    print(f'received {result=} from calculate')
    # result = _solutions(row, ids)

    finalTotal += result
    print('row', i + 1, 'of', len(rows), result)

print('finalTotal', finalTotal, 'in', datetime.now() - start)
