from numpy.random import shuffle, default_rng, seed


class InvalidAction(Exception):
    pass


class Card:
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank

    @property
    def is_ace(self) -> int:
        return (self.rank == "A") * 1

    def __repr__(self) -> str:
        return f"{self.rank} of {self.suit}s"

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}s"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Card):
            return False

        return self.suit == other.suit and self.rank == other.rank

    def __hash__(self) -> bool:
        return hash(f"{self.rank} of {self.suit}s")

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
    def __init__(self, num_decks: int, random_state: int | None = None):

        if not isinstance(num_decks, int):
            raise TypeError(f"Number of decks must be type int, Got {type(num_decks)}")
        if num_decks < 1:
            raise ValueError(f"Number of decks must be greater than 0. Got {num_decks}")

        if not isinstance(random_state, int | None):
            raise TypeError("Random state must be int or None")

        if random_state:
            if (random_state < 0) or (random_state > (2**32 - 1)):
                raise ValueError("Random state out of bounds")

        self.random_state = random_state
        self.num_decks = num_decks
        self.get_cards()
        self.cut_card = int(0.2 * len(self.cards))

        # Burn a card
        _ = self.draw()

    @property
    def is_active(self):
        """Determines if the shoe can support another game"""

        return len(self.cards) > self.cut_card

    def draw(self) -> Card:
        """Draws a card from the deck"""

        # Draw a card
        card = self.cards.pop()

        return card

    def shuffle_cards(self):
        """Shuffles the shoe with seed"""

        if self.random_state:
            seed(self.random_state)
        else:
            default_rng()

        shuffle(self.cards)

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

        self.shuffle_cards()


class Hand:
    def __init__(self, wager: int, card1: Card, card2: Card, split_aces: bool = False):

        if wager < 1:
            raise ValueError("Wager must be greater than 0")

        self.wager = wager
        self.cards = [card1, card2]
        self.stood = False
        self.split_aces = split_aces

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

        if (self.value >= 21) or (self.split_aces):
            # Can't hit on 21 and can't hit after splitting aces
            return False

        return True

    @property
    def can_split(self) -> bool:
        """Determines if hand can split"""

        if len(self.cards) != 2:
            return False

        if self.cards[0].rank != self.cards[1].rank:
            return False

        if self.cards[0].rank == "A" and self.split_aces:
            # Can't split aces more than once
            return False

        return True

    @property
    def can_double(self) -> bool:
        """Determines if hand can double"""

        if len(self.cards) != 2:
            return False

        if (self.value == 21) or (self.split_aces):
            # Can't double on 21 and can't double after splitting
            return False

        return True

    @property
    def is_hand_soft(self) -> bool:
        """Determines if hand is soft or not"""

        for card in self.cards:
            if card.rank == "A":
                return True

        return False

    @property
    def is_hand_bust(self) -> bool:
        """Determines if hand is bust"""

        if self.value > 21:
            return True

        return False

    @property
    def is_hand_locked(self) -> bool:
        """Determines if hand is still active"""

        if (self.value >= 21) or (self.split_aces) or (self.stood):
            return True

        return False

    @property
    def is_blackjack(self) -> bool:
        """Determines if hand is a blackjack"""

        return (len(self.cards) == 2) and (self.value == 21)

    def hit(self, card: Card):
        """Takes action to hit"""

        self.cards.append(card)

    def stand(self):
        """Takes action to stand"""

        self.stood = True

    def double(self, card: Card):
        """Takes action to double"""

        self.wager *= 2
        self.cards.append(card)

    def split(self, card1: Card, card2: Card) -> "Hand":
        """Takes action to split the hand"""

        # Create a new hand
        if self.cards[1].rank == "A" and card2.rank == "A":
            new_hand = Hand(self.wager, self.cards[1], card2, split_aces=True)
        else:
            new_hand = Hand(self.wager, self.cards[1], card2)

        # Replace the "split" card with the new card
        self.cards[1] = card1
        if self.cards[0].rank == "A" and self.cards[1].rank == "A":
            self.split_aces = True

        return new_hand


