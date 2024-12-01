from charsheets.constants import Ability
from charsheets.species import Species


#############################################################################
class Halfling(Species):
    #########################################################################
    def species_abilities(self) -> set[Ability]:
        return {Ability.BRAVE, Ability.HALFLING_NIMBLENESS, Ability.LUCK, Ability.NATURALLY_STEALTHY}


# EOF
