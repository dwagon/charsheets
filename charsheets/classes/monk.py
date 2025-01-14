from typing import Optional

from charsheets.abilities import (
    UnarmoredDefenseMonk,
    MonksFocus,
    UnarmoredMovement,
    UncannyMetabolism,
    DeflectAttacks,
    SlowFall,
    ExtraAttack,
    StunningStrike,
    MartialArts,
    EmpoweredStrikes,
)
from charsheets.abilities.base_ability import BaseAbility
from charsheets.character import Character
from charsheets.constants import Stat, Proficiency, Skill
from charsheets.reason import Reason


#################################################################################
class Monk(Character):
    _base_skill_proficiencies = {
        Skill.ACROBATICS,
        Skill.ATHLETICS,
        Skill.HISTORY,
        Skill.INSIGHT,
        Skill.RELIGION,
        Skill.STEALTH,
    }

    #############################################################################
    @property
    def hit_dice(self) -> int:
        return 8

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return None

    #############################################################################
    def weapon_proficiency(self) -> Reason[Proficiency]:
        return Reason("Monk", Proficiency.SIMPLE_WEAPONS, Proficiency.MARTIAL_WEAPONS)

    #############################################################################
    def armour_proficiency(self) -> Reason[Proficiency]:
        return Reason()

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        return stat in (Stat.STRENGTH, Stat.DEXTERITY)

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {UnarmoredDefenseMonk(), MartialArts()}

        if self.level >= 2:
            abilities.add(MonksFocus())
            abilities.add(UnarmoredMovement())
            abilities.add(UncannyMetabolism())
        if self.level >= 3:
            abilities.add(DeflectAttacks())
        if self.level >= 4:
            abilities.add(SlowFall())
        if self.level >= 5:
            abilities.add(ExtraAttack())
            abilities.add(StunningStrike())
        if self.level >= 6:
            abilities.add(EmpoweredStrikes())
        return abilities

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return 0

    #############################################################################
    def max_spell_level(self) -> int:
        return 0


# EOF
