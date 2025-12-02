sampleText = '''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'''

#response = requests.get('https://adventofcode.com/2025/day/1/input')
with open('input_2.txt', 'r') as handle:
 text = handle.read()

from functools import cache
#comment to run
#text = sampleText
rows = text.split(',')

@cache
def getAllFactors(integer):
    factorList = []
    for i in range(2,integer+1):
        if integer % i == 0:
            factorList.append(i)
    return factorList

assert [2] == getAllFactors(2)
assert [3] == getAllFactors(3)
assert [2,4] == getAllFactors(4)
assert [5] == getAllFactors(5)
assert [2,3,6] == getAllFactors(6)
assert [2,5,10] == getAllFactors(10)


def getSumInvalidIDs(start, end):
    print(f'Starting {start=} {end=}')
    end = end + 1
    total = 0


    for i in range(start, end):
        i_str = str(i)
        i_len = len(i_str)
        for factor in getAllFactors(i_len):
            #print(f' {i=} {factor=}')
            if i_len % factor != 0:
                continue
            part_len = int(i_len/factor)
            i_part = i_str[:part_len]
            #print(f'{i_part=} {i_part*factor=}')
            if i_str == i_part*factor:
                #print(f'Found something: {total=}')
                total += i
                break
    print(f'Returning something: {total=}')
    return total

assert 222222 == getSumInvalidIDs(222220,222224)

assert 33 == getSumInvalidIDs(11, 22)
assert 210 == getSumInvalidIDs(95, 115)
assert 2009 == getSumInvalidIDs(998, 1012)
assert 1188511885 == getSumInvalidIDs(1188511880,1188511890)
assert 222222 == getSumInvalidIDs(222220,222224)

assert 0 == getSumInvalidIDs(1698522,1698528)
assert 446446 == getSumInvalidIDs(446443,446449)
assert 38593859 == getSumInvalidIDs(38593856,38593862)
assert 565656 == getSumInvalidIDs(565653,565659)
assert 824824824 == getSumInvalidIDs(824824821,824824827)
assert 2121212121 == getSumInvalidIDs(2121212118,2121212124)

assert 11 == getSumInvalidIDs(11,12)
assert 11 == getSumInvalidIDs(10,11)
assert 11 == getSumInvalidIDs(11,11)
assert 1234512345 == getSumInvalidIDs(1234512345,1234512345)

bigTotal = 0
for row in rows:
    row = row.split('-')
    print(f'{row=}')
    bigTotal += getSumInvalidIDs(int(row[0]), int(row[1]))
print(f'{bigTotal=}')
