from charsheets.constants import Ability
from charsheets.species import Species


#############################################################################
class Goliath(Species):
    #########################################################################
    def species_abilities(self) -> set[Ability]:
        return set()

    #########################################################################
    @property
    def speed(self) -> int:
        return 35


# EOF
