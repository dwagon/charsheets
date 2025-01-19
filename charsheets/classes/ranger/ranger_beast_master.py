from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.ranger import Ranger
from charsheets.constants import Ability

if TYPE_CHECKING:  # pragma: no coverage
    pass


#################################################################################
class RangerBeastMaster(Ranger):
    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {PrimalCompanion()}
        abilities |= super().class_abilities()
        return abilities


#############################################################################
class PrimalCompanion(BaseAbility):
    tag = Ability.PRIMAL_COMPANION
    _desc = """You magically summon a primal beast, which draws strength from your bond with nature."""


# EOF
