from typing import Union


class Node:
    def __init__(self, value, next_=None, prev=None):
        self.value = value
        self.__prev = prev
        self.__next = next_

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_):
        if next_:
            if not isinstance(next_, Node):
                raise TypeError
            self.__next = next_
            next_._Node__prev = self

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, prev_):
        if prev_:
            if not isinstance(prev_, Node):
                raise TypeError
            self.__prev = prev_
            prev_._Node__next = self

    def __str__(self):
        return f"{repr(self.__prev)} >> {repr(self)} >> {repr(self.__next)}"

    def __repr__(self):
        return f"{self.__class__.__name__}(Value: {self.value})"