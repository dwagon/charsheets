""" Abilities"""

from typing import TYPE_CHECKING

from charsheets.attack import Attack
from charsheets.constants import Ability, DamageType, Tool, Skill
from charsheets.reason import Reason
from charsheets.spells import Spells

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class BaseAbility:
    _desc = "Unspecified"
    tag: Ability = Ability.NONE
    hide: bool = False

    #############################################################################
    @property
    def desc(self) -> str:
        return self._desc

    #############################################################################
    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spells]:
        return Reason()

    #############################################################################
    def mod_add_attack(self, character: "Character") -> Reason[Attack]:
        return Reason()

    #############################################################################
    def mod_add_damage_resistances(self, character: "Character") -> Reason[DamageType]:
        return Reason()

    #############################################################################
    def mod_swim_movement(self, character: "Character") -> Reason[int]:
        return Reason[int]()

    #############################################################################
    def mod_fly_movement(self, character: "Character") -> Reason[int]:
        return Reason[int]()

    #############################################################################
    def mod_add_tool_proficiency(self, character: "Character") -> Reason[Tool]:
        return Reason[Tool]()

    #############################################################################
    def mod_add_movement_speed(self, character: "Character") -> Reason[int]:
        return Reason()

    #############################################################################
    def mod_add_skill_proficiency(self, character: "Character") -> Reason[Skill]:
        return Reason()


# EOF
