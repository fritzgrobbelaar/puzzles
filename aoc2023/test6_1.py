Python 3.12.6 (v3.12.6:a4a2d2b0d85, Sep  6 2024, 16:08:03) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

================================================================= RESTART: /Users/fritzgrobbelaar/Documents/Advent of Code/test5_2.py ================================================================
row: seed-to-soil map:
row: 50 98 2
row: 52 50 48
row: 
row: 
row: soil-to-fertilizer map:
row: 0 15 37
row: 37 52 2
row: 39 0 15
row: 
row: 
row: fertilizer-to-water map:
row: 49 53 8
row: 0 11 42
row: 42 0 7
row: 57 7 4
row: 
row: 
row: water-to-light map:
row: 88 18 7
row: 18 25 70
row: 
row: 
row: light-to-temperature map:
row: 45 77 23
row: 81 45 19
row: 68 64 13
row: 
row: 
row: temperature-to-humidity map:
row: 0 69 1
row: 1 0 69
row: 
row: 
row: humidity-to-location map:
row: 60 56 37
row: 56 93 4
[]

================================================================= RESTART: /Users/fritzgrobbelaar/Documents/Advent of Code/test5_2.py ================================================================
row: seed-to-soil map:
row: 50 98 2
row: 52 50 48
row: 
row: 
row: soil-to-fertilizer map:
row: 0 15 37
row: 37 52 2
row: 39 0 15
row: 
row: 
row: fertilizer-to-water map:
row: 49 53 8
row: 0 11 42
row: 42 0 7
row: 57 7 4
row: 
row: 
row: water-to-light map:
row: 88 18 7
row: 18 25 70
row: 
row: 
row: light-to-temperature map:
row: 45 77 23
row: 81 45 19
row: 68 64 13
row: 
row: 
row: temperature-to-humidity map:
row: 0 69 1
row: 1 0 69
row: 
row: 
row: humidity-to-location map:
row: 60 56 37
row: 56 93 4
seeds []

