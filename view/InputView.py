from model.ExtraCardAnswer import ExtraCardAnswer
from model.Player import Player
from model.Players import Players
from model.BettingMoney import BettingMoney

SEPARATOR = ","


def read_players_name() -> Players:
    names = list(map(str.strip, input().split(SEPARATOR)))
    players = Players(list(map(Player, names)))
    return players


def read_answer_extra_card_question():
    answer = ExtraCardAnswer(input())
    return answer


def read_players_bet():
    betting_money = map(BettingMoney, input())
    return betting_money
