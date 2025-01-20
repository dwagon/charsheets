from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.ranger import Ranger
from charsheets.constants import Ability

if TYPE_CHECKING:  # pragma: no coverage
    pass


#################################################################################
class RangerBeastMaster(Ranger):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Ranger (Beast Master)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {PrimalCompanion()}
        abilities |= super().class_abilities()
        if self.level >= 7:
            abilities |= {ExceptionalTraining()}
        return abilities


#############################################################################
class PrimalCompanion(BaseAbility):
    tag = Ability.PRIMAL_COMPANION
    _desc = """You magically summon a primal beast, which draws strength from your bond with nature."""


#############################################################################
class ExceptionalTraining(BaseAbility):
    tag = Ability.EXCEPTIONAL_TRAINING
    _desc = """When you take a Bonus Action to command your Primal Companion beast to take an action, you can also 
    command it to take the dash, Disengage, Dodge, or Help action using its Bonus Action.
    
    In addition, whenever it hits with an attack roll and deals damage, it can deal your choice of Force damage or it 
    normal damage type."""


# EOF
