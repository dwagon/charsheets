from typing import TYPE_CHECKING

from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Ability, Sense, Stat
from charsheets.reason import Reason

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class Darkvision120(BaseAbility):
    tag = Ability.DARKVISION120
    _desc = """You have Darkvision with a range of 120 feet"""
    hide = True

    def mod_add_sense(self, character: "Character") -> Reason[Sense]:
        return Reason("Darkvsion120", Sense.DARKVISION120)


#############################################################################
class Darkvision60(BaseAbility):
    tag = Ability.DARKVISION60
    _desc = """You have Darkvision with a range of 60 feet"""
    hide = True

    def mod_add_sense(self, character: "Character") -> Reason[Sense]:
        return Reason("Darkvsion60", Sense.DARKVISION60)


#############################################################################
class ExtraAttack(BaseAbility):
    tag = Ability.EXTRA_ATTACK
    _desc = """You can attack twice instead of once whenever you take the Attack action on your turn."""


#############################################################################
class WeaponMastery(BaseAbility):
    tag = Ability.WEAPON_MASTERY
    _desc = """Your training with weapons allows you to use the mastery properties of two kinds of weapons of your
    choice with which you have proficiency. Whenever you finish a Long Rest, you can change the kinds of weapons
    you choose."""


#############################################################################
class AbilityScoreImprovement(BaseAbility):
    tag = Ability.ABILITY_SCORE_IMPROVEMENT
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
class Actor(BaseAbility):
    tag = Ability.ACTOR

    #############################################################################
    @property
    def desc(self) -> str:
        bonus = self.character.charisma.modifier + 8 + self.character.proficiency_bonus
        return f"""You gain the following benefits.

        Impersonation. While you're disguised as a real or fictional person,you have Advantage on Charisma (Deception 
        or Performance) checks to convince others that you are that person.

        Mimicry. You can mimic the sounds of other creatures, including speech. A creature that hears the mimicry 
        must succeed on a Wisdom (Insight) check to determine the effect is faked (DC {bonus})."""

    #############################################################################
    def mod_stat_cha(self, character: "Character") -> int:
        return 1


# EOF
