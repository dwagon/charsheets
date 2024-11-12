from typing import Optional

from charsheets.char_class import BaseCharClass
from charsheets.constants import Stat, Proficiencies, Ability, CharClassName
from charsheets.spells import Spells


#################################################################################
class CharClassBarbarian(BaseCharClass):
    tag = CharClassName.BARBARIAN

    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 12

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return None

    #############################################################################
    def weapon_proficiency(self) -> set[Proficiencies]:
        return {
            Proficiencies.SIMPLE_WEAPONS,
            Proficiencies.MARTIAL_WEAPONS,
        }

    #############################################################################
    def armour_proficiency(self) -> set[Proficiencies]:
        return {
            Proficiencies.SHIELDS,
            Proficiencies.LIGHT_ARMOUR,
            Proficiencies.MEDIUM_ARMOUR,
        }

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        if stat in (Stat.STRENGTH, Stat.CONSTITUTION):
            return True
        return False

    #############################################################################
    def class_abilities(self, level: int) -> set[Ability]:
        abilities = set()
        abilities.add(Ability.UNARMORED_DEFENSE)
        abilities.add(Ability.WEAPON_MASTERY)
        abilities.add(Ability.RAGE)
        if level >= 2:
            abilities.add(Ability.DANGER_SENSE)
            abilities.add(Ability.RECKLESS_ATTACK)

        return abilities

    #############################################################################
    def spell_slots(self, level: int) -> list[int]:
        return [0, 0, 0, 0, 0, 0, 0, 0, 0]

    #############################################################################
    def spells(self, spell_level: int) -> list[Spells]:
        return []

    #############################################################################
    def max_spell_level(self, char_level: int) -> int:
        return 0


# EOF