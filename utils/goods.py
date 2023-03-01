import csv


class Item():
    rate = 1.0
    all = []

    def __init__(self, __name, price, quantity):
        """__name - приватный атрибут товара
        price - float, публичный атрибут цены
        quantity - int, публичный атрибут количества"""
        self.__name = __name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self) -> str:
        """Возвращает атрибуты в понятном виде разработчику"""
        text = ""
        for dic in self.__dict__:
            text += dic + "=" + str(self.__dict__[dic]) + ", "
        return f"{text[:-2]}"

    def __str__(self):
        """Возвращает атрибуты в понятном виде пользователю"""
        return f'{self.__name}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value) > 10:
            raise NameError('Длина товара превышает 10 символов.')
        self.__name = value

    def calculate_price(self) -> float:
        """Возращается произведение цены и количества товара"""
        return self.price * self.quantity

    def discount_price(self) -> float:
        """Возращается цена со скидкой"""
        self.price = self.price * self.rate
        return int(self.price)

    @classmethod
    def instantiate_from_csv(cls) -> list:
        """Возвращает список объектов класса Goods из csv"""
        with open('data/items.csv', "r", newline='') as csvfile:
            csv_data = csv.DictReader(csvfile)
            items_list = []
            for item in csv_data:
                items_list.append(cls(item['name'], int(item['price']), int(item['quantity'])))
            return items_list

    @staticmethod
    def is_integer(number) -> bool:
        """Возвращает True- если число int, иначе - False"""
        return ((type(number) == int) or (type(number) == float)) \
               and (round(number) == number)
