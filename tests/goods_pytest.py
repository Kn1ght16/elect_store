import pytest
from goods import Goods


def test_calculate_amount():
    item1 = Goods("name", 50, 2)
    assert item1.calculate_price() == 100
    item2 = Goods("name", 50, 0)
    assert item2.calculate_price() == 0

def test_apply_discount():
    item1 = Goods("name", 100, 5)
    item1.rate = 0.8
    assert item1.discount_price() is None
    assert item1.price == 80
    assert int(item1.calculate_price()) == 400
