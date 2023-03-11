import os
from utils.goods import Item, Phone

path_csv = os.sep.join(["data", "items.csv"])


def main():
    item1 = Item("Смартфон", 10000, 20)
    print(item1.calculate_price())

    item2 = Item("Ноутбук", 20000, 5)
    print(item2.calculate_price())

    Item.rate = 0.8
    item1.discount_price()
    item2.instantiate_from_csv()

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

    # смартфон iPhone 14, цена 120_000, количетсво товара 5, симкарт 2
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    print(phone1)
    print(repr(phone1))
    # phone1.number_of_sim = 0 # проверка


if __name__ == "__main__":
    main()
