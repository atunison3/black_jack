from domain import Shoe, Hand


shoe = Shoe(num_decks=1, random_state=224)

card1 = shoe.draw()
card2 = shoe.draw()  # Dealer card
card3 = shoe.draw()
card4 = shoe.draw()  # Dealer card
card5 = shoe.draw()
card6 = shoe.draw()
card7 = shoe.draw()
card8 = shoe.draw()
card9 = shoe.draw()
card10 = shoe.draw()
card11 = shoe.draw()

print(f"{card2}  -  {card4}")
print(f"{card1}  -  {card7}  -  {card9} - {card10} - {card11}")
print(f"{card5}  -  {card8}")
print(f"{card3}  -  {card6}")

hand1 = Hand(wager=1, card1=card1, card2=card7)
hand2 = Hand(wager=1, card1=card5, card2=card8)
hand3 = Hand(wager=1, card1=card3, card2=card6)

hand1.cards.append(card9)
hand1.cards.append(card10)
hand1.cards.append(card11)

print(hand1.value)
print(hand2.value)
print(hand3.value)


# count = 0
# while count < 2**32-1:
#     shoe = Shoe(num_decks=1, random_state=count)
#     card1 = shoe.draw()
#     card2 = shoe.draw()
#     card3 = shoe.draw()
#     card4 = shoe.draw()

#     if (card1.rank == card3.rank) and (card1.rank == '8'):
#         card5 = shoe.draw()
#         card6 = shoe.draw()

#         if (card5.rank == '8') and (card6.rank == '8'):
#             print(count)
#             break
#     count += 1
