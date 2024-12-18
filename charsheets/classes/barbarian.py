from typing import Optional

from charsheets.character import Character
from charsheets.constants import Stat, Proficiencies, Ability
from charsheets.spells import Spells


#################################################################################
class Barbarian(Character):

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
    def class_abilities(self) -> set[Ability]:
        abilities = set()
        abilities.add(Ability.UNARMORED_DEFENSE)
        abilities.add(Ability.WEAPON_MASTERY)
        abilities.add(Ability.RAGE)
        if self.level >= 2:
            abilities.add(Ability.DANGER_SENSE)
            abilities.add(Ability.RECKLESS_ATTACK)
        if self.level >= 3:
            abilities.add(Ability.PRIMAL_KNOWLEDGE)
        return abilities

    #############################################################################
    def spell_slots(self, level: int) -> int:
        return 0

    #############################################################################
    def max_spell_level(self) -> int:
        return 0


# EOF
