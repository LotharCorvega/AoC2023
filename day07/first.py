file = open("input.txt", "r").read()
lines = file.split("\n")

cardValues = {
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "T": 8,
    "J": 9,
    "Q": 10,
    "K": 11,
    "A": 12
}

def getHand(line):
    split = line.split()
    hand = split[0]
    bid = int(split[1])
    
    cardDict = {}
    cardSet = set()
    handStrength = 0
    
    for card in hand:
        handStrength *= len(cardValues)
        handStrength += cardValues[card]
        
        if card in cardDict:
            cardDict[card] += 1
        else:
            cardDict[card] = 1
        
        cardSet.add(card)
    
    handType = -1
    mostCards = 0
    
    for card in cardDict:
        if cardDict[card] > mostCards:
            mostCards = cardDict[card]
    
    if len(cardSet) == 1:    # five of a kind
        handType = 6
    elif len(cardSet) == 2:
        if mostCards == 4:   # four of a kind
            handType = 5
        elif mostCards == 3: # full house
            handType = 4
        else:
            print("error")
            exit()
    elif len(cardSet) == 3:
        if mostCards == 3:   # three of a kind
            handType = 3
        elif mostCards == 2: # two pair
            handType = 2
        else:
            print("error")
            exit()
    elif len(cardSet) == 4:  # one pair
        handType = 1
    elif len(cardSet) == 5:  # high card
        handType = 0
    
    return (handType, handStrength, hand, bid)

hands = sorted([getHand(line) for line in lines])
s = 0

for i in range(len(hands)):
    s += (i + 1) * hands[i][3]

print(s)