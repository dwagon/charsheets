from charsheets.classes.ranger import Ranger
from charsheets.constants import Ability


#################################################################################
class BeastMaster(Ranger):
    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities: set[Ability] = {Ability.PRIMAL_COMPANION}
        abilities |= super().class_abilities()
        return abilities


# EOF
