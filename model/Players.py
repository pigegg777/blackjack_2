from model.Player import Player

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

