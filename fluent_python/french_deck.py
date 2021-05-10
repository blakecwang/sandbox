#!/usr/bin/env python

import collections
from random import choice

Card = collections.namedtuple("Card", ["rank", "suit"])

class FrenchDeck:
    ranks = [str(n) for n in list(range(2, 11)) + list("JQKA")]
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

suit_values = dict(
    clubs=3,
    diamonds=2,
    hearts=1,
    spades=0,
)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

deck = FrenchDeck()

print("from highest to lowest with clubs and aces high")
for card in reversed(sorted(deck, key=spades_high)):
    print(card)

print("all aces using slicing")
print(deck[12::13])

# reversed() and sorted() are possible because of the special method
# __getitem__()
