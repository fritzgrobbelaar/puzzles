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

sample3='''#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.'''.split('\n')

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
        block.append(list(row))
blocks.append(block)
#blocks = [blocks[0]]
#print('blocks:',blocks)

def printBlock(block):
    print()
    for row in block:
        print(''.join(row))

def calculate(block):
    #print('processing', '\n'.join(block),'\n')
    
    matched = list(range(1,len(block[0])))
    #print('matched:', matched)
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
            rowRev = list(reversed(row[i:]))
            rowFir = row[:i]
         #   print(f'{rowFir=}, {row[i:]=},{rowRev=}')
            if i <= rowLengthH:
  #              print('first half')
                revString = rowRev[-len(rowFir):]
 #               print(f'comparing {rowFir=}, and, {revString=}')
 #
                if rowFir == revString:
                    #print('*****matched', i)
                    pass
                else:
                    if i in matched:
                        #print(f'have to remove i{k=} {i=}')
                        matched.remove(i)
            else:
        #        print('second half')
                rowFir2 = row[i-len(rowRev):i]
       #         print(f'comparing {rowFir2=} {rowRev=}')
                if rowFir2 == rowRev:
                    #print('****matched',i)
                    pass
                else:
                        #print(f'have to remove i- locatino 2,{k=} {i=}')
                        matched.remove(i)
    #print('returning', matched)
        #print('matched', matched)
        
    return matched

def calculateAndFlipBlocks(block):
    originalResult = calculate(block)
    print(f' {originalResult=}')
    allResults = []
    for i, row in enumerate(block):
        for j, value in enumerate(row):
            if value == '.':
                block[i][j] = '#'
            else:
                block[i][j] = '.'
            result = calculate(block)
            if len(result) > 0:
         #       print(f'big test {result=} {originalResult=}')
                if result == originalResult:
        #            print('perfect match')
                    pass
                else:
                    print('Matched - returning after flipping 2', i,j, f'{originalResult=} {result=}')
                    if len(result) == 1:
                        allResults += result
                    else:
                        originalValue = originalResult[0]
                        if originalValue not in result:
                            allResults += result
                        else:
                            result.remove(originalValue)
                        
                            allResults += result
            block[i][j] = value
    print('returning', allResults)
    return allResults
        

finalTotal = 0
start = datetime.now()
for i,block in enumerate(blocks):
    print(f'Processing block number {i=}')
    printBlock(block)
    #print('processing block', block, finalTotal)
    result = calculateAndFlipBlocks(block)
    #print('received result 1', result)
    if len(result) >0:
        result = list(result)[0]
        
    else:
        #print('not found in block\n', '\n'.join(block))
        blockList = list(map(list, zip(*block)))
        block = []
        for row in blockList:
            block.append(row)
        #print('\n\nsending the transposed block', '\n'.join(block))
       
        result = calculateAndFlipBlocks(block)
        print('Added response:', result[0])
        if len(result) == 0:
            print('not found in block number', i)
            printBlock(block)
            raise Exception('something bad happened')
        result = result[0]*100
    print("Total adding the result", result)
    finalTotal += result

#25664 is too low

print('finalTotal', finalTotal, 'in', datetime.now()-start)
