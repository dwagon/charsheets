from charsheets.classes.wizard import Wizard
from charsheets.constants import Ability


#################################################################################
class Evoker(Wizard):
    pass

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities: set[Ability] = set()
        abilities |= super().class_abilities()
        abilities |= {Ability.EVOCATION_SAVANT, Ability.POTENT_CANTRIP}
        return abilities


# EOF
