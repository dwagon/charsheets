from charsheets.abilities import Darkvision60
from charsheets.abilities.base_ability import BaseAbility
from charsheets.species import Species


#############################################################################
class Elf(Species):
    #########################################################################
    def species_abilities(self) -> set[BaseAbility]:
        return {Darkvision60()}


# EOF
