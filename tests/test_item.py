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


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5.5


def test_instantiate_from_csv():
    Item.all = []
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert Item.all[0].name == 'Смартфон'
    assert Item.all[1].price == 1000
    assert Item.all[2].name == 'Кабель'
    assert Item.all[3].price == 50
    assert Item.all[4].name == 'Клавиатура'


def test_represent(item_1, phone_1):
    assert repr(item_1) == "Item('TestName_1', 1000, 5)"
    assert repr(phone_1) == "Phone('Phone_1', 50000, 7, 1)"


def test_str(item_2):
    assert str(item_2) == 'TestName_2'
