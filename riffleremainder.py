import random

remaindertally = 0

for i in range(10000):
    deck1 = 26
    deck2 = 26
    while deck1 > 0 and deck2 > 0:
        randomdeck = random.randint(1,2)
        if randomdeck == 1:
            deck1 -= 1
        else:
            deck2 -= 1
    remainder = max(deck1,deck2)
    remaindertally+= remainder

print(remaindertally)