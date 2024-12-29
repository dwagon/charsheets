from typing import TYPE_CHECKING

from charsheets.constants import Ability

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class Species:
    def __init__(self) -> None:
        self.character: Character | None = None

    #########################################################################
    def species_abilities(self) -> set[Ability]:
        raise NotImplementedError

    #########################################################################
    @property
    def name(self) -> str:
        return self.__class__.__name__.title()

    #########################################################################
    @property
    def speed(self) -> int:
        return 30


# EOF
