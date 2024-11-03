""" Class based Stuff"""

from charsheets.constants import CharClassName, Stat, Proficiencies
from charsheets.spells import Spells


#############################################################################
class CharClass:
    def __init__(self, name: CharClassName):
        self.class_name = name

    #########################################################################
    @property
    def hit_dice(self) -> int:
        match self.class_name:
            case CharClassName.RANGER:
                return 8
        return 0

    #############################################################################
    def spell_slots(self, level: int) -> list[int]:
        ranger_slots = {
            1: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            4: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            5: [4, 2, 0, 0, 0, 0, 0, 0, 0],
        }
        match self.class_name:
            case CharClassName.RANGER:
                return ranger_slots[level]

        return [0, 0, 0, 0, 0, 0, 0, 0, 0]

    #############################################################################
    def spells(self, level: int):
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
        }
        match self.class_name:
            case CharClassName.RANGER:
                return ranger_spells[level]

    #############################################################################
    @property
    def spell_casting_ability(self) -> Stat:
        match self.class_name:
            case CharClassName.RANGER:
                return Stat.WISDOM

    #############################################################################
    def __str__(self):
        return self.class_name.title()

    #############################################################################
    def weapon_proficiency(self) -> set[Proficiencies]:
        """Weapon proficiency"""
        match self.class_name:
            case CharClassName.RANGER:
                return {
                    Proficiencies.SIMPLE_WEAPONS,
                    Proficiencies.MARTIAL_WEAPONS,
                }
        return set()

    #############################################################################
    def armour_proficiency(self) -> set[Proficiencies]:
        """Armour proficiency"""
        match self.class_name:
            case CharClassName.RANGER:
                return {
                    Proficiencies.SHIELDS,
                    Proficiencies.LIGHT_ARMOUR,
                    Proficiencies.MEDIUM_ARMOUR,
                }
        return set()

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        match self.class_name:
            case CharClassName.RANGER:
                if stat in (Stat.STRENGTH, Stat.DEXTERITY):
                    return True
        return False
