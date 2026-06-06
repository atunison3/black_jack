from numpy.random import shuffle


class Card:
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}s"

    def value(self):
        return {
            "A": 11,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 10,
            "Q": 10,
            "K": 10,
        }[self.rank]


class Shoe:
    def __init__(self, num_decks: int):
        if num_decks < 1:
            raise ValueError("Number of decks must be greater than 0.")

        self.num_decks = num_decks
        self.get_cards()
        self.last_card = int(0.2 * len(self.cards))

        # Burn a card
        _ = self.cards.pop()

    @property
    def is_active(self):
        """Determines if the shoe can support another game"""

        return len(self.cards) > self.last_card

    def draw(self) -> Card:
        """Draws a card from the deck"""

        # Draw a card
        card = self.cards.pop()

        # Check if the deck is still active
        self.is_active = len(self.cards) > self.last_card

        return card

    def get_cards(self):
        """Builds the shoe"""

        self.cards = []
        for _ in range(self.num_decks):
            for suit in ["Heart", "Spade", "Diamond", "Club"]:
                for rank in [
                    "A",
                    "2",
                    "3",
                    "4",
                    "5",
                    "6",
                    "7",
                    "8",
                    "9",
                    "10",
                    "J",
                    "Q",
                    "K",
                ]:
                    self.cards.append(Card(suit=suit, rank=rank))

        shuffle(self.cards)
