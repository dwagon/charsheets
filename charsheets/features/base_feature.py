"""Abilities"""

from typing import TYPE_CHECKING

from charsheets.attack import Attack
from charsheets.constants import Feature, DamageType, Tool, Skill, Sense, Language, Recovery, Stat, Proficiency
from charsheets.exception import InvalidOption
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter


#############################################################################
class BaseFeature:
    _desc = "Unspecified"
    tag: Feature = Feature.NONE
    hide: bool = False
    recovery: Recovery = Recovery.NONE
    _goes: int = 0
    owner: "BaseCharacter"

    #############################################################################
    def __repr__(self):
        return self.__class__.__name__

    #############################################################################
    @property
    def long_rest(self) -> bool:
        return self.recovery == Recovery.LONG_REST

    #############################################################################
    @property
    def short_rest(self) -> bool:
        return self.recovery == Recovery.SHORT_REST

    #############################################################################
    @property
    def partial_rest(self) -> bool:
        """1/SR All / LR"""
        return self.recovery == Recovery.PARTIAL

    #############################################################################
    def add_owner(self, owner: "BaseCharacter"):
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
    def mod_add_prepared_spells(self, character: "BaseCharacter") -> Reason[Spell]:
        return Reason()

    #############################################################################
    def mod_add_attack(self, character: "BaseCharacter") -> Reason[Attack]:
        return Reason()

    #############################################################################
    def mod_add_damage_resistances(self, character: "BaseCharacter") -> Reason[DamageType]:
        return Reason()

    #############################################################################
    def mod_swim_movement(self, character: "BaseCharacter") -> Reason[int]:
        return Reason[int]()

    #############################################################################
    def mod_fly_movement(self, character: "BaseCharacter") -> Reason[int]:
        return Reason[int]()

    #############################################################################
    def mod_add_tool_proficiency(self, character: "BaseCharacter") -> Reason[Tool]:
        return Reason[Tool]()

    #############################################################################
    def mod_add_movement_speed(self, character: "BaseCharacter") -> Reason[int]:
        return Reason()

    #############################################################################
    def mod_add_skill_proficiency(self, character: "BaseCharacter") -> Reason[Skill]:
        return Reason()

    #############################################################################
    def mod_add_skill_expertise(self, character: "BaseCharacter") -> Reason[Skill]:
        return Reason()

    #############################################################################
    def mod_add_sense(self, character: "BaseCharacter") -> Reason[Sense]:
        return Reason[Sense]()

    #############################################################################
    def mod_add_known_spells(self, character: "BaseCharacter") -> Reason[Spell]:
        return Reason[Spell]()

    #############################################################################
    def mod_add_language(self, character: "BaseCharacter") -> Reason[Language]:
        return Reason[Language]()

    #############################################################################
    def mod_hp_bonus(self, character: "BaseCharacter") -> Reason[int]:
        return Reason[int]()

    #############################################################################
    def mod_ac_bonus(self, character: "BaseCharacter") -> Reason[int]:
        return Reason[int]()

    #############################################################################
    def mod_extra_attack(self, character: "BaseCharacter") -> Reason[str]:
        return Reason[str]()

    #############################################################################
    def mod_initiative_bonus(self, character: "BaseCharacter") -> Reason[int]:
        return Reason[int]()

    #############################################################################
    def mod_armour_proficiency(self, character: "BaseCharacter") -> Reason[Proficiency]:
        return Reason[Proficiency]()

    #############################################################################
    def mod_weapon_proficiency(self, character: "BaseCharacter") -> Reason[Proficiency]:
        return Reason[Proficiency]()


#############################################################################
class StatIncreaseFeature(BaseFeature):
    _valid_stats: list[Stat] = []
    _num_stats = 1

    def __init__(self, *stats: Stat):
        if len(self._valid_stats) == 1:
            stats = tuple(self._valid_stats)
        if not stats:
            raise InvalidOption(f"Need to specify a stat to increase for {self.__class__.__name__}")
        if len(stats) != self._num_stats:
            raise InvalidOption(f"Need to specify {self._num_stats} for {self.__class__.__name__}")
        for stat in stats:
            if stat not in self._valid_stats:
                raise InvalidOption(f"{stat} not valid for {self.__class__.__name__}")
        self.stats = stats

    #############################################################################
    def mod_stat_str(self, character: "BaseCharacter") -> Reason[int]:
        return Reason(self.__class__.__name__, self.stats.count(Stat.STRENGTH))

    #############################################################################
    def mod_stat_dex(self, character: "BaseCharacter") -> Reason[int]:
        return Reason(self.__class__.__name__, self.stats.count(Stat.DEXTERITY))

    #############################################################################
    def mod_stat_con(self, character: "BaseCharacter") -> Reason[int]:
        return Reason(self.__class__.__name__, self.stats.count(Stat.CONSTITUTION))

    #############################################################################
    def mod_stat_int(self, character: "BaseCharacter") -> Reason[int]:
        return Reason(self.__class__.__name__, self.stats.count(Stat.INTELLIGENCE))

    #############################################################################
    def mod_stat_wis(self, character: "BaseCharacter") -> Reason[int]:
        return Reason(self.__class__.__name__, self.stats.count(Stat.WISDOM))

    #############################################################################
    def mod_stat_cha(self, character: "BaseCharacter") -> Reason[int]:
        return Reason(self.__class__.__name__, self.stats.count(Stat.CHARISMA))


# EOF
