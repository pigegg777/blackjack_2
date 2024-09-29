import pytest

from model.CardsList import CardList


def test_duplicated_card_in_card_list():
    with pytest.raises(ValueError):
        assert CardList(["Dia 10", "Clover 2", "Dia 10"])


def test_cards_not_in_Cards_Enum():
    with pytest.raises(ValueError):
        assert CardList(["Dia 10", "Clover 2", "Dia 11"])


def test_sum_card_num_Ace_regard_11():
    assert CardList(["Dia 10", "Clover 2", "Dia Ace"]).sum_card_num() == 13


def test_sum_card_num_Ace_regard_1():
    assert CardList(["Dia 10", "Clover 10", "Dia Ace"]).sum_card_num() == 21


def test_sum_card_num_Ace_regard_both_1_11():
    assert CardList(["Dia Ace", "Clover Ace", "Heart Ace"]).sum_card_num() == 13


def test_how_regard_ace():
    assert CardList(["Dia Ace", "Clover Ace", "Heart 9"]).sum_card_num() == 21
