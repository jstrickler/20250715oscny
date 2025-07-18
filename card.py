class Card:   # inherits from 'object'
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    @property
    def rank(self):  # getter property
        return self._rank
    
    @rank.setter
    def rank(self, value):  # setter property
        if isinstance(value, str):
            self._rank = value
        else:
            raise TypeError("rank must be a str")

    def rank_setter(self, value):
        self._rank = value

    @property
    def suit(self): 
        return self._suit
    
    @suit.setter
    def suit(self, value):
        if isinstance(value, str):
            self._suit = value
        else:
            raise TypeError("suit must be a str")

    def __str__(self):
        return f"card:{self.rank}-{self.suit}"
    
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c1 = Card("3", 'Diamonds')
    c2 = Card('Q', "Clubs")
    print(f"{c1 = }")
    print(f"{c2 = }")
    print(f"{c1.rank = }")
    print(f"{c1.suit = }")
    c1.rank = '8'
    print(f"{c1.rank = }")
    c1.rank_setter('J')
    
# uses str(x):
# print(x)

# uses repr(x):
# print(repr(x))
# print(f"{x = }")
    print(c1)