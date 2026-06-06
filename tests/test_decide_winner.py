import unittest

from src.domain import Hand, Shoe, Player, decide_winner

CASH = 100
WAGER = 10


def setup_game(
    random_state: int, cash: int = CASH, wager: int = WAGER, num_decks: int = 1
) -> tuple[Player, Hand, Shoe]:
    """Sets up a game"""

    # Initialize a player
    player = Player(cash=cash)

    # Generate the shoe
    shoe = Shoe(num_decks=num_decks, random_state=random_state)

    # Draw the cards
    card1 = shoe.draw()
    card2 = shoe.draw()
    card3 = shoe.draw()
    card4 = shoe.draw()

    # Deal out to player and dealer
    player.deal(wager=WAGER, card1=card1, card2=card3)
    dealer = Hand(wager=WAGER, card1=card2, card2=card4)

    return player, dealer, shoe


class TestDecideWinner(unittest.TestCase):

    def test_blackjack(self):

        # Set up game
        player, dealer, _ = setup_game(10)

        # Test player gets blackjack (wins 1.5x wager)
        winnings = decide_winner(player.hands[0], dealer)
        self.assertEqual(winnings, 1.5 * WAGER)
        self.assertEqual(winnings, 1.5 * player.hands[0].wager)

    def test_player_busts(self):

        # Set up game
        player, dealer, shoe = setup_game(1)

        # Player hits 14 on dealer K
        shoe = player.take_action("hit", shoe)  # Draws a Q = BUST!

        # Test player loses wager
        winnings = decide_winner(player.hands[0], dealer)
        self.assertEqual(winnings, -WAGER)
        self.assertEqual(winnings, -player.hands[0].wager)

    def test_dealer_busts(self):

        # Set up game
        player, dealer, shoe = setup_game(3)

        # Situation: Player stands on 19 v Dealer 4
        # Dealer reveals 9 (Value: 13)
        # Dealer draws 9 = BUST!
        shoe = player.take_action("stand", shoe)
        dealer.cards.append(shoe.draw())

        # Test player wins wager
        winnings = decide_winner(player.hands[0], dealer)
        self.assertEqual(winnings, WAGER)
        self.assertEqual(winnings, player.hands[0].wager)

    def test_player_wins(self):

        # Set up game
        player, dealer, shoe = setup_game(30)

        # Situation: Player stands on 20 v 7
        # Dealer reveals 10 (Value: 17)
        # Player wins!
        shoe = player.take_action("stand", shoe)

        # Test player wins wager
        winnings = decide_winner(player.hands[0], dealer)
        self.assertEqual(winnings, WAGER)
        self.assertEqual(winnings, player.hands[0].wager)

    def test_player_loses(self):

        # Set up game
        player, dealer, shoe = setup_game(128)

        # Situation: Player stands on 17 v Q
        # Dealer reveals J (Value: 20)
        # Player loses :(
        shoe = player.take_action("stand", shoe)

        # Test player wins wager
        winnings = decide_winner(player.hands[0], dealer)
        self.assertEqual(winnings, -WAGER)
        self.assertEqual(winnings, -player.hands[0].wager)

    def test_player_pushes(self):

        # Set up game
        player, dealer, shoe = setup_game(322)

        # Situation: Player stands on 19 v 9
        # Dealer reveals K (Value: 19)
        # Player push :|
        shoe = player.take_action("stand", shoe)

        # Test player wins wager
        winnings = decide_winner(player.hands[0], dealer)
        self.assertEqual(winnings, 0 * WAGER)

    def test_player_loses_to_dealer_blackjack(self):

        # Set up game
        player, dealer, shoe = setup_game(22)

        # Situation: Dealer naturally has blackjack :(
        shoe = player.take_action("stand", shoe)

        # Test player wins wager
        winnings = decide_winner(player.hands[0], dealer)
        self.assertEqual(winnings, -WAGER)
        self.assertEqual(winnings, -player.hands[0].wager)


if __name__ == "__main__":
    unittest.main()
