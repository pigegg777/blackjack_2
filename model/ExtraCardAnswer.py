

VALUE_ERROR_MESSAGE = "info를 똑바로 보세요"
ANSWER_NO = "n"
ANSWER_YES = "y"


class ExtraCardAnswer:
    def __init__(self, answer: str):
        self.answer = answer
        if self.answer not in [ANSWER_NO, ANSWER_YES]:
            raise ValueError(VALUE_ERROR_MESSAGE)

