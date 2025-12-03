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



def getNumber(numberString,size):
   # print(f'{numberString=}')
    
    numberList = list(numberString)
    currentArray = numberList[:size]
    for number in numberList[size:]:
        #print(f'{currentArray=} {number=}')
        for i,value in enumerate(currentArray[:-1]):
            nextValue = currentArray[i+1]
            if nextValue > value:
                currentArray.pop(i)
                currentArray.append(number)
                #print(f'{currentArray=} changed array')
                break
        else:
            if currentArray[-1] < number:
                currentArray[-1] = number
                #print(f'{currentArray=} swiched number')
    print(f'{currentArray=} at the end')
    return int(''.join(currentArray))

assert 41 == getNumber('3341',2)
assert 341 == getNumber('341',3)
assert 98 == getNumber('987654321111111',2)
assert 89 == getNumber('811111111111119',2)
assert 78 == getNumber('234234234234278',2)
assert 92 == getNumber('818181911112111',2)
assert 987654321111 == getNumber('987654321111111',12)
assert 811111111119 == getNumber('811111111111119',12)
assert 434234234278 == getNumber('234234234234278',12)
assert 888911112111 == getNumber('818181911112111',12)


bigTotal = 0
for row in rows:
    if row.strip() == "":
        continue
    #print(f'{row=}')
    bigTotal += getNumber(row,12)
    print(f'{bigTotal=}')
print(f'{bigTotal=}')
