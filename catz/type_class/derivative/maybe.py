from catz.type_class.core.monad import Monad


class Maybe(Monad):
    def __init__(self, value):
        super().__init__(value)


class Just(Maybe):

    def __init__(self, value):
        super().__init__(value)

    def fmap(self, func, *args, **kwargs):
        return Just(func(self.value, *args, **kwargs))

    def bind(self, kleisli_func, *args, **kwargs):
        return kleisli_func(self.value, *args, **kwargs)

    def __repr__(self):
        return f"Just {self.value}"


class Nothing(Maybe):

    def __init__(self):
        super().__init__(None)

    def fmap(self, func, *args, **kwargs):
        return self

    def bind(self, kleisli_func, *args, **kwargs):
        return self

    def __repr__(self):
        return "Nothing"
