import pytest

from src.item import Item


@pytest.fixture
def item_1():
    return Item('test_name_1', 1000, 5)


@pytest.fixture
def item_2():
    return Item('test_name_2', 700.5, 2)
