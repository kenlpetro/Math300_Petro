from itertools import product
from random import shuffle
import re
import matplotlib.pyplot as plt

suits = ["C","D","H","S"] 
ranks = ["2","3","4","5","4","6","7","8","9","J","Q","K","A"]

pairs = 0
three_of_a_kind = 0
four_of_a_kind = 0

for hands in range(1000):
    cards = list(r + s for r, s in product(ranks, suits))
    shuffle(cards)

    y=cards[0]+cards[1]+cards[2]+cards[3]+cards[4]
    x=re.findall('\d+',y)
    x1=re.findall('A',y)
    x2=re.findall('J',y)
    x3=re.findall('Q',y)
    x4=re.findall('K',y)
    z=x+x1+x2+x3+x4
    
    hand=set(z)
    if len(hand)==4:
            pairs += 1
    elif len(hand)==3:
            three_of_a_kind += 1
    elif len(hand)==2:
            four_of_a_kind += 1
            
print(pairs)
print(three_of_a_kind)
print(four_of_a_kind)

labels = ['Two-of-a-kind', 'Three-of-a-kind', 'Four-of-a-kind']
sizes = [pairs, three_of_a_kind, four_of_a_kind]
plt.ylabel('Number of Pairs')
plt.yscale('log')
plt.bar(labels,sizes)
plt.show()
