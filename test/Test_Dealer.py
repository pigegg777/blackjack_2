from model.Dealer import Dealer
from model.GameState import GameState

def test_dealer_extra_card_under_16():
    dealer = Dealer('dealer')
    dealer.card_list.card_list = ["Dia 10", "Dia 5"]
    dealer.draw_extra_cards()
    assert len(dealer.card_list.card_list) == 3


def test_dealer_extra_card_up_16():
    dealer = Dealer('dealer')
    dealer.card_list.card_list = ["Dia 10", "Dia 7"]
    dealer.draw_extra_cards()
    assert len(dealer.card_list.card_list) == 2


def test_dealer_extra_card_if_state_is_blackjack():
    dealer = Dealer('dealer')
    dealer.card_list.card_list = ["Dia 10", "Dia Ace"]
    dealer.draw_extra_cards()
    assert dealer.state == GameState.BLACKJACK


def test_dealer_extra_card_if_state_is_bust():
    dealer = Dealer('dealer')
    dealer.card_list.card_list = ["Dia 10", "Dia 9", "Clover K"]
    dealer.draw_extra_cards()
    assert dealer.state == GameState.BUST
