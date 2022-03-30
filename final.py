import random
from collections import Counter
class Hand:
    def __init__(self):
        hand=[]
        suits=[]
        values=[]
        while len(hand)!=5:
            card=(random.randint(0,3),random.randint(1,13))
            if card not in hand:
                hand.append(card)
                suits.append(card[0])
                values.append(card[1])
        suits.sort()
        values.sort()
        self.suits=suits
        self.values=values
        self.hand=hand
    def is_straight(self):
        values=self.values
        if values[0]==1 and values[1]==10 and values[2]==11 and values[3]==12 and values[4]==13:
            return True
        value=values[0]
        for x in range(1,5):
            if value+x!=values[x]:
                return False
        return True
    def classify(self):
        flush=self.suits[0]==self.suits[4]
        straight=self.is_straight()
        frequency=list(Counter(self.values).values())
        frequency.sort(reverse=True)
        if flush and straight and 1 in self.values and 10 in self.values: return "Royal Flush"
        elif flush and straight: return "Straight Flush"
        elif frequency[0]==4: return "Four of a Kind"
        elif frequency[0]==3 and frequency[1]==2: return "Full House"
        elif flush: return "Flush"
        elif straight: return "Straight"
        elif frequency[0]==3: return "Three of a Kind"
        elif frequency[0]==2 and frequency[1]==2: return "Double Pairs"
        elif frequency[0]==2: return "Pair"
        else: return "High Card"
sims=100000
classify_hist={}
for x in range(sims):
    hand=Hand()
    result=hand.classify()
    if result in classify_hist: classify_hist[result]+=1
    else: classify_hist[result]=1
print(classify_hist)

final_hist=Counter(classify_hist)
for key in final_hist: final_hist[key]/=(sims/100)
print("High Card: " + str(final_hist["High Card"]))
print("Pair: " + str(final_hist["Pair"]))
print("Double Pairs: " + str(final_hist["Double Pairs"]))
print("Three of a Kind: " + str(final_hist["Three of a Kind"]))
print("Straight: " + str(final_hist["Straight"]))
print("Flush: " + str(final_hist["Flush"]))
print("Full House: " + str(final_hist["Full House"]))
print("Four of a Kind: " + str(final_hist["Four of a Kind"]))
print("Straight Flush: " + str(final_hist["Straight Flush"]))
print("Royal Flush: " + str(final_hist["Royal Flush"]))