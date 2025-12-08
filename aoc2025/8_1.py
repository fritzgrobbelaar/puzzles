import cleaninput
from datetime import datetime
from functools import cmp_to_key
import math
listOfText = cleaninput.getfileInputLinesAsList('input_8.txt')

sample='''162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689'''.split('\n')

#listOfText = sample
listOfText = [row.split(',') for row in listOfText]

distances = []
for i,row1 in enumerate(listOfText):
    #print(f'{i=} {row1=}')
    for j in range(i+1, len(listOfText)):
        x_1 = int(row1[0])
        y_1 = int(row1[1])
        z_1 = int(row1[2])
        row2 = listOfText[j]
        x_2 = int(row2[0])
        y_2 = int(row2[1])
        z_2 = int(row2[2])
        distance = round(math.sqrt((x_1-x_2)**2+(y_1-y_2)**2+(z_1-z_2)**2),2)
        distances.append((distance,i,j))
distances.sort()

circuits = []
counter = 1
for distance in distances:
    #print(f'{distance=}')
    i=distance[1]
    j=distance[2]
    i_circuit = None
    j_circuit = None
    for z,circuit in enumerate(circuits):
       # print(f'checking {i=}  in {circuit=}')
        if i in circuit:
            if i_circuit:
                raise Exception('this is unexpected i is already in a circuit')
            i_circuit=z
         #   print(f'{i_circuit=}')
        if j in circuit:
            if j_circuit:
                raise Exception('this is unexpected j is already in a circuit')
            j_circuit=z
    if i_circuit == None and j_circuit == None:
        circuits.append({i,j})
        counter+=1
       # print('nothing found')
    elif i_circuit == j_circuit:
       # print('pass')
        pass
        counter +=1 
    elif i_circuit is not None and j_circuit is  None:
        counter+=1
        circuits[i_circuit].add(j)
       # print('added j')
    elif j_circuit is not None and  i_circuit is  None:
        counter+=1
        circuits[j_circuit].add(i)
     #   print('added i')
    elif i_circuit != j_circuit:
        #print(f'{i_circuit=} and {j_circuit=}')
        counter+=1
        newCircuits = []
        for z,circuit in enumerate(circuits):
            if z == i_circuit or z == j_circuit:
                pass
            else:
                newCircuits.append(circuit)
        print('last length', len(circuits[i_circuit]) *len(circuits[j_circuit]))
        newCircuits.append(circuits[i_circuit] | circuits[j_circuit])
        circuits = newCircuits
    if counter == 1000:
        print(f'breaking {circuits=}')
        break
lenCircuits = []
for circuit in circuits:
    lenCircuits.append(len(circuit))
lenCircuits.sort()
lenCircuits = list(reversed(lenCircuits))

print(f'{lenCircuits=}')


answer = lenCircuits[0]*lenCircuits[1]*lenCircuits[2]
print(lenCircuits, lenCircuits[0], lenCircuits[0]*lenCircuits[1]*lenCircuits[2])
print('-- the end -- {answer=}')
#0 is wrong
#1000 is too low

