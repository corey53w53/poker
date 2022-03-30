import random
from collections import Counter
class Card():
    value_list=[None,None,"Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"]
    suit_list=["Clubs","Hearts","Spades","Diamonds"]
    def __init__(self,value,suit):
        self.value=value
        self.suit=suit
    def __str__(self):
        return Card.value_list[self.value]+" of "+Card.suit_list[self.suit]
class Deck():
    def __init__(self):
        self.deck=[]
        for suit in range(4):
            for value in range(2,15):
                self.deck.append(Card(value,suit))
    def __str__(self):
        all=""
        for card in self.deck:
            all+=str(card)+"\n"
        return all.strip()
    def shuffle(self):
        random.shuffle(self.deck)
    def put(self, pile):
        card=pile.pop()
        self.deck.append(card)
class Hand(Deck):
    def __init__(self, nums, main_deck):
        self.deck=[]
        for counter in range(nums):
            self.deck.append(main_deck.deck.pop())
        self.values=[]
        self.suits=[]
        for card in self.deck:
            self.values.append(card.value)
            self.suits.append(card.suit)
    def is_flush(self):
        suits=self.suits
        suits.sort()
        flush=False
        for value in range(len(suits)-4):
            if suits[value]==suits[value+4]:
                flush=True
        return flush
    def is_straight(self):
        values=self.values
        for start_position in range(len(values)):
            straight_starter_value=True
            value=values[start_position]
            for test_value in [value+1,value+2,value+3,value+4]:
                if test_value not in values:
                    straight_starter_value=False
            if straight_starter_value==True:
                return True
        return False
    def frequencies(self):
        histogram={}
        for value in self.values:
            if value in histogram:
                histogram[value]+=1
            else:
                histogram[value]=1
        frequency=list(histogram.values())
        frequency.sort(reverse=True)
        return frequency

    def classify(self):
        flush=self.is_flush()
        straight=self.is_straight()
        frequency=self.frequencies()
        if flush and straight:
            if 14 in self.values:
                return "Royal Flush"
            else:
                return "Straight Flush"
        elif frequency[0]>=4:
            return "Four of a Kind"
        elif frequency[0]>=3 and frequency[1]>=2:
            return "Full House"
        elif flush:
            return "Flush"
        elif straight:
            return "Straight"
        elif frequency[0]>=3:
            return "Three of a Kind"
        elif frequency[0]>=2 and frequency[1]>=2:
            return "Double Pairs"
        elif frequency[0]>=2:
            return "Pair"
        else:
            return "High Card"
counter=0
classify_hist={}
sims=10000000
while counter<sims:
    main_deck=Deck()
    main_deck.shuffle()
    hand=Hand(5,main_deck)
    result=hand.classify()
    if result in classify_hist:
        classify_hist[result]+=1
    else:
        classify_hist[result]=1
    counter+=1
final_hist=Counter(classify_hist)
for key in final_hist:
    final_hist[key]/=(sims/100)

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
