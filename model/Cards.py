from enum import Enum

card_numbers = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "Q", "J"]
card_patterns = ['Spade', 'Heart', 'Clover', "Dia"]


class Cards(Enum):
    cards = [pattern + " " + str(number) for number in card_numbers for pattern in card_patterns]
