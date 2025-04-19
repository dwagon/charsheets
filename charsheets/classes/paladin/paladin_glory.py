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
extend_enum(Feature, "GLORIOUS_DEFENSE", "Glorious Defense")
extend_enum(Feature, "INSPIRING_SMITE", "Inspiring Smite")
extend_enum(Feature, "LIVING_LEGEND", "Living Legend")
extend_enum(Feature, "OATH_OF_GLORY_SPELLS", "Oath of Glory Spells")
extend_enum(Feature, "PEERLESS_ATHLETE", "Peerless Athlete")


#################################################################################
class PaladinOathOfGlory(Paladin):
    _class_name = "Paladin (Oath of Glory)"
    _sub_class = True

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
    def level15(self, **kwargs: Any):
        self.add_feature(GloriousDefense())

    #############################################################################
    def level20(self, **kwargs: Any):
        self.add_feature(LivingLegend())


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

    @property
    def desc(self) -> str:
        assert self.owner.paladin is not None
        lev = self.owner.paladin.level
        return f"""Immediately after you cast Divine Smite, you can expend one use of your Channel Divinity and
            distribute Temporary Hit Points to creatures of your choice within 30 feet of yourself, which can include
            you. The total number of Temporary Hit Points equals 2d8 plus {lev}, divided among the chosen creatures 
            however you like."""


#############################################################################
class AuraOfAlacrity(BaseFeature):
    tag = Feature.AURA_OF_ALACRITY
    # Your Speed increases by 10 feet.
    _desc = """Whenever an ally enters your Aura of Protection for the first time on a turn or starts their turn 
    there, the ally's Speed increases by 10 feet until the end of their next turn."""

    def mod_add_movement_speed(self, character: "Character") -> Reason[int]:
        return Reason("Aura of Alacrity", 10)


#############################################################################
class GloriousDefense(BaseFeature):
    tag = Feature.GLORIOUS_DEFENSE
    _desc = """You can turn defense into a sudden strike. When you or another creature you can see within 10 feet of 
    you is hit by an attack roll, you can take a Reaction to grant a bonus to the target's AC against that attack, 
    potentially causing it to miss. The bonus equals your Charisma modifier (minimum of +1). If the attack misses, 
    you can make one attack with a weapon against the attacker as part of this Reaction if the attacker is within 
    your weapon's range.

    You can use this feature a number of times equal to your Charisma modifier (minimum of once), and you regain all 
    expended uses when you finish a Long Rest."""


#############################################################################
class LivingLegend(BaseFeature):
    tag = Feature.LIVING_LEGEND
    _desc = """As a Bonus Action, you gain the benefits below for 10 minutes. Once you use this feature, you can't 
    use it again until you finish a Long Rest. You can also restore your use of it by expending a level 5 spell slot 
    (no action required).

    Charismatic. You are blessed with an otherworldly presence and have Advantage on all Charisma checks.

    Saving Throw Reroll. If you fail a saving throw, you can take a Reaction to reroll it. You must use this new roll.

    Unerring Strike. Once on each of your turns when you make an attack roll with a weapon and miss, you can cause 
    that attack to hit instead."""


# EOF
