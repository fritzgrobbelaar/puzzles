import cleaninput
from datetime import datetime
listOfText_Puzzle = cleaninput.getfileInputLinesAsList('input12.txt')


input_sample = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''.split('\n')

#input_sample='''???????#??#.???????????????#??#.???????????????#??#.??????? 3,2,2,1,2,3,2,2,1,2,3,2,2,1,2'''.split('\n')

answers = [1, 4, 1, 1, 4, 10,1]

rows = input_sample
#rows= listOfText_Puzzle

def getRemainingStrings(id, row):
    id = int(id)
    searchString = '#'*id
    a =('row: searching for id', id,' in ', row)
    idsAndStrings = {'reconstruct':[], 'remainingStrings': []}
    length = len(row)
    for i in range(length):
       # print("entered for-loop", i, length)
        if '.' not in row[i:i+len(searchString)]:
            if len(searchString) + i == length:
      #          print("Last string matched", i, length, searchString, len(searchString))
                if len(row) > id:
                    lookBefore = row[i-1]
                    if lookBefore != '#':
                   #     print("appending at the end 2 because good", i + len(searchString))
                        idsAndStrings['remainingStrings'].append('')
                        idsAndStrings['reconstruct'].append(row[:i] + searchString + row[i+len(searchString):])
                    else:
                        pass
                  #      print("Look before disqualifies this ", i)
                        
                else:
                 #   print("appending at the end")
                    idsAndStrings['remainingStrings'].append('')
                    idsAndStrings['reconstruct'].append(row[:i] + searchString + row[i+len(searchString):])
            elif len(searchString)+i < length:
                #print('index: ', i+len(searchString),  row[i + len(searchString)])
                if (row[i + len(searchString)] in ['?', '.']):
                    if i == 0 or (row[i-1] in ['?', '.']):
               #         print("appending", i, 'because ahead is good', row[i + len(searchString)],
                #              'and behind is good',row[i-1], 'remaining row', row[i + len(searchString):],
                 #             'appending value ', row[i + len(searchString)+1:])
                        idsAndStrings['remainingStrings'].append(row[i + len(searchString)+1:])
                        idsAndStrings['reconstruct'].append(row[:i] + searchString + row[i+len(searchString):])
                        
    a = ("returning row search", idsAndStrings)
    return idsAndStrings


assert {'reconstruct': ['#?.?', '#?.#'], 'remainingStrings': ['.?','']} == getRemainingStrings(1, '#?.?')
assert {'reconstruct': ['#'], 'remainingStrings': ['']} == getRemainingStrings(1, '#')
assert {'reconstruct': [], 'remainingStrings': []} == getRemainingStrings(1, '##')
assert {'reconstruct': ['#?'], 'remainingStrings': ['']} == getRemainingStrings(1, '#?')
assert {'reconstruct': ['#?', '?#'], 'remainingStrings': ['', '']} == getRemainingStrings(1, '??')
assert {'reconstruct': ['##?', '?##'], 'remainingStrings': ['', '']} == getRemainingStrings(2, '???')
assert {'reconstruct': ['?#'], 'remainingStrings': ['']} == getRemainingStrings(1, '?#')
#assert {'reconstruct': ['#?', '?#'], 'remainingStrings': ['', '']} == getRemainingStrings(1, '?.?')
#assert ['..??...?##.', '.??...?##.', '...?##.', '..?##.'] == getRemainingStrings(1, '.??..??...?##.')
#assert [''] == getRemainingStrings(3, '...?##.')
#assert ['???#.', '#.', ''] == getRemainingStrings(2, '?##????#.')
#assert ['????#.', '?#.','#.', ''] == getRemainingStrings(2, '?##?????#.')
#assert ['????##.', '?##.','##.', ''] == getRemainingStrings(2, '?##?????##.')
#assert ['?????###.', '?###.','###.', ''] == getRemainingStrings(3, '?###??????###.')

#assert ['??????###????????',
#        '?????###????????',
#        '????###????????',
#        '???###????????',
#        '??###????????',
#        '?###????????',
#        '###????????',
#        '????',
#        '???',
#        '??',
#        '?',
#        '',
#        ''] == getRemainingStrings(2, '?????????###????????')

#assert '?????????###????????' == getRemainingStrings(3, '?###??????????###????????')[0]
#assert '?????###????????' == getRemainingStrings(3, '?###??????????###????????')[1]



expected = {'reconstruct': [
    '?###??????????###????????',
    '?###?###??????###????????',
    '?###??###?????###????????',
    '?###???###????###????????',
    '?###????###???###????????',
    '?###?????###??###????????',
    '?###??????###?###????????',
    '?###??????????###????????',
    '?###??????????###?###????',
    '?###??????????###??###???',
    '?###??????????###???###??',
    '?###??????????###????###?',
    '?###??????????###?????###'],
            'remainingStrings': [
                '?????????###????????',
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
                '']}
