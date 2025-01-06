from charsheets.abilities import IllusionSavant, ImprovedIllusions
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.wizard import Wizard


#################################################################################
class WizardIllusionist(Wizard):
    pass

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = set()
        abilities |= super().class_abilities()
        abilities |= {IllusionSavant(), ImprovedIllusions()}
        return abilities


# EOF
