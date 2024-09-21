from enum import Enum, auto


class GameState(Enum):
    DRAW = auto()
    STAY = auto()
    BUST = auto()
    BLACKJACK = auto()
