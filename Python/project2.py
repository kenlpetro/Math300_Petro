import itertools
from collections import Counter
import matplotlib.pyplot as plt

all_combinations = list(itertools.combinations(range(52), 5))
for combination in all_combinations:
# Convert the combination into a list of integers
    int_list = []

for card in combination:
    int_list.append(card)

# Use Counter to count the number of each card in the hand
    counts = Counter(int_list)

pairs = 0
three_of_a_kind = 0
four_of_a_kind = 0

for key, value in counts.items():

    if value == 2:

        pairs += 1

    elif value == 3:

        three_of_a_kind += 1

    elif value == 4:
        four_of_a_kind += 1
        
labels = ['Pairs', 'Three-of-a-kind', 'Four-of-a-kind']
sizes = [pairs, three_of_a_kind, four_of_a_kind]
colors = ['gold', 'lightskyblue', 'lightcoral']
explode = (0.1, 0, 0) # explode 1st slice
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show