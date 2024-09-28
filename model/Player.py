from model.ExtraCardAnswer import ExtraCardAnswer
from model.State import State
from model.GameState import GameState

WIN = "승"
DEFEAT = '패'
DRAW = "무"
VALUE_ERROR_MESSAGE = "info를 똑바로 보세요"
MINIMUM_NAME_LEN = 1
WIN_NUM = 21


class Player(State):
    def __init__(self, player: str):
        self.player = player
        self.betting_money = 0
        super().__init__()
        if len(self.player) < MINIMUM_NAME_LEN:
            raise ValueError(VALUE_ERROR_MESSAGE)

    def draw_card(self):
        super().draw_card()

    def first_draw(self):
        super().first_draw()

    def state_draw(self, extra_card_answer: ExtraCardAnswer):
        self.check_state()
        if self.state != GameState.BLACKJACK or self.state != GameState.BUST:
            if extra_card_answer.answer == "y":
                self.state = GameState.DRAW
                self.draw_card()
            elif extra_card_answer.answer == "n":
                self.state = GameState.STAY
        self.check_state()



