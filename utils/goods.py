import csv


class InstantiateCSVError(Exception):
    pass


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
        """Возвращает атрибуты в понятном виде пользователю."""
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
        """Возращается цену со скидкой"""
        self.price = self.price * self.rate
        return int(self.price)

    @classmethod
    def instantiate_from_csv(cls):
        """Возвращает список объектов класса Goods из csv"""
        try:
            with open('data/items.csv', "r", newline='') as csvfile:
                csv_data = csv.DictReader(csvfile)
                items_list = []
                if not (("name" in csv_data.fieldnames) and ("price" in csv_data.fieldnames) and (
                        "quantity" in csv_data.fieldnames)):
                    raise InstantiateCSVError('Файл items.csv поврежден')
                else:
                    for item in csv_data:
                        items_list.append(cls(item['name'], int(item['price']), int(item['quantity'])))
                    return items_list
        except FileNotFoundError:
            print('Отсутствует файл item.csv')

    @staticmethod
    def is_integer(number) -> bool:
        """Возвращает True- если число int, иначе - False"""
        return ((type(number) == int) or (type(number) == float)) \
               and (round(number) == number)

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity


class Phone(Item):

    def __init__(self, name, price, count, sim):
        super().__init__(name, price, count)
        self.sim = sim

    @property
    def number_of_sim(self):
        return self.sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if number_of_sim <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self.sim = number_of_sim

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity


class LangKeyBoard:

    def __init__(self, name, price, count):
        super().__init__(name, price, count)
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self.__language


class KeyBoard(LangKeyBoard, Item):
    pass
