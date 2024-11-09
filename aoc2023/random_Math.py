import sys
sys.set_int_max_str_digits(10000)
answer=1
for i in range(1,26):
    answer= answer*i
    print('i',i)
print('answer:', answer)
answer = list(str(answer))
answer.reverse()
print('answer', answer)
for i,value in enumerate(answer):
    if value != '0':
        break
print('counted zeroes:', i)


if False:
    counter = 0
    for i in range(1000,9999):
        a = list(str(i).zfill(4))
        a.reverse()
        a = int(''.join(a))
        if a - i == 4725:
            print(a, '-', i)
            counter += 1

    print('counter', counter)
