from __future__ import annotations
from abc import ABC, abstractmethod


class Remote:

    def __init__(self, interface: Interface):
        self.interface = interface

    def remote_operation_enable(self):
        return (f"Remote: enable operation\n"
                f"{self.interface.operation_enable()}")

    def remote_operation_disable(self):
        return (f"Remote: disable operation\n"
                f"{self.interface.operation_disable()}")

    def remote_operation_set_channel(self):
        return (f"Remote: set channel operation\n"
                f"{self.interface.operation_set_channel()}")

    def remote_operation_set_volume(self):
        return (f"Remote: set volume operation\n"
                f"{self.interface.operation_set_volume()}")


class Interface(ABC):

    @abstractmethod
    def operation_enable(self):
        pass

    @abstractmethod
    def operation_disable(self):
        pass

    @abstractmethod
    def operation_set_volume(self):
        pass

    @abstractmethod
    def operation_set_channel(self):
        pass


class Tv(Interface):

    def operation_enable(self):
        return "TV: Enable"

    def operation_disable(self):
        return "TV: Disable"

    def operation_set_volume(self):
        return "Tv: Volume change"

    def operation_set_channel(self):
        return "TV: Channel change"


class Radio(Interface):
    def operation_enable(self):
        return "Radio: Enable"

    def operation_disable(self):
        return "Radio: Disable"

    def operation_set_volume(self):
        return "Radio: Volume change"

    def operation_set_channel(self):
        return "Radio: Channel change"


def client_actions(remote: Remote):
    print(remote.remote_operation_enable())
    print(remote.remote_operation_set_channel())
    print(remote.remote_operation_set_volume())


if __name__ == "__main__":
    interface_tv = Tv()
    interface_radio = Radio()

    remote_tv = Remote(interface_tv)
    remote_radio = Remote(interface_radio)

    client_actions(remote_tv)

    print("\n")

    client_actions(remote_radio)
