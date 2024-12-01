from charsheets.constants import Ability
from charsheets.species import Species


#############################################################################
class Elf(Species):
    #########################################################################
    def species_abilities(self) -> set[Ability]:
        return {Ability.DARKVISION60}


# EOF
