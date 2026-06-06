import unittest

from src.domain import Card, Shoe, Player, InvalidAction


class TestPlayer(unittest.TestCase):

    def test_initializing_player(self):

        # Create a generic player
        player = Player(cash=1)

        # Assert
        self.assertEqual(player.cash, 1)
        self.assertEqual(len(player.hands), 0)
        self.assertIsNone(player.active_hand)

        # Test edge cases
        with self.assertRaises(ValueError):
            player = Player(cash=0)
        with self.assertRaises(ValueError):
            player = Player(cash=-1)
        with self.assertRaises(TypeError):
            player = Player(cash="1")
        with self.assertRaises(TypeError):
            player = Player(cash=1.0)

    def test_player_deal(self):

        # Create a player
        player = Player(cash=1)

        # Deal out cards to table
        card1 = Card(suit="Spade", rank="5")
        card2 = Card(suit="Club", rank="10")
        player.deal(wager=1, card1=card1, card2=card2)

        # Perform assertions
        self.assertEqual(player.cash, 0)
        self.assertEqual(player.active_hand, 0)
        self.assertEqual(len(player.hands), 1)
        self.assertEqual(player.hands[player.active_hand].value, 15)

        # Test edge cases
        with self.assertRaises(ValueError):
            player.deal(wager=2, card1=card1, card2=card2)

        with self.assertRaises(ValueError):
            player.deal(wager=-1, card1=card1, card2=card2)

        with self.assertRaises(ValueError):
            player.deal(wager=0, card1=card1, card2=card2)

    def test_player_actions_hit(self):

        # Create a player
        player = Player(cash=1)

        # Deal out cards to table
        shoe = Shoe(num_decks=1, random_state=42)
        card1 = shoe.draw()
        card2 = shoe.draw()
        player.deal(wager=1, card1=card1, card2=card2)

        # Pre action asserts
        self.assertEqual(len(shoe.cards), 52 - 3)
        self.assertEqual(player.hands[player.active_hand].value, 5)

        # Perform hit action
        shoe = player.take_action("hit", shoe)

        # Assert
        self.assertEqual(len(shoe.cards), 52 - 4)
        self.assertEqual(len(player.hands), 1)
        self.assertEqual(player.hands[player.active_hand].value, 9)

    def test_player_actions_stang(self):
        pass

    def test_player_actions_split(self):

        # Seeds:
        #  2's: 448
        #  3's: 320
        #  4's:  90
        #  5's: 241
        #  6's: 382
        #  7's: 225
        #  8's: 224
        #  9's: 393
        # 10's: 462
        #  J's: 266
        #  Q's: 491
        #  K's: 193
        #  A's: 204

        # Create a player
        player = Player(cash=10)

        # Deal out cards to table
        shoe = Shoe(num_decks=1, random_state=224)  # Always split 8's
        card1 = shoe.draw()
        _ = shoe.draw()  # Dealer card
        card2 = shoe.draw()
        _ = shoe.draw()  # Dealer card
        player.deal(wager=1, card1=card1, card2=card2)

        # Pre-split asserts
        self.assertEqual(player.cash, 9)
        self.assertEqual(player.hands[0].cards[0].rank, player.hands[0].cards[1].rank)
        self.assertEqual(player.hands[0].can_split, True)
        self.assertEqual(player.active_hand, 0)
        self.assertEqual(len(player.hands), 1)

        # Perform splitting action
        shoe = player.take_action("split", shoe)

        # Post-split assertions
        self.assertEqual(len(player.hands), 2)
        self.assertEqual(player.active_hand, 0)
        self.assertEqual(player.hands[player.active_hand].value, 16)
        self.assertEqual(player.hands[1].value, 19)
        self.assertEqual(player.hands[0].can_split, True)
        self.assertEqual(player.hands[1].can_split, False)

        # Perform further actions
        # Player's first hand can split 8's again
        shoe = player.take_action("split", shoe)
        self.assertEqual(len(player.hands), 3)
        self.assertEqual(player.active_hand, 0)
        self.assertEqual(player.hands[player.active_hand].value, 12)
        self.assertEqual(player.hands[1].value, 18)
        self.assertEqual(player.hands[2].value, 19)
        self.assertEqual(player.hands[0].can_split, False)
        self.assertEqual(player.hands[1].can_split, False)
        self.assertEqual(player.hands[2].can_split, False)

        # Perform further actions on first hand
        shoe = player.take_action("hit", shoe)
        shoe = player.take_action("hit", shoe)
        shoe = player.take_action("hit", shoe)
        self.assertEqual(len(player.hands), 3)
        self.assertEqual(player.active_hand, 1)
        self.assertEqual(player.hands[0].value, 22)
        self.assertEqual(player.hands[1].value, 18)
        self.assertEqual(player.hands[2].value, 19)

        # Perform actions on two split hands
        shoe = player.take_action("stand", shoe)
        shoe = player.take_action("stand", shoe)
        self.assertEqual(player.hands[1].value, 18)
        self.assertEqual(player.hands[2].value, 19)
        self.assertEqual(player.active_hand, 3)

        ## Check player not enough cash
        player = Player(cash=1)
        shoe = Shoe(num_decks=1, random_state=224)  # Always split 8's
        card1 = shoe.draw()
        _ = shoe.draw()  # Dealer card
        card2 = shoe.draw()
        _ = shoe.draw()  # Dealer card
        player.deal(wager=1, card1=card1, card2=card2)

        with self.assertRaises(InvalidAction):
            shoe = player.take_action("split", shoe)

        ## Testing player trying to split A's twice
        player = Player(cash=100)
        shoe = Shoe(num_decks=1, random_state=12154)
        card1 = shoe.draw()
        _ = shoe.draw()  # Dealer card
        card2 = shoe.draw()
        _ = shoe.draw()  # Dealer card
        player.deal(wager=1, card1=card1, card2=card2)  # Has pair Aces
        shoe = player.take_action("split", shoe)

        # Player's hands are locked


if __name__ == "__main__":
    unittest.main()
