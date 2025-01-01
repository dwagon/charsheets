from charsheets.abilities import EvocationSavant, PotentCantrip
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.wizard import Wizard


#################################################################################
class Evoker(Wizard):
    pass

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = set()
        abilities |= super().class_abilities()
        abilities |= {EvocationSavant(), PotentCantrip()}
        return abilities


# EOF
