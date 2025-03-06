from aenum import extend_enum

from charsheets.classes.wizard import Wizard
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature


#################################################################################
class WizardEvoker(Wizard):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Evoker"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {EvocationSavant(), PotentCantrip()}
        abilities |= super().class_features()
        if self.level >= 6:
            abilities |= {SculptSpells()}
        if self.level >= 10:
            abilities |= {EmpoweredEvocation()}
        return abilities


#############################################################################
class EvocationSavant(BaseFeature):
    tag = Feature.EVOCATION_SAVANT
    hide = True
    _desc = """Choose two Wizard spells from the Evocation school, each of which must be no higher than level 2, 
    and add them to your spellbook for free. In addition, whenever you gain access to a new level of spell slots in 
    this class, you can add one Wizard spell from the Evocation school to your spellbook for free. The chosen spell 
    must be of a level for which you have spell slots."""


extend_enum(Feature, "EMPOWERED_EVOCATION", "Empowered Evocation")
extend_enum(Feature, "POTENT_CANTRIP", "Potent Cantrip")
extend_enum(Feature, "SCULPT_SPELLS", "Sculpt Spells")


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


# EOF
