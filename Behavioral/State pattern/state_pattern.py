from abc import ABC, abstractmethod


class State(ABC):

    def __init__(self):
        self.coffee_state = None

    @abstractmethod
    def next_state(self):
        pass

    @abstractmethod
    def prev_state(self):
        pass


class CoffeeMaker:

    def __init__(self, st: State):
        self.set_state(st)

    def set_state(self, st: State):
        self.state = st
        self.state.coffee_state = self

    def next_state(self):
        self.state.next_state()

    def prev_state(self):
        self.state.prev_state()


class Idle(State):

    def next_state(self):
        print("Checking coffee amount")
        self.coffee_state.set_state(CheckCoffeeAmount())

    def prev_state(self):
        print("Idle")


class CheckCoffeeAmount(State):

    def next_state(self):
        print("Confirm coffee amount, checking amount of milk")
        self.coffee_state.set_state(MilkCheckAmount())

    def prev_state(self):
        print("Canceling checking coffee amount, waiting")
        self.coffee_state.set_state(Idle())


class MilkCheckAmount(State):
    def next_state(self):
        print("Confirm amount of milk, making coffee")
        print("ENJOY!")

    def prev_state(self):
        print("Canceling milk check, checking coffee amount")
        self.coffee_state.set_state(CheckCoffeeAmount())


coffee_maker = CoffeeMaker(Idle())
coffee_maker.next_state()
coffee_maker.prev_state()
coffee_maker.prev_state()
coffee_maker.next_state()
coffee_maker.next_state()
coffee_maker.next_state()
coffee_maker.prev_state()
