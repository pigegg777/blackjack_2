from model.GameState import GameState
from model.State import State  # 임의의 파일 경로를 사용하세요.


class TestPlayerState(State):
    def draw_card(self):
        super().draw_card()  # 부모 draw_card 메서드 호출할 수 있습니다.


# 테스트 파일
def test_initial_state():
    player_state = TestPlayerState()

    assert player_state.state == GameState.DRAW
    assert player_state.card_list.sum_card_num() == 0  # 초기 카드의 합은 0


def test_first_draw():
    player_state = TestPlayerState()
    player_state.first_draw()
    assert len(player_state.card_list.card_list) == 2  # 첫 번째 드로우에서 두 장의 카드를 받아야 함


def test_bust_drawing():
    player_state = TestPlayerState()
    player_state.card_list.card_list = ([("Dia", 10), ("Dia", "Ace"), ("Clover", "K"), ("Clover", 3)])  # 초기값 설정
    player_state.bust_draw()
    assert player_state.state == GameState.BUST  # Bust 상태가 되어야 함


def test_blackjack_condition():
    player_state = TestPlayerState()
    player_state.card_list.card_list = [("Dia", 10), ("Dia", "K")]  # A를 11로 처리할 때
    assert player_state.state == GameState.DRAW  # 아직 bust 가 아니므로 상태가 DRAW여야 함

    # Now let's force a blackjack
    player_state.card_list.card_list = [("Dia", 10), ("Dia", "Ace")]
    assert player_state.state == GameState.BLACKJACK
