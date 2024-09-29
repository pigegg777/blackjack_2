import pytest

from model.Player import Player
from model.Players import Players

VALUE_ERROR_MESSAGE = "info를 똑바로 보세요"
players_dup = ["a", "b", "a"]


player1 = Player("a")
player2 = Player("b")


def test_players_name_duplicated():
    with pytest.raises(ValueError):
        Players(list(map(Player, ("a", "a", "c"))))
