from typing import Any

from catz.type_class.core.functor import Functor


class Applicative(Functor):

    def __init__(self, value: Any):
        super().__init__(value)

    @classmethod
    def pure(cls, value: Any) -> 'Applicative':
        return cls(value)

    def apply(self, applicative_func: 'Applicative') -> 'Applicative':
        return applicative_func.fmap(self.value)
