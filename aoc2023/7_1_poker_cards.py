with open('input7.txt') as handle:
    text=handle.readlines()

text_='''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''.split('\n')

hands = []
bids = []
handsBids = {}
for i, row in enumerate(text):
    print ('splitting', row)
    hand, bid = row.split(' ')
    hands.append(hand)
    bids.append(bid)
    handsBids[hand] = bid

print('hands:', hands)
print('bids:', bids)

def profileCards(hand):
    dictOfCards = {}
    for card in list(hand):
        if card not in dictOfCards.keys():
            dictOfCards[card] = 0
        dictOfCards[card] += 1
    listOfDictOfCards = []
    for i in range(5, 0, -1):
        for key in dictOfCards.keys():
            if dictOfCards[key] == i:
                listOfDictOfCards.append({key: dictOfCards[key]})
    return listOfDictOfCards

assert [{'A':4}, {'B':1}] == profileCards('AAABA') 
assert [{'A':3}, {'C':1}, {'B':1}] == profileCards('ACABA') 


def isThereFiveOfAKind(hand):
    cards = list(hand)
    if len(set(cards)) == 1:
        return True
    return False

assert True == isThereFiveOfAKind('AAAAA')
assert False == isThereFiveOfAKind('AABBA')


def isThereFourOfAKind(hand):
    cards = list(hand)
    if len(set(cards)) != 2:
        return False
    cardsByCount = profileCards(hand)
    print('cardsByCount', list(cardsByCount[0].values()))
    if list(cardsByCount[0].values()) == [4]:
        return True
    return False

assert True == isThereFourOfAKind('AAAAB')
assert False == isThereFourOfAKind('AABBA')

def isThereFullHouse(hand):
    cards = list(hand)
    if len(set(cards)) == 2:
        return True
    return False

assert True == isThereFullHouse('AABBA')
assert False == isThereFullHouse('ACBBA')

def isThereThreeOfAKind(hand):
    cardsByCount = profileCards(hand)
    if list(cardsByCount[0].values()) == [3]:
        return True
    return False

assert True == isThereThreeOfAKind('AACBA')
assert False == isThereThreeOfAKind('ACBBA')

def isThereTwoPair(hand):
    cardsByCount = profileCards(hand)
    if list(cardsByCount[0].values()) == [2] and list(cardsByCount[1].values() )== [2]:
        return True
    return False

assert True == isThereTwoPair('ACCBA')
assert False == isThereTwoPair('ACB3A')

def isThereOnePair(hand):
    cardsByCount = profileCards(hand)
    if list(cardsByCount[0].values()) == [2]:
        return True
    return False

assert True == isThereOnePair('ACDBA')
assert False == isThereOnePair('ACB34')

def rankCards():
    cards = 'AKQJT98765432'
    cardsOrder = {}
    for i, value in enumerate(cards):
        cardsOrder[value] = i
    return cardsOrder

cardsOrder = rankCards() # 1 beats 10

def firstWinsSecondOrderRule(first, second):
    for i, valueOne in enumerate(first):
        valueTwo = second[i]
        if cardsOrder[valueOne] < cardsOrder[valueTwo]:
            print(f'{first=} beats {second=} secondOrderRule')
            return 1
        elif cardsOrder[valueOne] > cardsOrder[valueTwo]:
            print(f'{second=} beats {first=} secondOrderRule')
            return -1

assert 1  == firstWinsSecondOrderRule('AAAAA', 'KKKKK')
assert -1  == firstWinsSecondOrderRule('KKKKK', 'AAAAA')


def doesFirstRankHigher(first, second):
    methodList = [isThereFiveOfAKind, isThereFourOfAKind, isThereFullHouse, isThereThreeOfAKind,
                  isThereTwoPair, isThereOnePair]

    for method in methodList:
        check = method(first)
        check2 = method(second)
        if check and not check2:
            print(f'{first=} beats {second=} {method.__name__=}')
            return 1
        elif check2 and not check:
            print(f'{second=} beats {first=} {method.__name__=}')
            return -1
        if check and check2:
            return firstWinsSecondOrderRule(first, second)
    return firstWinsSecondOrderRule(first, second)

print('---- does firs rank higher ---')
assert 1  == doesFirstRankHigher('AAAAA', 'KKKKK')
assert 1  == doesFirstRankHigher('AAA2A', '443KK')
assert -1 == doesFirstRankHigher('AACAA', 'KKKKK')
assert 1  == doesFirstRankHigher('AA543', 'K3456')
assert 1  == doesFirstRankHigher('A4837', 'K5432')

print ('\n ---- Start the test --- ')
from functools import cmp_to_key
print('hands: ', hands)
sortedHands = sorted(hands, key=cmp_to_key(doesFirstRankHigher))

print('sorted hands', sortedHands)
answer = 0
for i, value in enumerate(sortedHands):
    rank = i+1
    bid = handsBids[value]
    answer += rank*int(bid)
print('answer:', answer)
