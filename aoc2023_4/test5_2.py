with open('input6.txt') as handle:
    text=handle.readlines()

text='''Time:      7  15   30
Distance:  9  40  200'''.split('\n')


times = []
distances = []
for i, row in enumerate(text):
    row = row.replace(' ','')
    for j, value in enumerate(row.split(':')[1:]):
        if i == 0:
            times.append(value)
        elif i == 1:
            distances.append(value)

print(times)
print(distances)

speed = 1
wincounts = [0]*len(times)
print(wincounts)

for i, time in enumerate(times):
    time = int(time)
    distanceBaseline = int(distances[i])
    for chargingTime in range(time):
        distance = (time - chargingTime) * chargingTime
        if distance > distanceBaseline:
            wincounts[i] += 1

print(wincounts)
answer = 1
for wincount in wincounts:
    answer = answer * wincount

print(answer)
