from abc import ABC, abstractmethod


class ValueInterface:

    @abstractmethod
    def change(self, price):
        pass

    @abstractmethod
    def add_obs(self, obs):
        pass

    @abstractmethod
    def remove_obs(self, obs):
        pass

    @abstractmethod
    def notify(self):
        pass


class Euro(ValueInterface):

    def __init__(self, price):
        self.price = price
        self.all_observers = []
        self.name = "Euro"

    def change(self, price):
        self.price = price
        self.notify()

    def add_obs(self, obs):
        self.all_observers.append(obs)

    def remove_obs(self, obs):
        self.all_observers.remove(obs)

    def notify(self):
        for obs in self.all_observers:
            obs.update(self.price)


class Dollar(ValueInterface):

    def __init__(self, price):
        self.price = price
        self.all_observers = []
        self.name = "Dollar"

    def change(self, price):
        self.price = price
        self.notify()

    def add_obs(self, obs):
        self.all_observers.append(obs)

    def remove_obs(self, obs):
        self.all_observers.remove(obs)

    def notify(self):
        for obs in self.all_observers:
            obs.update(self.price)


class ObserverInterface(ABC):

    @abstractmethod
    def update(self, subject):
        pass


class HighValueBuyer(ObserverInterface):
    def __init__(self, obs):
        self.product = obs
        obs.add_obs(self)

    def update(self, price):

        if price < 50:
            print(f"Buy {self.product.name} for HIGH {price} price ")
            self.product.remove_obs(self)


class LowValueBuyer(ObserverInterface):
    def __init__(self, obs):
        self.product = obs
        obs.add_obs(self)

    def update(self, price):

        if price < 30:
            print(f"Buy {self.product.name} for LOW {price} price ")
            self.product.remove_obs(self)


euro = Euro(40)
dollar = Dollar(35)

high_euro = HighValueBuyer(euro)
high_dollar = HighValueBuyer(dollar)

low_euro = LowValueBuyer(euro)
low_dollar = LowValueBuyer(dollar)

euro.change(25)
dollar.change(25)
