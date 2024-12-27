""" Traceable reason for a value"""

from typing import Any, SupportsInt


#############################################################################
class ReasonLink:
    def __init__(self, cause: str = "", value: Any = None):
        self.cause = cause
        self.value = value

    #########################################################################
    def __repr__(self):
        return f"{self.cause} ({self.value})"


#############################################################################
class Reason:
    def __init__(self, cause: str = "", value: Any = None) -> None:
        self.reasons: list[ReasonLink] = []
        self.add(cause, value)

    #########################################################################
    def add(self, cause: str, value: Any):
        """Add another link to the Reason chain"""
        self.reasons.append(ReasonLink(cause, value))

    #########################################################################
    def extend(self, other: "Reason"):
        """Extend a Reason with another Reason"""
        self.reasons.extend(other.reasons)

    #########################################################################
    @property
    def value(self):
        return sum(_.value for _ in self.reasons if isinstance(_.value, SupportsInt))

    #########################################################################
    def __int__(self):
        return self.value

    #########################################################################
    def __bool__(self):
        return any(_.value for _ in self.reasons)

    #########################################################################
    @property
    def reason(self) -> str:
        return " + ".join([str(_) for _ in self.reasons if _.value])

    #########################################################################
    def __repr__(self):
        """ """
        return f"-{abs(self.value)}" if self.value < 0 else f"{self.value}"

    #########################################################################
    def copy(self) -> "Reason":
        new_copy = Reason()
        new_copy.reasons = self.reasons[:]
        return new_copy


#############################################################################
class SignedReason(Reason):
    """Same as Reason but returns a "+" if positive, so can be used for 1d6+3 sort of reasons"""

    def __repr__(self):
        """ """
        if self.value == 0:
            return ""
        return f"-{abs(self.value)}" if self.value < 0 else f"+{self.value}"
