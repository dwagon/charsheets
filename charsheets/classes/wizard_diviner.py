from charsheets.abilities import DivinationSavant, Portent, ExpertDivination
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.wizard import Wizard


#################################################################################
class WizardDiviner(Wizard):
    pass

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {DivinationSavant(), Portent()}
        abilities |= super().class_abilities()
        if self.level >= 6:
            abilities |= {ExpertDivination()}
        return abilities


# EOF
