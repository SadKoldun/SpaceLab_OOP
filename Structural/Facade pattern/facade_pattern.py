class Client:

    def __init__(self, name):
        self.name = name

    def make_order(self):
        print(f"Client {self.get_name()} making order")

    def eating_food(self):
        print(f"Client {self.get_name()} eating")

    def get_name(self):
        return self.name


class Kitchen:

    def make_food(self):
        print("Making food on the kitchen")


class Waiter:

    def take_order(self, client: Client):
        print(f"Waiter took order from client {client.get_name()}")

    def return_food(self, client: Client):
        print(f"Return food for client {client.get_name()}")


class Facade:
    def __init__(self):
        self.kitchen = Kitchen()
        self.waiter = Waiter()

    def complete_order(self, client: Client):
        client.make_order()
        self.waiter.take_order(client)
        self.kitchen.make_food()
        self.waiter.return_food(client)
        client.eating_food()


pizzeria = Facade()

client1 = Client("CLIENT 1")

client2 = Client("CLIENT 2")


pizzeria.complete_order(client1)
print()
pizzeria.complete_order(client2)


