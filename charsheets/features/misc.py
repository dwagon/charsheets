"""Features that are shared between multiple species or classes"""

from typing import TYPE_CHECKING, cast

from aenum import extend_enum
from charsheets.constants import Feature, Sense, Skill
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter

extend_enum(Feature, "DARKVISION120", "Darkvision 120'")
extend_enum(Feature, "DARKVISION60", "Darkvision 60'")
extend_enum(Feature, "EVASION", "Evasion")
extend_enum(Feature, "EXPERTISE", "Expertise")
extend_enum(Feature, "EXTRA_ATTACK", "Extra Attack")
extend_enum(Feature, "WEAPON_MASTERY", "Weapon Mastery")


#############################################################################
class Expertise(BaseFeature):
    tag = Feature.EXPERTISE
    hide = True
    _desc = """You gain Expertise in two of your skill preferences of your choice."""

    #############################################################################
    def __init__(self, skill1: Skill, skill2: Skill):
        super().__init__()
        self.skills = [skill1, skill2]

    #############################################################################
    def mod_add_skill_expertise(self, character: "BaseCharacter") -> Reason[Skill]:
        return Reason("Expertise", *self.skills)


#############################################################################
class Darkvision120(BaseFeature):
    tag = Feature.DARKVISION120
    _desc = """You have Darkvision with a range of 120 feet"""
    hide = True

    def mod_add_sense(self, character: "BaseCharacter") -> Reason[Sense]:
        return Reason("Darkvsion120", cast(Sense, Sense.DARKVISION120))


#############################################################################
class Darkvision60(BaseFeature):
    tag = Feature.DARKVISION60
    _desc = """You have Darkvision with a range of 60 feet"""
    hide = True

    def mod_add_sense(self, character: "BaseCharacter") -> Reason[Sense]:
        return Reason("Darkvsion60", cast(Sense, Sense.DARKVISION60))


#############################################################################
class ExtraAttack(BaseFeature):
    tag = Feature.EXTRA_ATTACK
    _desc = """You can attack twice instead of once whenever you take the Attack action on your turn."""
    hide = True

    def __init__(self):
        self.number_str = "twice"

    def mod_extra_attack(self, character: "BaseCharacter") -> Reason[str]:
        return Reason("Extra Attack", f"Attack {self.number_str} per Attack action")


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
class Evasion(BaseFeature):
    tag = Feature.EVASION
    _desc = """When you're subjected to an effect that allows you to make a Dexterity saving throw to take only half 
    damage, you instead take no damage if you succeed on the saving throw and only half damage if you fail. You can't 
    use this feature if you have the Incapacitated Condition."""


# EOF
