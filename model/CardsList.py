DEFAULT_CARD_SUM = 0
DEFAULT_ACE_CARD_COUNT = 0
CARD_INDEX_OF_CARD_LIST = 1
REGARD_AS_TEN = 10
ACE_CARD_COUNT_PLUS = 1
ACE_CARD_REGARD_ONE = 1
ACE_CARD_REGARD_ELEVEN = 11
ACE_SELECT_POINT = 11
WIN_NUM = 21
NUM_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
REGARD_AS_TEN_CARDS_LIST = ["K", "Q", "J"]


class CardList:
    def __init__(self, card_list: list):
        self.card_list = card_list

    def sum_card_num(self) -> int:
        card_sum = DEFAULT_CARD_SUM
        ace_card_count = DEFAULT_ACE_CARD_COUNT
        for card in self.card_list:
            card_num = card[1]
            if card_num in REGARD_AS_TEN_CARDS_LIST:
                card_sum += REGARD_AS_TEN
            elif card_num in NUM_LIST:
                card_sum += int(card_num)
            elif card_num == "Ace":
                ace_card_count += ACE_CARD_COUNT_PLUS
        card_sum = self.how_regard_ace_card(ace_card_count, card_sum)
        return card_sum

    def how_regard_ace_card(self, ace_card_count: int, card_sum: int) -> int:
        for _ in range(ace_card_count):
            if abs(WIN_NUM - (card_sum + ACE_CARD_REGARD_ONE)) >= abs(WIN_NUM - (card_sum + ACE_CARD_REGARD_ELEVEN)):
                card_sum += ACE_CARD_REGARD_ELEVEN
            elif abs(WIN_NUM - (card_sum + ACE_CARD_REGARD_ONE)) <= abs(WIN_NUM - (card_sum + ACE_CARD_REGARD_ELEVEN)):
                card_sum += ACE_CARD_REGARD_ONE
        return card_sum
