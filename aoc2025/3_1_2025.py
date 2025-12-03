sampleText = '''987654321111111
811111111111119
234234234234278
818181911112111'''

#response = requests.get('https://adventofcode.com/2025/day/1/input')
with open('input_3.txt', 'r') as handle:
 text = handle.read()

from functools import cache
#comment to run
#text = sampleText
rows = text.split('\n')



def getNumber(numberString):
   # print(f'{numberString=}')
    
    numberList = list(numberString)
    finalList = numberList[:2]
    for number in numberList[2:]:
        #print(f'{finalList=} {number=}')
        if finalList[1] > finalList[0]:
            finalList = [finalList[1]] + [number]
            #print(f'After shifting {finalList=} ')
        elif number > finalList[1]:
            finalList[1] = number
            #print(f'After swopping {finalList=} ')
    print(f'{finalList=} ')
    return int(''.join(finalList))
    
assert 41 == getNumber('3341')
assert 98 == getNumber('987654321111111')
assert 89 == getNumber('811111111111119')
assert 78 == getNumber('234234234234278')
assert 92 == getNumber('818181911112111')


bigTotal = 0
for row in rows:
    if row.strip() == "":
        continue
    #print(f'{row=}')
    bigTotal += getNumber(row)
    print(f'{bigTotal=}')
print(f'{bigTotal=}')
