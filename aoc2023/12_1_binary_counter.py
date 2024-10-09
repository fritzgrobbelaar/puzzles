import cleaninput
listOfText_Puzzle = cleaninput.getfileInputLinesAsList('input12.txt')


input_sample = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''.split('\n')

answers = [1, 4, 1, 1, 4, 10]

rows = listOfText_Puzzle

def doesStringMatch(binaryString, originalString):
    binary = list(binaryString)
    originalString = originalString.replace('.','0').replace('#','1')
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
    

def calculateCombinations(row):
    row, ids = row.split(' ')
    total = 0
    import itertools
    for binaryString in map(''.join, itertools.product('01', repeat=len(row))):
        if doesStringMatch(binaryString, row):
            #print('match: ', binaryString, row, ids)
            if doesIdsMatch(binaryString, ids):
                total+=1
    return total

finalTotal = 0

for i,row in enumerate(rows):
    result = calculateCombinations(row)
    #print('comparing, ', result, ' and', answers[i], row, i)
    #assert answers[i] == result
    finalTotal += result
    print('row', i, 'of', len(rows))

print('finalTotal', finalTotal)

