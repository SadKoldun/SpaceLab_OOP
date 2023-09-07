from abc import ABC, abstractmethod


class MementoInterface(ABC):

    @abstractmethod
    def get_uah(self):
        pass

    @abstractmethod
    def get_dollars(self):
        pass

    @abstractmethod
    def get_euro(self):
        pass


class SellerMemento(MementoInterface):

    def __init__(self, uah, dollar, euro):
        self.uah = uah
        self.dollar = dollar
        self.euro = euro

    def get_uah(self):
        return self.uah

    def get_dollars(self):
        return self.dollar

    def get_euro(self):
        return self.euro


class Seller:

    def __init__(self, uah, dollars, euro):
        self.uah = uah
        self.dollars = dollars
        self.euro = euro

    def return_uah(self):
        print(f"Uah: {self.uah}")

    def return_dollars(self):
        print(f"Dollars: {self.dollars}")

    def return_euro(self):
        print(f"Euro: {self.euro}")

    def sell_uah(self):
        self.uah -= 1

    def sell_dollar(self):
        self.dollars -= 1

    def sell_euro(self):
        self.euro -= 1

    def save(self):
        return SellerMemento(self.uah, self.dollars, self.euro)

    def restore(self, memento):
        self.uah = memento.get_uah()
        self.dollars = memento.get_dollars()
        self.euro = memento.get_euro()


class Saved:

    def __init__(self, seller: Seller):
        self.seller = seller
        self.history = []

    def save(self):
        self.history.append(self.seller.save())

    def undo(self):
        if len(self.history) == 0:
            return
        else:
            self.seller.restore(self.history.pop())


exchange = Seller(50, 30, 20)
mem = Saved(exchange)

exchange.sell_euro()
exchange.sell_dollar()

exchange.return_euro()
exchange.return_dollars()
mem.save()

exchange.sell_euro()
exchange.sell_dollar()
exchange.sell_uah()
mem.save()
exchange.sell_euro()
exchange.sell_dollar()
exchange.sell_uah()
print()
exchange.return_euro()
exchange.return_dollars()
mem.undo()
mem.undo()
print()
exchange.return_euro()
exchange.return_dollars()


