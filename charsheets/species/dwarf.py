from charsheets.constants import Ability
from charsheets.species import Species


#############################################################################
class Dwarf(Species):
    #########################################################################
    def species_abilities(self) -> set[Ability]:
        return {Ability.DARKVISION120, Ability.DWARVEN_RESILIANCE, Ability.DWARVEN_TOUGHNESS, Ability.STONE_CUNNING}


# EOF
