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

#input_sample='''?###???????? 3,2,1'''.split('\n')
input_sample='''??#??#?? 1,1'''.split('\n')


rows = input_sample
#rows= listOfText_Puzzle

def _solutions(row, pattern):
    permutations = defaultdict(int)
    
    permutations[(0, 0)] = 1 # key is (group_id, group_amount)
    print(permutations)
    for c in row:
        next = []
        for key, perm_count in permutations.items():
            group_id, group_amount = key
            if c != '#':
                if group_amount == 0:
                    next.append((group_id, group_amount, perm_count))
                elif group_amount == pattern[group_id]:
                    next.append((group_id + 1, 0, perm_count))
            if c != '.':
                if group_id < len(pattern) and group_amount < pattern[group_id]:
                    next.append((group_id, group_amount + 1, perm_count))
        permutations.clear()
        for group_id, group_amount, perm_count in next:
            permutations[(group_id, group_amount)] += perm_count

    def is_valid(group_id, group_amount):
         return group_id == len(pattern) or group_id == len(pattern) - 1 and group_amount == pattern[group_id]
    return sum(v for k, v in permutations.items() if is_valid(*k))

def calculate(row, ids):
  #  print('\nstarting with ',row,ids)
    if len(ids) == 0:
        return 0
    finalChecksList = row.replace('?','.').split('.')
    if '' in finalChecksList:
        finalChecksList.remove('')
    finalChecks = [len(value) for value in finalChecksList if len(value) != 0]
  #  print('finalCheck',finalChecks, ids)
    if finalChecks == ids:
  #    print('its final - lets return')
      return 1
    
    consumingID = ids[0]
    minStringLengthRequired = sum(ids) + len(ids) - 1
    remainingIDs = ids[1:]
    totalCount = 0
    while len(row) >= minStringLengthRequired:
     #   print('row',row, remainingIDs)

        
        if row[:ids[0]].replace('?','#') == '#'*consumingID and \
            ((len(row) == consumingID) or (row[consumingID] in ['.','?'])):
               # print(f'criteria has matched {row=} started with {consumingID=}')
                if len(remainingIDs) == 0:
                 #   print('incrementing')
                    totalCount += 1
                    if row[:ids[0]] == '#'*consumingID:
                  #      print('we need it to match - we need to return as we have nothing left')
                        return totalCount
                    return totalCount
                else:
              #      print('go deeper',row[consumingID+1:], remainingIDs)
                    count= calculate(row[consumingID+1:], remainingIDs)
                    totalCount += count
             #       print(f'received from lets go deeper with',row[consumingID+1:], remainingIDs,'adding:',count)
                    
        row = row[1:]
   # print(f'ended while loop, because {len(row)=} {row=} is less than {minStringLengthRequired=}\n'
    #      f'returning {totalCount=} on {ids=}\n')
    return totalCount
            


rowFinal = []
finalTotal = 0
start = datetime.now()
for i,row in enumerate(rows):

    row, ids = row.split(' ')
    row = row + '?' + row +'?' + row+'?' + row+'?' + row
    ids = ids.split(',')*5
    ids = [int(id) for id in ids]
    result = _solutions(row, ids)

    finalTotal += result
    rowFinal.append(result)
    print('row', i+1, 'of', len(rows), result)


print('finalTotal', finalTotal, 'in', datetime.now()-start)
