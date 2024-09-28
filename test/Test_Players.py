import pytest

from model.Player import Player
from model.Players import Players

VALUE_ERROR_MESSAGE = "info를 똑바로 보세요"
duplicated_players = list(map(Player, ["a", "b", "a"]))
normal_players = list(map(Player, ["a", "b", "c"]))

player1 = Player("a")
player2 = Player("b")


def test_players_name_duplicated():
    with pytest.raises(ValueError):
        Players(duplicated_players)


