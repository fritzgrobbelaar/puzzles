import cleaninput
from datetime import datetime
from collections import defaultdict
from itertools import repeat
listOfText_Puzzle = cleaninput.getfileInputLinesAsList('input13.txt')


input_sample = '''#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#'''.split('\n')

input_sample2='''##...######...##.
......#..#.......
##.##########.###
###..........###.
...#..#..#..#...#
##..###..###..###
..##.#.##.#.##..#
..####.##.####..#
####........####.
..#.##.##.##.#..#
##.###.##.###.###
###.#......#.####
......####......#
#..#.##..##.#..##
..#.########.#...
##...######...##.
..#.##....##.#..#'''.split('\n')

sample3='''#.##..#
##.#.#.
##.#.##
#.##..#
...####
#.#..#.
#.#..#.'''.split('\n')

sample4 = '''##..#..#.
..###..##
###.###..
###......
....#..#.
...#.##.#
.....##..
##...##..
##.#....#'''.split('\n')

rows = input_sample
rows = listOfText_Puzzle
#rows = sample4

blocks = []
block = []
for row in rows:
    if row.strip() == '':
        blocks.append(block)
        block = []
    else:
        block.append(row)
blocks.append(block)
#blocks = [blocks[0]]
print('blocks:',blocks)

def calculate(block):
    print('processing', '\n'.join(block),'\n')
    matched = list(range(1,len(block[0])))
    print('matched:', matched)
    rowLengthH = len(block[0])/2
    for k,row in enumerate(block):
    #    print(f'\nprocessing {row=} {matched=} {k=}')
        matchedCopy = matched[:]
        for i in matchedCopy:
            value = row[i]
       #     print(f'{i=}, {row=}')
            if (i == 0) or i == len(row):
      #          print('start or end - skip')
                continue
            rowRev = ''.join(list(reversed(row[i:])))
            rowFir = row[:i]
            #print(f'{rowFir=}, {row[i:]=},{rowRev=}')
            if i <= rowLengthH:
  #              print('first half')
                revString = rowRev[-len(rowFir):]
 #               print(f'comparing {rowFir=}, and, {revString=}')
 #
                if rowFir == revString:
                    print('*****matched', i)
                else:
                    if i in matched:
                        print(f'have to remove i{k=} {i=}')
                        matched.remove(i)
            else:
        #        print('second half')
                rowFir2 = row[i-len(rowRev):i]
                print(f'comparing {rowFir2=} {rowRev=}')
                if rowFir2 == rowRev:
                    print('****matched',i)

                else:
                        print(f'have to remove i- locatino 2,{k=} {i=}')
                        matched.remove(i)
    #print('returning', matched)
        print('matched', matched)
        
    return matched

finalTotal = 0
start = datetime.now()
for block in blocks:
    print('processing block', block, finalTotal)
    result = calculate(block)
    
    if len(result) == 1:
        result = list(result)[0]
        
    else:
        print('not found in block\n', '\n'.join(block))
        blockList = list(map(list, zip(*block)))
        block = []
        for row in blockList:
            block.append(''.join(row))
        print('\n\nsending the transposed block', '\n'.join(block))
        result = list(calculate(block))[0]*100

        
    finalTotal += result


print('finalTotal', finalTotal, 'in', datetime.now()-start)
