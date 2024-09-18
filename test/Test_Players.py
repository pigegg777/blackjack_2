import pytest

from model.Player import Player
from model.PlayerCardList import PlayerCardList
from model.Players import Players

duplicated_players = list(map(Player, ["a", "b", "a"]))
normal_players = list(map(Player, ["a", "b", "c"]))

player1 = Player("a")
player2 = Player("b")
player1.player_card_list = PlayerCardList(["Spade 10", "Clover 9"])
player2.player_card_list = PlayerCardList(["Spade 9", "Heart 8"])


def test_players_name_duplicated():
    with pytest.raises(ValueError):
        Players(duplicated_players)


def test_dealer_included():
    normal_players_list = Players(normal_players)
    assert any(player.player == '딜러' for player in normal_players_list.players)


def test_get_result_win():
    players = Players([player1, player2])
    players.dealer.player_card_list = PlayerCardList(["Heart 10", "Spade 8"])
    result = players.get_result()
    assert result == [1, 0, 1]


def test_get_result_defeat():
    players = Players([player1, player2])
    players.dealer.player_card_list = PlayerCardList(["Heart 10", "Heart 2"])
    result = players.get_result()
    assert result == [0, 0, 2]


def test_get_result_draw():
    players = Players([player1, player2])
    players.dealer.player_card_list = PlayerCardList(["Heart 10", "Heart 7"])
    result = players.get_result()
    assert result == [0, 1, 1]
