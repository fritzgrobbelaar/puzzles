import cleaninput
listOfText_Puzzle = cleaninput.getfileInputLinesAsList('input12.txt')


input_sample = '''???.### 1,1,3
.??..??...?##. 1,1,3'''.split('\n')
test1='''?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''.split('\n')

answers = [1, 4, 1, 1, 4, 10]

rows = input_sample
#rows= listOfText_Puzzle

# def doesStringMatch(binaryString, originalString):
#     binary = list(binaryString)
#
#     original = list(originalString)
#     for i, value in enumerate(original):
#         if value == '?':
#             pass
#         elif value == binary[i]:
#             pass
#         else:
#             #print('comparing', ''.join(original), ''.join(binary),value, binary[i],'returning False')
#             return False
#     #print('comparing', ''.join(original), ''.join(binary),'returning True')
#     return True
#
# def doesIdsMatch(binaryString, ids):
#     listBinary = binaryString.split('0')
#     lengths = [str(len(x)) for x in listBinary if len(x) != 0]
#     lengthsString = ','.join(lengths)
#     if lengthsString == ids:
#         #print('Full match found:', lengthsString, ids, 'True')
#         return True
#     if binaryString == '01000100001110':
#         #print('comparing', lengthsString, ids, 'False')
#         pass
#     return False
#
#
# def replaceWithBinary(row, binaryString):
#     newString = ''
#     binaryIndex = 0
#     for value in row:
#         if value == '?':
#             value = binaryString[binaryIndex]
#             binaryIndex += 1
#         newString = newString + value
#     return newString
#
#
# assert '000001111' == replaceWithBinary('000??1?11', '001')
# assert '0100101111' == replaceWithBinary('0?00??1?11', '1101')

def getRemainingStrings(id, row):
    id = int(id)
    searchString = '#'*id
    print('\nsearching for id', id,' in ', row)
    idsAndStrings = []
    length = len(row)
    for i in range(length):
       # print("entered for-loop", i, length)
        if '.' != row[i]:
            if len(searchString) + i == length:
      #          print("Last string matched", i, length, searchString, len(searchString))
                if len(row) > id:
                    lookBefore = row[i-1]
                    if lookBefore != '#':
                        idsAndStrings.append('')
                    else:
                        pass
     #                   print("Look before disqualifies this ", i)
                else:
                    idsAndStrings.append('')
            elif len(searchString)+i < length:
    #            print('index: ', i+len(searchString) + 1,  row[i + len(searchString)])
                if row[i + len(searchString)] in ['?', '.']:
   #                 print("appending", i)
                    idsAndStrings.append(row[i + len(searchString)+1:])
    print("returning", idsAndStrings)
    return idsAndStrings

#assert [''] == getRemainingStrings(1, '#')
#assert [] == getRemainingStrings(1, '##')
#assert [''] == getRemainingStrings(1, '#?')
#assert ['', ''] == getRemainingStrings(1, '??')
#assert [''] == getRemainingStrings(1, '?#')
#assert ['?', ''] == getRemainingStrings(1, '?.?')
#assert ['.?','?', ''] == getRemainingStrings(1, '#?.?')
#print("passed all unit tests")

def calculateRemainingCombinations(remainingRow, remainingIds):
    print('processing row', remainingRow, remainingIds)
    consumingID = remainingIds[0]
    newRemainingIds = remainingIds[1:]
    remainingStrings = getRemainingStrings(consumingID, remainingRow)
    count = 0
    for remaining in remainingStrings:
        if len(newRemainingIds) == 0:
            print("Found a matching one! returning", len(remainingStrings))
            return len(remainingStrings)
        else:
            count += calculateRemainingCombinations(remaining, newRemainingIds)
            print("received", count)
    print("returning counts added ", count )
    return count

#assert 1 == calculateRemainingCombinations('#', [1])
#assert 2 == calculateRemainingCombinations('??', [1])
#print('passed')

finalTotal = 0
for i,row in enumerate(rows):
    row, ids = row.split(' ')
    row = row
    ids = ids.split(',')
    result = calculateRemainingCombinations(row, ids)
    print("received result", result)
    #print('comparing, ', result, ' and', answers[i], row, i)
    #assert answers[i] == result
    finalTotal += result
    print('row', i, 'of', len(rows))
#total: 6827
print('finalTotal', finalTotal)

