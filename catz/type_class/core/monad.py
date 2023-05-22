from typing import Any, Callable

from catz.type_class.core.applicative import Applicative


class Monad(Applicative):

    def __init__(self, value: Any):
        super().__init__(value)

    @classmethod
    def ret(cls, value: Any) -> 'Monad':
        return cls(value)

    def bind(self, kleisli_func: Callable) -> 'Monad':
        pass

    @classmethod
    def k_func(cls, func: Callable) -> Callable:
        def wrap_func(*args, **kwargs):
            return cls.ret(func(*args, **kwargs))

        return wrap_func
