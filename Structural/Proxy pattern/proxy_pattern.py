from abc import ABC, abstractmethod


class Money(ABC):

    @abstractmethod
    def get_value(self):
        pass


class BankAcc(Money):

    def get_value(self):
        print("Check your valet")


class ATM(Money):

    def __init__(self, bank_acc: BankAcc):
        self.bank_acc = bank_acc

    def get_value(self):
        if self.check_pin():
            print("check with ATM proxy")
            self.bank_acc.get_value()

    def check_pin(self):
        print('Proxy: Checking pin')
        return True


def client_code(money: Money):
    money.get_value()


bank = BankAcc()
client_code(bank)
print()
proxy = ATM(bank)
client_code(proxy)

