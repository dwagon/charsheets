from typing import Optional

from charsheets.abilities import RitualAdept, ArcaneRecovery, Scholar, MemorizeSpell
from charsheets.abilities.base_ability import BaseAbility
from charsheets.character import Character
from charsheets.constants import Stat, Proficiency, Skill
from charsheets.reason import Reason


#################################################################################
class Wizard(Character):
    _base_skill_proficiencies = {
        Skill.ARCANA,
        Skill.HISTORY,
        Skill.INSIGHT,
        Skill.INVESTIGATION,
        Skill.MEDICINE,
        Skill.NATURE,
        Skill.RELIGION,
    }

    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 6

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.INTELLIGENCE

    #############################################################################
    def weapon_proficiency(self) -> Reason[Proficiency]:
        return Reason("Class Proficiency", Proficiency.SIMPLE_WEAPONS)

    #############################################################################
    def armour_proficiency(self) -> Reason[Proficiency]:
        return Reason()

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        return stat in (Stat.INTELLIGENCE, Stat.WISDOM)

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {RitualAdept()}
        abilities.add(ArcaneRecovery())

        if self.level >= 2:
            abilities.add(Scholar())
        if self.level >= 5:
            abilities.add(MemorizeSpell())

        return abilities

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return {
            1: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [4, 2, 0, 0, 0, 0, 0, 0, 0],
            4: [4, 3, 0, 0, 0, 0, 0, 0, 0],
            5: [4, 3, 2, 0, 0, 0, 0, 0, 0],
        }[self.level][spell_level - 1]

    #############################################################################
    def max_spell_level(self) -> int:
        return min(9, ((self.level + 1) // 2))


# EOF
