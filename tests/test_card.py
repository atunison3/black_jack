import unittest

from src.domain import Card


class TestCard(unittest.TestCase):

    def test_01(self):

        card = Card(suit="Diamond", rank="2")
        self.assertEqual(card.value, 2)
        self.assertEqual(card.is_ace, 0)
        card = Card(suit="Diamond", rank="3")
        self.assertEqual(card.value, 3)
        self.assertEqual(card.is_ace, 0)
        card = Card(suit="Diamond", rank="4")
        self.assertEqual(card.value, 4)
        self.assertEqual(card.is_ace, 0)
        card = Card(suit="Diamond", rank="5")
        self.assertEqual(card.value, 5)
        self.assertEqual(card.is_ace, 0)
        card = Card(suit="Diamond", rank="6")
        self.assertEqual(card.value, 6)
        self.assertEqual(card.is_ace, 0)
        card = Card(suit="Diamond", rank="7")
        self.assertEqual(card.value, 7)
        self.assertEqual(card.is_ace, 0)
        card = Card(suit="Diamond", rank="8")
        self.assertEqual(card.value, 8)
        self.assertEqual(card.is_ace, 0)
        card = Card(suit="Diamond", rank="9")
        self.assertEqual(card.value, 9)
        self.assertEqual(card.is_ace, 0)
        card = Card(suit="Diamond", rank="10")
        self.assertEqual(card.value, 10)
        self.assertEqual(card.is_ace, 0)
        card = Card(suit="Diamond", rank="J")
        self.assertEqual(card.value, 10)
        self.assertEqual(card.is_ace, 0)
        card = Card(suit="Diamond", rank="Q")
        self.assertEqual(card.value, 10)
        self.assertEqual(card.is_ace, 0)
        card = Card(suit="Diamond", rank="K")
        self.assertEqual(card.value, 10)
        self.assertEqual(card.is_ace, 0)
        card = Card(suit="Diamond", rank="A")
        self.assertEqual(card.value, 11)
        self.assertEqual(card.is_ace, 1)

    def test_02_card_equals(self):

        # Same card
        suit = "Diamond"
        rank = "2"
        card = Card(suit=suit, rank=rank)
        other = Card(suit=suit, rank=rank)
        self.assertEqual(card, other)

        # Same suit different ranks
        other = Card(suit="Diamond", rank="3")
        self.assertNotEqual(card, other)

        # Different suits same ranks
        other = Card(suit="Spade", rank="2")
        self.assertNotEqual(card, other)

        # Different suits different ranks
        other = Card(suit="Heart", rank="Q")
        self.assertNotEqual(card, other)


if __name__ == "__main__":
    unittest.main()
