from charsheets.classes.wizard import Wizard
from charsheets.constants import Ability


#################################################################################
class Illusionist(Wizard):
    pass

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities: set[Ability] = set()
        abilities |= super().class_abilities()
        abilities |= {Ability.ILLUSION_SAVANT, Ability.IMPROVED_ILLUSIONS}
        return abilities


# EOF
