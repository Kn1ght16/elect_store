from utils.goods import Goods


def main():
    item1 = Goods("Смартфон", 10000, 20)
    item2 = Goods("Ноутбук", 20000, 5)
    print(item1.calculate_price())
    print(item2.calculate_price())
    Goods.rate = 0.8

    item1.discount_price()

    print(item1.price)
    print(item2.price)
    print(item1, item2)


if __name__ == "__main__":
    main()
