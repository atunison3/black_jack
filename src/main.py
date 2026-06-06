from domain import Shoe, Hand  # noqa: F401  # Still developing


count = 0
while count < 2**32 - 1:
    shoe = Shoe(num_decks=1, random_state=count)

    card1 = shoe.draw()
    card2 = shoe.draw()
    card3 = shoe.draw()
    card4 = shoe.draw()

    player = Hand(wager=1, card1=card1, card2=card3)
    dealer = Hand(wager=1, card1=card2, card2=card4)

    if dealer.value in [21]:

        print(count)
        break

    count += 1

print("Player:")
for card in player.cards:
    print(f"\t{card}")
print("Dealer:")
for card in dealer.cards:
    print(f"\t{card}")
