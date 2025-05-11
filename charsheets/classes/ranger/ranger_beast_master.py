from typing import Any

from aenum import extend_enum
from charsheets.classes.ranger import Ranger
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature

extend_enum(Feature, "BESTIAL_FURY", "Bestial Fury")
extend_enum(Feature, "EXCEPTIONAL_TRAINING", "Exceptional Training")
extend_enum(Feature, "PRIMAL_COMPANION", "Primal Companion")
extend_enum(Feature, "SHARE_SPELLS", "Share Spells")


#################################################################################
class RangerBeastMaster(Ranger):
    _class_name = "Beast Master"
    _sub_class = True

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(PrimalCompanion())

    #############################################################################
    def level7(self, **kwargs: Any):
        self.add_feature(ExceptionalTraining())

    #############################################################################
    def level11(self, **kwargs: Any):
        self.add_feature(BestialFury())

    #############################################################################
    def level15(self, **kwargs: Any):
        self.add_feature(ShareSpells())


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


#############################################################################
class ShareSpells(BaseFeature):
    tag = Feature.SHARE_SPELLS
    _desc = """When you cast a spell targeting yourself, you can also affect your Primal Companion beast with the 
    spell if the beast is within 30 feet of you."""


# EOF
