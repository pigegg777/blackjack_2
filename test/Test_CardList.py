from model.CardsList import CardList

numbers = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "K", "Q", "J"]
patterns = ['Spade', 'Heart', 'Clover', "Dia"]

card_list_dict = {}
normal_player_card_list = [("Dia", "Ace"), ("Clover", 3), ("Spade", 3)]
duplicated_player_card_list = [("Dia", "Ace"), ("Clover", 3), ("Dia", "Ace")]
not_in_player_card_list = ["Dia 11", "Clover1 2", "Spade 1", "Heart3 Ace"]


def test_sum_card_num_Ace_regard_11():
    assert CardList(["Dia 10", "Clover 2","Dia Ace"]).sum_card_num() == 13


def test_sum_card_num_Ace_regard_1():
    assert CardList(["Dia 10", "Clover 10","Dia Ace"]).sum_card_num() == 21


def test_sum_card_num_Ace_regard_both_1_11():
    assert CardList(["Dia Ace", "Clover Ace", "Heart Ace"]).sum_card_num() == 13


def test_how_regard_ace():
    assert CardList(["Dia Ace", "Clover Ace", "Heart 9"]).sum_card_num() == 21
