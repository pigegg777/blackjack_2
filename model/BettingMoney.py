class BettingMoney:
    def __init__(self, betting_money):
        self.betting_money = betting_money
        if self.betting_money is not int:
            raise ValueError

