from model.Dealer import Dealer
from model.GameState import GameState
from model.Player import Player


class Profit:
    def __init__(self, dealer: Dealer, player: Player):
        self.dealer = dealer
        self.player = player

    def get_profit(self):
        if self.player.state == GameState.BLACKJACK:
            return self.blackjack()
        elif self.player.state == GameState.BUST:
            return -self.player.betting_money.betting_money
        elif self.dealer.state == GameState.BUST and self.player.state != GameState.BUST:
            return self.player.betting_money.betting_money
        elif self.dealer.state and self.player.state != GameState.BUST:
            return self.fight()

    def blackjack(self):
        if self.dealer.state == GameState.BLACKJACK:
            return 0
        elif self.dealer.state != GameState.BLACKJACK:
            return self.player.betting_money.betting_money * 1.5

    def fight(self):
        if self.dealer.state and self.player.state != GameState.BUST:
            if abs(21 - self.dealer.card_list.sum_card_num()) > abs(21 - self.player.card_list.sum_card_num()):
                return self.player.betting_money.betting_money
            elif abs(21 - self.dealer.card_list.sum_card_num()) < abs(21 - self.player.card_list.sum_card_num()):
                return -self.player.betting_money.betting_money
