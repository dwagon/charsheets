from charsheets.abilities.base_ability import BaseAbility
from charsheets.species import Species


#############################################################################
class Goliath(Species):
    #########################################################################
    def species_abilities(self) -> set[BaseAbility]:
        return set()

    #########################################################################
    @property
    def speed(self) -> int:
        return 35


# EOF
