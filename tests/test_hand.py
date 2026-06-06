import unittest

from src.domain import Card, Hand


class TestHand(unittest.TestCase):

    def test_wager(self):
        card1 = Card(suit="Diamond", rank="2")
        card2 = Card(suit="Diamond", rank="10")

        with self.assertRaises(ValueError):
            hand = Hand(wager=-1, card1=card1, card2=card2)  # noqa: F841

        with self.assertRaises(ValueError):
            hand = Hand(wager=0, card1=card1, card2=card2)  # noqa: F841

    def test_hand(self):
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        for r1 in ranks:
            for r2 in ranks:
                card1 = Card(suit="Diamond", rank=r1)
                card2 = Card(suit="Diamond", rank=r2)
                hand = Hand(1, card1, card2)
                self.assertLessEqual(hand.value, 21)


if __name__ == "__main__":
    unittest.main()
