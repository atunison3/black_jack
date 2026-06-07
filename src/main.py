import argparse

import matplotlib.pyplot as plt  # noqa: F401

from domain import Shoe, Player, Dealer, decide_winner, get_hand_state
from player_actions import decide_player_action
from helper_functions import format_cell

parser = argparse.ArgumentParser()

parser.add_argument("--upcard", type=int)
args = parser.parse_args()


def colorize(suit: str) -> str:
    """Return a suit string with terminal coloring."""
    colors = {
        "H": "\033[91m",  # red
        "D": "\033[94m",  # blue
        "S": "\033[93m",  # yellow
        "P": "\033[92m",  # green
    }

    reset = "\033[0m"
    color = colors.get(suit, "")

    return f"{color}{suit}{reset}" if color else suit


def game_round(state_, dv_, posneg_):

    player_cash = 1000
    wager = 10

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
            # action_ = colorize(action)
            if state == state_ and dealer.upcard == dv_ and ["NEG", "POS"][count > 0] == posneg_:
                return action

            shoe = player.take_action(action, shoe)

        while dealer.should_hit(player):
            shoe = dealer.hit(shoe)

        for hand in player.hands:
            winnings = decide_winner(hand, dealer)
            player.cash += winnings

    return None


table = []
values = set()
states = ["62", "53", "44", "9", "10", "11", "A2", "A3", "A4", "A5", "A6", "A7", "A8"]
states = ["12", "13", "14", "15", "16", "A7"]
states = ["AA", "22", "33", "66", "77", "88", "99"]
for state_ in states:
    row = []
    for dv_ in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
        pos = None
        neg = None
        while not pos:
            pos = game_round(state_, dv_, "POS")
        while not neg:
            neg = game_round(state_, dv_, "NEG")
        row.append(" ".join([pos, neg]))
    table.append(row)
    for thing in row:
        values.add(thing)


print()
pipe = format_cell("|")
header = pipe.join([format_cell(i) for i in [" ", "2", "3", "4", "5", "6", "7", "8", "9", "10", "A"]])

print(header)
for state_, row in zip(states, table):
    print(pipe.join([format_cell(i) for i in [state_] + row]))

print()
# print(f"    |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  |  A  |")
# for s, row in zip(states, table):
#     stuff = [format_suits(i) for i in row]
#     line = f" {s:>2} | " + "|".join([format_suits(i) for i in row])

#     print(line)
#     print('-' * 64)

# for i in values:
#     print(i, repr(i))


# 'S H'   # prints white background with black text " S H "
# 'S S'   # prints yellow background with balck text = "  S  "
# 'H H'   # prints red background with black text = "  H  "
# 'D S'   # prints white background with black text = " D S "
# 'D D'   # prints blue background with black text = "  D  "
# 'D H'   # prints white background with black text = " D H "
# '2'     # prints white background with black text = '  2  '
# '3'     # prints white background with black text = '  3  '
# '4'     # prints white background with black text = '  4  '
# '5'     # prints white background with black text = '  5  '
# '6'     # prints white background with black text = '  6  '
# '7'     # prints white background with black text = '  7  '
# '8'     # prints white background with black text = '  8  '
# '9'     # prints white background with black text = '  9  '
# '10'     # prints white background with black text = ' 10  '
# '11'     # prints white background with black text = ' 11  '
# '|'     # prints white background with black text = '|'
# literally anything (x)  # prints white background with black text = " {x:>2} "
