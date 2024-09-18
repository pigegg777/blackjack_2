from model.CardList import CardList


class DealerCardList(CardList):
    def __init__(self, dealer_card_list: list[str]):
        self.dealer_card_list = dealer_card_list
        super().__init__(self.dealer_card_list)

    def sum_card_num(self):
        dealer_card_sum = super().sum_card_num()
        return dealer_card_sum
