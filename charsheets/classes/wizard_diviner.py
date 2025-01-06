from charsheets.abilities import DivinationSavant, Portent
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.wizard import Wizard


#################################################################################
class WizardDiviner(Wizard):
    pass

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = set()
        abilities |= super().class_abilities()
        abilities |= {DivinationSavant(), Portent()}
        return abilities


# EOF