#result = getRemainingStrings(3, '?###??????????###????????')
#assert expected == result

#assert ['????', '???', '??', '?', '', ''] == getRemainingStrings(2, '??###????????')
#print("passed all unit tests")

def doesIdsMatch(binaryString, ids):
    binaryString = binaryString.replace('?','.')
    listBinary = binaryString.split('.')
    lengths = [str(len(x)) for x in listBinary if len(x) != 0]
    if lengths == ids:
        a = ('Full match found:', lengths, ids, 'True')
        return True
    a = ('returning false from doesIdsMatch', binaryString, ids)
    return False

def calculateRemainingCombinations(row, remainingIds, depth):
    #print('\nprocessing row', row, 'with remainingIds', remainingIds)
    a = ('\nprocessing row', row, 'with remainingIds', remainingIds, 'depth:', depth)

    if len(remainingIds) > len(row):
        a =('returning early')
        return []
    consumingID = remainingIds[0]
    newRemainingIds = remainingIds[1:]
    remainingStringsAndReconstruct = getRemainingStrings(consumingID, row)
    a = ("Ready to start processing results of new row:", remainingStringsAndReconstruct,
          'depth', depth)
    reconstruct = remainingStringsAndReconstruct['reconstruct']
    remainingStrings = remainingStringsAndReconstruct['remainingStrings']
    reconstructResult = []
    for i,remaining in enumerate(remainingStrings):
        a = ("Processing remaining in for-loop", remaining,
              'depth:', depth,
              'i:',i)
        if len(newRemainingIds) == 0:
            if remaining.find('#') == -1:
                    a= ('incrementing count as it fits. Reconstruct: ', reconstruct[i],
                          'remaining:', remaining,
                          'started with:', row)
                    fullReconstructResult = row[:len(row)-len(reconstruct[i])] + reconstruct[i]
                    reconstructResult = reconstructResult+ [fullReconstructResult]
            else:
                    a  = ('# not found in ', remaining)
        else:
            a = ('sending downstream, remaining:', remaining,
                  'newRemainingIds:', newRemainingIds,
                  'consumingId:', consumingID,
                  'i',i)
            received = calculateRemainingCombinations(remaining, newRemainingIds, depth+1)
            if received == []:
                continue
            fullReceived = []
            for receive in received:
                fullReceived.append(reconstruct[i][:len(reconstruct[i])-len(receive)] + receive)
            reconstructResult = reconstructResult + fullReceived
            a= ("received:", received,
                  'started with:',row,
                  'remainingIds:', remainingIds,
                  'depth:', depth,
                  'fullReceived',fullReceived,
                  'also interesting',remainingStringsAndReconstruct,
                  'reconstructResult', reconstructResult)
   #         print('known about and could have chosen', reconstruct[i])



#    print("Before final checks reconstructResult:", reconstructResult, 'depth:',depth)
    if depth== 0:
        reconstructResult = list(set(reconstructResult))
        finalResult = []
        for reconstruct in reconstructResult:
            if doesIdsMatch(reconstruct, remainingIds):
                finalResult.append(reconstruct)
        reconstructResult = finalResult
  #  print("Returning reconstructResult:", reconstructResult, 'depth:',depth)
    return reconstructResult

#assert 1 == calculateRemainingCombinations('#', [1])
#assert 2 == calculateRemainingCombinations('??', [1])
#print('passed')

def calculateStartingWithIds(row, ids):
    idsLocation = {}
    for i,id in enumerate(ids):
        idsLocation[i] = 0
    optionsRemaining = True
    while optionsRemaining:
        highWaterMark = 0
        for i,id in enumerate(ids):
            for j in row:
                pass
        

rowFinal = []
finalTotal = 0
start = datetime.now()
for i,row in enumerate(rows):
    #print('-----Processing new row', row, 'at', datetime.now())
    
    row, ids = row.split(' ')
    row = row + '?' + row +'?' + row+'?' + row+'?' + row
    ids = ids.split(',')*5
    
    print('-----Processing new row', row, ','.join(ids), 'at', datetime.now())
    result = calculateRemainingCombinations(row, ids, depth=0)
#    print("received result", len( result))
    #print('comparing, ', result, ' and', answers[i], row, i)
    #assert answers[i] == result
    #print('result', len(result))
    finalTotal += len(result)
    rowFinal.append(result)
    print('row', i, 'of', len(rows), len(result))
    if i > 11:
        break
#total: 6827 in 3sec8 - power 1
# power 2: 14 seconds
print('finalTotal', finalTotal, 'in', datetime.now()-start)
#print(rowFinal)

