import unittest

from src.domain import Card


class TestCard(unittest.TestCase):

    def test_01(self):

        card = Card(suit="Diamond", rank="2")
        self.assertEqual(card.value, 2)
        card = Card(suit="Diamond", rank="3")
        self.assertEqual(card.value, 3)
        card = Card(suit="Diamond", rank="4")
        self.assertEqual(card.value, 4)
        card = Card(suit="Diamond", rank="5")
        self.assertEqual(card.value, 5)
        card = Card(suit="Diamond", rank="6")
        self.assertEqual(card.value, 6)
        card = Card(suit="Diamond", rank="7")
        self.assertEqual(card.value, 7)
        card = Card(suit="Diamond", rank="8")
        self.assertEqual(card.value, 8)
        card = Card(suit="Diamond", rank="9")
        self.assertEqual(card.value, 9)
        card = Card(suit="Diamond", rank="10")
        self.assertEqual(card.value, 10)
        card = Card(suit="Diamond", rank="J")
        self.assertEqual(card.value, 10)
        card = Card(suit="Diamond", rank="Q")
        self.assertEqual(card.value, 10)
        card = Card(suit="Diamond", rank="K")
        self.assertEqual(card.value, 10)
        card = Card(suit="Diamond", rank="A")
        self.assertEqual(card.value, 11)


if __name__ == "__main__":
    unittest.main()
