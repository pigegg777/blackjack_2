import pytest

from model.PlayerCardList import PlayerCardList

numbers = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "Q", "J"]
patterns = ['Spade', 'Heart', 'Clover', "Dia"]

card_list_dict = {}
normal_player_card_list = PlayerCardList(["Dia Ace", "Clover 2", "Spade K", "Heart Ace"])
duplicated_player_card_list = ["Dia 2", "Dia 2", "Spade K", "Heart Ace"]
not_in_player_card_list = PlayerCardList(["Dia 11", "Clover1 2", "Spade 1", "Heart3 Ace"])


def test_card_list_type():
    assert PlayerCardList(card_list_dict)


def test_card_list_examine_card():
    for card in not_in_player_card_list.player_card_list:
        card_split = list(map(str, card.split(" ")))
        assert (card_split[0] not in patterns) or (card_split[1] not in numbers)


def test_card_list_card_duplicated():
    with pytest.raises(ValueError):
        PlayerCardList(duplicated_player_card_list)


def test_sum_card_num_Ace_regard():
    assert PlayerCardList(["Dia Ace", "Clover 2"]).sum_card_num() == 13
    assert PlayerCardList(["Dia Ace", "Clover K", "Clover 10"]).sum_card_num() == 21
    assert PlayerCardList(["Dia Ace", "Clover Ace","Heart Ace"]).sum_card_num() == 23
