from catz.type_class.core.monad import Monad


class Try(Monad):
    def __init__(self, value):
        super().__init__(value)

    @classmethod
    def ret(cls, value):
        return Try(value)

    def fmap(self, func, *args, **kwargs):
        pass

    def bind(self, kleisli_func, *args, **kwargs):
        pass


class Success(Try):

    def __init__(self, value):
        super().__init__(value)

    def fmap(self, func, *args, **kwargs):
        return Success(func(self.value, *args, **kwargs))

    def bind(self, kleisli_func, *args, **kwargs):
        return kleisli_func(self.value, *args, **kwargs)


class Error(Try):

    def __init__(self, exception):
        super().__init__(exception)

    def fmap(self, func, *args, **kwargs):
        return self

    def bind(self, kleisli_func, *args, **kwargs):
        return self


def exception_handling(func):
    def wrap_func(*args, **kwargs):
        kleisli_func = Try.k_func(func)
        return kleisli_func(*args, **kwargs)

    return wrap_func
