from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Interface(ABC):

    def __init__(self, name):
        self.item_name = name
        self.owner_name = None

    def set_owner(self, owner):
        self.owner_name = owner

    @abstractmethod
    def add(self, sub_item):
        pass

    @abstractmethod
    def remove(self, sub_item):
        pass

    @abstractmethod
    def display(self):
        pass


class Ingredient(Interface):

    def __init__(self, name):
        super().__init__(name)

    def add(self, sub_item):
        print("End element can't have a sub_item")

    def remove(self, sub_item):
        print("End element can't have a sub_item")

    def display(self):
        print("\t\t" + self.item_name)


class Parts(Interface):

    def __init__(self, name):
        super().__init__(name)
        self.added = []

    def add(self, sub_item: Interface):
        sub_item.set_owner(self.item_name)
        self.added.append(sub_item)

    def remove(self, sub_item):
        self.added.remove(sub_item)

    def display(self):
        if self.owner_name is not None:
            print(self.owner_name + ":")
            print("\t" + self.item_name + ":")
        for item in self.added:

            item.display()


pizza = Parts("Pepperoni")
dough = Parts("Dough")
filling = Parts("Filling")
sauce = Parts("Sauce")

dough.add(Ingredient("Flour"))
dough.add(Ingredient("Egg"))
dough.add(Ingredient("Egg"))

filling.add(Ingredient("Pepperoni"))
filling.add(Ingredient("Cheese"))
filling.add(Ingredient("Pork"))

sauce.add(Ingredient("Tomato sauce"))

pizza.add(dough)
pizza.add(filling)
pizza.add(sauce)

pizza.display()
print()

