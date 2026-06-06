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

    def test_04_cut_card(self):

        # Verify cut_card is doing something
        for num_decks in [1, 2, 3, 4]:
            shoe = Shoe(num_decks)
            self.assertEqual(shoe.cut_card, int(0.3 * num_decks * 52))

        # Test the is_active
        shoe = Shoe(num_decks=1)
        n = int(0.3 * 52)
        for _ in range(52 - n - 2):
            _ = shoe.draw()
        self.assertEqual(n, 15)
        self.assertEqual(shoe.cut_card, 15)
        self.assertEqual(len(shoe.cards), 16)
        self.assertEqual(shoe.is_active, True)

        _ = shoe.draw()
        self.assertEqual(len(shoe.cards), 15)
        self.assertEqual(shoe.is_active, False)

    def test_05_keeping_count(self):

        # Assumes all cards are visible
        shoe = Shoe(num_decks=2, random_state=42)
        for _ in range(10):
            _ = shoe.draw()
        self.assertEqual(shoe.count, 2)

        # Check the visible parameter
        shoe = Shoe(num_decks=1, random_state=43)
        low_cards = [3, 4, 5, 6, 7, 13, 16, 20, 21, 22, 32, 34, 35, 36, 38, 40, 42, 46, 47]
        for i in range(51):
            if i in low_cards:
                # Player sees it
                _ = shoe.draw()
            else:
                # Player misses it
                _ = shoe.draw(is_visible=False)
        self.assertEqual(shoe.count, 19)


if __name__ == "__main__":
    unittest.main
