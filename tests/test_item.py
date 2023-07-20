"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


def test_item(item_1, item_2):
    assert item_1.name == 'TestName_1'
    assert item_1.price == 1000
    assert item_1.quantity == 5
    assert item_2.name == 'TestName_2'
    assert item_2.price == 700.5
    assert item_2.quantity == 2


def test_calculate_total_price(item_1, item_2):
    assert item_1.calculate_total_price() == 5000
    assert item_2.calculate_total_price() == 1401
    assert isinstance(item_1.calculate_total_price(), float)


@pytest.mark.parametrize('rate, total', [(0.5, 2500), (0.92, 4600)])
def test_discount(item_1, rate, total):
    item_1.pay_rate = rate
    item_1.apply_discount()
    assert item_1.calculate_total_price() == total


def test_get_instance_list():
    Item.all = []
    item = Item('item_3', 200, 50)
    assert len(item.all) == 1
    assert isinstance(Item.all[0], Item)
    new_item = Item('item_3', 200, 50)
    assert len(new_item.all) == 2
    assert isinstance(new_item.all[1], Item)


def test_name(item_1):
    assert item_1.name == 'TestName_1'
    item_1.name = '0123456789876543210'
    assert item_1.name == '0123456789'
