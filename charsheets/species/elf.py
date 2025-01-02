from charsheets.abilities import Darkvision60
from charsheets.abilities.base_ability import BaseAbility
from charsheets.species.base_species import BaseSpecies


#############################################################################
class Elf(BaseSpecies):
    #########################################################################
    def species_abilities(self) -> set[BaseAbility]:
        return {Darkvision60()}


# EOF
