from abc import abstractmethod, ABC


class CoffeeBuilder:

    def add_amount(self, amount):
        self.amount = amount

    def add_milk(self, milk):
        self.milk = milk

    def add_sugar(self, sugar):
        self.sugar = sugar

    def create_coffee(self):
        return Coffee(self)


class Coffee:
    def __init__(self, builder: CoffeeBuilder):
        self.amount = builder.amount
        self.milk = builder.milk
        self.sugar = builder.sugar

    @staticmethod
    def get_builder():
        return CoffeeBuilder()


builder = Coffee.get_builder()


builder.add_milk(8)
builder.add_amount(4)
builder.add_sugar(2)
new_coffee = builder.create_coffee()

print(new_coffee.milk, new_coffee.sugar, new_coffee.amount)

