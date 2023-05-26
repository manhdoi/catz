from typing import Callable

from catz.type_class.core.monad import Monad


class Try(Monad):
    def __init__(self, value):
        super().__init__(value)

    @classmethod
    def ret(cls, value):
        if value is not Exception:
            return Success(value)
        return Error(value)

    def fmap(self, func, *args, **kwargs):
        pass

    def fold(self, func_error, func_success):
        pass

    def bind(self, kleisli_func, *args, **kwargs):
        pass

    def is_success(self):
        return False

    def is_error(self):
        return False

    @classmethod
    def k_func(cls, func: Callable) -> Callable:
        def wrap_func(*args, **kwargs):
            try:
                return Success.ret(func(*args, **kwargs))
            except Exception as e:
                return Error(e)

        return wrap_func


class Success(Try):

    def __init__(self, value):
        super().__init__(value)

    def fmap(self, func, *args, **kwargs):
        return Success(func(self.value, *args, **kwargs))

    def bind(self, kleisli_func, *args, **kwargs):
        return kleisli_func(self.value, *args, **kwargs)

    def fold(self, func_error, func_success):
        return func_success(self.value)

    def is_success(self):
        return True

    def __repr__(self):
        return f"Success: {self.value}"

    def __eq__(self, other: 'Success'):
        return self.value == other.value


class Error(Try):

    def __init__(self, exception):
        super().__init__(exception)

    def fmap(self, func, *args, **kwargs):
        return self

    def bind(self, kleisli_func, *args, **kwargs):
        return self

    def is_error(self):
        return True

    def fold(self, func_error, func_success):
        return func_error(self.value)

    def __repr__(self):
        return f"Error: {self.value}"


def exception_handling(func):
    def wrap_func(*args, **kwargs):
        kleisli_func = Try.k_func(func)
        return kleisli_func(*args, **kwargs)

    return wrap_func
