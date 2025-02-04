from charsheets.classes.ranger import Ranger
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature


#################################################################################
class RangerBeastMaster(Ranger):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Beast Master"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {PrimalCompanion()}
        abilities |= super().class_features()
        if self.level >= 7:
            abilities |= {ExceptionalTraining()}
        return abilities


#############################################################################
class PrimalCompanion(BaseFeature):
    tag = Feature.PRIMAL_COMPANION
    _desc = """You magically summon a primal beast, which draws strength from your bond with nature."""


#############################################################################
class ExceptionalTraining(BaseFeature):
    tag = Feature.EXCEPTIONAL_TRAINING
    _desc = """When you take a Bonus Action to command your Primal Companion beast to take an action, you can also 
    command it to take the dash, Disengage, Dodge, or Help action using its Bonus Action.
    
    In addition, whenever it hits with an attack roll and deals damage, it can deal your choice of Force damage or it 
    normal damage type."""


# EOF
