import random
from collections import Counter


def twopair():
    while True:
        cards = []
        for i in range(5):
            cards.append(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))

        counted_cards = Counter(cards)
        two_most_common, count = zip(*counted_cards.most_common(2))

        count_to_message = {
            (1, 1): "Nothing",
            (2, 1): "One Pair",
            (3, 1): "Three of a Kind",
            (4, 1): "Four of a Kind",
            (5, 1): "Whoops, who's cheating",
            (2, 2): "Two Pairs",
            (3, 2): "Full House",
        }

        msg = count_to_message[count]
        print(msg)
        if msg == "Two Pairs":
            break
twopair()