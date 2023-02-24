import os
import pytest
from utils.goods import Item

path_csv = os.sep.join(["..", "data", "items.csv"])


def test_calculate_amount():
    item1 = Item("name", 50, 2)
    assert item1.calculate_price() == 100
    item2 = Item("name", 50, 0)
    assert item2.calculate_price() == 0


def test_apply_discount():
    item1 = Item("name", 100, 5)
    item1.rate = 0.8
    assert item1.discount_price() is 80
    assert item1.price == 80
    assert int(item1.calculate_price()) == 400


def test_instantiate_from_csv():
    items = Item("name", 100, 5)
    assert len(items.instantiate_from_csv(path_csv)) == 5
    assert isinstance(items.instantiate_from_csv(path_csv)[0], Item)


def test_is_integer():
    item = Item("name", 100, 5)
    assert item.is_integer(5) is True
    assert item.is_integer(5.0) is True
    assert item.is_integer(5.5) is False
    assert item.is_integer("5") is False
