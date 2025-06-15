"""Base for all magic items"""

from typing import TYPE_CHECKING, Any, Optional

from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter


#############################################################################
class BaseItem:
    """Magic Item Base Class"""

    hide = False  # Set to True to not have in inventory

    def __init__(self, **kwargs: Any):
        self.str = ""
        self.owner: Optional["BaseCharacter"] = None

    #############################################################################
    def mod_stat_str_set(self, character: "BaseCharacter") -> Reason[int]:  # pragma: no coverage
        return Reason()

    #############################################################################
    def mod_desc(self, character: "BaseCharacter") -> Reason[str]:
        return Reason()


# EOF
