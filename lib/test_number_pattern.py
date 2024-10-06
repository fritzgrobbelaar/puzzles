from number_pattern import extrapolatePattern, buildNumberPyramid

input = [0, 3, 6, 9, 12, 15]
assert buildNumberPyramid(input) == [[0, 3, 6, 9, 12, 15],
                                     [3, 3, 3, 3, 3],
                                     [0, 0, 0, 0]]
print('success 1')
input = [1, 3, 6, 10, 15, 21]

assert buildNumberPyramid(input) == [[1, 3, 6, 10, 15, 21],
                                     [2, 3, 4, 5, 6],
                                     [1, 1, 1, 1],
                                     [0, 0, 0]]
print('success 2')
input = [10, 13, 16, 21, 30, 45]

assert buildNumberPyramid(input) == [
    [10, 13, 16, 21, 30, 45],
    [3, 3, 5, 9, 15],
    [0, 2, 4, 6],
    [2, 2, 2],
    [0, 0]]
print('success 3')

input = [0, 3, 6, 9, 12, 15]

assert extrapolatePattern(input) == 18
print('success')

assert extrapolatePattern([1, 3, 6, 10, 15, 21]) == 28
print('success28')

assert extrapolatePattern( [10, 13, 16, 21, 30, 45]) == 68
print('success68')


#, [1, 3, 6, 10, 15, 21], [10, 13, 16, 21, 30, 45]]
