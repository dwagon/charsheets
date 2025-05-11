from typing import Any

from aenum import extend_enum
from charsheets.classes.wizard import Wizard
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature

extend_enum(Feature, "EMPOWERED_EVOCATION", "Empowered Evocation")
extend_enum(Feature, "EVOCATION_SAVANT", "Evocation Savant")
extend_enum(Feature, "OVERCHANNEL", "Overchannel")
extend_enum(Feature, "POTENT_CANTRIP", "Potent Cantrip")
extend_enum(Feature, "SCULPT_SPELLS", "Sculpt Spells")


#################################################################################
class WizardEvoker(Wizard):
    _class_name = "Evoker"
    _sub_class = True

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(EvocationSavant())
        self.add_feature(PotentCantrip())

    #############################################################################
    def level6(self, **kwargs: Any):
        self.add_feature(SculptSpells())

    #############################################################################
    def level10(self, **kwargs: Any):
        self.add_feature(EmpoweredEvocation())

    #############################################################################
    def level14(self, **kwargs: Any):
        self.add_feature(Overchannel())


#############################################################################
class EvocationSavant(BaseFeature):
    tag = Feature.EVOCATION_SAVANT
    hide = True
    _desc = """Choose two Wizard spells from the Evocation school, each of which must be no higher than level 2, 
    and add them to your spellbook for free. In addition, whenever you gain access to a new level of spell slots in 
    this class, you can add one Wizard spell from the Evocation school to your spellbook for free. The chosen spell 
    must be of a level for which you have spell slots."""


#############################################################################
class PotentCantrip(BaseFeature):
    tag = Feature.POTENT_CANTRIP
    _desc = """Your damaging cantrips affect even creatures that avoid the brunt of the effect. When you cast a 
    cantrip at a creature and you miss with the attack roll or the target succeeds on a saving throw against the 
    cantrip, the target takes half the cantrip’s damage (if any) but suffers no additional effect from the cantrip."""


#############################################################################
class SculptSpells(BaseFeature):
    tag = Feature.SCULPT_SPELLS
    _desc = """You can create pockets of relative safety within the effects of your evocations. When you cast an 
    Evocation spell that affects other creatures that you can see, you can choose a number of them equal to 1 plus 
    the spell's level. The chosen creatures automatically succeed on their saving throws against the spell, 
    and they take no damage if they would normally take half damage on a successful save."""


#############################################################################
class EmpoweredEvocation(BaseFeature):
    tag = Feature.EMPOWERED_EVOCATION
    _desc = """Whenever you cast a Wizard spell from the Evocation school, you can add your Intelligence modifier to 
    one damage roll of that spell."""


#############################################################################
class Overchannel(BaseFeature):
    tag = Feature.OVERCHANNEL
    _desc = """You can increase the power of your spells. When you cast a Wizard spell with a spell slot of levels 
    1-5 that deals damage, you can deal maximum damage with that spell on the turn you cast it.

    The first time you do so, you suffer no adverse effect. If you use this feature again before you finish a 
    Long Rest, you take 2d12 Necrotic damage for each level of the spell slot immediately after you cast it. This 
    damage ignores Resistance and Immunity.

    Each time you use this feature again before finishing a Long Rest, the Necrotic damage per spell level 
    increases by 1d12."""


# EOF
