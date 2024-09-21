from model.Player import Player
from model.Players import Players

PLAYER_NAME_INFO = "게임에 참여할 사람의 이름을 입력하세요.(쉼표 기준으로 분리),중복안됨"
DEALER = '딜러'
WIN = "승"
DEFEAT = '패'
DRAW = "무"
WITHOUT_DEALER_RANGE = -1
EXTRA_CARD_QUESTION = "{0}는 한장의 카드를 더 받겠습니까?(예는 y, 아니오는 n)"
DEAL_FIRST_CARD = "{}에게 2장이 나누었습니다"
DEALER_EXTRA_CARD_INFO = "딜러는 16이하라 한장의 카드를 더 받았습니다."
DEALT_CARD = "{name}카드:{card_list}"
FINAL_RESULT = "## 최종 결과 "
NUM_EXCESS = "숫자가 21이 초과되었습니다"
BETTING_MONEY = "{name}의 배팅금액은"


def show_players_name_info():
    print(PLAYER_NAME_INFO)


def show_first_dealing_cards(players: Players):
    player_names = ''
    for player in players.players:
        player_names += player.player + ' '
    print(DEAL_FIRST_CARD.format(player_names.strip()))


def show_dealt_cards(players: Players, dealer: DEALER):
    for player in players.players:
        print(player.player, end=" ")
        print(*player.card_list.card_list)
    print(dealer.dealer, *dealer.card_list.card_list)


def show_question_deal_extra_card(player: Player):
    print(EXTRA_CARD_QUESTION.format(player.player))


def show_player_dealt_cards(player: Player):
    print(player.card_list.card_list)


def show_players_dealer_dealt_cards(player: Player, dealer: DEALER):
    print(DEALT_CARD.format(name=player.player, card_list=', '.join(player.player_card_list.player_card_list)))
    print(DEALT_CARD.format(name=dealer.dealer, card_list=', '.join(dealer.dealer_card_list.dealer_card_list)))


def show_dealer_get_extra_card():
    print(DEALER_EXTRA_CARD_INFO)


def show_players_dealt_card(players: Players):
    for player in players.players:
        show_player_dealt_cards(player)


def show_game_result(player: Player, profit: int):
    print(player.player, ":", profit)


def show_question_players_betting_money(player: Player):
    print(BETTING_MONEY.format(name=player.player))


def show_value_error(e):
    print(e)


def show_dealt_cards_with_card_sum(players: Players, dealer: DEALER):
    for player in players.players:
        print(player.player, end=" ")
        print(*player.card_list.card_list, player.card_list.sum_card_num())
    print(dealer.dealer, *dealer.card_list.card_list, dealer.card_list.sum_card_num())
