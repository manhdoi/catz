class Eq:
    """
    This class brings equality to the world.
    https://www.cis.upenn.edu/~cis1940/fall16/lectures/04-typeclasses.html
    """

    @staticmethod
    def eq(a, b):
        """Return True if a and b are equal, False otherwise."""
        raise NotImplementedError

    @staticmethod
    def ne(a, b):
        """Return True if a and b are not equal, False otherwise."""
        return not Eq.eq(a, b)


class PartialOrd(Eq):
    """
    This class brings partial order to the world.
    """

    @staticmethod
    def lt(a, b):
        """Return True if a is less than b, False otherwise."""
        raise NotImplementedError

    @staticmethod
    def gt(a, b):
        """Return True if a is greater than b, False otherwise."""
        return PartialOrd.lt(b, a)

    @staticmethod
    def le(a, b):
        """Return True if a is less than or equal to b, False otherwise."""
        return not PartialOrd.gt(a, b)

    @staticmethod
    def ge(a, b):
        """Return True if a is greater than or equal to b, False otherwise."""
        return not PartialOrd.lt(a, b)


class Ord(PartialOrd):
    """
    This class brings order to the world.
    """

    @staticmethod
    def lt(a, b):
        """Return True if a is less than b, False otherwise."""
        raise NotImplementedError

    @staticmethod
    def gt(a, b):
        """Return True if a is greater than b, False otherwise."""
        return Ord.lt(b, a)

    @staticmethod
    def le(a, b):
        """Return True if a is less than or equal to b, False otherwise."""
        return not Ord.gt(a, b)

    @staticmethod
    def ge(a, b):
        """Return True if a is greater than or equal to b, False otherwise."""
        return not Ord.lt(a, b)


class Hash(Eq):
    """
    This class brings hashing to the world.
    """

    @staticmethod
    def hash(a):
        """Return a hash of a."""
        raise NotImplementedError
