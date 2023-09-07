from abc import ABC, abstractmethod


class PizzaMaker(ABC):

    def create_pizza(self, pizza):
        self.make_sauce(pizza)
        self.make_toppings(pizza)
        self.return_pizza(pizza)

    @abstractmethod
    def make_sauce(self, pizza):
        pass

    @abstractmethod
    def make_toppings(self, pizza):
        pass

    @abstractmethod
    def return_pizza(self, pizza):
        pass


class Pizza:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        print(f"Add some {ingredient}")
        self.ingredients.append(ingredient)


class Mozzarella(PizzaMaker):

    def make_sauce(self, pizza: Pizza):
        pizza.add_ingredient('Tomato paste')

    def make_toppings(self, pizza):
        pizza.add_ingredient('Mozzarella')
        pizza.add_ingredient('Basil')

    def return_pizza(self, pizza):
        print("Mozzarella is ready")
        print(f"Ingredients: {pizza.ingredients}")


class Pepperoni(PizzaMaker):

    def make_sauce(self, pizza):
        pizza.add_ingredient('Tomato paste')

    def make_toppings(self, pizza):
        pizza.add_ingredient('Pepperoni')
        pizza.add_ingredient('Pork')
        pizza.add_ingredient('Cheddar')

    def return_pizza(self, pizza):
        print("Pepperoni is ready")
        print(f"Ingredients: {pizza.ingredients}")


class Cook:
    def __init__(self, template):
        self.recipe = template

    def set_template(self, template):
        self.recipe = template

    def make_pizza(self):
        pizza = Pizza()
        self.recipe.create_pizza(pizza)
        return pizza


cook = Cook(Mozzarella())
cook.make_pizza()

print()

cook.set_template(Pepperoni())
cook.make_pizza()
print()
cook.make_pizza()
