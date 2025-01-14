from charsheets.abilities import EvocationSavant, PotentCantrip, SculptSpells
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.wizard import Wizard


#################################################################################
class WizardEvoker(Wizard):
    pass

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {EvocationSavant(), PotentCantrip()}
        abilities |= super().class_abilities()
        if self.level >= 6:
            abilities |= {SculptSpells()}
        return abilities


# EOF
