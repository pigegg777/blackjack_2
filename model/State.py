import random
from abc import ABCMeta, abstractmethod

from model import CardsList
from model.Cards import Cards
from model.GameState import GameState


class State(metaclass=ABCMeta):
    def __init__(self):
        self.state = GameState.DRAW
        self.card_list = CardsList.CardList([])
        self.check_state()

    @abstractmethod
    def draw_card(self):
        if self.state == GameState.DRAW:
            dealt_card = random.choice(Cards.cards.value)
            Cards.cards.value.remove(dealt_card)
            self.card_list.card_list.append(dealt_card)
            self.check_state()
            return dealt_card

    def first_draw(self):
        for _ in range(2):
            self.draw_card()
        self.check_state()

    def check_state(self):
        if len(self.card_list.card_list) == 2 and self.card_list.sum_card_num() == 21:
            self.state = GameState.BLACKJACK
        elif self.card_list.sum_card_num() > 21:
            self.state = GameState.BUST

