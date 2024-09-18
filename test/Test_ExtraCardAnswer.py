import pytest

from model.ExtraCardAnswer import ExtraCardAnswer



def test_answer_type():
    with pytest.raises(TypeError):
        answer = any(str)
        ExtraCardAnswer(answer)
