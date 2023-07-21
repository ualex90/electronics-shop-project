import pytest

from src.item import Item


@pytest.fixture
def item_1():
    return Item('TestName_1', 1000, 5)


@pytest.fixture
def item_2():
    return Item('TestName_2_zxc', 700.5, 2)
