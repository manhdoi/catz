from unittest import mock

from catz.type_class.core.monad import Monad


def test_whole_monad():
    import importlib
    import pkgutil

    package_name = "catz.type_class.derivative"
    package = importlib.import_module(package_name)
    for _, module_name, _ in pkgutil.walk_packages(package.__path__, package_name + '.'):
        importlib.import_module(module_name)

    klasses = Monad.subclasses()

    for klass in klasses:
        print(klass)
        monad = klass.ret(1)

        func = mock.Mock()
        func.__code__ = mock.Mock()
        func.__code__.co_argcount = 0
        func.return_value = klass.ret(1)

        func_h = mock.Mock()
        func_h.__code__ = mock.Mock()
        func_h.__code__.co_argcount = 0
        func_h.return_value = klass.ret(2)

        func_g = mock.Mock()
        func_g.__code__ = mock.Mock()
        func_g.__code__.co_argcount = 0
        func_g.return_value = klass.ret(3)

        assert klass.ret(1).bind(func) == func(1)
        assert monad.bind(klass.ret) == monad
        assert monad.bind(func_g).bind(func_h) == monad.bind(lambda x: func_g(x).bind(func_h))
