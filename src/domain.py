from numpy.random import shuffle


class Card:
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank

    @property
    def is_ace(self) -> int:
        return (self.rank == "A") * 1

    def __repr__(self):
        return f"{self.rank} of {self.suit}s"

    @property
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
        _ = self.draw()

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


class Hand:
    def __init__(self, wager: int, card1: Card, card2: Card):

        if wager < 1:
            raise ValueError("Wager must be greater than 0")

        self.wager = wager
        self.cards = [card1, card2]
        self.stayed = False

    @property
    def value(self) -> int:
        """Determines the value of the hand"""

        num_aces = sum([c.is_ace for c in self.cards])
        value = sum([c.value for c in self.cards])

        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1

        return value

    @property
    def can_hit(self) -> bool:
        """Determines if hand can hit"""

        return self.is_hand_bust

    @property
    def can_split(self) -> bool:
        """Determines if hand can split"""

        if len(self.cards) != 2:
            return False

        if self.cards[0].rank != self.cards[1].rank:
            return False

        return True

    @property
    def can_double(self) -> bool:
        """Determines if hand can double"""

        if len(self.cards) != 2:
            return False

        return True

    @property
    def is_hand_bust(self) -> bool:
        """Determines if hand is bust"""

        if self.value > 21:
            return True

        return False

    @property
    def is_hand_dead(self) -> bool:
        """Determines if hand is still active"""

        if self.is_hand_bust:
            return True

        if self.stayed:
            return True

        return False

    def hit(self, card: Card):
        """Takes action to hit"""

        self.cards.append(card)

    def stay(self):
        """Takes action to stay"""

        self.stayed = True

    def double(self, card: Card):
        """Takes action to double"""

        self.wager *= 2
        self.cards.append(card)

    def split(self, card1: Card, card2: Card) -> "Hand":
        """Takes action to split the hand"""

        # Create a new hand
        new_hand = Hand(self.wager, self.cards[1], card2)

        # Replace the "split" card with the new card
        self.cards[1] = card1

        return new_hand


class Player:
    def __init__(self, cash: int):

        if cash < 1:
            raise ValueError("Cash must be greater than 0")

        self.cash = cash
        self.hands = []
        self.active_hand = None

    def deal(self, wager: int, card1: Card, card2: Card):
        """Deals a game"""

        self.hands.append(Hand(wager=wager, card1=card1, card2=card2))
        self.active_hand = 0

    def decide(self, action: str, shoe: Shoe) -> None:
        """Takes an action to hit, stay, double, or split"""

        if action == "hit":
            card = shoe.draw()
            self.hands[self.active_hand].hit(card)
            if self.hands[self.active_hand].is_hand_dead:
                self.active_hand += 1
        elif action == "stay":
            self.hands[self.active_hand].stay()
            self.active_hand += 1
        elif action == "double":
            card = shoe.draw()
            self.hands[self.active_hand].double(card)
            self.active_hand += 1
        elif action == "split":
            card1 = shoe.draw()
            card2 = shoe.draw()
            new_hand = self.hands[self.active_hand].split(card1, card2)
            self.hands.insert(self.active_hand, new_hand)
