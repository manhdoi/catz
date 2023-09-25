from typing import Any

from catz.type_class.core.monad import Monad


class Maybe(Monad):
    def __init__(self, value):
        super().__init__(value)

    @classmethod
    def is_terminal(cls):
        return False


class Just(Maybe):

    def __init__(self, value):
        super().__init__(value)

    def fmap(self, func, *args, **kwargs):
        return Just(func(self.value, *args, **kwargs))

    def bind(self, kleisli_func, *args, **kwargs):
        return kleisli_func(self.value, *args, **kwargs)

    def __repr__(self):
        return f"Just {self.value}"

    def __eq__(self, other):
        return isinstance(other, Just) and self.value == other.value or False

    @classmethod
    def is_terminal(cls):
        return True


class Nothing(Maybe):

    def __init__(self, *args, **kwargs):
        super().__init__(None)

    def fmap(self, func, *args, **kwargs):
        return self

    def bind(self, kleisli_func, *args, **kwargs):
        return self

    def __repr__(self):
        return "Nothing"

    def __eq__(self, other):
        return isinstance(other, Nothing) and True or False

    @classmethod
    def is_terminal(cls):
        return True
