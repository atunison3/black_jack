import unittest

from src.domain import Card, Hand, decide_dealer_action


class TestDealerActions(unittest.TestCase):
    cards = {}
    for rank in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
        cards[rank] = Card(suit="Diamond", rank=rank)

    def test_dealer_stands(self):

        for rank in ["7", "8", "9", "10", "J", "Q", "K", "A"]:
            hand = Hand(wager=1, card1=self.cards["10"], card2=self.cards[rank])
            action = decide_dealer_action(hand)
            self.assertEqual(action, "S")

        for rank in ["8", "9", "10", "J", "Q", "K", "A"]:
            hand = Hand(wager=1, card1=self.cards["9"], card2=self.cards[rank])
            action = decide_dealer_action(hand)
            self.assertEqual(action, "S")

        for rank in ["9", "10", "J", "Q", "K", "A"]:
            hand = Hand(wager=1, card1=self.cards["8"], card2=self.cards[rank])
            action = decide_dealer_action(hand)
            self.assertEqual(action, "S")

        for rank in ["10", "J", "Q", "K", "A"]:
            hand = Hand(wager=1, card1=self.cards["7"], card2=self.cards[rank])
            action = decide_dealer_action(hand)
            self.assertEqual(action, "S")

        for rank in ["A"]:
            hand = Hand(wager=1, card1=self.cards["6"], card2=self.cards[rank])
            action = decide_dealer_action(hand)
            self.assertEqual(action, "S")

    def test_dealer_hits(self):

        for rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
            for rank2 in ["2", "3", "4", "5", "5"]:
                hand = Hand(wager=1, card1=self.cards[rank], card2=self.cards[rank2])
                action = decide_dealer_action(hand)
                self.assertEqual(action, "H")

        for rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
            hand = Hand(wager=1, card1=self.cards["6"], card2=self.cards[rank])
            action = decide_dealer_action(hand)
            self.assertEqual(action, "H")


if __name__ == "__main__":
    unittest.main()
