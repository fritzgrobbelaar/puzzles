sampleText = '''
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
'''
test2='''L100
R100
L101
R101
L32
R100'''
import math

#response = requests.get('https://adventofcode.com/2025/day/1/input')
with open('input_1.txt', 'r') as handle:
 text = handle.read()

#comment to run
#text = sampleText
rows = text.split('\n')

def calculateCounter(oldPosition, newPosition):
	#print(f'\n-- {oldPosition=}, {newPosition=}')
	counterAdd = 0
	if newPosition == 0:
		counterAdd = counterAdd + 1
	if newPosition < 0 and oldPosition != 0:
		counterAdd += 1
		print('below 1')
	rotationsCount = math.floor(abs(newPosition/100))
	print(f'{rotationsCount=}')
	counterAdd += rotationsCount
	print(f'{counterAdd=} {rotationsCount=}')
	return int(counterAdd)
	
assert 0 == calculateCounter(oldPosition = 0, newPosition = 99)
assert 1 == calculateCounter(oldPosition = 1, newPosition = 0)
assert 1 == calculateCounter(oldPosition = 1, newPosition = -1)
assert 2 == calculateCounter(oldPosition = 1, newPosition = -101)
assert 1 == calculateCounter(oldPosition = 0, newPosition = 100)
assert 2 == calculateCounter(oldPosition = 0, newPosition = 200)
assert 0 == calculateCounter(oldPosition = 0, newPosition = -1)
assert 0 == calculateCounter(oldPosition = 0, newPosition = 99)
assert 2 == calculateCounter(oldPosition = 2, newPosition = 202)
assert 3 == calculateCounter(oldPosition = 2, newPosition = -202)
assert 3 == calculateCounter(oldPosition = 2, newPosition = -200)

position = 50
size = 100
counter = 0
previousDirection = 'O'
for i, row in enumerate(rows):
	if row.strip() == '':
		continue
	#print(f'{row=}')
	direction = row[0]
	distance = int(row[1:])
	oldPosition = position
	if direction == 'L':
		position = position - distance
	else:
		position = position + distance
	counter += calculateCounter(oldPosition, position)
	position = position % 100
	previousDirection = direction
	print(f'{position=} after {row=} {counter=} {i=} {oldPosition=}')
#822 is too low
