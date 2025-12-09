import cleaninput
from datetime import datetime
from functools import cmp_to_key
import math
listOfText = cleaninput.getfileInputLinesAsList('input_9.txt')

sample='''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''.split('\n')

#listOfText = sample
listOfText = [row.split(',') for row in listOfText]
print(f'{abs(-2)=}')

areas = []
for i,row1 in enumerate(listOfText):
    #print(f'{i=} {row1=}')
    for j in range(i+1, len(listOfText)):
        x_1 = int(row1[0])
        y_1 = int(row1[1])
        row2 = listOfText[j]
        x_2 = int(row2[0])
        y_2 = int(row2[1])
        #print(f'{i=} {j=} {(abs(x_1-x_2)+1)=} {(abs(y_1-y_2)+1)=}')
        area = (abs(x_1-x_2)+1)*(abs(y_1-y_2)+1)
        areas.append([area,i,j,row1,row2])
    #print(areas)
areas.sort()
print(areas[-1])
