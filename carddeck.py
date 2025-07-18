import random
from card import Card

class CardDeck:
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self):
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @classmethod    
    def get_ranks(cls):
        return cls.RANKS
    
    @property
    def cards(self):
        return self._cards
    
    def __len__(self):
        return len(self._cards)


if __name__ == "__main__":
    c1 = CardDeck()
    c2 = CardDeck()
    c1.shuffle()
    print(f"{c1.cards = }")
    
    for _ in range(5):
        c = c1.draw()
        print(c)
    print()
    print(f"{c1.get_ranks() = }")
    print(f"{CardDeck.get_ranks() = }")
    print(f"{len(c1)}")
    