from model.Participation import Participation
from model.PlayerCardList import PlayerCardList

WIN = "승"
DEFEAT = '패'
DRAW = "무"
VALUE_ERROR_MESSAGE = "info를 똑바로 보세요"
MINIMUM_NAME_LEN = 1
WIN_NUM = 21


class Player(Participation):
    def __init__(self, player: str):
        self.player = player
        self.player_card_list = PlayerCardList([])
        super().__init__()
        if len(self.player) < MINIMUM_NAME_LEN:
            raise ValueError(VALUE_ERROR_MESSAGE)

    def player_deal_card(self):
        dealt_card = super().player_deal_card()
        self.player_card_list.player_card_list.append(dealt_card)
        return self.player_card_list

    def determine_result(self, dealer_result: int) -> str:
        if abs(WIN_NUM - self.player_card_list.sum_card_num()) < abs(WIN_NUM - dealer_result):
            player_result = WIN
        elif abs(WIN_NUM - self.player_card_list.sum_card_num()) > abs(WIN_NUM - dealer_result):
            player_result = DEFEAT
        elif abs(WIN_NUM - self.player_card_list.sum_card_num()) == abs(WIN_NUM - dealer_result):
            player_result = DRAW
        return player_result

    def deal_first_cards(self) -> PlayerCardList:
        for _ in range(2):
            self.player_deal_card()
        return self.player_card_list
