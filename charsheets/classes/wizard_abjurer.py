from charsheets.classes.wizard import Wizard
from charsheets.constants import Ability


#################################################################################
class Abjurer(Wizard):
    pass

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities: set[Ability] = set()
        abilities |= super().class_abilities()
        abilities |= {Ability.ABJURATION_SAVANT, Ability.ARCANE_WARD}
        return abilities


# EOF
