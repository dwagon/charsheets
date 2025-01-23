""" Abilities"""

from typing import TYPE_CHECKING

from charsheets.attack import Attack
from charsheets.constants import Feature, DamageType, Tool, Skill, Sense, Language
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class BaseFeature:
    _desc = "Unspecified"
    tag: Feature = Feature.NONE
    hide: bool = False
    _goes: int = 0
    owner: "Character"

    #############################################################################
    def add_owner(self, owner: "Character"):
        self.owner = owner

    #############################################################################
    @property
    def goes(self) -> int:
        return self._goes

    #############################################################################
    @property
    def desc(self) -> str:
        return self._desc

    #############################################################################
    def __lt__(self, other):
        return self.tag < other.tag

    #############################################################################
    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
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

    #############################################################################
    def mod_add_sense(self, character: "Character") -> Reason[Sense]:
        return Reason[Sense]()

    #############################################################################
    def mod_add_known_spells(self, character: "Character") -> Reason[Spell]:
        return Reason[Spell]()

    #############################################################################
    def mod_add_language(self, character: "Character") -> Reason[Language]:
        return Reason[Language]()

    #############################################################################
    def mod_hp_bonus(self, character: "Character") -> Reason[int]:
        return Reason[int]()

    #############################################################################
    def mod_ac_bonus(self, character: "Character") -> Reason[int]:
        return Reason[int]()


# EOF
