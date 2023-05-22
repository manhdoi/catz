from typing import Callable, Any


class Functor:

    def __init__(self, value: Any):
        self.value = value

    @classmethod
    def id(cls) -> 'Functor':
        pass

    def fmap(self, f: Callable) -> 'Functor':
        pass
