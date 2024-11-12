from typing import Optional

from charsheets.char_class import BaseCharClass
from charsheets.constants import Stat, Proficiencies, Ability, CharSubclassName, CharClassName
from charsheets.exception import UnhandledException
from charsheets.spells import Spells


#################################################################################
class CharClassRanger(BaseCharClass):
    tag = CharClassName.RANGER

    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 8

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.WISDOM

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
        if stat in (Stat.STRENGTH, Stat.DEXTERITY):
            return True

        return False

    #############################################################################
    def class_abilities(self, level: int) -> set[Ability]:
        abilities = set()

        abilities.add(Ability.FAVOURED_ENEMY)
        abilities.add(Ability.WEAPON_MASTERY)
        if level >= 2:
            abilities.add(Ability.DEFT_EXPLORER)
            abilities.add(Ability.FIGHTING_STYLE)
        if level >= 3:
            match self.sub_class_name:
                case CharSubclassName.HUNTER:
                    abilities.add(Ability.HUNTERS_LORE)
                    abilities.add(Ability.HUNTERS_PREY)
                case _:
                    raise UnhandledException(f"{self.sub_class_name} doesn't have ranger_class_ability() defined")

        return abilities

    #############################################################################
    def spell_slots(self, level: int) -> list[int]:
        return {
            1: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            4: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            5: [4, 2, 0, 0, 0, 0, 0, 0, 0],
        }[level]

    #############################################################################
    def spells(self, spell_level: int) -> list[Spells]:
        ranger_spells = {
            0: [],
            1: [
                Spells.ALARM,
                Spells.ANIMAL_FRIENDSHIP,
                Spells.CURE_WOUNDS,
                Spells.DETECT_MAGIC,
                Spells.DETECT_POISON_AND_DISEASE,
                Spells.ENSNARING_STRIKE,
                Spells.ENTANGLE,
                Spells.FOG_CLOUD,
                Spells.GOODBERRY,
                Spells.HAIL_OF_THORNS,
                Spells.HUNTERS_MARK,
                Spells.JUMP,
                Spells.LONGSTRIDER,
                Spells.SPEAK_WITH_ANIMALS,
            ],
            2: [
                Spells.AID,
                Spells.ANIMAL_MESSENGER,
                Spells.BARKSKIN,
                Spells.BEAST_SENSE,
                Spells.CORDON_OF_ARROWS,
                Spells.DARKVISION,
                Spells.ENHANCE_ABILITY,
                Spells.FIND_TRAPS,
                Spells.GUST_OF_WIND,
                Spells.LESSER_RESTORATION,
                Spells.LOCATE_ANIMALS_OR_PLANTS,
                Spells.MAGIC_WEAPON,
                Spells.PASS_WITHOUT_TRACE,
                Spells.PROTECTION_FROM_POISON,
                Spells.SILENCE,
                Spells.SPIKE_GROWTH,
                Spells.SUMMON_BEAST,
            ],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
        }

        return ranger_spells[spell_level]

    #############################################################################
    def max_spell_level(self, char_level: int) -> int:
        if char_level >= 17:
            return 5
        if char_level >= 13:
            return 4
        if char_level >= 9:
            return 3
        if char_level >= 5:
            return 2
        return 1


# EOF
