from model.Dealer import Dealer
from model.Player import Player
from model.Players import Players
from view import OutputView, InputView


def enter_game():
    while True:
        try:
            OutputView.show_players_name_info()
            players = InputView.read_players_name()
            bet_money(players)
            return players
        except ValueError as e:
            OutputView.show_value_error(e)


def bet_money(players: Players):
    for player in players.players:
        OutputView.show_question_players_betting_money(player)
        InputView.read_players_bet()


def first_deal_card(players: Players, dealer: Dealer):
    OutputView.show_first_dealing_cards(players)
    for player in players.players:
        player.first_draw()
    dealer.dealer_draw_first()
    OutputView.show_dealt_cards(players, dealer)


def player_deal_extra_card(player: Player):
    try:
        while player.state is True:
            OutputView.show_question_deal_extra_card(player)
            OutputView.show_player_dealt_cards(player)
            answer = InputView.read_answer_extra_card_question()
            player.state_draw(answer)
    except ValueError as e:
        OutputView.show_value_error(e)


def players_deal_extra_card(players: Players):
    for player in players.players:
        player_deal_extra_card(player)


def dealer_deal_extra_card(dealer: Dealer):
    while dealer.state is True:
        dealer.draw_extra_cards()
        OutputView.show_dealer_get_extra_card()


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
        OutputView.show_dealt_cards(players,dealer)
    except ValueError as e:
        OutputView.show_value_error(e)
