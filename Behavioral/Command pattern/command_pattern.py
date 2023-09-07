from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


class MakePizza(Command):
    def __init__(self, executor):
        self.executor = executor

    def execute(self):
        self.executor.make_pizza()


class MakeSteak(Command):
    def __init__(self, executor):
        self.executor = executor

    def execute(self):
        self.executor.make_steak()


class MakeDrink(Command):

    def __init__(self, executor):
        self.executor = executor

    def execute(self):
        self.executor.make_drink()


class MakeCoffee(Command):

    def __init__(self, executor):
        self.executor = executor

    def execute(self):
        self.executor.make_coffee()


class Cook:

    def make_pizza(self):
        print("Making pizza")

    def make_steak(self):
        print("Making steak")


class Barmen:

    def make_drink(self):
        print("Making drink")

    def make_coffee(self):
        print("Making coffee")


class Waiter:

    def __init__(self):
        self.history = []

    def set_command(self, commands: Command):
        self.history.append(commands)

    def undo_command(self):
        self.history.pop()

    def execute_commands(self):
        for command in self.history:
            command.execute()
        print("Return order to client")


def client():
    waiter = Waiter()
    waiter.set_command(MakePizza(cook))
    waiter.set_command(MakeSteak(cook))
    waiter.set_command(MakeCoffee(barmen))
    waiter.set_command(MakePizza(cook))
    waiter.undo_command()
    waiter.set_command(MakeDrink(barmen))
    waiter.execute_commands()


cook = Cook()
barmen = Barmen()
client()


