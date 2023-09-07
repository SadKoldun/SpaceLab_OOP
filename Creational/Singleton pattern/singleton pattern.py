class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class CoffeeMaker(metaclass=SingletonMeta):

    def __init__(self, coffee_amount=30, milk=30, sugar=30):
        self.coffee_amount = coffee_amount
        self.milk = milk
        self.sugar = sugar

    def check_ingredients(self):
        print(self.coffee_amount, self.milk, self.sugar)

    def make_espresso(self):
        print("Making espresso")
        self.milk -= 5
        self.coffee_amount -= 3

    def make_mocca(self):
        print("Making mocca")
        self.milk -= 4
        self.sugar -= 5


if __name__ == "__main__":

    s1 = CoffeeMaker(coffee_amount=25)
    s2 = CoffeeMaker(milk=1)
    s1.check_ingredients()
    s2.check_ingredients()
    s2.make_mocca()
    s2.check_ingredients()
    s1.check_ingredients()
    if id(s1) == id(s2):
        print("The same instance of class")
    else:
        print("Error. Multiple instance")

