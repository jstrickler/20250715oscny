from carddeck import CardDeck
from card import Card

class Game:
    def register(self):
        pass

class JokerDeck(Game, CardDeck):
    def _make_deck(self):
        super()._make_deck()
        for joker_number in 1, 2:
            card = Card(f"JOKER-{joker_number}", "**JOKER**")
            self._cards.append(card)

if __name__ == "__main__":
    j = JokerDeck()
    j.shuffle()
    print(f"{j.cards = }")
    
    print(f"{j.draw() = }")
    j.register()
    print(f"{JokerDeck.mro() = }")
    
    