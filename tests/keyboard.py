import pytest

from src.keyboard import Keyboard


def test_keyboard_str(keyboard_1):
    assert str(keyboard_1) == "Dark Project KD87A"
    keyboard_2 = Keyboard('Noname', 500, 50)
    assert keyboard_2._name == 'Noname'


def test_change_lang(keyboard_1):
    assert str(keyboard_1.language) == "EN"
    keyboard_1.change_lang()
    assert str(keyboard_1.language) == "RU"
    keyboard_1.change_lang().change_lang()
    assert str(keyboard_1.language) == "RU"


def test_language(keyboard_1):
    with pytest.raises(AttributeError):
        keyboard_1.language = 'CH'
