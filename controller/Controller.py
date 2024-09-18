from model.Dealer import Dealer
from model.Player import Player
from model.Players import Players
from view import OutputView, InputView


def enter_game():
    while True:
        try:
            OutputView.show_players_name_info()
            players = InputView.read_players_name()
            return players
        except ValueError as e:
            OutputView.show_value_error(e)


def first_deal_card(players: Players, dealer: Dealer):
    OutputView.show_first_dealing_cards(players)
    for player in players.players:
        player.deal_first_cards()
    dealer.dealer_deal_first_card()
    OutputView.show_dealt_cards(players, dealer)


def player_deal_extra_card(player: Player):
    while True:
        try:
            OutputView.show_question_deal_extra_card(player)
            OutputView.show_player_dealt_cards(player)
            if player.player_card_list.sum_card_num() > 21:
                OutputView.show_num_excess()
                break
            answer = InputView.read_answer_extra_card_question()
            if answer.answer == "n":
                break
            elif answer.answer == "y":
                player.player_deal_card()
        except ValueError as e:
            OutputView.show_value_error(e)


def players_deal_extra_card(players: Players):
    for player in players.players:
        player_deal_extra_card(player)


def dealer_deal_extra_card(dealer: Dealer):
    while dealer.dealer_card_list.sum_card_num() < 16:
        OutputView.show_dealer_get_extra_card()
        dealer.player_deal_card()


def get_game_result(dealer: Dealer, players: Players):
    dealer_card_sum = dealer.dealer_card_list.sum_card_num()
    OutputView.show_dealt_cards(players, dealer)
    dealer_result = players.get_result(dealer_card_sum)
    OutputView.show_game_result(players, dealer_result, dealer_card_sum)


def start():
    try:
        dealer = Dealer("딜러")
        players = enter_game()
        first_deal_card(players, dealer)
        players_deal_extra_card(players)
        dealer_deal_extra_card(dealer)
        get_game_result(dealer, players)
    except ValueError as e:
        OutputView.show_value_error(e)
