import pytest

from model.CardsList import CardList

numbers = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "Q", "J"]
patterns = ['Spade', 'Heart', 'Clover', "Dia"]

card_list_dict = {}
normal_player_card_list = [("Dia", "Ace"), ("Clover", 3), ("Spade", 3)]
duplicated_player_card_list = [("Dia", "Ace"), ("Clover", 3), ("Dia", "Ace")]
not_in_player_card_list = ["Dia 11", "Clover1 2", "Spade 1", "Heart3 Ace"]



def test_sum_card_num_Ace_regard():
    assert CardList([("Dia", "Ace"), ("Clover", 2)]).sum_card_num() == 13
    assert CardList([("Dia", "Ace"), ("Clover", "K"), ("Clover", 10)]).sum_card_num() == 21
    assert CardList([("Dia", "Ace"), ("Clover", "Ace"), ("Heart", "Ace")]).sum_card_num() == 23
