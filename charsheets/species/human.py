from charsheets.constants import Ability
from charsheets.species import Species


#############################################################################
class Human(Species):
    #########################################################################
    def species_abilities(self) -> set[Ability]:
        return {Ability.RESOURCEFUL, Ability.SKILLFUL}


# EOF
