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

    def __iter__(self):
        yield self.value

    @classmethod
    def subclasses(cls):
        def subclasses_rec(c, result):
            if c.__subclasses__():
                for x in c.__subclasses__():
                    if x.is_terminal():
                        result.append(x)
                    result = result + x.subclasses()
            return result

        return subclasses_rec(cls, [])

    @classmethod
    def is_terminal(cls):
        return False
