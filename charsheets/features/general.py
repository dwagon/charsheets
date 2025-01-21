from typing import TYPE_CHECKING

from charsheets.features.base_feature import BaseFeature
from charsheets.constants import Feature, Sense, Stat
from charsheets.reason import Reason

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class Darkvision120(BaseFeature):
    tag = Feature.DARKVISION120
    _desc = """You have Darkvision with a range of 120 feet"""
    hide = True

    def mod_add_sense(self, character: "Character") -> Reason[Sense]:
        return Reason("Darkvsion120", Sense.DARKVISION120)


#############################################################################
class Darkvision60(BaseFeature):
    tag = Feature.DARKVISION60
    _desc = """You have Darkvision with a range of 60 feet"""
    hide = True

    def mod_add_sense(self, character: "Character") -> Reason[Sense]:
        return Reason("Darkvsion60", Sense.DARKVISION60)


#############################################################################
class ExtraAttack(BaseFeature):
    tag = Feature.EXTRA_ATTACK
    _desc = """You can attack twice instead of once whenever you take the Attack action on your turn."""


#############################################################################
class WeaponMastery(BaseFeature):
    tag = Feature.WEAPON_MASTERY

    def __init__(self, num=2):
        super().__init__()
        self.num_weapons = num

    @property
    def desc(self) -> str:
        return f"""Your training with weapons allows you to use the mastery properties of {self.num_weapons} kinds of
         weapons of your choice with which you have proficiency. Whenever you finish a Long Rest, you can change
         the kinds of weapons you choose."""


#############################################################################
class AbilityScoreImprovement(BaseFeature):
    tag = Feature.ABILITY_SCORE_IMPROVEMENT
    _desc = """Increase a stat twice"""
    hide = True

    def __init__(self, stat1: Stat, stat2: Stat):
        super().__init__()
        self.stats = [stat1, stat2]

    #############################################################################
    @property
    def desc(self) -> str:
        if self.stats[0] == self.stats[1]:
            return f"Increased {self.stats[0].title()} twice"
        return f"Increased {self.stats[0].title()} and {self.stats[1].title()}"

    #############################################################################
    def mod_stat_str(self, character: "Character") -> int:
        return self.stats.count(Stat.STRENGTH)

    #############################################################################
    def mod_stat_dex(self, character: "Character") -> int:
        return self.stats.count(Stat.DEXTERITY)

    #############################################################################
    def mod_stat_con(self, character: "Character") -> int:
        return self.stats.count(Stat.CONSTITUTION)

    #############################################################################
    def mod_stat_int(self, character: "Character") -> int:
        return self.stats.count(Stat.INTELLIGENCE)

    #############################################################################
    def mod_stat_wis(self, character: "Character") -> int:
        return self.stats.count(Stat.WISDOM)

    #############################################################################
    def mod_stat_cha(self, character: "Character") -> int:
        return self.stats.count(Stat.CHARISMA)


#############################################################################
class Actor(BaseFeature):
    tag = Feature.ACTOR

    #############################################################################
    @property
    def desc(self) -> str:
        bonus = self.owner.charisma.modifier + 8 + self.owner.proficiency_bonus
        return f"""You gain the following benefits.

        Impersonation. While you're disguised as a real or fictional person,you have Advantage on Charisma (Deception 
        or Performance) checks to convince others that you are that person.

        Mimicry. You can mimic the sounds of other creatures, including speech. A creature that hears the mimicry 
        must succeed on a Wisdom (Insight) check to determine the effect is faked (DC {bonus})."""

    #############################################################################
    def mod_stat_cha(self, character: "Character") -> int:
        return 1


#############################################################################
class Evasion(BaseFeature):
    tag = Feature.EVASION
    _desc = """You can nimbly dodge out of the way of certain dangers. When you're subjected to an effect that allows 
    you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the 
    saving throw and only half damage if you fail. You can't use this feature if you have the Incapacitated 
    Condition."""


# EOF
