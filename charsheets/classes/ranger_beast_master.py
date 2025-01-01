from charsheets.abilities import PrimalCompanion
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.ranger import Ranger


#################################################################################
class BeastMaster(Ranger):
    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {PrimalCompanion()}
        abilities |= super().class_abilities()
        return abilities


# EOF
