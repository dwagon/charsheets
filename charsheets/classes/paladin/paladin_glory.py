from charsheets.classes.paladin import Paladin
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature
from charsheets.spell import Spell


#################################################################################
class PaladinOathOfGlory(Paladin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Paladin (Oath of Glory)"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {PeerlessAthlete(), InspiringSmite()}
        abilities |= super().class_features()
        self.prepare_spells(Spell.GUIDING_BOLT, Spell.HEROISM)
        if self.level >= 5:
            self.prepare_spells(Spell.ENHANCE_ABILITY, Spell.MAGIC_WEAPON)
        if self.level >= 7:
            abilities |= {AuraOfAlacrity()}
        if self.level >= 9:
            self.prepare_spells(Spell.HASTE, Spell.PROTECTION_FROM_ENERGY)
        return abilities


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
