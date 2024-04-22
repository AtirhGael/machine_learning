import random

suit = ['Heart',"spades","clubs","diamond"]
cards =[]
ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]



for suits in suit:
    for rank in ranks:
        cards.append([suits,rank])

random.shuffle(cards)
card = cards.pop()
print(card)