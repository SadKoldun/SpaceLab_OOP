from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import List


class SliceIterator(Iterator):
    def __init__(self, pizza: List):
        self.pizza = pizza
        self._index = 0

    def __next__(self):
        try:
            slice = self.pizza[self._index]
            self._index += 1
        except IndexError:
            raise StopIteration()
        return slice


class PizzaSlices(Iterable):

    def __init__(self, slice_number):
        self._slices = [f"Slice {i + 1}" for i in range(slice_number)]

    def amount_slice(self):
        return len(self._slices)

    def __iter__(self):
        return SliceIterator(self._slices)

    def __str__(self):
        return f"Pizza have {self.amount_slice()} slices"


pizza = PizzaSlices(10)
print(pizza)

for slice in pizza:
    print(slice)
