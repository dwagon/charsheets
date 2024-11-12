from typing import Optional

from charsheets.char_class import BaseCharClass
from charsheets.constants import Stat, Proficiencies, Ability, CharSubclassName, CharClassName
from charsheets.exception import UnhandledException
from charsheets.spells import Spells, SPELL_LEVELS


#################################################################################
class CharClassWarlock(BaseCharClass):
    tag = CharClassName.WARLOCK

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
    def spell_slots(self, level: int) -> list[int]:
        return {
            1: [1, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [2, 2, 0, 0, 0, 0, 0, 0, 0],
            4: [2, 2, 0, 0, 0, 0, 0, 0, 0],
            5: [2, 2, 2, 0, 0, 0, 0, 0, 0],
        }[level]

    #############################################################################
    def max_spell_level(self, char_level: int) -> int:
        return min(5, (char_level + 1) // 2)

    #############################################################################
    def spells(self, spell_level: int) -> list[Spells]:
        result = []
        for spell in self.pcm.spells:
            if SPELL_LEVELS[spell] == spell_level:
                result.append(spell)
        return result


# EOF
