from model.GameState import GameState
from model.State import State


class Dealer(State):
    def __init__(self, dealer):
        self.dealer = dealer
        self.dealer_profit = 0
        super().__init__()

    def draw_card(self):
        super().draw_card()

    def dealer_draw_first(self):
        for _ in range(2):
            self.draw_card()

    def draw_extra_cards(self):
        self.check_state()
        if self.card_list.sum_card_num() > 17 and self.state != GameState.BLACKJACK:
            self.state = GameState.STAY
        elif self.card_list.sum_card_num() <= 16 and self.state == GameState.DRAW:
            self.draw_card()
