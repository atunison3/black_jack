import matplotlib.pyplot as plt  # noqa: F401

from domain import Shoe, Player, Dealer, decide_winner, get_hand_state
from player_actions import decide_player_action


def game_round(wager: int = 10, player_cash: int = 300):

    # Initiate player
    player = Player(player_cash)

    shoe = Shoe(num_decks=2)

    while (shoe.is_active) and (player.cash >= wager):

        # Dish out initial cards
        card1 = shoe.draw()
        card2 = shoe.draw()
        card3 = shoe.draw()
        card4 = shoe.draw(is_visible=False)  # Dealer's down card (not visible)
        player.deal(10, card1, card3)
        dealer = Dealer(card2, card4)

        # Player makes their moves
        while player.still_active:
            state = get_hand_state(player.hands[player.active_hand])
            count = shoe.count
            action = decide_player_action(state, dealer, count)
            print(f"\t{state:>2}   {dealer.upcard:>2}   {['NEG', 'POS'][count>0]:>3}  {action}")
            shoe = player.take_action(action, shoe)

        while dealer.should_hit(player):
            shoe = dealer.hit(shoe)

        for hand in player.hands:
            winnings = decide_winner(hand, dealer)
            player.cash += winnings


game_round()
