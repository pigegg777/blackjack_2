from model.DealerCardList import DealerCardList
from model.Participation import Participation



class Dealer(Participation):
    def __init__(self,dealer):
        self.dealer = dealer
        self.dealer_card_list = DealerCardList([])
        super().__init__()

    def player_deal_card(self):
        dealt_card = super().player_deal_card()
        self.dealer_card_list.dealer_card_list.append(dealt_card)
        return self.dealer_card_list

    def dealer_deal_first_card(self):
        for _ in range(2):
            self.player_deal_card()
        return self.dealer_card_list

