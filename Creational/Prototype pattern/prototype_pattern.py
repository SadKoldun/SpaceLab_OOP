import copy


class CopyPizza:

    def __init__(self, dough, ham, cheese):
        self.dough = dough
        self.ham = ham
        self.cheese = cheese

    def __copy__(self):

        new = self.__class__(
            self.dough, self.ham, self.cheese
        )
        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memo=None):
        if memo is None:
            memo = {}

        new = self.__class__(
            self.dough, self.ham, self.cheese
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)
        return new


some_pizza = CopyPizza(3, 3, 3)

copied_pizza = copy.copy(some_pizza)
deep_copied_pizza = copy.deepcopy(copied_pizza)

some_pizza.ham = 5
copied_pizza.ham = 8
deep_copied_pizza.dough = 10
print(some_pizza.ham, some_pizza.dough, some_pizza.cheese)
print(copied_pizza.ham, copied_pizza.dough, copied_pizza.cheese)
print(deep_copied_pizza.ham, deep_copied_pizza.dough, deep_copied_pizza.cheese)
