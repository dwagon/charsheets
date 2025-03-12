from aenum import extend_enum
from typing import TYPE_CHECKING

from charsheets.classes.paladin import Paladin
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character

extend_enum(Feature, "OATH_OF_VENGEANCE_SPELLS", "Oath of Vengeance Spells")
extend_enum(Feature, "RELENTLESS_AVENGER", "Relentless Avenger")
extend_enum(Feature, "VOW_OF_EMNITY", "Vow of Emnity")


#################################################################################
class PaladinOathOfVengeance(Paladin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Paladin (Oath of Vengeance)"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {VowOfEmnity(), OathOfVengeanceSpells()}
        abilities |= super().class_features()
        if self.level >= 7:
            abilities |= {RelentlessAvenger()}
        return abilities


#############################################################################
class OathOfVengeanceSpells(BaseFeature):
    tag = Feature.OATH_OF_VENGEANCE_SPELLS
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        spells = Reason("Oath of Devotion", Spell.BANE, Spell.HUNTERS_MARK)
        if character.level >= 5:
            spells |= Reason("Oath of Devotion", Spell.HOLD_PERSON, Spell.MISTY_STEP)
        if character.level >= 9:
            spells |= Reason("Oath of Devotion", Spell.HASTE, Spell.PROTECTION_FROM_ENERGY)
        return spells


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
