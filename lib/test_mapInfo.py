import unittest
# import lib.mapInfo as mapInfo
from lib.mapInfo import *


class TestMap(unittest.TestCase):

    def setUp(self):
        self.input1 = '''RL
        
        AAA = (BBB, CCC)
        BBB = (DDD, EEE)
        CCC = (ZZZ, GGG)
        DDD = (DDD, DDD)
        EEE = (EEE, EEE)
        GGG = (GGG, GGG)
        ZZZ = (ZZZ, ZZZ)'''.split('\n')

        self.input2 = '''LLR
        
        AAA = (BBB, BBB)
        BBB = (AAA, ZZZ)
        ZZZ = (ZZZ, ZZZ)'''.split('\n')

    def test_getMapInfo(self):
        actualMap1 = getMapInfo(self.input1)
        expectedMap1 = {'AAA': {'L': 'BBB', 'R': 'CCC'},
                        'BBB': {'L': 'DDD', 'R': 'EEE'},
                        'CCC': {'L': 'ZZZ', 'R': 'GGG'},
                        'DDD': {'L': 'DDD', 'R': 'DDD'},
                        'EEE': {'L': 'EEE', 'R': 'EEE'},
                        'GGG': {'L': 'GGG', 'R': 'GGG'},
                        'ZZZ': {'L': 'ZZZ', 'R': 'ZZZ'},
                        'entryPoint': 'AAA',
                        'exitPoint': 'ZZZ'}
        self.assertEqual(actualMap1, expectedMap1)

    def test_navigateToZZZ(self):
        actualMap1 = getMapInfo(self.input1)
        jumps = navigateToZZZ(self.input1[0], actualMap1)
        self.assertEqual(2, jumps)

    def test_navigateToZZZ_2(self):
        actualMap2 = getMapInfo(self.input2)
        jumps = navigateToZZZ(self.input2[0], actualMap2)
        self.assertEqual(6, jumps)


if __name__ == '__main__':
    unittest.main()
