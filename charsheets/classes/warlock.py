from typing import Optional

from charsheets.character import Character
from charsheets.constants import Stat, Proficiencies, Ability, CharSubclassName
from charsheets.exception import UnhandledException
from charsheets.spells import Spells, SPELL_LEVELS


#################################################################################
class Warlock(Character):
    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 8

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.CHARISMA

    #############################################################################
    def weapon_proficiency(self) -> set[Proficiencies]:
        return {
            Proficiencies.SIMPLE_WEAPONS,
        }

    #############################################################################
    def armour_proficiency(self) -> set[Proficiencies]:
        return {
            Proficiencies.LIGHT_ARMOUR,
        }

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        if stat in (Stat.WISDOM, Stat.CHARISMA):
            return True

        return False

    #############################################################################
    def class_abilities(self, level: int) -> set[Ability]:
        abilities = set()

        abilities.add(Ability.ELDRITCH_INVOCATIONS)
        abilities.add(Ability.PACT_MAGIC)
        if level >= 2:
            abilities.add(Ability.MAGICAL_CUNNING)
        if level >= 3:
            match self.sub_class_name:
                case CharSubclassName.GREAT_OLD_ONE_PATRON:
                    if level >= 3:
                        pass
                case _:
                    raise UnhandledException(f"{self.sub_class_name} doesn't have class_abilities() defined")

        return abilities

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return {
            1: [1, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [2, 2, 0, 0, 0, 0, 0, 0, 0],
            4: [2, 2, 0, 0, 0, 0, 0, 0, 0],
            5: [2, 2, 2, 0, 0, 0, 0, 0, 0],
        }[self.level][spell_level - 1]

    #############################################################################
    def max_spell_level(self, char_level: int) -> int:
        return min(5, (char_level + 1) // 2)

    #############################################################################
    def spells(self, spell_level: int) -> list[Spells]:
        result = []
        for spell in self.known_spells:
            if SPELL_LEVELS[spell] == spell_level:
                result.append(spell)
        return result


# EOF
