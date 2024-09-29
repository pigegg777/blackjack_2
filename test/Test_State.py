from model.Cards import Cards
from model.ExtraCardAnswer import ExtraCardAnswer
from model.GameState import GameState
from model.State import State  # 임의의 파일 경로를 사용하세요.

yes_answer = ExtraCardAnswer("y")
no_answer = ExtraCardAnswer("n")


class TestPlayerState(State):
    def draw_card(self):
        super().draw_card()  # 부모 draw_card 메서드 호출할 수 있습니다.


# 테스트 파일
def test_initial_state():
    player_state = TestPlayerState()
    assert player_state.state == GameState.DRAW
    assert player_state.card_list.sum_card_num() == 0  # 초기 카드의 합은 0


def test_if_draw_card_enum_remove_card():
    player = TestPlayerState()
    player.first_draw()
    for card in player.card_list.card_list:
        assert card not in Cards.cards.value


def test_first_draw():
    player_state = TestPlayerState()
    player_state.first_draw()
    assert len(player_state.card_list.card_list) == 2


def test_bust_drawing():
    player_state = TestPlayerState()
    player_state.card_list.card_list = (["Dia 10", "Dia K", "Dia 9"])
    player_state.check_state()
    assert player_state.state == GameState.BUST


def test_draw_condition():
    player_state = TestPlayerState()
    player_state.card_list.card_list = ["Dia 10", "Dia K"]
    assert player_state.state == GameState.DRAW


def test_check_blackjack():
    player_state = TestPlayerState()
    player_state.card_list.card_list = ["Dia 10", "Dia Ace"]
    player_state.check_state()
    assert player_state.state == GameState.BLACKJACK


