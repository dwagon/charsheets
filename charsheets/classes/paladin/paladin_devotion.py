from typing import TYPE_CHECKING, Any

from aenum import extend_enum

from charsheets.classes.paladin import Paladin
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character

extend_enum(Feature, "AURA_OF_DEVOTION", "Aura of Devotion")
extend_enum(Feature, "HOLY_NIMBUS", "Holy Nimbus")
extend_enum(Feature, "OATH_OF_DEVOTION_SPELLS", "Oath of Devotion Spells")
extend_enum(Feature, "SACRED_WEAPON", "Sacred Weapon")
extend_enum(Feature, "SMITE_OF_PROTECTION", "Smit of Protection")


#################################################################################
class PaladinOathOfDevotion(Paladin):
    _class_name = "Paladin (Oath of the Devotion)"
    _sub_class = True

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(SacredWeapon())
        self.add_feature(OathOfDevotionSpells())
        super().level3(**kwargs)

    #############################################################################
    def level7(self, **kwargs: Any):
        self.add_feature(AuraOfDevotion())

    #############################################################################
    def level15(self, **kwargs: Any):
        self.add_feature(SmiteOfProtection())

    #############################################################################
    def level20(self, **kwargs: Any):
        self.add_feature(HolyNimbus())


#############################################################################
class OathOfDevotionSpells(BaseFeature):
    tag = Feature.OATH_OF_DEVOTION_SPELLS
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        spells = Reason("Oath of Devotion", Spell.PROTECTION_FROM_EVIL_AND_GOOD, Spell.SHIELD_OF_FAITH)
        if character.level >= 5:
            spells |= Reason("Oath of Devotion", Spell.AID, Spell.ZONE_OF_TRUTH)
        if character.level >= 9:
            spells |= Reason("Oath of Devotion", Spell.BEACON_OF_HOPE, Spell.DISPEL_MAGIC)
        if character.level >= 13:
            spells |= Reason("Oath of Devotion", Spell.FREEDOM_OF_MOVEMENT, Spell.GUARDIAN_OF_FAITH)
        if character.level >= 17:
            spells |= Reason("Oath of Devotion", Spell.COMMUNE, Spell.FLAME_STRIKE)
        return spells


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


#############################################################################
class SmiteOfProtection(BaseFeature):
    tag = Feature.SMITE_OF_PROTECTION
    _desc = """Your magical smite now radiates protective energy. Whenever you cast Divine Smite, you and your allies 
    have Half Cover while in your Aura of Protection. The aura has this benefit until the start of your next turn."""


#############################################################################
class HolyNimbus(BaseFeature):
    tag = Feature.HOLY_NIMBUS
    _desc = """As a Bonus Action, you can imbue your Aura of Protection with holy power, granting the benefits below 
    for 10 minutes or until you end them (no action required). Once you use this feature, you can't use it again 
    until you finish a Long Rest. You can also restore your use of it by expending a level 5 spell slot (no action 
    required).
    
    Holy Ward. You have Advantage on any saving throw you are forced to make by a Fiend or an Undead.

    Radiant Damage. Whenever an enemy starts its turn in the aura, that creature takes Radiant damage equal to your 
    Charisma modifier plus your Proficiency Bonus.

    Sunlight. The aura is filled with Bright Light that is sunlight."""


# EOF
