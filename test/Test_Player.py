import pytest

from model.ExtraCardAnswer import ExtraCardAnswer
from model.GameState import GameState
from model.Player import Player


def test_player_initialization():
    player = Player("Alice")
    assert player.player == "Alice"
    assert player.state == GameState.DRAW
    with pytest.raises(ValueError, match="info를 똑바로 보세요"):
        Player("")


def test_state_draw_yes():
    player = Player("Bob")
    player.card_list.card_list = ["Dia 3", "Dia 2"]
    extra_card_answer = ExtraCardAnswer("y")
    player.state_draw(extra_card_answer)
    assert player.state == GameState.DRAW and len(player.card_list.card_list) == 3


def test_state_draw_no():
    player = Player("Charlie")
    extra_card_answer = ExtraCardAnswer("n")
    player.card_list.card_list = ["Dia 3", "Dia 2"]
    player.state_draw(extra_card_answer)
    assert player.state == GameState.STAY and len(player.card_list.card_list) == 2


def test_state_draw_if_blackjack():
    player = Player("Charlie")
    extra_card_answer = ExtraCardAnswer("n")
    player.card_list.card_list = ["Dia Ace", "Dia 10"]
    player.state_draw(extra_card_answer)
    assert player.state == GameState.BLACKJACK


def test_state_draw_if_bust():
    player = Player("Charlie")
    extra_card_answer = ExtraCardAnswer("n")
    player.card_list.card_list = ["Dia Ace", "Dia 10", "Clover 10", "Spade 2"]
    player.state_draw(extra_card_answer)
    assert player.state == GameState.BUST and len(player.card_list.card_list)==4