====== RESTART: /Users/fritzgrobbelaar/Documents/Advent of Code/test5_2.py =====
row: seed-to-soil map:
row: 50 98 2
row: 52 50 48
row: 
row: 
row: soil-to-fertilizer map:
row: 0 15 37
row: 37 52 2
row: 39 0 15
row: 
row: 
row: fertilizer-to-water map:
row: 49 53 8
row: 0 11 42
row: 42 0 7
row: 57 7 4
row: 
row: 
row: water-to-light map:
row: 88 18 7
row: 18 25 70
row: 
row: 
row: light-to-temperature map:
row: 45 77 23
row: 81 45 19
row: 68 64 13
row: 
row: 
row: temperature-to-humidity map:
row: 0 69 1
row: 1 0 69
row: 
row: 
row: humidity-to-location map:
row: 60 56 37
row: 56 93 4
seeds []
{'seed-to-soil': {'destinationStart': [50, 52], 'sourceStart': [98, 50], 'range': [2, 48]}, 'soil-to-fertilizer': {'destinationStart': [0, 37, 39], 'sourceStart': [15, 52, 0], 'range': [37, 2, 15]}, 'fertilizer-to-water': {'destinationStart': [49, 0, 42, 57], 'sourceStart': [53, 11, 0, 7], 'range': [8, 42, 7, 4]}, 'water-to-light': {'destinationStart': [88, 18], 'sourceStart': [18, 25], 'range': [7, 70]}, 'light-to-temperature': {'destinationStart': [45, 81, 68], 'sourceStart': [77, 45, 64], 'range': [23, 19, 13]}, 'temperature-to-humidity': {'destinationStart': [0, 1], 'sourceStart': [69, 0], 'range': [1, 69]}, 'humidity-to-location': {'destinationStart': [60, 56], 'sourceStart': [56, 93], 'range': [37, 4]}}
['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
lowestLocation: 9999999999999

============= RESTART: /Users/fritzgrobbelaar/Documents/Advent of Code/test5_2.py ============
row: seed-to-soil map:
row: 50 98 2
row: 52 50 48
row: 
row: 
row: soil-to-fertilizer map:
row: 0 15 37
row: 37 52 2
row: 39 0 15
row: 
row: 
row: fertilizer-to-water map:
row: 49 53 8
row: 0 11 42
row: 42 0 7
row: 57 7 4
row: 
row: 
row: water-to-light map:
row: 88 18 7
row: 18 25 70
row: 
row: 
row: light-to-temperature map:
row: 45 77 23
row: 81 45 19
row: 68 64 13
row: 
row: 
row: temperature-to-humidity map:
row: 0 69 1
row: 1 0 69
row: 
row: 
row: humidity-to-location map:
row: 60 56 37
row: 56 93 4
seedList ['79', '14', '55', '13']
seeds []
{'seed-to-soil': {'destinationStart': [50, 52], 'sourceStart': [98, 50], 'range': [2, 48]}, 'soil-to-fertilizer': {'destinationStart': [0, 37, 39], 'sourceStart': [15, 52, 0], 'range': [37, 2, 15]}, 'fertilizer-to-water': {'destinationStart': [49, 0, 42, 57], 'sourceStart': [53, 11, 0, 7], 'range': [8, 42, 7, 4]}, 'water-to-light': {'destinationStart': [88, 18], 'sourceStart': [18, 25], 'range': [7, 70]}, 'light-to-temperature': {'destinationStart': [45, 81, 68], 'sourceStart': [77, 45, 64], 'range': [23, 19, 13]}, 'temperature-to-humidity': {'destinationStart': [0, 1], 'sourceStart': [69, 0], 'range': [1, 69]}, 'humidity-to-location': {'destinationStart': [60, 56], 'sourceStart': [56, 93], 'range': [37, 4]}}
['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
lowestLocation: 9999999999999

============= RESTART: /Users/fritzgrobbelaar/Documents/Advent of Code/test5_2.py ============
row: seed-to-soil map:
row: 50 98 2
row: 52 50 48
row: 
row: 
row: soil-to-fertilizer map:
row: 0 15 37
row: 37 52 2
row: 39 0 15
row: 
row: 
row: fertilizer-to-water map:
row: 49 53 8
row: 0 11 42
row: 42 0 7
row: 57 7 4
row: 
row: 
row: water-to-light map:
row: 88 18 7
row: 18 25 70
row: 
row: 
row: light-to-temperature map:
row: 45 77 23
row: 81 45 19
row: 68 64 13
row: 
row: 
row: temperature-to-humidity map:
row: 0 69 1
row: 1 0 69
row: 
row: 
row: humidity-to-location map:
row: 60 56 37
row: 56 93 4
seedList ['79', '14', '55', '13']
seeds []
{'seed-to-soil': {'destinationStart': [50, 52], 'sourceStart': [98, 50], 'range': [2, 48]}, 'soil-to-fertilizer': {'destinationStart': [0, 37, 39], 'sourceStart': [15, 52, 0], 'range': [37, 2, 15]}, 'fertilizer-to-water': {'destinationStart': [49, 0, 42, 57], 'sourceStart': [53, 11, 0, 7], 'range': [8, 42, 7, 4]}, 'water-to-light': {'destinationStart': [88, 18], 'sourceStart': [18, 25], 'range': [7, 70]}, 'light-to-temperature': {'destinationStart': [45, 81, 68], 'sourceStart': [77, 45, 64], 'range': [23, 19, 13]}, 'temperature-to-humidity': {'destinationStart': [0, 1], 'sourceStart': [69, 0], 'range': [1, 69]}, 'humidity-to-location': {'destinationStart': [60, 56], 'sourceStart': [56, 93], 'range': [37, 4]}}
['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
lowestLocation: 9999999999999

============= RESTART: /Users/fritzgrobbelaar/Documents/Advent of Code/test5_2.py ============
row: seed-to-soil map:
row: 50 98 2
row: 52 50 48
row: 
row: 
row: soil-to-fertilizer map:
row: 0 15 37
row: 37 52 2
row: 39 0 15
row: 
row: 
row: fertilizer-to-water map:
row: 49 53 8
row: 0 11 42
row: 42 0 7
row: 57 7 4
row: 
row: 
row: water-to-light map:
row: 88 18 7
row: 18 25 70
row: 
row: 
row: light-to-temperature map:
row: 45 77 23
row: 81 45 19
row: 68 64 13
row: 
row: 
row: temperature-to-humidity map:
row: 0 69 1
row: 1 0 69
row: 
row: 
row: humidity-to-location map:
row: 60 56 37
row: 56 93 4
seedList ['79', '14', '55', '13']
entered for loop
Traceback (most recent call last):
  File "/Users/fritzgrobbelaar/Documents/Advent of Code/test5_2.py", line 66, in <module>
    seeds.append(seedList[i],seedList[i+1])
TypeError: list.append() takes exactly one argument (2 given)

============= RESTART: /Users/fritzgrobbelaar/Documents/Advent of Code/test5_2.py ============
row: seed-to-soil map:
row: 50 98 2
row: 52 50 48
row: 
row: 
row: soil-to-fertilizer map:
row: 0 15 37
row: 37 52 2
row: 39 0 15
row: 
row: 
row: fertilizer-to-water map:
row: 49 53 8
row: 0 11 42
row: 42 0 7
row: 57 7 4
row: 
row: 
row: water-to-light map:
row: 88 18 7
row: 18 25 70
row: 
row: 
row: light-to-temperature map:
row: 45 77 23
row: 81 45 19
row: 68 64 13
row: 
row: 
row: temperature-to-humidity map:
row: 0 69 1
row: 1 0 69
row: 
row: 
row: humidity-to-location map:
row: 60 56 37
row: 56 93 4
seedList ['79', '14', '55', '13']
entered for loop
Traceback (most recent call last):
  File "/Users/fritzgrobbelaar/Documents/Advent of Code/test5_2.py", line 66, in <module>
    seeds.append(seedList[i],seedList[i+1])
TypeError: list.append() takes exactly one argument (2 given)

============= RESTART: /Users/fritzgrobbelaar/Documents/Advent of Code/test5_2.py ============
row: seed-to-soil map:
row: 50 98 2
row: 52 50 48
row: 
row: 
row: soil-to-fertilizer map:
row: 0 15 37
row: 37 52 2
row: 39 0 15
row: 
row: 
row: fertilizer-to-water map:
row: 49 53 8
row: 0 11 42
row: 42 0 7
row: 57 7 4
row: 
row: 
row: water-to-light map:
row: 88 18 7
row: 18 25 70
row: 
row: 
row: light-to-temperature map:
row: 45 77 23
row: 81 45 19
row: 68 64 13
row: 
row: 
row: temperature-to-humidity map:
row: 0 69 1
row: 1 0 69
row: 
row: 
row: humidity-to-location map:
row: 60 56 37
row: 56 93 4
seedList ['79', '14', '55', '13']
entered for loop
entered for loop
seeds [['79', '14'], ['55', '13']]
Traceback (most recent call last):
  File "/Users/fritzgrobbelaar/Documents/Advent of Code/test5_2.py", line 70, in <module>
    origin = int(seed)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
>>> 
============= RESTART: /Users/fritzgrobbelaar/Documents/Advent of Code/test5_2.py ============
row: seed-to-soil map:
row: 50 98 2
row: 52 50 48
row: 
row: 
row: soil-to-fertilizer map:
row: 0 15 37
row: 37 52 2
row: 39 0 15
row: 
row: 
row: fertilizer-to-water map:
row: 49 53 8
row: 0 11 42
row: 42 0 7
row: 57 7 4
row: 
row: 
row: water-to-light map:
row: 88 18 7
row: 18 25 70
row: 
row: 
row: light-to-temperature map:
row: 45 77 23
row: 81 45 19
row: 68 64 13
row: 
row: 
row: temperature-to-humidity map:
row: 0 69 1
row: 1 0 69
row: 
row: 
row: humidity-to-location map:
row: 60 56 37
row: 56 93 4
seedList ['79', '14', '55', '13']
entered for loop
entered for loop
seeds [('79', '14'), ('55', '13')]
Traceback (most recent call last):
  File "/Users/fritzgrobbelaar/Documents/Advent of Code/test5_2.py", line 70, in <module>
    origin = int(seed)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
>>> 
============= RESTART: /Users/fritzgrobbelaar/Documents/Advent of Code/test5_2.py ============
row: seed-to-soil map:
row: 50 98 2
row: 52 50 48
row: 
row: 
row: soil-to-fertilizer map:
row: 0 15 37
row: 37 52 2
row: 39 0 15
row: 
row: 
row: fertilizer-to-water map:
row: 49 53 8
row: 0 11 42
row: 42 0 7
row: 57 7 4
row: 
row: 
row: water-to-light map:
row: 88 18 7
row: 18 25 70
row: 
row: 
row: light-to-temperature map:
row: 45 77 23
row: 81 45 19
row: 68 64 13
row: 
row: 
row: temperature-to-humidity map:
row: 0 69 1
row: 1 0 69
row: 
row: 
row: humidity-to-location map:
row: 60 56 37
row: 56 93 4
seedList ['79', '14', '55', '13']
entered for loop
entered for loop
seeds [('79', '14'), ('55', '13')]
seed: ('79', '14')
adding destination found mapName='seed-to-soil' origin=79, sourceStart=50 rangeEnv=48  seed-to-soil 79
new origin: 81
not found - keeping mapName='soil-to-fertilizer' origin=81, sourceStart=0 rangeEnv=15
not found - keeping mapName='fertilizer-to-water' origin=81, sourceStart=7 rangeEnv=4
adding destination found mapName='water-to-light' origin=81, sourceStart=25 rangeEnv=70  water-to-light 81
new origin: 74
adding destination found mapName='light-to-temperature' origin=74, sourceStart=64 rangeEnv=13  light-to-temperature 74
new origin: 78
not found - keeping mapName='temperature-to-humidity' origin=78, sourceStart=0 rangeEnv=69
adding destination found mapName='humidity-to-location' origin=78, sourceStart=56 rangeEnv=37  humidity-to-location 78
new origin: 82
seed: ('55', '13')
adding destination found mapName='seed-to-soil' origin=55, sourceStart=50 rangeEnv=48  seed-to-soil 55
new origin: 57
not found - keeping mapName='soil-to-fertilizer' origin=57, sourceStart=0 rangeEnv=15
adding destination found mapName='fertilizer-to-water' origin=57, sourceStart=53 rangeEnv=8  fertilizer-to-water 57
new origin: 53
adding destination found mapName='water-to-light' origin=53, sourceStart=25 rangeEnv=70  water-to-light 53
new origin: 46
adding destination found mapName='light-to-temperature' origin=46, sourceStart=45 rangeEnv=19  light-to-temperature 46
new origin: 82
not found - keeping mapName='temperature-to-humidity' origin=82, sourceStart=0 rangeEnv=69
adding destination found mapName='humidity-to-location' origin=82, sourceStart=56 rangeEnv=37  humidity-to-location 82
new origin: 86
{'seed-to-soil': {'destinationStart': [50, 52], 'sourceStart': [98, 50], 'range': [2, 48]}, 'soil-to-fertilizer': {'destinationStart': [0, 37, 39], 'sourceStart': [15, 52, 0], 'range': [37, 2, 15]}, 'fertilizer-to-water': {'destinationStart': [49, 0, 42, 57], 'sourceStart': [53, 11, 0, 7], 'range': [8, 42, 7, 4]}, 'water-to-light': {'destinationStart': [88, 18], 'sourceStart': [18, 25], 'range': [7, 70]}, 'light-to-temperature': {'destinationStart': [45, 81, 68], 'sourceStart': [77, 45, 64], 'range': [23, 19, 13]}, 'temperature-to-humidity': {'destinationStart': [0, 1], 'sourceStart': [69, 0], 'range': [1, 69]}, 'humidity-to-location': {'destinationStart': [60, 56], 'sourceStart': [56, 93], 'range': [37, 4]}}
['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
lowestLocation: 82

============= RESTART: /Users/fritzgrobbelaar/Documents/Advent of Code/test5_2.py ============
row: seed-to-soil map:
row: 50 98 2
row: 52 50 48
row: 
row: 
row: soil-to-fertilizer map:
row: 0 15 37
row: 37 52 2
row: 39 0 15
row: 
row: 
row: fertilizer-to-water map:
row: 49 53 8
row: 0 11 42
row: 42 0 7
row: 57 7 4
row: 
row: 
row: water-to-light map:
row: 88 18 7
row: 18 25 70
row: 
row: 
row: light-to-temperature map:
row: 45 77 23
row: 81 45 19
row: 68 64 13
row: 
row: 
row: temperature-to-humidity map:
row: 0 69 1
row: 1 0 69
row: 
row: 
row: humidity-to-location map:
row: 60 56 37
row: 56 93 4
seedList ['79', '14', '55', '13']
entered for loop
entered for loop
seeds [('79', '14'), ('55', '13')]
seed: (79, 0)
adding destination found mapName='seed-to-soil' origin=79, sourceStart=50 rangeEnv=48  seed-to-soil 79
new origin: 81
not found - keeping mapName='soil-to-fertilizer' origin=81, sourceStart=0 rangeEnv=15
not found - keeping mapName='fertilizer-to-water' origin=81, sourceStart=7 rangeEnv=4
adding destination found mapName='water-to-light' origin=81, sourceStart=25 rangeEnv=70  water-to-light 81
new origin: 74
adding destination found mapName='light-to-temperature' origin=74, sourceStart=64 rangeEnv=13  light-to-temperature 74
new origin: 78
not found - keeping mapName='temperature-to-humidity' origin=78, sourceStart=0 rangeEnv=69
adding destination found mapName='humidity-to-location' origin=78, sourceStart=56 rangeEnv=37  humidity-to-location 78
new origin: 82
seed: (14, 0)
not found - keeping mapName='seed-to-soil' origin=14, sourceStart=50 rangeEnv=48
adding destination found mapName='soil-to-fertilizer' origin=14, sourceStart=0 rangeEnv=15  soil-to-fertilizer 14
new origin: 53
adding destination found mapName='fertilizer-to-water' origin=53, sourceStart=53 rangeEnv=8  fertilizer-to-water 53
new origin: 49
adding destination found mapName='water-to-light' origin=49, sourceStart=25 rangeEnv=70  water-to-light 49
new origin: 42
not found - keeping mapName='light-to-temperature' origin=42, sourceStart=64 rangeEnv=13
adding destination found mapName='temperature-to-humidity' origin=42, sourceStart=0 rangeEnv=69  temperature-to-humidity 42
new origin: 43
not found - keeping mapName='humidity-to-location' origin=43, sourceStart=93 rangeEnv=4
seed: (55, 0)
adding destination found mapName='seed-to-soil' origin=55, sourceStart=50 rangeEnv=48  seed-to-soil 55
new origin: 57
not found - keeping mapName='soil-to-fertilizer' origin=57, sourceStart=0 rangeEnv=15
adding destination found mapName='fertilizer-to-water' origin=57, sourceStart=53 rangeEnv=8  fertilizer-to-water 57
new origin: 53
adding destination found mapName='water-to-light' origin=53, sourceStart=25 rangeEnv=70  water-to-light 53
new origin: 46
adding destination found mapName='light-to-temperature' origin=46, sourceStart=45 rangeEnv=19  light-to-temperature 46
new origin: 82
not found - keeping mapName='temperature-to-humidity' origin=82, sourceStart=0 rangeEnv=69
adding destination found mapName='humidity-to-location' origin=82, sourceStart=56 rangeEnv=37  humidity-to-location 82
new origin: 86
seed: (13, 0)
not found - keeping mapName='seed-to-soil' origin=13, sourceStart=50 rangeEnv=48
adding destination found mapName='soil-to-fertilizer' origin=13, sourceStart=0 rangeEnv=15  soil-to-fertilizer 13
new origin: 52
adding destination found mapName='fertilizer-to-water' origin=52, sourceStart=11 rangeEnv=42  fertilizer-to-water 52
new origin: 41
adding destination found mapName='water-to-light' origin=41, sourceStart=25 rangeEnv=70  water-to-light 41
new origin: 34
not found - keeping mapName='light-to-temperature' origin=34, sourceStart=64 rangeEnv=13
adding destination found mapName='temperature-to-humidity' origin=34, sourceStart=0 rangeEnv=69  temperature-to-humidity 34
new origin: 35
not found - keeping mapName='humidity-to-location' origin=35, sourceStart=93 rangeEnv=4
{'seed-to-soil': {'destinationStart': [50, 52], 'sourceStart': [98, 50], 'range': [2, 48]}, 'soil-to-fertilizer': {'destinationStart': [0, 37, 39], 'sourceStart': [15, 52, 0], 'range': [37, 2, 15]}, 'fertilizer-to-water': {'destinationStart': [49, 0, 42, 57], 'sourceStart': [53, 11, 0, 7], 'range': [8, 42, 7, 4]}, 'water-to-light': {'destinationStart': [88, 18], 'sourceStart': [18, 25], 'range': [7, 70]}, 'light-to-temperature': {'destinationStart': [45, 81, 68], 'sourceStart': [77, 45, 64], 'range': [23, 19, 13]}, 'temperature-to-humidity': {'destinationStart': [0, 1], 'sourceStart': [69, 0], 'range': [1, 69]}, 'humidity-to-location': {'destinationStart': [60, 56], 'sourceStart': [56, 93], 'range': [37, 4]}}
['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
lowestLocation: 35

================================================================= RESTART: /Users/fritzgrobbelaar/Documents/Advent of Code/test5_2.py ================================================================
row: seed-to-soil map:
row: 50 98 2
row: 52 50 48
row: 
row: 
row: soil-to-fertilizer map:
row: 0 15 37
row: 37 52 2
row: 39 0 15
row: 
row: 
row: fertilizer-to-water map:
row: 49 53 8
row: 0 11 42
row: 42 0 7
row: 57 7 4
row: 
row: 
row: water-to-light map:
row: 88 18 7
row: 18 25 70
row: 
row: 
row: light-to-temperature map:
row: 45 77 23
row: 81 45 19
row: 68 64 13
row: 
row: 
row: temperature-to-humidity map:
row: 0 69 1
row: 1 0 69
row: 
row: 
row: humidity-to-location map:
row: 60 56 37
row: 56 93 4
seedList ['79', '14', '55', '13']
entered for loop
entered for loop
seeds [('79', '14'), ('55', '13')]
Traceback (most recent call last):
  File "/Users/fritzgrobbelaar/Documents/Advent of Code/test5_2.py", line 73, in <module>
    originEnd = origin + seed[1]
TypeError: unsupported operand type(s) for +: 'int' and 'str'
