class UAH:

    def get_value(self):
        return self.value

    def set_uah_value(self, value):
        self.value = value


class Dollar:

    def set_dollar_value(self, value):
        self.value = value
        print(f"Here is {self.value} $")

    def get_dollar_value(self):
        return self.value


class Converter(UAH):

    def __init__(self, dollar: Dollar):
        self.dollar = dollar

    def get_value(self):
        print(f"Converting {uah.value} UAH")
        return self.dollar.set_dollar_value(round(uah.value / 35, 2))


uah = UAH()
dollar = Dollar()
converter = Converter(dollar)

uah.set_uah_value(5000)
print(uah.get_value())
converter.get_value()

print()

uah.set_uah_value(2000)
converter.get_value()

