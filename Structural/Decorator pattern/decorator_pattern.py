from abc import ABC, abstractmethod


class CoffeeInterface(ABC):

    @abstractmethod
    def get_ingredients(self):
        pass


class Coffee:
    def __init__(self, amount_of_coffee):
        self.amount = amount_of_coffee
        self.milk = 0
        self.sugar = 0

    def get_ingredients(self):
        return self.amount, self.milk, self.sugar


class DecoratorInterface(CoffeeInterface):

    def __init__(self, wrapped):
        self.wrapped = wrapped

    @abstractmethod
    def get_ingredients(self):
        self.wrapped.get_ingredients()


class Mocca(DecoratorInterface):

    def __init__(self, wrapped):
        super().__init__(wrapped)

    def get_ingredients(self):
        self.amount, self.milk, self.sugar = self.wrapped.get_ingredients()
        self.milk += 15
        self.sugar += 15

        return self.amount, self.milk, self.sugar


class Espresso(DecoratorInterface):

    def __init__(self, wrapped):
        super().__init__(wrapped)

    def get_ingredients(self):
        self.amount, self.milk, self.sugar = self.wrapped.get_ingredients()
        self.milk += 5
        self.sugar += 5

        return self.amount, self.milk, self.sugar


coffee1 = Coffee(15)
print(coffee1.get_ingredients())
print()
mocca = Mocca(coffee1)
print(mocca.get_ingredients())
print()
espresso = Espresso(mocca)
print(espresso.get_ingredients())




