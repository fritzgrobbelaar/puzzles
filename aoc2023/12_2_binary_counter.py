import cleaninput
listOfText_Puzzle = cleaninput.getfileInputLinesAsList('input12.txt')


input_sample = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''.split('\n')

input_sample='''?###???????? 3,2,1'''.split('\n')

answers = [1, 4, 1, 1, 4, 10]

rows = input_sample
#rows= listOfText_Puzzle

def getRemainingStrings(id, row):
    id = int(id)
    searchString = '#'*id
    print('searching for id', id,' in ', row)
    idsAndStrings = []
    length = len(row)
    for i in range(length):
     #   print("entered for-loop", i, length)
        if '.' not in row[i:i+len(searchString)]:
            if len(searchString) + i == length:
      #          print("Last string matched", i, length, searchString, len(searchString))
                if len(row) > id:
                    lookBefore = row[i-1]
                    if lookBefore != '#':
        #                print("appending at the end 2 because good", i + len(searchString))
                        idsAndStrings.append('')
                    else:
                        pass
       #                 print("Look before disqualifies this ", i)
                else:
        #            print("appending at the end")
                    idsAndStrings.append('')
            elif len(searchString)+i < length:
         #       print('index: ', i+len(searchString),  row[i + len(searchString)])
                if (row[i + len(searchString)] in ['?', '.']):
                    if i == 0 or (row[i-1] in ['?', '.']):
   #                     print("appending", i, 'because ahead is good', row[i + len(searchString)],
    #                          'and behind is good',row[i-1], 'remaining row', row[i + len(searchString):],
     #                         'appending value ', row[i + len(searchString)+1:])
                        idsAndStrings.append(row[i + len(searchString)+1:])
    print("returning", idsAndStrings)
    return idsAndStrings

assert [''] == getRemainingStrings(1, '#')
assert [] == getRemainingStrings(1, '##')
assert [''] == getRemainingStrings(1, '#?')
assert ['', ''] == getRemainingStrings(1, '??')
assert ['', ''] == getRemainingStrings(2, '???')
assert [''] == getRemainingStrings(1, '?#')
assert ['?', ''] == getRemainingStrings(1, '?.?')
assert ['.?',''] == getRemainingStrings(1, '#?.?')
assert ['..??...?##.', '.??...?##.', '...?##.', '..?##.'] == getRemainingStrings(1, '.??..??...?##.')
assert [''] == getRemainingStrings(3, '...?##.')
assert ['???#.', '#.', ''] == getRemainingStrings(2, '?##????#.')
assert ['????#.', '?#.','#.', ''] == getRemainingStrings(2, '?##?????#.')
assert ['????##.', '?##.','##.', ''] == getRemainingStrings(2, '?##?????##.')
assert ['?????###.', '?###.','###.', ''] == getRemainingStrings(3, '?###??????###.')

assert ['??????###????????',
        '?????###????????',
        '????###????????',
        '???###????????',
        '??###????????',
        '?###????????',
        '###????????',
        '????',
        '???',
        '??',
        '?',
        '',
        ''] == getRemainingStrings(2, '?????????###????????')

assert '?????????###????????' == getRemainingStrings(3, '?###??????????###????????')[0]
assert '?????###????????' == getRemainingStrings(3, '?###??????????###????????')[1]



expected = ['?????????###????????',
            
            '?????###????????',
            '????###????????',
            '???###????????',
            '??###????????',
            '?###????????',
            '###????????',
            
            '???????',
            '???',
            '??',
            '?',
            '',
            '']
result = getRemainingStrings(3, '?###??????????###????????')
assert expected == result

assert ['????', '???', '??', '?', '', ''] == getRemainingStrings(2, '??###????????')
#print("passed all unit tests")

def calculateRemainingCombinations(row, remainingIds):
    print('\nprocessing row', row, 'with remainingIds', remainingIds)

    if len(remainingIds) > len(row): return 0
    #print('\nprocessing row', row, 'with remainingIds', remainingIds)
    consumingID = remainingIds[0]
    newRemainingIds = remainingIds[1:]
    remainingStrings = getRemainingStrings(consumingID, row)
    count = 0
    for remaining in remainingStrings:
        print("Getting remaining", remaining)
        if len(newRemainingIds) == 0:
            print("Found no ids remaining! returning", len(remainingStrings), 'string remaining',
                  remainingStrings, 'started with', row)
            count3 = 0
            for string in remainingStrings:
                if '#' not in string:
                    count3 += 1
            return count3
        else:
            count += calculateRemainingCombinations(remaining, newRemainingIds)
  #          print("received", count)
    if count != 0:
        pass
        print("returning counts added ", count, 'from',row, 'and', remainingIds )
    return count

#assert 1 == calculateRemainingCombinations('#', [1])
#assert 2 == calculateRemainingCombinations('??', [1])
#print('passed')

rowFinal = []
finalTotal = 0
for i,row in enumerate(rows):
    row, ids = row.split(' ')
    row = row + '?' #+ row #+'?' + row+'?' + row+'?' + row
    ids = ids.split(',')*2
    result = calculateRemainingCombinations(row, ids)
    print("received result", result)
    #print('comparing, ', result, ' and', answers[i], row, i)
    #assert answers[i] == result
    finalTotal += result
    rowFinal.append(result)
    print('row', i, 'of', len(rows))
#total: 6827
print('finalTotal', finalTotal)
print(rowFinal)

