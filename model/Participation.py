import random
from abc import abstractmethod, ABCMeta

from model.Cards import Cards
from model.UsedCards import UsedCards


class Participation(metaclass=ABCMeta):
    def __init__(self):
        self.used_cards = UsedCards([])

    @abstractmethod
    def player_deal_card(self):
        while True:
            dealt_card = [random.choice(Cards.patterns.value), random.choice(Cards.numbers.value)]
            dealt_card = ' '.join(str(card) for card in dealt_card)
            if dealt_card not in self.used_cards.used_cards:
                self.used_cards.used_cards.append(dealt_card)
                break
        return dealt_card
