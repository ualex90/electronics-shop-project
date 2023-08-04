import pytest

from src.item import Item
from src.phone import Phone
from src.keyboard import Keyboard


@pytest.fixture
def item_1():
    return Item('TestName_1', 1000, 5)


@pytest.fixture
def item_2():
    return Item('TestName_2_zxc', 700.5, 2)


@pytest.fixture
def phone_1():
    return Phone("Phone_1", 50_000, 7, 1)


@pytest.fixture
def phone_2():
    return Phone("Phone_2", 35_000, 3, 2)


@pytest.fixture
def keyboard_1():
    return Keyboard('Dark Project KD87A', 9600, 5)
