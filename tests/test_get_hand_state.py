import unittest

from src.domain import Card, Hand, get_hand_state


class TestGetHandState(unittest.TestCase):

    def test_01_hit_stand(self):

        # 12
        cards = {
            r: Card(suit="Spade", rank=r) for r in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        }

        # 12
        hand = Hand(wager=1, card1=cards["2"], card2=cards["10"])
        self.assertEqual(get_hand_state(hand), "12")
        hand = Hand(wager=1, card1=cards["2"], card2=cards["J"])
        self.assertEqual(get_hand_state(hand), "12")
        hand = Hand(wager=1, card1=cards["2"], card2=cards["Q"])
        self.assertEqual(get_hand_state(hand), "12")
        hand = Hand(wager=1, card1=cards["2"], card2=cards["K"])
        self.assertEqual(get_hand_state(hand), "12")
        hand = Hand(wager=1, card1=cards["3"], card2=cards["9"])
        self.assertEqual(get_hand_state(hand), "12")
        hand = Hand(wager=1, card1=cards["4"], card2=cards["8"])
        self.assertEqual(get_hand_state(hand), "12")
        hand = Hand(wager=1, card1=cards["5"], card2=cards["7"])
        self.assertEqual(get_hand_state(hand), "12")

        # 13
        hand = Hand(wager=1, card1=cards["3"], card2=cards["10"])
        self.assertEqual(get_hand_state(hand), "13")
        hand = Hand(wager=1, card1=cards["3"], card2=cards["J"])
        self.assertEqual(get_hand_state(hand), "13")
        hand = Hand(wager=1, card1=cards["3"], card2=cards["Q"])
        self.assertEqual(get_hand_state(hand), "13")
        hand = Hand(wager=1, card1=cards["3"], card2=cards["K"])
        self.assertEqual(get_hand_state(hand), "13")
        hand = Hand(wager=1, card1=cards["4"], card2=cards["9"])
        self.assertEqual(get_hand_state(hand), "13")
        hand = Hand(wager=1, card1=cards["5"], card2=cards["8"])
        self.assertEqual(get_hand_state(hand), "13")
        hand = Hand(wager=1, card1=cards["6"], card2=cards["7"])
        self.assertEqual(get_hand_state(hand), "13")

        # 14
        hand = Hand(wager=1, card1=cards["4"], card2=cards["10"])
        self.assertEqual(get_hand_state(hand), "14")
        hand = Hand(wager=1, card1=cards["4"], card2=cards["J"])
        self.assertEqual(get_hand_state(hand), "14")
        hand = Hand(wager=1, card1=cards["4"], card2=cards["Q"])
        self.assertEqual(get_hand_state(hand), "14")
        hand = Hand(wager=1, card1=cards["4"], card2=cards["K"])
        self.assertEqual(get_hand_state(hand), "14")
        hand = Hand(wager=1, card1=cards["5"], card2=cards["9"])
        self.assertEqual(get_hand_state(hand), "14")
        hand = Hand(wager=1, card1=cards["6"], card2=cards["8"])
        self.assertEqual(get_hand_state(hand), "14")

        # 15
        hand = Hand(wager=1, card1=cards["5"], card2=cards["10"])
        self.assertEqual(get_hand_state(hand), "15")
        hand = Hand(wager=1, card1=cards["5"], card2=cards["J"])
        self.assertEqual(get_hand_state(hand), "15")
        hand = Hand(wager=1, card1=cards["5"], card2=cards["Q"])
        self.assertEqual(get_hand_state(hand), "15")
        hand = Hand(wager=1, card1=cards["5"], card2=cards["K"])
        self.assertEqual(get_hand_state(hand), "15")
        hand = Hand(wager=1, card1=cards["6"], card2=cards["9"])
        self.assertEqual(get_hand_state(hand), "15")
        hand = Hand(wager=1, card1=cards["7"], card2=cards["8"])
        self.assertEqual(get_hand_state(hand), "15")

        # 16
        hand = Hand(wager=1, card1=cards["6"], card2=cards["10"])
        self.assertEqual(get_hand_state(hand), "16")
        hand = Hand(wager=1, card1=cards["6"], card2=cards["J"])
        self.assertEqual(get_hand_state(hand), "16")
        hand = Hand(wager=1, card1=cards["6"], card2=cards["Q"])
        self.assertEqual(get_hand_state(hand), "16")
        hand = Hand(wager=1, card1=cards["6"], card2=cards["K"])
        self.assertEqual(get_hand_state(hand), "16")
        hand = Hand(wager=1, card1=cards["7"], card2=cards["9"])
        self.assertEqual(get_hand_state(hand), "16")

        # A7
        hand = Hand(wager=1, card1=cards["A"], card2=cards["7"])
        self.assertEqual(get_hand_state(hand), "A7")
        hand = Hand(wager=1, card1=cards["7"], card2=cards["A"])
        self.assertEqual(get_hand_state(hand), "A7")

    def test_02_split_pairs(self):

        # 12
        cards = {
            r: Card(suit="Spade", rank=r) for r in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        }

        # AA
        hand = Hand(wager=1, card1=cards["A"], card2=cards["A"])
        self.assertEqual(get_hand_state(hand), "AA")

        # 22
        hand = Hand(wager=1, card1=cards["2"], card2=cards["2"])
        self.assertEqual(get_hand_state(hand), "22")

        # AA
        hand = Hand(wager=1, card1=cards["3"], card2=cards["3"])
        self.assertEqual(get_hand_state(hand), "33")

        # AA
        hand = Hand(wager=1, card1=cards["6"], card2=cards["6"])
        self.assertEqual(get_hand_state(hand), "66")

        # AA
        hand = Hand(wager=1, card1=cards["7"], card2=cards["7"])
        self.assertEqual(get_hand_state(hand), "77")

        # AA
        hand = Hand(wager=1, card1=cards["8"], card2=cards["8"])
        self.assertEqual(get_hand_state(hand), "88")

        # AA
        hand = Hand(wager=1, card1=cards["9"], card2=cards["9"])
        self.assertEqual(get_hand_state(hand), "99")

    def test_03_double_down(self):

        cards = {
            r: Card(suit="Spade", rank=r) for r in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        }

        # 62
        hand = Hand(wager=1, card1=cards["6"], card2=cards["2"])
        self.assertEqual(get_hand_state(hand), "62")
        hand = Hand(wager=1, card1=cards["2"], card2=cards["6"])
        self.assertEqual(get_hand_state(hand), "62")
        hand = Hand(wager=1, card1=cards["A"], card2=cards["7"])
        self.assertNotEqual(get_hand_state(hand), "62")

        # 53
        hand = Hand(wager=1, card1=cards["5"], card2=cards["3"])
        self.assertEqual(get_hand_state(hand), "53")
        hand = Hand(wager=1, card1=cards["3"], card2=cards["5"])
        self.assertEqual(get_hand_state(hand), "53")
        hand = Hand(wager=1, card1=cards["7"], card2=cards["A"])
        self.assertNotEqual(get_hand_state(hand), "53")

        # 44
        hand = Hand(wager=1, card1=cards["4"], card2=cards["4"])
        self.assertEqual(get_hand_state(hand), "44")

        # 9
        hand = Hand(wager=1, card1=cards["A"], card2=cards["8"])
        self.assertNotEqual(get_hand_state(hand), "9")
        hand = Hand(wager=1, card1=cards["2"], card2=cards["7"])
        self.assertEqual(get_hand_state(hand), "9")
        hand = Hand(wager=1, card1=cards["3"], card2=cards["6"])
        self.assertEqual(get_hand_state(hand), "9")
        hand = Hand(wager=1, card1=cards["4"], card2=cards["5"])
        self.assertEqual(get_hand_state(hand), "9")
        hand = Hand(wager=1, card1=cards["5"], card2=cards["4"])
        self.assertEqual(get_hand_state(hand), "9")
        hand = Hand(wager=1, card1=cards["6"], card2=cards["3"])
        self.assertEqual(get_hand_state(hand), "9")
        hand = Hand(wager=1, card1=cards["7"], card2=cards["2"])
        self.assertEqual(get_hand_state(hand), "9")
        hand = Hand(wager=1, card1=cards["8"], card2=cards["A"])
        self.assertNotEqual(get_hand_state(hand), "9")

        # 10
        hand = Hand(wager=1, card1=cards["A"], card2=cards["9"])
        self.assertNotEqual(get_hand_state(hand), "10")
        hand = Hand(wager=1, card1=cards["2"], card2=cards["8"])
        self.assertEqual(get_hand_state(hand), "10")
        hand = Hand(wager=1, card1=cards["3"], card2=cards["7"])
        self.assertEqual(get_hand_state(hand), "10")
        hand = Hand(wager=1, card1=cards["4"], card2=cards["6"])
        self.assertEqual(get_hand_state(hand), "10")
        hand = Hand(wager=1, card1=cards["5"], card2=cards["5"])
        self.assertEqual(get_hand_state(hand), "10")
        hand = Hand(wager=1, card1=cards["6"], card2=cards["4"])
        self.assertEqual(get_hand_state(hand), "10")
        hand = Hand(wager=1, card1=cards["7"], card2=cards["3"])
        self.assertEqual(get_hand_state(hand), "10")
        hand = Hand(wager=1, card1=cards["9"], card2=cards["A"])
        self.assertNotEqual(get_hand_state(hand), "10")

        # 11
        hand = Hand(wager=1, card1=cards["A"], card2=cards["10"])
        self.assertNotEqual(get_hand_state(hand), "11")
        hand = Hand(wager=1, card1=cards["A"], card2=cards["J"])
        self.assertNotEqual(get_hand_state(hand), "11")
        hand = Hand(wager=1, card1=cards["A"], card2=cards["Q"])
        self.assertNotEqual(get_hand_state(hand), "11")
        hand = Hand(wager=1, card1=cards["A"], card2=cards["K"])
        self.assertNotEqual(get_hand_state(hand), "11")
        hand = Hand(wager=1, card1=cards["2"], card2=cards["9"])
        self.assertEqual(get_hand_state(hand), "11")
        hand = Hand(wager=1, card1=cards["3"], card2=cards["8"])
        self.assertEqual(get_hand_state(hand), "11")
        hand = Hand(wager=1, card1=cards["4"], card2=cards["7"])
        self.assertEqual(get_hand_state(hand), "11")
        hand = Hand(wager=1, card1=cards["5"], card2=cards["6"])
        self.assertEqual(get_hand_state(hand), "11")
        hand = Hand(wager=1, card1=cards["6"], card2=cards["5"])
        self.assertEqual(get_hand_state(hand), "11")
        hand = Hand(wager=1, card1=cards["7"], card2=cards["4"])
        self.assertEqual(get_hand_state(hand), "11")
        hand = Hand(wager=1, card1=cards["8"], card2=cards["3"])
        self.assertEqual(get_hand_state(hand), "11")
        hand = Hand(wager=1, card1=cards["9"], card2=cards["2"])
        self.assertEqual(get_hand_state(hand), "11")

        # A2
        hand = Hand(wager=1, card1=cards["A"], card2=cards["2"])
        self.assertEqual(get_hand_state(hand), "A2")
        hand = Hand(wager=1, card1=cards["2"], card2=cards["A"])
        self.assertEqual(get_hand_state(hand), "A2")

        # A3
        hand = Hand(wager=1, card1=cards["A"], card2=cards["3"])
        self.assertEqual(get_hand_state(hand), "A3")
        hand = Hand(wager=1, card1=cards["3"], card2=cards["A"])
        self.assertEqual(get_hand_state(hand), "A3")

        # A4
        hand = Hand(wager=1, card1=cards["A"], card2=cards["4"])
        self.assertEqual(get_hand_state(hand), "A4")
        hand = Hand(wager=1, card1=cards["4"], card2=cards["A"])
        self.assertEqual(get_hand_state(hand), "A4")

        # A5
        hand = Hand(wager=1, card1=cards["A"], card2=cards["5"])
        self.assertEqual(get_hand_state(hand), "A5")
        hand = Hand(wager=1, card1=cards["5"], card2=cards["A"])
        self.assertEqual(get_hand_state(hand), "A5")

        # A6
        hand = Hand(wager=1, card1=cards["A"], card2=cards["6"])
        self.assertEqual(get_hand_state(hand), "A6")
        hand = Hand(wager=1, card1=cards["6"], card2=cards["A"])
        self.assertEqual(get_hand_state(hand), "A6")

        # A7
        hand = Hand(wager=1, card1=cards["A"], card2=cards["7"])
        self.assertEqual(get_hand_state(hand), "A7")
        hand = Hand(wager=1, card1=cards["7"], card2=cards["A"])
        self.assertEqual(get_hand_state(hand), "A7")

        # A8
        hand = Hand(wager=1, card1=cards["A"], card2=cards["8"])
        self.assertEqual(get_hand_state(hand), "A8")
        hand = Hand(wager=1, card1=cards["8"], card2=cards["A"])
        self.assertEqual(get_hand_state(hand), "A8")

    def test_04_standing_states(self):

        cards = {
            r: Card(suit="Spade", rank=r) for r in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        }

        #
        for rank in ["7", "8", "9", "10", "J", "Q", "K", "A"]:
            hand = Hand(wager=1, card1=cards[rank], card2=cards["10"])
            self.assertEqual(get_hand_state(hand), "17")
            hand = Hand(wager=1, card1=cards[rank], card2=cards["J"])
            self.assertEqual(get_hand_state(hand), "17")
            hand = Hand(wager=1, card1=cards[rank], card2=cards["Q"])
            self.assertEqual(get_hand_state(hand), "17")
            hand = Hand(wager=1, card1=cards[rank], card2=cards["K"])
            self.assertEqual(get_hand_state(hand), "17")

    def test_05_hitting_states(self):

        cards = {
            r: Card(suit="Spade", rank=r) for r in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        }

        #
        hand = Hand(wager=1, card1=cards["2"], card2=cards["3"])
        self.assertEqual(get_hand_state(hand), "7")
        hand = Hand(wager=1, card1=cards["2"], card2=cards["4"])
        self.assertEqual(get_hand_state(hand), "7")
        hand = Hand(wager=1, card1=cards["2"], card2=cards["5"])
        self.assertEqual(get_hand_state(hand), "7")
        hand = Hand(wager=1, card1=cards["3"], card2=cards["2"])
        self.assertEqual(get_hand_state(hand), "7")
        hand = Hand(wager=1, card1=cards["3"], card2=cards["4"])
        self.assertEqual(get_hand_state(hand), "7")
        hand = Hand(wager=1, card1=cards["5"], card2=cards["2"])
        self.assertEqual(get_hand_state(hand), "7")
        hand = Hand(wager=1, card1=cards["A"], card2=cards["6"])
        self.assertNotEqual(get_hand_state(hand), "7")


if __name__ == "__main__":
    unittest.main()
