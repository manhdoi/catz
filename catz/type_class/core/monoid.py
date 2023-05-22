from functools import reduce
from typing import Iterator

from catz.type_class.core.semi_group import SemiGroup


class Monoid(SemiGroup):
    @classmethod
    def m_empty(cls) -> 'Monoid':
        pass

    def m_append(self, other: 'Monoid') -> 'Monoid':
        return self.append(other)

    def m_concat(self, elements: Iterator['Monoid']) -> 'Monoid':
        return reduce(lambda r, e: r.m_append(e), elements, self.m_empty())
