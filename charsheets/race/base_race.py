from typing import TYPE_CHECKING

from charsheets.features.base_feature import BaseFeature

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class BaseRace:
    def __init__(self) -> None:
        self.character: Character | None = None
        self.speed = 30

    #########################################################################
    def species_feature(self) -> set[BaseFeature]:
        raise NotImplementedError

    #########################################################################
    @property
    def name(self) -> str:
        return self.__class__.__name__.title()


# EOF
