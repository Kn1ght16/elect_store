import os
import pytest
from utils.goods import Item, Phone


def test_apply_discount():
    item1 = Item("name", 100, 5)
    item1.rate = 0.8
    assert item1.discount_price() is 80
    assert item1.price == 80
    assert int(item1.calculate_price()) == 400


def test_is_integer():
    item = Item("name", 100, 5)
    assert item.is_integer(5) is True
    assert item.is_integer(5.0) is True
    assert item.is_integer(5.5) is False
    assert item.is_integer("5") is False


def test_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item = Item("iPhone 14", 120_000, 5)
    assert phone1 + item == 10
