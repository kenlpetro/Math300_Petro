import random as rnd
import matplotlib.pyplot as plt
from collections import Counter
import re

cards={1:'Ace',
       2:'2',
       3:'3',
       4:'4',
       5:'5',
       6:'6',
       7:'7',
       8:'8',
       9:'9',
       10:'10',
       11:'Jack',
       12:'Queen',
       13:'King'}

suits={1:'Spades',
       2:'Clubs',
       3:'Diamonds',
       4:'Hearts'}

def draw (num_cards, list_dealt=[]):
    for a in range(num_cards):
        b=rnd.randint(1,4)
        c=rnd.randint(1,13)
        dealt="{0} of {1}".format(cards[c],suits[b])
        if dealt not in list_dealt:
            list_dealt.append(dealt)
        else:
            num_cards=num_cards-a
            return draw(num_cards,list_dealt)
    return list_dealt
dealt=draw(5)
#print(dealt)
#dealt=['King of Hearts','King of Spades','King of Diamonds','2 of Hearts','2 of Hearts']

y=dealt[0]+dealt[1]+dealt[2]+dealt[3]+dealt[4]
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
#print(c2)
#print(cK)      


def fun():
    pairs = 0
    three_of_a_kind = 0
    four_of_a_kind = 0
    for dealt in range(500):
        if cA or c2 or c3 or c4 or c5 or c6 or c7 or c8 or c9 or c10 or cJ or cQ or cK ==2:
            pairs+=1
        elif cA or c2 or c3 or c4 or c5 or c6 or c7 or c8 or c9 or c10 or cJ or cQ or cK ==3:
            three_of_a_kind +=1
        elif cA or c2 or c3 or c4 or c5 or c6 or c7 or c8 or c9 or c10 or cJ or cQ or cK ==4:
            four_of_a_kind +=1

    print(pairs)
    print(three_of_a_kind)
    print(four_of_a_kind)

    
"""
counts = Counter(z)
count_pairs=counts['2']
#print(count_pairs)
"""  

'''
num_pairs = 0
num_three_of_a_kind = 0
num_four_of_a_kind = 0

for key, value in counts.items():
    if x == 2:
        num_pairs += 1
    elif value == 3:
        num_three_of_a_kind += 1
    elif value == 4:
        num_four_of_a_kind += 1
'''
