import unittest
# import lib.mapInfo as mapInfo
from lib.left_right_mapInfo import *


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

        self.ghostInput = '''LR

            11A = (11B, XXX)
            11B = (XXX, 11Z)
            11Z = (11B, XXX)
            22A = (22B, XXX)
            22B = (22C, 22C)
            22C = (22Z, 22Z)
            22Z = (22B, 22B)
            XXX = (XXX, XXX)'''.split('\n')

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

    def test_ghostNavigate(self):
        actualMap = getMapInfo(self.ghostInput)

        ghostMap = convertMapInfoToGhostEntriesAndExits(actualMap)
        self.assertEqual(['11A', '22A'], ghostMap['entryPoints'])
        self.assertEqual(['11Z', '22Z'], ghostMap['exitPoints'])
        print('ghostMap', ghostMap)

    def test_countGhostNavigate(self):
        actualMap = getMapInfo(self.ghostInput)
        ghostMap = convertMapInfoToGhostEntriesAndExits(actualMap)
        pathsCount = navigateToZ_Ghost(self.ghostInput[0], ghostMap)
        self.assertEqual(6, pathsCount)

    def test_countGhostNavigate_EndlessLoop(self):
        self.ghostInput = '''LRR

            11A = (11B, XXX)
            11B = (XXX, 11E)
            22B = (22C, 22C)
            22C = (22E, 22E)
            22Z = (22B, 22B)
            22A = (22B, 22B)
            22E = (22B, 22B)
            XXX = (XXX, XXX)
            11E = (11E, 11E)'''.split('\n')
        actualMap = getMapInfo(self.ghostInput)
        ghostMap = convertMapInfoToGhostEntriesAndExits(actualMap)
        with self.assertRaises(ValueError) as e:
            pathsCount = navigateToZ_Ghost(self.ghostInput[0], ghostMap, checkUniqueNess=True)
        print(e.exception)

    def test_getfirstHitsAndFrequencies(self):
        self.ghostInput = '''LR

            11A = (11B, XXX)
            11B = (XXX, 11Z)
            11Z = (11B, XXX)
            22A = (22B, XXX)
            22B = (22C, 22C)
            22C = (22Z, 22Z)
            22Z = (22B, 22B)
            XXX = (XXX, XXX)
            33A = (33B, 33B)
            33B = (33C, 33C)
            33C = (33D, 33D)
            33D = (33Z, 33Z)
            33Z = (33A, 33A)
            44A = (44B, 44B)
            44B = (44C, 44C)
            44C = (44D, 44D)
            44D = (44Z, 44Z)
            44Z = (44B, 44B)'''.split('\n')
        actualMap = getMapInfo(self.ghostInput)
        ghostMap = convertMapInfoToGhostEntriesAndExits(actualMap)

        firstHits = getfirstHitsAndFrequencies(self.ghostInput[0], ghostMap)
        self.assertEqual([[2, 4, 6, 8, 10, 12, 14, 16, 18], [3, 6, 9, 12, 15, 18], [4, 9, 14, 19], [4, 8, 12, 16]],
                         firstHits)

        answer = navigateToZ_Ghost(self.ghostInput[0], ghostMap)
        self.assertEqual(24, answer)

    def test_syncTwoCycles_1(self):
        start1 = 2
        start2 = 7
        frequency1 = 4
        frequency2 = 5

        firstHit, frequency = syncTwoCycles(start1, start2, frequency1, frequency2)

        print(firstHit, frequency)
        self.assertEqual(frequency, 20)
        self.assertEqual(22, firstHit)

    def test_syncTwoCycles_2(self):
        start1 = 2
        start2 = 3
        frequency1 = 2
        frequency2 = 3

        firstHit, frequency = syncTwoCycles(start1, start2, frequency1, frequency2)

        print(firstHit, frequency)
        self.assertEqual(6, frequency)
        self.assertEqual(6, firstHit)

    def test_syncTwoCycles_3(self):
        start1 = 3
        start2 = 4
        frequency1 = 3
        frequency2 = 5

        firstHit, frequency = syncTwoCycles(start1, start2, frequency1, frequency2)

        print(firstHit, frequency)
        self.assertEqual(15, frequency)
        self.assertEqual(9, firstHit)

    def test_calculateAnswerFromFirstHits(self):
        firstHits = [[2, 4, 6, 8, 10, 12, 14, 16, 18], [3, 6, 9, 12, 15, 18], [4, 9, 14, 19], [4, 8, 12, 16]]
        syncedNumber, frequency = calculateAnswerFromFirstHits(firstHits)
        self.assertEqual(24, syncedNumber)
        self.assertEqual(60, frequency)

    def testChained(self):
        self.ghostInput = '''LR

            11A = (11B, XXX)
            11B = (XXX, 11Z)
            11Z = (11B, XXX)
            22A = (22B, XXX)
            22B = (22C, 22C)
            22C = (22Z, 22Z)
            22Z = (22B, 22B)
            XXX = (XXX, XXX)
            33A = (33B, 33B)
            33B = (33C, 33C)
            33C = (33D, 33D)
            33D = (33Z, 33Z)
            33Z = (33A, 33A)
            44A = (44B, 44B)
            44B = (44C, 44C)
            44C = (44D, 44D)
            44D = (44Z, 44Z)
            44Z = (44B, 44B)'''.split('\n')
        actualMap = getMapInfo(self.ghostInput)
        ghostMap = convertMapInfoToGhostEntriesAndExits(actualMap)
        firstHits = getfirstHitsAndFrequencies(self.ghostInput[0], ghostMap)
        syncedNumber, frequency = calculateAnswerFromFirstHits(firstHits)
        print('syncedNumber:', syncedNumber)
        self.assertEqual(24, syncedNumber)

if __name__ == '__main__':
    unittest.main()
