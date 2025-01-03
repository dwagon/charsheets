""" Feats"""

from typing import TYPE_CHECKING

from charsheets.constants import Feat

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class BaseFeat:
    tag = Feat.NONE
    _desc = ""

    def __init__(self, character: "Character"):
        self.character = character

    @property
    def desc(self) -> str:
        return self._desc


# EOF
