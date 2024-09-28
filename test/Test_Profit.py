from model.BettingMoney import BettingMoney
from model.Dealer import Dealer
from model.GameState import GameState
from model.Player import Player
from model.Profit import Profit


def test_profit_both_state_blackjack():
    player = Player("Alice")
    dealer = Dealer("dealer")
    player.state = GameState.BLACKJACK
    player.betting_money = 100
    dealer.state = GameState.BLACKJACK
    profit = Profit(dealer, player)
    assert profit.player_profit() == 0


def test_profit_player_state_blackjack():
    player = Player("Alice")
    dealer = Dealer("dealer")
    player.state = GameState.BLACKJACK
    player.betting_money = BettingMoney(100)
    dealer.state = GameState.STAY
    profit = Profit(dealer, player)
    assert profit.player_profit() == 150

def test_profit_dealer_state_blackjack():
    player = Player("Alice")
    dealer = Dealer("dealer")
    player.state = GameState.STAY
    player.betting_money = BettingMoney(100)
    dealer.state = GameState.BLACKJACK
    profit = Profit(dealer, player)
    assert profit.player_profit() == -100

def test_profit_player_state_bust():
    player = Player("Alice")
    dealer = Dealer("dealer")
    player.state = GameState.BUST
    player.betting_money = BettingMoney(100)
    dealer.state = GameState.BUST
    profit = Profit(dealer, player)
    assert profit.player_profit() == -100

def test_profit_dealer_state_bust():
    player = Player("Alice")
    dealer = Dealer("dealer")
    player.state = GameState.STAY
    player.betting_money = BettingMoney(100)
    dealer.state = GameState.BUST
    profit = Profit(dealer, player)
    assert profit.player_profit() == 100


def test_profit_both_state_stay_dealer_win():
    player = Player("Alice")
    dealer = Dealer("dealer")
    player.card_list.card_list=["Dia 3", "Dia 2"]
    dealer.card_list.card_list = ["Dia 10", "Dia 2"]
    player.state = GameState.STAY
    player.betting_money = BettingMoney(100)
    dealer.state = GameState.STAY
    profit = Profit(dealer, player)
    assert profit.player_profit() == -100


def test_profit_both_state_stay_player_win():
    player = Player("Alice")
    dealer = Dealer("dealer")
    player.card_list.card_list = ["Dia 3", "Dia 2","Clover Ace"]
    dealer.card_list.card_list = ["Dia 10", "Dia 2"]
    player.state = GameState.STAY
    player.betting_money = BettingMoney(100)
    dealer.state = GameState.STAY
    profit = Profit(dealer, player)
    assert profit.player_profit() == 100


def test_profit_both_state_stay_result_draw():
    player = Player("Alice")
    dealer = Dealer("dealer")
    player.card_list.card_list = ["Dia 3", "Dia 2","Clover Ace"]
    dealer.card_list.card_list = ["Dia 10", "Dia 6"]
    player.state = GameState.STAY
    player.betting_money = BettingMoney(100)
    dealer.state = GameState.STAY
    profit = Profit(dealer, player)
    assert profit.player_profit() == 0






