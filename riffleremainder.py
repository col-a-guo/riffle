import random
   
from scipy.stats import binom   
remaindertally = 0
n = 52
p = 0.5
r_values = list(range(n + 1)) 
dist = [binom.pmf(r, n, p) for r in r_values]


for i in range(10000):
    
    dist_rand = random.uniform(0,1)
    dist_marker = 0
    deck1 = 0
    for i, prob in enumerate(dist):
        dist_marker += prob
        if dist_rand < dist_marker:
            deck1 = i
            break
    deck2 = 52-deck1
    while deck1 > 0 and deck2 > 0:
        randomdeck = random.randint(1,2)
        if randomdeck == 1:
            deck1 -= 1
        else:
            deck2 -= 1
    remainder = max(deck1,deck2)
    remaindertally+= remainder

print(remaindertally)