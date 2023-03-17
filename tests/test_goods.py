import os
import pytest
from utils.goods import Item, Phone, KeyBoard


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


def test_item_instantiate_from_csv():
    items_list = Item.instantiate_from_csv()
    assert len(items_list) == 3
    assert items_list[0].name == 'item1'
    assert items_list[0].price == 10
    assert items_list[0].quantity == 5
    assert items_list[1].name == 'item2'
    assert items_list[1].price == 20
    assert items_list[1].quantity == 3


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


def test_item_init(item):
    assert item.name == 'test'
    assert item.price == 10.0
    assert item.quantity == 5


@pytest.fixture()
def keyboard():
    return KeyBoard('test', 10.0, 5)


def test_keyboard_init(keyboard):
    assert keyboard.name == 'test'
    assert keyboard.price == 10.0
    assert keyboard.quantity == 5
    assert keyboard.language == 'EN'


def test_lang_keyboard_change_lang(keyboard):
    keyboard.change_lang()
    assert keyboard.language == 'RU'
    keyboard.change_lang()
    assert keyboard.language == 'EN'
