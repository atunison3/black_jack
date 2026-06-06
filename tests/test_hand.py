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

        # Testing first card is 2
        card1 = Card(suit="Diamond", rank="2")
        test_cases = [
            # rank, expected_value, can_double, can_hit, can_split, is_blackjack, is_hand_locked, is_hand_soft
            ("2", 4, True, True, True, False, False, False),
            ("3", 5, True, True, False, False, False, False),
            ("4", 6, True, True, False, False, False, False),
            ("5", 7, True, True, False, False, False, False),
            ("6", 8, True, True, False, False, False, False),
            ("7", 9, True, True, False, False, False, False),
            ("8", 10, True, True, False, False, False, False),
            ("9", 11, True, True, False, False, False, False),
            ("10", 12, True, True, False, False, False, False),
            ("J", 12, True, True, False, False, False, False),
            ("Q", 12, True, True, False, False, False, False),
            ("K", 12, True, True, False, False, False, False),
            ("A", 13, True, True, False, False, False, True),
        ]
        for (
            rank,
            expected_value,
            expected_can_double,
            expected_can_hit,
            expected_can_split,
            expected_is_blackjack,
            expected_is_hand_locked,
            expected_is_hand_soft,
        ) in test_cases:
            with self.subTest(first_card="2", second_card=rank):
                card2 = Card(suit="Heart", rank=rank)
                hand = Hand(wager=1, card1=card1, card2=card2)

                self.assertEqual(hand.value, expected_value)
                self.assertEqual(hand.can_double, expected_can_double)
                self.assertEqual(hand.can_hit, expected_can_hit)
                self.assertEqual(hand.can_split, expected_can_split)
                self.assertEqual(hand.is_blackjack, expected_is_blackjack)
                self.assertEqual(hand.is_hand_locked, expected_is_hand_locked)
                self.assertEqual(hand.is_hand_soft, expected_is_hand_soft)

        # Testing first card is 3
        card1 = Card(suit="Diamond", rank="3")
        test_cases = [
            # rank, expected_value, can_double, can_hit, can_split, is_blackjack, is_hand_locked, is_hand_soft
            ("2", 5, True, True, False, False, False, False),
            ("3", 6, True, True, True, False, False, False),
            ("4", 7, True, True, False, False, False, False),
            ("5", 8, True, True, False, False, False, False),
            ("6", 9, True, True, False, False, False, False),
            ("7", 10, True, True, False, False, False, False),
            ("8", 11, True, True, False, False, False, False),
            ("9", 12, True, True, False, False, False, False),
            ("10", 13, True, True, False, False, False, False),
            ("J", 13, True, True, False, False, False, False),
            ("Q", 13, True, True, False, False, False, False),
            ("K", 13, True, True, False, False, False, False),
            ("A", 14, True, True, False, False, False, True),
        ]
        for (
            rank,
            expected_value,
            expected_can_double,
            expected_can_hit,
            expected_can_split,
            expected_is_blackjack,
            expected_is_hand_locked,
            expected_is_hand_soft,
        ) in test_cases:
            with self.subTest(first_card="3", second_card=rank):
                card2 = Card(suit="Heart", rank=rank)
                hand = Hand(wager=1, card1=card1, card2=card2)

                self.assertEqual(hand.value, expected_value)
                self.assertEqual(hand.can_double, expected_can_double)
                self.assertEqual(hand.can_hit, expected_can_hit)
                self.assertEqual(hand.can_split, expected_can_split)
                self.assertEqual(hand.is_blackjack, expected_is_blackjack)
                self.assertEqual(hand.is_hand_locked, expected_is_hand_locked)
                self.assertEqual(hand.is_hand_soft, expected_is_hand_soft)

        # Testing first card is 4
        card1 = Card(suit="Diamond", rank="4")
        test_cases = [
            # rank, expected_value, can_double, can_hit, can_split, is_blackjack, is_hand_locked, is_hand_soft
            ("2", 6, True, True, False, False, False, False),
            ("3", 7, True, True, False, False, False, False),
            ("4", 8, True, True, True, False, False, False),
            ("5", 9, True, True, False, False, False, False),
            ("6", 10, True, True, False, False, False, False),
            ("7", 11, True, True, False, False, False, False),
            ("8", 12, True, True, False, False, False, False),
            ("9", 13, True, True, False, False, False, False),
            ("10", 14, True, True, False, False, False, False),
            ("J", 14, True, True, False, False, False, False),
            ("Q", 14, True, True, False, False, False, False),
            ("K", 14, True, True, False, False, False, False),
            ("A", 15, True, True, False, False, False, True),
        ]
        for (
            rank,
            expected_value,
            expected_can_double,
            expected_can_hit,
            expected_can_split,
            expected_is_blackjack,
            expected_is_hand_locked,
            expected_is_hand_soft,
        ) in test_cases:
            with self.subTest(first_card="4", second_card=rank):
                card2 = Card(suit="Heart", rank=rank)
                hand = Hand(wager=1, card1=card1, card2=card2)

                self.assertEqual(hand.value, expected_value)
                self.assertEqual(hand.can_double, expected_can_double)
                self.assertEqual(hand.can_hit, expected_can_hit)
                self.assertEqual(hand.can_split, expected_can_split)
                self.assertEqual(hand.is_blackjack, expected_is_blackjack)
                self.assertEqual(hand.is_hand_locked, expected_is_hand_locked)
                self.assertEqual(hand.is_hand_soft, expected_is_hand_soft)

        # Testing first card is 5
        card1 = Card(suit="Diamond", rank="5")
        test_cases = [
            # rank, expected_value, can_double, can_hit, can_split, is_blackjack, is_hand_locked, is_hand_soft
            ("2", 7, True, True, False, False, False, False),
            ("3", 8, True, True, False, False, False, False),
            ("4", 9, True, True, False, False, False, False),
            ("5", 10, True, True, True, False, False, False),
            ("6", 11, True, True, False, False, False, False),
            ("7", 12, True, True, False, False, False, False),
            ("8", 13, True, True, False, False, False, False),
            ("9", 14, True, True, False, False, False, False),
            ("10", 15, True, True, False, False, False, False),
            ("J", 15, True, True, False, False, False, False),
            ("Q", 15, True, True, False, False, False, False),
            ("K", 15, True, True, False, False, False, False),
            ("A", 16, True, True, False, False, False, True),
        ]
        for (
            rank,
            expected_value,
            expected_can_double,
            expected_can_hit,
            expected_can_split,
            expected_is_blackjack,
            expected_is_hand_locked,
            expected_is_hand_soft,
        ) in test_cases:
            with self.subTest(first_card="5", second_card=rank):
                card2 = Card(suit="Heart", rank=rank)
                hand = Hand(wager=1, card1=card1, card2=card2)

                self.assertEqual(hand.value, expected_value)
                self.assertEqual(hand.can_double, expected_can_double)
                self.assertEqual(hand.can_hit, expected_can_hit)
                self.assertEqual(hand.can_split, expected_can_split)
                self.assertEqual(hand.is_blackjack, expected_is_blackjack)
                self.assertEqual(hand.is_hand_locked, expected_is_hand_locked)
                self.assertEqual(hand.is_hand_soft, expected_is_hand_soft)

        # Testing first card is 6
        card1 = Card(suit="Diamond", rank="6")
        test_cases = [
            # rank, expected_value, can_double, can_hit, can_split, is_blackjack, is_hand_locked, is_hand_soft
            ("2", 8, True, True, False, False, False, False),
            ("3", 9, True, True, False, False, False, False),
            ("4", 10, True, True, False, False, False, False),
            ("5", 11, True, True, False, False, False, False),
            ("6", 12, True, True, True, False, False, False),
            ("7", 13, True, True, False, False, False, False),
            ("8", 14, True, True, False, False, False, False),
            ("9", 15, True, True, False, False, False, False),
            ("10", 16, True, True, False, False, False, False),
            ("J", 16, True, True, False, False, False, False),
            ("Q", 16, True, True, False, False, False, False),
            ("K", 16, True, True, False, False, False, False),
            ("A", 17, True, True, False, False, False, True),
        ]
        for (
            rank,
            expected_value,
            expected_can_double,
            expected_can_hit,
            expected_can_split,
            expected_is_blackjack,
            expected_is_hand_locked,
            expected_is_hand_soft,
        ) in test_cases:
            with self.subTest(first_card="6", second_card=rank):
                card2 = Card(suit="Heart", rank=rank)
                hand = Hand(wager=1, card1=card1, card2=card2)

                self.assertEqual(hand.value, expected_value)
                self.assertEqual(hand.can_double, expected_can_double)
                self.assertEqual(hand.can_hit, expected_can_hit)
                self.assertEqual(hand.can_split, expected_can_split)
                self.assertEqual(hand.is_blackjack, expected_is_blackjack)
                self.assertEqual(hand.is_hand_locked, expected_is_hand_locked)
                self.assertEqual(hand.is_hand_soft, expected_is_hand_soft)

        # Testing first card is 7
        card1 = Card(suit="Diamond", rank="7")
        test_cases = [
            # rank, expected_value, can_double, can_hit, can_split, is_blackjack, is_hand_locked, is_hand_soft
            ("2", 9, True, True, False, False, False, False),
            ("3", 10, True, True, False, False, False, False),
            ("4", 11, True, True, False, False, False, False),
            ("5", 12, True, True, False, False, False, False),
            ("6", 13, True, True, False, False, False, False),
            ("7", 14, True, True, True, False, False, False),
            ("8", 15, True, True, False, False, False, False),
            ("9", 16, True, True, False, False, False, False),
            ("10", 17, True, True, False, False, False, False),
            ("J", 17, True, True, False, False, False, False),
            ("Q", 17, True, True, False, False, False, False),
            ("K", 17, True, True, False, False, False, False),
            ("A", 18, True, True, False, False, False, True),
        ]
        for (
            rank,
            expected_value,
            expected_can_double,
            expected_can_hit,
            expected_can_split,
            expected_is_blackjack,
            expected_is_hand_locked,
            expected_is_hand_soft,
        ) in test_cases:
            with self.subTest(first_card="7", second_card=rank):
                card2 = Card(suit="Heart", rank=rank)
                hand = Hand(wager=1, card1=card1, card2=card2)

                self.assertEqual(hand.value, expected_value)
                self.assertEqual(hand.can_double, expected_can_double)
                self.assertEqual(hand.can_hit, expected_can_hit)
                self.assertEqual(hand.can_split, expected_can_split)
                self.assertEqual(hand.is_blackjack, expected_is_blackjack)
                self.assertEqual(hand.is_hand_locked, expected_is_hand_locked)
                self.assertEqual(hand.is_hand_soft, expected_is_hand_soft)

        # Testing first card is 8
        card1 = Card(suit="Diamond", rank="8")
        test_cases = [
            # rank, expected_value, can_double, can_hit, can_split, is_blackjack, is_hand_locked, is_hand_soft
            ("2", 10, True, True, False, False, False, False),
            ("3", 11, True, True, False, False, False, False),
            ("4", 12, True, True, False, False, False, False),
            ("5", 13, True, True, False, False, False, False),
            ("6", 14, True, True, False, False, False, False),
            ("7", 15, True, True, False, False, False, False),
            ("8", 16, True, True, True, False, False, False),
            ("9", 17, True, True, False, False, False, False),
            ("10", 18, True, True, False, False, False, False),
            ("J", 18, True, True, False, False, False, False),
            ("Q", 18, True, True, False, False, False, False),
            ("K", 18, True, True, False, False, False, False),
            ("A", 19, True, True, False, False, False, True),
        ]
        for (
            rank,
            expected_value,
            expected_can_double,
            expected_can_hit,
            expected_can_split,
            expected_is_blackjack,
            expected_is_hand_locked,
            expected_is_hand_soft,
        ) in test_cases:
            with self.subTest(first_card="8", second_card=rank):
                card2 = Card(suit="Heart", rank=rank)
                hand = Hand(wager=1, card1=card1, card2=card2)

                self.assertEqual(hand.value, expected_value)
                self.assertEqual(hand.can_double, expected_can_double)
                self.assertEqual(hand.can_hit, expected_can_hit)
                self.assertEqual(hand.can_split, expected_can_split)
                self.assertEqual(hand.is_blackjack, expected_is_blackjack)
                self.assertEqual(hand.is_hand_locked, expected_is_hand_locked)
                self.assertEqual(hand.is_hand_soft, expected_is_hand_soft)

        # Testing first card is 9
        card1 = Card(suit="Diamond", rank="9")
        test_cases = [
            # rank, expected_value, can_double, can_hit, can_split, is_blackjack, is_hand_locked, is_hand_soft
            ("2", 11, True, True, False, False, False, False),
            ("3", 12, True, True, False, False, False, False),
            ("4", 13, True, True, False, False, False, False),
            ("5", 14, True, True, False, False, False, False),
            ("6", 15, True, True, False, False, False, False),
            ("7", 16, True, True, False, False, False, False),
            ("8", 17, True, True, False, False, False, False),
            ("9", 18, True, True, True, False, False, False),
            ("10", 19, True, True, False, False, False, False),
            ("J", 19, True, True, False, False, False, False),
            ("Q", 19, True, True, False, False, False, False),
            ("K", 19, True, True, False, False, False, False),
            ("A", 20, True, True, False, False, False, True),
        ]
        for (
            rank,
            expected_value,
            expected_can_double,
            expected_can_hit,
            expected_can_split,
            expected_is_blackjack,
            expected_is_hand_locked,
            expected_is_hand_soft,
        ) in test_cases:
            with self.subTest(first_card="9", second_card=rank):
                card2 = Card(suit="Heart", rank=rank)
                hand = Hand(wager=1, card1=card1, card2=card2)

                self.assertEqual(hand.value, expected_value)
                self.assertEqual(hand.can_double, expected_can_double)
                self.assertEqual(hand.can_hit, expected_can_hit)
                self.assertEqual(hand.can_split, expected_can_split)
                self.assertEqual(hand.is_blackjack, expected_is_blackjack)
                self.assertEqual(hand.is_hand_locked, expected_is_hand_locked)
                self.assertEqual(hand.is_hand_soft, expected_is_hand_soft)

        # Testing first card is 10
        card1 = Card(suit="Diamond", rank="10")
        test_cases = [
            # rank, expected_value, can_double, can_hit, can_split, is_blackjack, is_hand_locked, is_hand_soft
            ("2", 12, True, True, False, False, False, False),
            ("3", 13, True, True, False, False, False, False),
            ("4", 14, True, True, False, False, False, False),
            ("5", 15, True, True, False, False, False, False),
            ("6", 16, True, True, False, False, False, False),
            ("7", 17, True, True, False, False, False, False),
            ("8", 18, True, True, False, False, False, False),
            ("9", 19, True, True, False, False, False, False),
            ("10", 20, True, True, True, False, False, False),
            ("J", 20, True, True, False, False, False, False),
            ("Q", 20, True, True, False, False, False, False),
            ("K", 20, True, True, False, False, False, False),
            ("A", 21, False, False, False, True, True, True),
        ]
        for (
            rank,
            expected_value,
            expected_can_double,
            expected_can_hit,
            expected_can_split,
            expected_is_blackjack,
            expected_is_hand_locked,
            expected_is_hand_soft,
        ) in test_cases:
            with self.subTest(first_card="10", second_card=rank):
                card2 = Card(suit="Heart", rank=rank)
                hand = Hand(wager=1, card1=card1, card2=card2)

                self.assertEqual(hand.value, expected_value)
                self.assertEqual(hand.can_double, expected_can_double)
                self.assertEqual(hand.can_hit, expected_can_hit)
                self.assertEqual(hand.can_split, expected_can_split)
                self.assertEqual(hand.is_blackjack, expected_is_blackjack)
                self.assertEqual(hand.is_hand_locked, expected_is_hand_locked)
                self.assertEqual(hand.is_hand_soft, expected_is_hand_soft)

        # Testing first card is J
        card1 = Card(suit="Diamond", rank="J")
        test_cases = [
            # rank, expected_value, can_double, can_hit, can_split, is_blackjack, is_hand_locked, is_hand_soft
            ("2", 12, True, True, False, False, False, False),
            ("3", 13, True, True, False, False, False, False),
            ("4", 14, True, True, False, False, False, False),
            ("5", 15, True, True, False, False, False, False),
            ("6", 16, True, True, False, False, False, False),
            ("7", 17, True, True, False, False, False, False),
            ("8", 18, True, True, False, False, False, False),
            ("9", 19, True, True, False, False, False, False),
            ("10", 20, True, True, False, False, False, False),
            ("J", 20, True, True, True, False, False, False),
            ("Q", 20, True, True, False, False, False, False),
            ("K", 20, True, True, False, False, False, False),
            ("A", 21, False, False, False, True, True, True),
        ]
        for (
            rank,
            expected_value,
            expected_can_double,
            expected_can_hit,
            expected_can_split,
            expected_is_blackjack,
            expected_is_hand_locked,
            expected_is_hand_soft,
        ) in test_cases:
            with self.subTest(first_card="J", second_card=rank):
                card2 = Card(suit="Heart", rank=rank)
                hand = Hand(wager=1, card1=card1, card2=card2)

                self.assertEqual(hand.value, expected_value)
                self.assertEqual(hand.can_double, expected_can_double)
                self.assertEqual(hand.can_hit, expected_can_hit)
                self.assertEqual(hand.can_split, expected_can_split)
                self.assertEqual(hand.is_blackjack, expected_is_blackjack)
                self.assertEqual(hand.is_hand_locked, expected_is_hand_locked)
                self.assertEqual(hand.is_hand_soft, expected_is_hand_soft)

        # Testing first card is Q
        card1 = Card(suit="Diamond", rank="Q")
        test_cases = [
            # rank, expected_value, can_double, can_hit, can_split, is_blackjack, is_hand_locked, is_hand_soft
            ("2", 12, True, True, False, False, False, False),
            ("3", 13, True, True, False, False, False, False),
            ("4", 14, True, True, False, False, False, False),
            ("5", 15, True, True, False, False, False, False),
            ("6", 16, True, True, False, False, False, False),
            ("7", 17, True, True, False, False, False, False),
            ("8", 18, True, True, False, False, False, False),
            ("9", 19, True, True, False, False, False, False),
            ("10", 20, True, True, False, False, False, False),
            ("J", 20, True, True, False, False, False, False),
            ("Q", 20, True, True, True, False, False, False),
            ("K", 20, True, True, False, False, False, False),
            ("A", 21, False, False, False, True, True, True),
        ]
        for (
            rank,
            expected_value,
            expected_can_double,
            expected_can_hit,
            expected_can_split,
            expected_is_blackjack,
            expected_is_hand_locked,
            expected_is_hand_soft,
        ) in test_cases:
            with self.subTest(first_card="Q", second_card=rank):
                card2 = Card(suit="Heart", rank=rank)
                hand = Hand(wager=1, card1=card1, card2=card2)

                self.assertEqual(hand.value, expected_value)
                self.assertEqual(hand.can_double, expected_can_double)
                self.assertEqual(hand.can_hit, expected_can_hit)
                self.assertEqual(hand.can_split, expected_can_split)
                self.assertEqual(hand.is_blackjack, expected_is_blackjack)
                self.assertEqual(hand.is_hand_locked, expected_is_hand_locked)
                self.assertEqual(hand.is_hand_soft, expected_is_hand_soft)

        # Testing first card is K
        card1 = Card(suit="Diamond", rank="K")
        test_cases = [
            # rank, expected_value, can_double, can_hit, can_split, is_blackjack, is_hand_locked, is_hand_soft
            ("2", 12, True, True, False, False, False, False),
            ("3", 13, True, True, False, False, False, False),
            ("4", 14, True, True, False, False, False, False),
            ("5", 15, True, True, False, False, False, False),
            ("6", 16, True, True, False, False, False, False),
            ("7", 17, True, True, False, False, False, False),
            ("8", 18, True, True, False, False, False, False),
            ("9", 19, True, True, False, False, False, False),
            ("10", 20, True, True, False, False, False, False),
            ("J", 20, True, True, False, False, False, False),
            ("Q", 20, True, True, False, False, False, False),
            ("K", 20, True, True, True, False, False, False),
            ("A", 21, False, False, False, True, True, True),
        ]
        for (
            rank,
            expected_value,
            expected_can_double,
            expected_can_hit,
            expected_can_split,
            expected_is_blackjack,
            expected_is_hand_locked,
            expected_is_hand_soft,
        ) in test_cases:
            with self.subTest(first_card="K", second_card=rank):
                card2 = Card(suit="Heart", rank=rank)
                hand = Hand(wager=1, card1=card1, card2=card2)

                self.assertEqual(hand.value, expected_value)
                self.assertEqual(hand.can_double, expected_can_double)
                self.assertEqual(hand.can_hit, expected_can_hit)
                self.assertEqual(hand.can_split, expected_can_split)
                self.assertEqual(hand.is_blackjack, expected_is_blackjack)
                self.assertEqual(hand.is_hand_locked, expected_is_hand_locked)
                self.assertEqual(hand.is_hand_soft, expected_is_hand_soft)

        # Testing first card is 10
        card1 = Card(suit="Diamond", rank="A")
        test_cases = [
            # rank, expected_value, can_double, can_hit, can_split, is_blackjack, is_hand_locked, is_hand_soft
            ("2", 13, True, True, False, False, False, True),
            ("3", 14, True, True, False, False, False, True),
            ("4", 15, True, True, False, False, False, True),
            ("5", 16, True, True, False, False, False, True),
            ("6", 17, True, True, False, False, False, True),
            ("7", 18, True, True, False, False, False, True),
            ("8", 19, True, True, False, False, False, True),
            ("9", 20, True, True, False, False, False, True),
            ("10", 21, False, False, False, True, True, True),
            ("J", 21, False, False, False, True, True, True),
            ("Q", 21, False, False, False, True, True, True),
            ("K", 21, False, False, False, True, True, True),
            ("A", 12, True, True, True, False, False, True),
        ]
        for (
            rank,
            expected_value,
            expected_can_double,
            expected_can_hit,
            expected_can_split,
            expected_is_blackjack,
            expected_is_hand_locked,
            expected_is_hand_soft,
        ) in test_cases:
            with self.subTest(first_card="A", second_card=rank):
                card2 = Card(suit="Heart", rank=rank)
                hand = Hand(wager=1, card1=card1, card2=card2)

                self.assertEqual(hand.value, expected_value)
                self.assertEqual(hand.can_double, expected_can_double)
                self.assertEqual(hand.can_hit, expected_can_hit)
                self.assertEqual(hand.can_split, expected_can_split)
                self.assertEqual(hand.is_blackjack, expected_is_blackjack)
                self.assertEqual(hand.is_hand_locked, expected_is_hand_locked)
                self.assertEqual(hand.is_hand_soft, expected_is_hand_soft)

    def test_hit(self):

        # Build a mock hand
        card1 = Card(suit="Diamond", rank="4")
        card2 = Card(suit="Heart", rank="5")
        hand = Hand(wager=1, card1=card1, card2=card2)

        # Assert prior to split
        self.assertEqual(hand.can_hit, True)
        self.assertEqual(hand.value, 9)

        new_card = Card(suit="Club", rank="A")
        hand.hit(new_card)

        # Post hit asserts
        self.assertEqual(hand.can_hit, True)
        self.assertEqual(hand.value, 20)
        self.assertEqual(hand.wager, 1)
        self.assertEqual(len(hand.cards), 3)

    def test_splitting(self):

        # Build a mock hand
        card1 = Card(suit="Diamond", rank="2")
        card2 = Card(suit="Heart", rank="2")
        hand1 = Hand(wager=1, card1=card1, card2=card2)

        # Assert prior to split
        self.assertEqual(hand1.can_split, True)
        self.assertEqual(hand1.value, 4)

        # Perform a split
        card1 = Card(suit="Club", rank="5")
        card2 = Card(suit="Spade", rank="10")
        hand2 = hand1.split(card1, card2)

        # Post split asserts
        self.assertEqual(hand1.value, 7)
        self.assertEqual(hand2.value, 12)
        self.assertEqual(len(hand1.cards), 2)
        self.assertEqual(len(hand2.cards), 2)
        self.assertEqual(hand1.cards[0].rank, "2")
        self.assertEqual(hand1.cards[1].rank, "5")
        self.assertEqual(hand2.cards[0].rank, "2")
        self.assertEqual(hand2.cards[1].rank, "10")

        # Splitting Aces (can only split ones)
        card1 = Card(suit="Spade", rank="A")
        card2 = Card(suit="Spade", rank="A")
        hand1 = Hand(wager=1, card1=card1, card2=card2)

        # Pre-split asserts
        self.assertEqual(hand1.value, 12)
        self.assertEqual(hand1.can_split, True)

        # Perform split
        card1 = Card(suit="Club", rank="A")
        card2 = Card(suit="Club", rank="10")
        hand2 = hand1.split(card1=card1, card2=card2)

        # Post-split asserts
        self.assertEqual(hand1.value, 12)
        self.assertEqual(hand1.can_split, False)
        self.assertEqual(hand1.can_hit, False)
        self.assertEqual(hand1.can_double, False)
        self.assertEqual(hand1.is_hand_locked, True)
        self.assertEqual(hand2.value, 21)
        self.assertEqual(hand2.can_split, False)
        self.assertEqual(hand2.can_hit, False)
        self.assertEqual(hand2.can_double, False)
        self.assertEqual(hand2.is_hand_locked, True)

    def test_doubling(self):

        # Build a mock hand
        card1 = Card(suit="Diamond", rank="3")
        card2 = Card(suit="Heart", rank="8")
        hand = Hand(wager=1, card1=card1, card2=card2)

        # Assert prior to split
        self.assertEqual(hand.can_double, True)
        self.assertEqual(hand.value, 11)
        self.assertEqual(hand.wager, 1)

        # Perform doubleing down action
        card = Card(suit="Spade", rank="10")
        hand.double(card)

        # Post double asserts
        self.assertEqual(hand.value, 21)
        self.assertEqual(hand.can_double, False)
        self.assertEqual(hand.wager, 2)
        self.assertEqual(hand.is_hand_locked, True)
        self.assertEqual(hand.is_blackjack, False)
        self.assertEqual(len(hand.cards), 3)

    def test_stand(self):

        # Build the hand
        card1 = Card(suit="Diamond", rank="10")
        card2 = Card(suit="Club", rank="9")
        hand = Hand(wager=1, card1=card1, card2=card2)

        # Pre-stand asserts
        self.assertEqual(hand.value, 19)
        self.assertEqual(hand.is_hand_locked, False)

        # Perform saction
        hand.stand()

        # Check
        self.assertEqual(hand.value, 19)
        self.assertEqual(hand.is_hand_locked, True)


if __name__ == "__main__":
    unittest.main()
