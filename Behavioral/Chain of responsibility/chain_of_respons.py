from abc import ABC, abstractmethod


class WorkerInterface(ABC):
    @abstractmethod
    def set_next(self, worker):
        pass

    @abstractmethod
    def execute(self, command):
        pass


class Worker(WorkerInterface):
    def __init__(self):
        self._next_worker = None

    def set_next(self, worker: WorkerInterface):
        self._next_worker = worker
        return worker

    def execute(self, command):
        if self._next_worker is not None:
            return self._next_worker.execute(command)
        return None


class Waiter(Worker):
    def execute(self, command):
        if command == "bill":
            return "Get bill command from waiter class"
        else:
            print("Waiter can't do operation, next worker")
            return super().execute(command)


class Barmen(Worker):
    def execute(self, command):
        if command == "drink":
            return "Get drink command from barmen class"
        else:
            print("Barmen can't do operation, next worker")
            return super().execute(command)


class Cook(Worker):
    def execute(self, command):
        if command == "food":
            return "Get food command from cook class"
        else:
            print("Cook can't do operation, next worker")
            return super().execute(command)


def client(worker: WorkerInterface, command):
    outer = worker.execute(command)
    if not outer:
        print("Can't do this operation")
    else:
        print(outer)


waiter = Waiter()
barmen = Barmen()
cook = Cook()

waiter.set_next(barmen).set_next(cook)

client(barmen, "bill")
print()
client(barmen, "drink")
print()
client(waiter, "drink")
print()
client(waiter, "food")
