import unittest

from src.domain import Card, Shoe


class TestShoe(unittest.TestCase):

    def test_01(self):

        # Test all cards are present
        # Yes, this is testing signs that all cards are there.
        # I assume this won't break
        shoe = Shoe(num_decks=1)
        ranks = list(set([c.rank for c in shoe.cards]))
        suits = list(set([c.suit for c in shoe.cards]))
        self.assertEqual(len(ranks), 13)
        self.assertEqual(len(suits), 4)

        # Creates shoe and burns a card
        for num_decks in list(range(1, 10)):
            shoe = Shoe(num_decks=num_decks)
            self.assertEqual(len(shoe.cards), 52 * num_decks - 1)

        with self.assertRaises(ValueError):
            shoe = Shoe(num_decks=0)

        with self.assertRaises(ValueError):
            shoe = Shoe(num_decks=-1)

        with self.assertRaises(TypeError):
            shoe = Shoe(num_decks=1.5)

    def test_02_random_state(self):

        first_cards = []
        for _ in range(52):
            shoe = Shoe(num_decks=1)
            first_card = shoe.draw()
            first_cards.append(first_card)

        # If this was random each time, we would have a
        # very, very small chance of this failing. At
        # least one card would be different
        self.assertGreater(len(set(first_cards)), 1)

        first_cards = []
        for _ in range(52):
            shoe = Shoe(num_decks=1, random_state=1)
            first_card = shoe.draw()
            first_cards.append(first_card)

        # If the random state is fixed, we should have a
        # very, very small chance of this failing
        self.assertEqual(len(set(first_cards)), 1)

    def test_03_draw(self):

        shoe = Shoe(num_decks=2, random_state=42)

        self.assertEqual(len(shoe.cards), 103)
        self.assertEqual(shoe.draw(), Card(suit="Club", rank="K"))
        self.assertEqual(shoe.draw(), Card(suit="Club", rank="2"))
        self.assertEqual(shoe.draw(), Card(suit="Spade", rank="2"))
        self.assertEqual(len(shoe.cards), 100)


if __name__ == "__main__":
    unittest.main
