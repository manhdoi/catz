from functools import reduce
from typing import Iterator


class SemiGroup:
    @classmethod
    def s_concat(cls, elements: Iterator['SemiGroup']) -> 'SemiGroup':
        return reduce(lambda r, e: r.append(e), elements, next(elements))

    def s_times(self, n: int) -> 'SemiGroup':
        if n == 0:
            return self
        elif n < 0:
            raise ValueError("n must be positive")
        else:
            return reduce(lambda r, x: r.append(self), range(n - 1), self)

    def append(self, other: 'SemiGroup') -> 'SemiGroup':
        pass

    def get(self):
        pass
