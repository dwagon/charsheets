from typing import TYPE_CHECKING, Any

from aenum import extend_enum

from charsheets.classes.paladin import Paladin
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character

extend_enum(Feature, "AURA_OF_ALACRITY", "Aura of Alacrity")
extend_enum(Feature, "INSPIRING_SMITE", "Inspiring Smite")
extend_enum(Feature, "OATH_OF_GLORY_SPELLS", "Oath of Glory Spells")
extend_enum(Feature, "PEERLESS_ATHLETE", "Peerless Athlete")


#################################################################################
class PaladinOathOfGlory(Paladin):
    _class_name = "Paladin (Oath of Glory)"

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(PeerlessAthlete())
        self.add_feature(InspiringSmite())
        self.add_feature(OathOfGlorySpells())
        super().level3(**kwargs)

    #############################################################################
    def level7(self, **kwargs: Any):
        self.add_feature(AuraOfAlacrity())


#############################################################################
class OathOfGlorySpells(BaseFeature):
    tag = Feature.OATH_OF_GLORY_SPELLS
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        spells = Reason("Oath of Glory", Spell.GUIDING_BOLT, Spell.HEROISM)
        if character.level >= 5:
            spells |= Reason("Oath of Glory", Spell.ENHANCE_ABILITY, Spell.MAGIC_WEAPON)
        if character.level >= 9:
            spells |= Reason("Oath of Glory", Spell.HASTE, Spell.PROTECTION_FROM_ENERGY)
        if character.level >= 13:
            spells |= Reason("Oath of Glory", Spell.COMPULSION, Spell.FREEDOM_OF_MOVEMENT)
        if character.level >= 17:
            spells |= Reason("Oath of Glory", Spell.LEGEND_LORE, Spell.YOLANDES_REGAL_PRESENCE)
        return spells


#############################################################################
class PeerlessAthlete(BaseFeature):
    tag = Feature.PEERLESS_ATHLETE
    _desc = """As a Bonus Action, you can expend one use of your Channel Divinity to augment your athleticism. For 1 
    hour, you have Advantage on Strength (Athletics) and Dexterity (Acrobatics) checks, and the distance of your Long 
    and High Jumps increases by 10 feet

    In addition, whenever an ally enters your Aura of Protection for the first time on a turn or starts their turn
    there, the ally's Speed increases by 10 feet until the end of their next turn."""


#############################################################################
class InspiringSmite(BaseFeature):
    tag = Feature.INSPIRING_SMITE
    _desc = """Immediately after you cast Divine Smite, you can expend one use of your Channel Divinity and 
    distribute Temporary Hit Points to creatures of your choice within 30 feet of yourself, which can include you. 
    The total number of Temporary Hit Points equals 2d8 plus your Paladin level, divided among the chosen creatures 
    however you like."""


#############################################################################
class AuraOfAlacrity(BaseFeature):
    tag = Feature.AURA_OF_ALACRITY
    _desc = """Your Speed increases by 10 feet.
    
    In addition, whenever an ally enters your Aura of Protection for the first time on a turn or starts their turn 
    there, the ally's Speed increases by 10 feet until the end of their next turn."""


# EOF
