from model.Dealer import Dealer
from model.GameState import GameState
from model.Player import Player
from model.Players import Players
from model.Profit import Profit
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
        player.betting_money = InputView.read_players_bet()
        print(player.betting_money.betting_money)


def first_deal_card(players: Players, dealer: Dealer):
    OutputView.show_first_dealing_cards(players)
    for player in players.players:
        player.first_draw()
    dealer.dealer_draw_first()
    OutputView.show_dealt_cards(players, dealer)


def player_deal_extra_card(player: Player):
    try:
        while player.state is GameState.DRAW:
            OutputView.show_question_deal_extra_card(player)
            OutputView.show_player_dealt_cards(player)
            answer = InputView.read_answer_extra_card_question()
            player.state_draw(answer)
    except ValueError as e:
        OutputView.show_value_error(e)


def players_deal_extra_card(players: Players):
    for player in players.players:
        player_deal_extra_card(player)
        print(player.betting_money.betting_money)


def dealer_deal_extra_card(dealer: Dealer):
    while dealer.state is GameState.DRAW:
        dealer.draw_extra_cards()
        OutputView.show_dealer_get_extra_card()


def get_game_result(players: Players, dealer: Dealer):
    for player in players.players:
        profit = Profit(dealer, player).get_profit()
        OutputView.show_game_result(player, profit)


def start():
    try:
        dealer = Dealer("딜러")
        players = enter_game()
        first_deal_card(players, dealer)
        players_deal_extra_card(players)
        dealer_deal_extra_card(dealer)
        OutputView.show_dealt_cards_with_card_sum(players, dealer)
        get_game_result(players, dealer)
    except ValueError as e:
        OutputView.show_value_error(e)
