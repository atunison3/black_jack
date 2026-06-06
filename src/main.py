from domain import Shoe, Hand  # noqa: F401  # Still developing


shoe = Shoe(num_decks=2, random_state=42)

for _ in range(5):
    print(shoe.draw())
