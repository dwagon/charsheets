from charsheets.classes.wizard import Wizard
from charsheets.constants import Ability


#################################################################################
class Diviner(Wizard):
    pass

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities: set[Ability] = set()
        abilities |= super().class_abilities()
        abilities |= {Ability.DIVINATION_SAVANT, Ability.PORTENT}
        return abilities


# EOF
