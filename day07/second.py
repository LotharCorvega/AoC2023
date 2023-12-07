file = open("input.txt", "r").read()
lines = file.split("\n")

cardValues = {
    "J": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "Q": 10,
    "K": 11,
    "A": 12
}

def getHand(line):
    split = line.split()
    hand = split[0]
    bid = int(split[1])
    
    if hand == "JJJJJ":
        return (6, 0, bid)
    
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
        
        if card != "J":
            cardSet.add(card)
    
    handType = -1
    mostCards = 0
    
    for card in cardDict:
        if card != "J" and cardDict[card] > mostCards:
            mostCards = cardDict[card]
    
    if "J" in cardDict:
        mostCards += cardDict["J"]
    
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
    
    return (handType, handStrength, bid)

hands = sorted([getHand(line) for line in lines])
s = 0

for i in range(len(hands)):
    s += (i + 1) * hands[i][2]

print(s)