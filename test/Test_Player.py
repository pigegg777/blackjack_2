import pytest

from model.Player import Player
from model.PlayerCardList import PlayerCardList
from model.UsedCards import UsedCards

numbers = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "Q", "J"]
patterns = ['Spade', 'Heart', 'Clover', "Dia"]

player = "a"
normal_used_card = UsedCards(["Dia 1", "Clover 2", "Spade K", "Heart Ace"])
normal_player_card_list = PlayerCardList(["Dia 1", "Clover 2", "Spade K", "Heart Ace"])

normal_dealer_card_sum = 16

len_zero_player = ""
normal_player = Player(player)




def test_player_name_len():
    with pytest.raises(ValueError):
        assert Player(len_zero_player)


def test_deal_card_duplicated():
    card_list = normal_player.deal_cards(normal_used_card)
    assert len(card_list.player_card_list) == len(set(card_list.player_card_list))


def test_deal_card_card():
    card_list = normal_player.deal_cards(normal_used_card)
    for card in card_list.player_card_list:
        card_split = list(map(str, card.split(" ")))
        assert (card_split[0] in patterns) or (card_split[1] in numbers)


def test_first_deal_card():
    normal_player.deal_first_cards(normal_used_card)
    assert len(normal_player.player_card_list.player_card_list) != 2


def test_determine_winner():
    normal_player_card_list.sum_card_num()
