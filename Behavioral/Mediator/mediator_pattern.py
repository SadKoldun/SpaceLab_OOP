from __future__ import annotations
from abc import ABC


class Mediator(ABC):

    def get_order(self, sender: object, event: str):
        pass


class Waiter(Mediator):

    def __init__(self, cook: Cook, barmen: Barmen):
        self.cook = cook
        self.cook.mediator = self
        self.barmen = barmen
        self.barmen.mediator = self

    def get_order(self, sender, menu):
        if menu == "steak menu":
            self.cook.make_steak_menu()
        elif menu == "pizza menu":
            self.cook.make_pizza_menu()
        elif menu == "full":
            self.cook.make_pizza_menu()
            self.cook.make_steak_menu()
        elif menu == "drink":
            self.barmen.make_drink()


class Worker:

    def __init__(self, mediator: Mediator = None):
        self._mediator = mediator

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator):
        self._mediator = mediator


class Cook(Worker):

    def make_steak_menu(self):
        print("make some steak")
        return self.mediator.get_order(self, "drink")

    def make_pizza_menu(self):
        print("make some pizza")
        return self.mediator.get_order(self, "drink")

    def make_full_menu(self):
        print("making full menu:")
        return self.mediator.get_order(self, "full")


class Barmen(Worker):

    def make_drink(self):
        print("make some drink")


def client_order():
    cook.make_full_menu()


def another_order():
    cook.make_steak_menu()


cook = Cook()
barmen = Barmen()

waiter = Waiter(cook, barmen)

client_order()
print()
another_order()
