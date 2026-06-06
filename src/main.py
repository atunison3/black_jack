from domain import Shoe, Hand  # noqa: F401  # Still developing


count = 0
while count < 2**32 - 1:
    shoe = Shoe(num_decks=1, random_state=count)

    if (card1 := shoe.draw()).rank != "A":
        count += 1
        continue

    card2 = shoe.draw()  # Dealer
    if (card3 := shoe.draw()).rank != "A":
        count += 1
        continue

    card4 = shoe.draw()
    if (card5 := shoe.draw()).rank == "A":
        print(count)
        break

    count += 1

show = Shoe(num_decks=1, random_state=count)
for _ in range(6):
    print(show.draw())
