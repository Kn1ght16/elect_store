class Goods():
    rate = 1.0

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_price(self):
        return self.price * self.quantity

    def discount_price(self):
        self.price = self.price * self.rate
