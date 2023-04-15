import catz.common.functions as functions


def curry(func):
    num_params = func.__code__.co_argcount
    curry_func = getattr(functions, f'curry{num_params}')
    return curry_func(func)
