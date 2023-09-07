from abc import ABC, abstractmethod


class Coffee(ABC):

    @abstractmethod
    def create_coffee(self, size):
        pass


class CoffeeMaker:

    def __init__(self, coffee: Coffee):
        self.coffee = coffee

    def set_coffee(self, coffee: Coffee):
        self.coffee = coffee

    def make(self, size):
        self.coffee.create_coffee(size)


class MoccaMaker(Coffee):

    def create_coffee(self, size):
        print(f'Create {size} mocca')


class EspressoMaker(Coffee):

    def create_coffee(self, size):
        print(f'Create {size} espresso')


coffee = CoffeeMaker(MoccaMaker())
coffee.make("big")

coffee.set_coffee(EspressoMaker())
coffee.make("small")
