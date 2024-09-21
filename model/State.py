import random
from abc import ABCMeta, abstractmethod

from model import CardsList
from model.Cards import Cards
from model.ExtraCardAnswer import ExtraCardAnswer
from model.GameState import GameState

DEFAULT_CARD_SUM = 0
DEFAULT_ACE_CARD_COUNT = 0
CARD_INDEX_OF_CARD_LIST = 1
REGARD_AS_TEN = 10
ACE_CARD_COUNT_PLUS = 1
ACE_CARD_REGARD_ONE = 1
ACE_CARD_REGARD_ELEVEN = 11
ACE_SELECT_POINT = 11
WIN_NUM = 21
NUM_LIST = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
REGARD_AS_TEN_CARDS_LIST = ["K", "Q", "J"]


class BustException(Exception):
    pass


class State(metaclass=ABCMeta):
    def __init__(self):

        self.state = GameState.DRAW
        self.card_list = CardsList.CardList([])
        self.bust_draw()

    @abstractmethod
    def draw_card(self):
        if self.state is GameState.DRAW:
            dealt_card = random.choice(Cards.cards.value)
            Cards.cards.value.remove(dealt_card)
            self.card_list.card_list.append(dealt_card)
            self.bust_draw()
            return dealt_card

    def first_draw(self):
        for _ in range(2):
            self.draw_card()
            if self.card_list.sum_card_num() == 21:
                self.state = GameState.BLACKJACK

    def bust_draw(self):
        if self.card_list.sum_card_num() > 21:
            self.state = GameState.BUST

    def state_draw(self, extra_card_answer: ExtraCardAnswer):
        if extra_card_answer.answer == "y":
            self.state = GameState.DRAW
            self.draw_card()
        elif extra_card_answer.answer == "n":
            self.state = GameState.STAY
