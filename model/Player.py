from model.State import State

WIN = "승"
DEFEAT = '패'
DRAW = "무"
VALUE_ERROR_MESSAGE = "info를 똑바로 보세요"
MINIMUM_NAME_LEN = 1
WIN_NUM = 21


class Player(State):
    def __init__(self, player: str):
        self.player = player
        super().__init__()
        if len(self.player) < MINIMUM_NAME_LEN:
            raise ValueError(VALUE_ERROR_MESSAGE)

    def draw_card(self):
        super().draw_card()

    def first_draw(self):
        for _ in range(2):
            self.draw_card()


    def determine_result(self, dealer_result: int) -> str:
        if abs(WIN_NUM - self.player_card_list.sum_card_num()) < abs(WIN_NUM - dealer_result):
            player_result = WIN
        elif abs(WIN_NUM - self.player_card_list.sum_card_num()) > abs(WIN_NUM - dealer_result):
            player_result = DEFEAT
        elif abs(WIN_NUM - self.player_card_list.sum_card_num()) == abs(WIN_NUM - dealer_result):
            player_result = DRAW
        return player_result
