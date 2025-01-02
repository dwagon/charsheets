from charsheets.abilities.base_ability import BaseAbility
from charsheets.species.base_species import BaseSpecies


#############################################################################
class Goliath(BaseSpecies):
    #########################################################################
    def species_abilities(self) -> set[BaseAbility]:
        return set()

    #########################################################################
    @property
    def speed(self) -> int:
        return 35


# EOF
