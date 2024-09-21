from model.Dealer import Dealer
from model.Player import Player
from model.UsedCards import UsedCards

VALUE_ERROR_MESSAGE = "info를 똑바로 보세요"
DEALER = '딜러'
WIN = "승"
DEFEAT = '패'
DRAW = "무"
WITHOUT_DEALER_RANGE = -1


class Players:
    def __init__(self, players: list[Player]):
        self.players = players
        if len(list(player.player for player in self.players)) != len(set(player.player for player in self.players)):
            raise ValueError(VALUE_ERROR_MESSAGE)

    def get_result(self, dealer_card_sum) -> list[int]:
        dealer_result = []
        for player in self.players:
            dealer_result.append(player.determine_result(dealer_card_sum))
        win_count = dealer_result.count(DEFEAT)
        draw_count = dealer_result.count(DRAW)
        defeat_count = dealer_result.count(WIN)
        dealer_results = [win_count, draw_count, defeat_count]
        return dealer_results
