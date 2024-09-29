from model.BettingMoney import BettingMoney
from model.ExtraCardAnswer import ExtraCardAnswer
from model.Player import Player
from model.Players import Players

VALUE_ERROR_MESSAGE='INFO를 제대로 봐주세요'
SEPARATOR = ","


def read_players_name() -> Players:
    names = list(map(str.strip, input().split(SEPARATOR)))
    players = Players(list(map(Player, names)))
    return players


def read_answer_extra_card_question():
    while True:
        try:
            answer = ExtraCardAnswer(input())
            return answer
        except ValueError as e:
            print(VALUE_ERROR_MESSAGE)


def read_players_bet():
    while True:
        try:
            print('입력')
            betting_money = BettingMoney(int(input()))
            return betting_money
        except ValueError as e:
            print(VALUE_ERROR_MESSAGE)

