from typing import TYPE_CHECKING
from aenum import extend_enum

from charsheets.ability import BaseAbility
from charsheets.constants import Ability, Movements
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character

#############################################################################
extend_enum(Ability, "AMPHIBIOUS", "Amphibious")
extend_enum(Ability, "SPEAK_WITH_FISH", "Speak with Fish")
extend_enum(Ability, "SLIPPERY", "Slippery")
extend_enum(Ability, "OTHERWORLDLY_PERCEPTION", "Otherworldly Perception")
extend_enum(Ability, "SWIM", "Swim")
extend_enum(Ability, "DARKVISION_UNDERWATER120", "Darkvision Underwater 120")


#############################################################################
class AbilityAmphibious(BaseAbility):
    tag = Ability.AMPHIBIOUS
    desc = """You can breathe air and water."""


#############################################################################
class AbilitySpeakWithFish(BaseAbility):
    tag = Ability.SPEAK_WITH_FISH
    desc = """As a bonus action you can cast Speak With Animals that works only on aquatic or underwater animals.
    You can use this Bonus Action a number of times equal to your Proficiency Bonus, and you regain all expended uses
    when you finish a Long Rest."""


#############################################################################
class AbilitySlippery(BaseAbility):
    tag = Ability.SLIPPERY
    desc = """You have advantage on ability checks and saving throws made to escape a grapple."""


#############################################################################
class AbilityOtherworldlyPerception(BaseAbility):
    tag = Ability.OTHERWORLDLY_PERCEPTION
    desc = """As a bonus action you can sense invisible creatures within 30 feet and pinpoint
    such a creature that is moving."""


#############################################################################
class AbilitySwim(BaseAbility):
    tag = Ability.SWIM
    desc = """Swim 30 feet"""

    def mod_swim_movement(self, character: "Character") -> int:
        return 30


#############################################################################
class AbilityDarkvisionUnderwater120(BaseAbility):
    tag = Ability.DARKVISION_UNDERWATER120
    desc = """Darkvision Underwater for 120 feet"""
