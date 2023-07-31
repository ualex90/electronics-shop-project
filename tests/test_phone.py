import pytest

from src.phone import Phone


def test_number_of_sim(phone_1):
    # Test case #1
    phone_1.number_of_sim = 1
    assert phone_1.number_of_sim == 1
    # Test case #2
    with pytest.raises(ValueError):
        phone_1.number_of_sim = 0
    with pytest.raises(ValueError):
        phone_1.number_of_sim = -1
    with pytest.raises(ValueError):
        phone_1.number_of_sim = 1.0
    with pytest.raises(ValueError):
        phone_1.number_of_sim = '1'
    assert phone_1.number_of_sim == 1
    # Test case #3
    with pytest.raises(ValueError):
        phone_3 = Phone("Phone_3", 50_000, 7, 0)


def test_add(item_1, phone_1, phone_2):
    assert item_1 + phone_1 == 12
    assert phone_1 + item_1 == 12
    assert phone_1 + phone_2 == 10
    with pytest.raises(ValueError):
        sum_ = phone_1 + 10


def test_represent(phone_1, phone_2):
    assert repr(phone_1) == "Phone('Phone_1', 50000, 7, 1)"
    assert repr(phone_2) == "Phone('Phone_2', 35000, 3, 2)"


def test_str(phone_1, phone_2):
    assert str(phone_1) == 'Phone_1'
    assert str(phone_2) == 'Phone_2'
