from aenum import extend_enum

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
        if self.level >= 11:
            abilities |= {BestialFury()}
        return abilities


extend_enum(Feature, "BESTIAL_FURY", "Bestial Fury")
extend_enum(Feature, "EXCEPTIONAL_TRAINING", "Exceptional Training")
extend_enum(Feature, "PRIMAL_COMPANION", "Primal Companion")


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


#############################################################################
class BestialFury(BaseFeature):
    tag = Feature.BESTIAL_FURY
    _desc = """When you command your Primal Companion beast to take the Beast's Strike action, the beast can use it 
    twice.

    In addition, the first time each turn it hits a creature under the effect of your Hunter's Mark spell, 
    the beast deals extra Force damage equal to the bonus damage of that spell."""


# EOF
