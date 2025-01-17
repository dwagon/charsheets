from typing import Optional, Any

from charsheets.abilities import WeaponMastery, ActionSurge, SecondWind, TacticalMind, TacticalShift, ExtraAttack
from charsheets.abilities.base_ability import BaseAbility
from charsheets.character import Character
from charsheets.constants import Stat, Proficiency, Skill
from charsheets.exception import InvalidOption
from charsheets.reason import Reason


#################################################################################
class Fighter(Character):
    _base_skill_proficiencies = {
        Skill.ACROBATICS,
        Skill.ANIMAL_HANDLING,
        Skill.ATHLETICS,
        Skill.HISTORY,
        Skill.INSIGHT,
        Skill.INTIMIDATION,
        Skill.PERSUASION,
        Skill.PERCEPTION,
        Skill.SURVIVAL,
    }

    #############################################################################
    @property
    def hit_dice(self) -> int:
        return 10

    #############################################################################
    def fighting_style(self, style: BaseAbility):
        self.add_ability(style)

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return None

    #############################################################################
    def weapon_proficiency(self) -> Reason[Proficiency]:
        return Reason("Fighter", Proficiency.SIMPLE_WEAPONS, Proficiency.MARTIAL_WEAPONS)

    #############################################################################
    def armour_proficiency(self) -> Reason[Proficiency]:
        return Reason("Fighter", Proficiency.LIGHT_ARMOUR, Proficiency.MEDIUM_ARMOUR, Proficiency.HEAVY_ARMOUR, Proficiency.SHIELDS)

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        return stat in (Stat.STRENGTH, Stat.CONSTITUTION)

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {WeaponMastery(), ActionSurge(), SecondWind()}

        if self.level >= 2:
            abilities.add(TacticalMind())
        if self.level >= 5:
            abilities.add(ExtraAttack())
            abilities.add(TacticalShift())
        return abilities

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return 0

    #############################################################################
    def max_spell_level(self) -> int:
        return 0

    #############################################################################
    def level6(self, **kwargs: Any):
        self.level = 6
        if "feat" not in kwargs:
            raise InvalidOption("Level 6 fighter should specify a feat")
        self._add_level(self.level, **kwargs)


# EOF
