from typing import Optional

from charsheets.abilities import (
    UnarmoredDefenseBarbarian,
    WeaponMastery,
    Rage,
    DangerSense,
    RecklessAttack,
    ExtraAttack,
    FastMovement,
)
from charsheets.abilities.base_ability import BaseAbility
from charsheets.character import Character
from charsheets.constants import Stat, Proficiency, Skill, Ability
from charsheets.reason import Reason


#################################################################################
class Barbarian(Character):
    _base_skill_proficiencies = {
        Skill.ANIMAL_HANDLING,
        Skill.ATHLETICS,
        Skill.INTIMIDATION,
        Skill.NATURE,
        Skill.PERCEPTION,
        Skill.SURVIVAL,
    }

    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 12

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return None

    #############################################################################
    def weapon_proficiency(self) -> Reason[Proficiency]:
        return Reason(
            "Barbarian",
            Proficiency.SIMPLE_WEAPONS,
            Proficiency.MARTIAL_WEAPONS,
        )

    #############################################################################
    def armour_proficiency(self) -> Reason[Proficiency]:
        return Reason(
            "Barbarian",
            Proficiency.SHIELDS,
            Proficiency.LIGHT_ARMOUR,
            Proficiency.MEDIUM_ARMOUR,
        )

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        return stat in (Stat.STRENGTH, Stat.CONSTITUTION)

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {UnarmoredDefenseBarbarian()}
        abilities.add(WeaponMastery())
        abilities.add(Rage())
        if self.level >= 2:
            abilities.add(DangerSense())
            abilities.add(RecklessAttack())
        if self.level >= 3:
            # Primal knowledge done in level up
            pass
        if self.level >= 5:
            abilities.add(ExtraAttack())
            abilities.add(FastMovement())
        return abilities

    #############################################################################
    def spell_slots(self, level: int) -> int:
        return 0

    #############################################################################
    def max_spell_level(self) -> int:
        return 0


# EOF
