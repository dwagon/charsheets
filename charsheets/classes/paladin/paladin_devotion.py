from charsheets.classes.paladin import Paladin
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature
from charsheets.spell import Spell


#################################################################################
class PaladinOathOfDevotion(Paladin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Paladin (Oath of Devotion)"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {SacredWeapon()}
        abilities |= super().class_features()
        self.prepare_spells(Spell.PROTECTION_FROM_EVIL_AND_GOOD, Spell.SHIELD_OF_FAITH)
        if self.level >= 5:
            self.prepare_spells(Spell.AID, Spell.ZONE_OF_TRUTH)
        if self.level >= 7:
            abilities |= {AuraOfDevotion()}
        if self.level >= 9:
            self.prepare_spells(Spell.BEACON_OF_HOPE, Spell.DISPEL_MAGIC)
        return abilities


#############################################################################
class SacredWeapon(BaseFeature):
    tag = Feature.SACRED_WEAPON
    _desc = ""

    @property
    def desc(self) -> str:
        bonus = max(1, self.owner.charisma.modifier)
        return f"""When you take the Attack action, you can expend one use of your Channel Divinity to imbue one 
        Melee weapon that you are holding with positive energy. For 10 minutes or until you use this feature again, 
        you add {bonus}, and each time you hit with it, you cause it to deal its normal damage type or Radiant 
        damage. The weapon also emits Bright Light in a 20-foot radius and Dim Light 20 feet beyond that. You can end 
        this effect early (no action required). This effect also ends if you aren't carrying the weapon."""


#############################################################################
class AuraOfDevotion(BaseFeature):
    tag = Feature.AURA_OF_DEVOTION
    _desc = """You and your allies have Immunity to the Charmed condition while you are in your Aura of Protection. 
    If a Charmed ally enters the aura, that condition has no effect on that ally while there."""


# EOF
