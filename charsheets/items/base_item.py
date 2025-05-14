"""Base for all magic items"""

from typing import TYPE_CHECKING, Any, Optional

from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter


#############################################################################
class BaseItem:
    """Magic Item Base Class"""

    def __init__(self, **kwargs: Any):
        self.owner: Optional["BaseCharacter"] = None
        self.name: str = ""

    #############################################################################
    def mod_stat_str_set(self, character: "BaseCharacter") -> Reason[int]:  # pragma: no coverage
        return Reason()


# EOF