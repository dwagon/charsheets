""" Traceable reason for a value"""

from typing import Any, SupportsInt, Generic, TypeVar

T = TypeVar("T")


#############################################################################
class ReasonLink(Generic[T]):
    def __init__(self, reason: str, value: T | None):
        self.reason = reason
        self.value = value

    #########################################################################
    def __repr__(self):
        return f"{self.reason} ({self.value})"

    #########################################################################
    def __eq__(self, other) -> bool:
        if not isinstance(other, ReasonLink):
            return False
        return other.reason == self.reason and other.value == self.value

    #########################################################################
    def __lt__(self, other) -> bool:
        return other.reason < self.reason

    #########################################################################
    def __hash__(self):
        return hash((self.reason, self.value))


#############################################################################
class Reason(Generic[T]):
    def __init__(self, cause: str = "", *values: T) -> None:
        self._reasons: set[ReasonLink] = set()
        self._index = -1

        if cause or values:
            for obj in values:
                self.add(cause, obj)

    #########################################################################
    def add(self, cause: str, value: T | None):
        """Add another link to the Reason chain"""
        if cause or value:
            self._reasons.add(ReasonLink(cause, value))

    #########################################################################
    def count(self, value: T) -> int:
        values = [_.value for _ in self._reasons]
        return values.count(value)

    #########################################################################
    def extend(self, other: "Reason"):
        """Extend a Reason with another Reason"""
        self._reasons |= other._reasons

    #########################################################################
    @property
    def value(self):
        return sum(_.value for _ in self._reasons if isinstance(_.value, SupportsInt))

    #########################################################################
    def __contains__(self, item):
        return any(_.value == item for _ in self._reasons)

    #########################################################################
    def __int__(self):
        return self.value

    #########################################################################
    def __iter__(self):
        self._index = -1
        return self

    #########################################################################
    def __next__(self):
        self._index += 1
        try:
            return sorted(list(self._reasons))[self._index]
        except IndexError:
            raise StopIteration

    #########################################################################
    def __or__(self, other: Any):
        self.extend(other)
        return self

    #########################################################################
    def __bool__(self):
        return any(_.value for _ in self._reasons)

    #########################################################################
    def __len__(self) -> int:
        return len(self._reasons)

    #########################################################################
    @property
    def reason(self) -> str:
        return " + ".join([str(_) for _ in sorted(self._reasons) if _.value])

    #########################################################################
    def __repr__(self):
        """ """
        return f"-{abs(self.value)}" if self.value < 0 else f"{self.value}"

    #########################################################################
    def copy(self) -> "Reason":
        new_copy = Reason[T]()
        new_copy._reasons = self._reasons.copy()
        return new_copy


#############################################################################
class SignedReason(Reason):
    """Same as Reason but returns a "+" if positive, so can be used for 1d6+3 sort of reasons"""

    def __repr__(self):
        """ """
        if self.value == 0:
            return ""
        return f"-{abs(self.value)}" if self.value < 0 else f"+{self.value}"
