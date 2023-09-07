class Coffee:
    def __init__(self, coffee_amount, name):
        self.coffee_amount = coffee_amount
        self.name = name

    def get_coffee_amount(self):
        return self.coffee_amount

    def get_name(self):
        return self.name


class Mocca(Coffee):
    def __init__(self):
        super().__init__(10, "Mocca")


class Espresso(Coffee):

    def __init__(self):
        super().__init__(30, "Espresso")


class CoffeeMaker:
    @staticmethod
    def coffee_create(coffee_type):
        return coffee_type()


mocca = CoffeeMaker.coffee_create(Mocca)
espresso = CoffeeMaker.coffee_create(Espresso)

print(mocca.get_name(), mocca.get_coffee_amount())
print(espresso.name, espresso.coffee_amount)
