from lib import cleaninput
from lib.number_pattern import  calculateTotalReversedFromInput

listOfText_Puzzle = cleaninput.getRowsOfNumbersLists('aoc2023\\input9.txt')

listOfText_Sample='''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''.split('\n')
listOfText_Sample = cleaninput.convertRowsOfTextToRowsOfNumbers(listOfText_Sample)

listOfText = listOfText_Sample
listOfText = listOfText_Puzzle

print('total: ', calculateTotalReversedFromInput(listOfText))

exit()
