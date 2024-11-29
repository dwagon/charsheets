from typing import TYPE_CHECKING
from charsheets.constants import Ability

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class Species:
    def __init__(self, character: "Character"):
        self.character = character

    #########################################################################
    def species_abilities(self) -> set[Ability]:
        raise NotImplemented

    #########################################################################
    @property
    def name(self) -> str:
        return self.__class__.__name__.title()

    #########################################################################
    @property
    def speed(self) -> int:
        return 30


# EOF
