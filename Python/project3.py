from itertools import product
from random import shuffle
import re

suits = ["C","D","H","S"] 
ranks = ["2","3","4","5","4","6","7","8","9","J","Q","K","A"]


for hands in range(500):
    cards = list(r + s for r, s in product(ranks, suits))
    shuffle(cards)

#print(cards[:5], cards[5:10])
    y=cards[0]+cards[1]+cards[2]+cards[3]+cards[4]
    x=re.findall('\d+',y)
    x1=re.findall('A',y)
    x2=re.findall('J',y)
    x3=re.findall('Q',y)
    x4=re.findall('K',y)
    z=x+x1+x2+x3+x4
    print(z)  
    cA=z.count('A')
    c2=z.count('2')
    c3=z.count('3')
    c4=z.count('4')
    c5=z.count('5')
    c6=z.count('6')
    c7=z.count('7')
    c8=z.count('8')
    c9=z.count('9')
    c10=z.count('10')
    cJ=z.count('J')
    cQ=z.count('Q')
    cK=z.count('K')

    pairs = 0
    three_of_a_kind = 0
    four_of_a_kind = 0
    if cK ==2:
            pairs+=1
    elif cK ==3:
            three_of_a_kind +=1
    elif cK ==4:
            four_of_a_kind +=1
        
print(pairs)
print(three_of_a_kind)
print(four_of_a_kind)