import os
import pytest
from goods import Item, Phone


@pytest.fixture
def item():
    return Item("test", 10.0, 5)


@pytest.fixture
def phone():
    return Phone("test_phone", 100.0, 2, 1)


def test_item_repr(item):
    assert item.__repr__() == "_Item__name=test, price=10.0, quantity=5"


def test_item_str(item):
    assert item.__str__() == "test"


def test_is_integer():
    assert Item.is_integer(5) == True
    assert Item.is_integer(5.0) == True
    assert Item.is_integer(5.5) == False
    assert Item.is_integer("5") == False


def test_item_discount_price(item):
    item.rate = 0.8
    assert item.discount_price() == 8
    assert item.discount_price() is 6
    assert item.price == 6.4
    assert int(item.calculate_price()) == 32


