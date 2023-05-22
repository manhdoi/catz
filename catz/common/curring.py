from functools import wraps


def curry_rec(func, args):
    @wraps(func)
    def wrapper(*args2):
        new_args = args + list(args2)
        if len(new_args) >= func.__code__.co_argcount:
            return func(*new_args)
        else:
            return curry_rec(func, new_args)

    return wrapper


curry = curry_rec(lambda f: curry_rec(f, []), [])
