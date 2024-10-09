import cleaninput
listOfText_Puzzle = cleaninput.getfileInputLinesAsList('input12.txt')


input_sample = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''.split('\n')

answers = [1, 4, 1, 1, 4, 10]

rows = input_sample
#rows= listOfText_Puzzle

def doesStringMatch(binaryString, originalString):
    binary = list(binaryString)
    
    original = list(originalString)
    for i, value in enumerate(original):
        if value == '?':
            pass
        elif value == binary[i]:
            pass
        else:
            #print('comparing', ''.join(original), ''.join(binary),value, binary[i],'returning False')
            return False
    #print('comparing', ''.join(original), ''.join(binary),'returning True')
    return True
        
def doesIdsMatch(binaryString, ids):
    listBinary = binaryString.split('0')
    lengths = [str(len(x)) for x in listBinary if len(x) != 0]
    lengthsString = ','.join(lengths)
    if lengthsString == ids:
        #print('Full match found:', lengthsString, ids, 'True')
        return True
    if binaryString == '01000100001110':
        #print('comparing', lengthsString, ids, 'False')
        pass
    return False


assert 3 == countUnknowns('...??#?##')
assert 4 == countUnknowns('.?..??#?##')

def replaceWithBinary(row, binaryString):
    newString = ''
    binaryIndex = 0 
    for value in row:
        if value == '?':
            value = binaryString[binaryIndex]
            binaryIndex += 1
        newString = newString + value
    return newString


assert '000001111' == replaceWithBinary('000??1?11', '001')
assert '0100101111' == replaceWithBinary('0?00??1?11', '1101')


    


def calculateRemainingCombinations(remainingRow, remainingIds):
    print('processing row', remainingRow, remainingIds)

    total = 0
    import itertools
    remainingRow = remainingRow.replace('.','0').replace('#','1')
    remainingIds = ids


    # for binaryString in map(''.join, itertools.product('01', repeat=countUnknowns(row))):
    #     binaryString = replaceWithBinary(row, binaryString)
    #     if doesIdsMatch(binaryString, ids):
    #         if doesStringMatch(binaryString, row):
    #             print('match: ', binaryString, row, ids)
    #             total+=1
    return total

finalTotal = 0

for i,row in enumerate(rows):
    row, ids = row.split(' ')
    row = row*2
    ids = ids = ','.join([ids]*2)
    result = calculateRemainingCombinations(row, ids)
    #print('comparing, ', result, ' and', answers[i], row, i)
    #assert answers[i] == result
    finalTotal += result
    print('row', i, 'of', len(rows))
#total: 6827
print('finalTotal', finalTotal)