class Player:
    def __init__(self, cash: int):

        if not isinstance(cash, int):
            raise TypeError("Cash must be an integer")

        if cash < 1:
            raise ValueError("Cash must be greater than 0")

        self.cash = cash
        self.hands = []
        self.active_hand = None

    def deal(self, wager: int, card1: Card, card2: Card):
        """Deals a game"""

        if wager > self.cash:
            raise ValueError("Wager must be less than or equal to player cash")
        if wager < 1:
            raise ValueError("Wager must be greater than 0.")

        self.cash -= wager
        self.hands.append(Hand(wager=wager, card1=card1, card2=card2))
        self.active_hand = 0

    def take_action(self, action: str, shoe: Shoe) -> Shoe:
        """Takes an action to hit, stand, double, or split"""

        if action == "hit":
            # Draw a card
            card = shoe.draw()
            self.hands[self.active_hand].hit(card)

            # If hand is bust: move to next hand
            if self.hands[self.active_hand].is_hand_locked:
                self.active_hand += 1

        elif action == "stand":
            # Perform stand action
            self.hands[self.active_hand].stand()

            # Move to next hand
            self.active_hand += 1

        elif action == "double":

            # Get the hand's wager
            wager = self.hands[self.active_hand].wager
            if wager > self.cash:
                raise InvalidAction("Player does not have cash to support double")
            self.cash -= wager

            # Draw a card
            card = shoe.draw()
            self.hands[self.active_hand].double(card)

            # Move to next hand
            self.active_hand += 1

        elif action == "split":

            # Get the hand's wager
            wager = self.hands[self.active_hand].wager
            if wager > self.cash:
                raise InvalidAction("Player does not have cash to support splitting")
            self.cash -= wager

            # Draw two cards from deck
            card1 = shoe.draw()
            card2 = shoe.draw()

            # Split the hands
            new_hand = self.hands[self.active_hand].split(card1, card2)

            # Insert new hand just being the active hand
            self.hands.insert(self.active_hand + 1, new_hand)

            # Iterate active hand if split was aces
            if self.hands[self.active_hand].cards[0].rank == "A":
                self.active_hand += 2  # Cycles two hands

        return shoe


def decide_player_action(hand: Hand, dealer: Card, count: int = 0) -> str:
    """Decides what action to take"""

    if hand.value == 21:
        return "stand"
    elif hand.value == 20:
        return "stand"
    elif hand.value == 19:
        return "stand"
    elif hand.value == 18:
        return "stand"
    elif hand.value == 17:
        return "stand"
    elif hand.value == 16:
        if dealer.value > 16:
            return "hit"
        else:
            return "stand"
    elif hand.value == 15:
        if dealer.value > 16:
            return "hit"
        else:
            return "stand"
    elif hand.value == 14:
        if dealer.value > 16:
            return "hit"
        else:
            return "stand"
    elif hand.value == 13:
        if dealer.value > 16:
            return "hit"
        else:
            return "stand"
    elif hand.value == 12:
        if dealer.value > 16:
            return "hit"
        else:
            return "stand"
    elif hand.value == 11:
        return "double"
    elif hand.value == 10:
        if dealer.value < 10:
            return "double"
        else:
            return "hit"
    elif hand.value == 9:
        if dealer.value < 17:
            return "double"
        else:
            return "hit"

    return "hit"


def decide_dealer_action(hand: Hand) -> str:
    """Decide action for the dealer"""

    while hand.value < 17:
        return "hit"

    return "stand"


def decide_winner(player: Hand, dealer: Hand) -> int:
    """Decides the"""

    if player.is_blackjack and (not dealer.is_blackjack):
        # Winner winner chicken dinner!
        return 1.5 * player.wager
    elif player.value > 21:
        # Player busts
        return -player.wager
    elif dealer.value > 21:
        # Dealer busts
        return player.wager
    elif player.value > dealer.value:
        # Player wins
        return player.wager
    elif player.value < dealer.value:
        return -player.wager
    elif player.value == dealer.value:
        # Push
        return 0
