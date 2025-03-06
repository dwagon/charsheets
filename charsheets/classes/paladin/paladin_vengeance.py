from aenum import extend_enum

from charsheets.classes.paladin import Paladin
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature
from charsheets.spell import Spell


#################################################################################
class PaladinOathOfVengeance(Paladin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Paladin (Oath of Vengeance)"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {VowOfEmnity()}
        abilities |= super().class_features()
        self.prepare_spells(Spell.BANE, Spell.HUNTERS_MARK)
        if self.level >= 5:
            self.prepare_spells(Spell.HOLD_PERSON, Spell.MISTY_STEP)
        if self.level >= 7:
            abilities |= {RelentlessAvenger()}
        if self.level >= 9:
            self.prepare_spells(Spell.HASTE, Spell.PROTECTION_FROM_ENERGY)
        return abilities


extend_enum(Feature, "RELENTLESS_AVENGER", "Relentless Avenger")
extend_enum(Feature, "VOW_OF_EMNITY", "Vow of Emnity")


#############################################################################
class VowOfEmnity(BaseFeature):
    tag = Feature.VOW_OF_EMNITY
    _desc = """When you take the Attack action, you can expend one use of your Channel Divinity to utter a vow of
    enmity against a creature you can see within 30 feet of yourself. You have Advantage on attack rolls
    against the creature for 1 minute or until you use this feature again.

    If the creature drops to O Hit Points before the vow ends, you can transfer the vow to a different creature within 
    30 feet of yourself (no action required)."""


#############################################################################
class RelentlessAvenger(BaseFeature):
    tag = Feature.RELENTLESS_AVENGER
    _desc = """Your supernatural focus helps you close off a foe's retreat. When you hit a creature with an 
    Opportunity Attack, you can reduce the creature's Speed to 0 until the end of the current turn. You can then move 
    up to half your Speed as part of the same Reaction. This movement doesn't provoke Opportunity Attacks."""


# EOF
