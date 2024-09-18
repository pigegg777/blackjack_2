from model.CardList import CardList


class PlayerCardList(CardList):
    def __init__(self, player_card_list: list[str]):
        self.player_card_list = player_card_list
        super().__init__(self.player_card_list)
        if len(self.player_card_list) != len(set(self.player_card_list)):
            raise ValueError

    def sum_card_num(self):
        card_sum = super().sum_card_num()
        return card_sum

