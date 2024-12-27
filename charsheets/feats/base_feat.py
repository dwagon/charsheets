""" Feats"""

from typing import TYPE_CHECKING

from charsheets.constants import Feat

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class BaseFeat:
    tag = Feat.NONE

    def __init__(self, character: "Character"):
        self.character = character


# EOF
