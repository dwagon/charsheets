from charsheets.abilities import IllusionSavant, ImprovedIllusions, PhantasmalCreatures
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.wizard import Wizard


#################################################################################
class WizardIllusionist(Wizard):
    pass

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {IllusionSavant(), ImprovedIllusions()}
        abilities |= super().class_abilities()
        if self.level >= 6:
            abilities |= {PhantasmalCreatures()}
        return abilities


# EOF
