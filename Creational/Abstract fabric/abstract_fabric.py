from abc import ABC, abstractmethod


class Mocca(ABC):
    def __init__(self, name, amount_of_coffee):
        self.name = name
        self.amount_of_coffee = amount_of_coffee

    @abstractmethod
    def create(self):
        pass


class Espresso(ABC):
    def __init__(self, name, amount_of_coffee):
        self.name = name
        self.amount_of_coffee = amount_of_coffee

    @abstractmethod
    def create(self):
        pass


class BigMocca(Mocca):
    def __init__(self):
        super().__init__("big", 50)

    def create(self):
        print(f"Create {self.name} mocca with {self.amount_of_coffee} amount")


class SmallMocca(Mocca):
    def __init__(self):
        super().__init__("small", 25)

    def create(self):
        print(f"Create {self.name} mocca with {self.amount_of_coffee} amount")


class BigEspresso(Espresso):
    def __init__(self):
        super().__init__("big", 30)

    def create(self):
        print(f"Create {self.name} espresso for {self.amount_of_coffee} amount")


class SmallEspresso(Espresso):
    def __init__(self):
        super().__init__("small", 15)

    def create(self):
        print(f"Create {self.name} espresso for {self.amount_of_coffee} amount")


class AbstractFabric(ABC):
    @abstractmethod
    def get_mocca(self):
        pass

    @abstractmethod
    def get_espresso(self):
        pass


class BigAbstractFabric(AbstractFabric):
    def get_mocca(self):
        return BigMocca()

    def get_espresso(self):
        return BigEspresso()


class SmallAbstractFabric(AbstractFabric):
    def get_mocca(self):
        return SmallMocca()

    def get_espresso(self):
        return SmallEspresso()


class CoffeeMaker:
    def __init__(self, factory: AbstractFabric, coffee_name):
        self.factory = factory
        self.coffee_name = coffee_name

    def create_coffee(self):
        if self.coffee_name == 'mocca':
            mocca = self.factory.get_mocca()
            mocca.create()
        elif self.coffee_name == 'espresso':
            espresso = self.factory.get_espresso()
            espresso.create()

    @staticmethod
    def factory_create(factory_type):
        return factory_type()


some_big_coffee = CoffeeMaker.factory_create(BigAbstractFabric)
some_small_coffee = CoffeeMaker.factory_create(SmallAbstractFabric)
new_espresso = CoffeeMaker(some_big_coffee, coffee_name='espresso')
new_espresso.create_coffee()
new_mocca = CoffeeMaker(some_big_coffee, coffee_name='mocca')
new_mocca.create_coffee()
print()
another_espresso = CoffeeMaker(some_small_coffee, "espresso")
another_espresso.create_coffee()
