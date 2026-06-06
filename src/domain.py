from numpy.random import shuffle, default_rng, seed


class InvalidAction(Exception):
    pass


class NoActionError(Exception):
    pass


class NoStateError(Exception):
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
    def count_value(self):
        if self.rank in ["2", "3", "4", "5", "6"]:
            return 1
        elif self.rank in ["10", "J", "Q", "K", "A"]:
            return -1
        return 0

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
        self.cut_card = int(0.3 * self.num_decks * 52)

        self.count = 0

        # Burn a card
        _ = self.draw(is_visible=False)

    @property
    def is_active(self):
        """Determines if the shoe can support another game"""

        return len(self.cards) > self.cut_card

    def draw(self, is_visible: bool = True) -> Card:
        """Draws a card from the deck"""

        # Draw a card
        card = self.cards.pop()

        if is_visible:
            self.count += card.count_value

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
        """Determines if hand can H"""

        if (self.value >= 21) or (self.split_aces):
            # Can't H on 21 and can't H after splitting aces
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
        """Determines if hand can D"""

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
        """Takes action to hit (H)"""

        self.cards.append(card)

    def stand(self):
        """Takes action to stand (S)"""

        self.stood = True

    def double(self, card: Card):
        """Takes action to double (D)"""

        self.wager *= 2
        self.cards.append(card)

    def split(self, card1: Card, card2: Card) -> "Hand":
        """Takes action to split (P) the hand"""

        # Create a new hand
        if self.cards[1].rank == "A" and card2.rank == "A":
            new_hand = Hand(self.wager, self.cards[1], card2, split_aces=True)
        else:
            new_hand = Hand(self.wager, self.cards[1], card2)

        # Replace the "P" card with the new card
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

    @property
    def still_active(self):
        return self.active_hand < len(self.hands)

    @property
    def has_at_least_one_hand_in_play(self):
        for hand in self.hands:
            if hand.value <= 21:
                return True
        return False

    def deal(self, wager: int, card1: Card, card2: Card):
        """Deals a game"""

        # Reset the player's hands
        self.hands = []

        if wager > self.cash:
            raise ValueError("Wager must be less than or equal to player cash")
        if wager < 1:
            raise ValueError("Wager must be greater than 0.")

        self.cash -= wager
        self.hands.append(Hand(wager=wager, card1=card1, card2=card2))
        self.active_hand = 0

    def take_action(self, action: str, shoe: Shoe) -> Shoe:
        """Takes an action to H, S, D, or P"""

        if action == "H":
            # Draw a card
            card = shoe.draw()
            self.hands[self.active_hand].hit(card)

            # If hand is bust: move to next hand
            if self.hands[self.active_hand].is_hand_locked:
                self.active_hand += 1

        elif action == "S":
            # Perform split action
            self.hands[self.active_hand].stand()

            # Move to next hand
            self.active_hand += 1

        elif action == "D":

            # Get the hand's wager
            wager = self.hands[self.active_hand].wager
            if wager > self.cash:
                raise InvalidAction("Player does not have cash to support D")
            self.cash -= wager

            # Draw a card
            card = shoe.draw()
            self.hands[self.active_hand].double(card)

            # Move to next hand
            self.active_hand += 1

        elif action == "P":

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


class Dealer:
    def __init__(self, card2: Card, card4: Card):
        self.hand = Hand(wager=1, card1=card2, card2=card4)

    def should_hit(self, player: Player):
        return self.hand.value < 17 and player.has_at_least_one_hand_in_play

    @property
    def upcard(self):
        return self.hand.cards[0].value

    @property
    def value(self):
        return self.hand.value

    @property
    def is_blackjack(self):
        return self.hand.is_blackjack

    def hit(self, shoe: Shoe) -> Shoe:
        """Draws a card"""

        card = shoe.draw()
        self.hand.hit(card)

        return shoe


def get_hand_state(hand: Hand) -> str:
    """Gets the hand's state"""

    rank1 = hand.cards[0].rank
    rank2 = hand.cards[1].rank
    ranks = [rank1, rank2]

    if hand.can_split:
        if rank1 in ["A", "2", "3", "6", "7", "8", "9"]:
            return rank1 * 2
    if hand.is_hand_soft:
        for i in ["2", "3", "4", "5", "6", "7", "8"]:
            if i in ranks:
                return "A" + i
    if hand.value in [9, 10, 11, 12, 13, 14, 15, 16]:
        return str(hand.value)
    if hand.value == 8:
        if "6" in ranks:
            return "62"
        elif "5" in ranks:
            return "53"
        elif "4" in ranks:
            return "44"
        else:
            return "8"
    if hand.value >= 17:
        return "17"
    if hand.value < 8:
        return "7"

    raise NoStateError(hand.cards)


def decide_winner(player: Hand, dealer: Dealer) -> int:
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


# Deprecating this
def decide_dealer_action(hand: Hand) -> str:
    """Decide action for the dealer"""

    while hand.value < 17:
        return "H"

    return "S"
