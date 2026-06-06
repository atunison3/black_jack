from domain import Shoe, Player, decide_player_action, Dealer, decide_winner


def shoe_round(player_cash: int):

    player = Player(player_cash)

    shoe = Shoe(num_decks=2)

    while (shoe.is_active) and (player.cash > 0):

        # Dish out initial cards
        card1 = shoe.draw()
        card2 = shoe.draw()
        card3 = shoe.draw()
        card4 = shoe.draw(is_visible=False)  # Dealer's down card (not visible)
        player.deal(10, card1, card3)
        dealer = Dealer(card2, card4)

        # Player makes their moves
        while player.still_active:
            action = decide_player_action(player.hands[player.active_hand], dealer)
            shoe = player.take_action(action, shoe)

        while dealer.should_hit(player):
            shoe = dealer.hit(shoe)

        for hand in player.hands:
            winnings = decide_winner(hand, dealer)
            player.cash += winnings

        print(player.cash)


shoe_round(300)
