import os
from utils.goods import Item

path_csv = os.sep.join(["data", "items.csv"])


def main():
    item1 = Item("Смартфон", 10000, 20)
    print(item1.calculate_price())

    item2 = Item("Ноутбук", 20000, 5)
    print(item2.calculate_price())

    Item.rate = 0.8
    item1.discount_price()
    item2.instantiate_from_csv(path_csv)

    print(item1.price)
    print(item2.price)
    try:
        for item in Item.all:
            print(item)
    except NameError:
        print("Длина названия товара не должна превышать 10 символов.")

    print(Item.is_integer(5))
    print(Item.is_integer(5.0))
    print(Item.is_integer(5.5))


if __name__ == "__main__":
    main()
