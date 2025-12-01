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

#response = requests.get('https://adventofcode.com/2025/day/1/input')
with open('input_1.txt', 'r') as handle:
 text = handle.read()

#comment to run
#text = sampleText
rows = text.split('\n')

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
	if position == 0:
		#if (direction == 'L') or (previousDirection == 'L'):
			counter +=1
			print('increase counter')
	if direction == 'L':
		position = position - distance
	else:
		position = position + distance

	position = position % 100
	previousDirection = direction
	print(f'{position=} after {row=} {counter=} {i=}')
#822 is too low
