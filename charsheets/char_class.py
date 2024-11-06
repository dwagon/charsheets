""" Class based Stuff"""

import sys
from typing import Optional, Type

from charsheets.constants import CharClassName, Stat, Proficiencies, Ability, CharSubclassName
from charsheets.spells import Spells
from charsheets.exception import UnhandledException


#############################################################################
class CharClass:
    def __init__(self, class_name: CharClassName, sub_class: CharSubclassName):
        self.class_name = class_name
        self.sub_class_name = sub_class

    #########################################################################
    @property
    def hit_dice(self) -> int:
        raise NotImplemented

    #############################################################################
    def spell_slots(self, level: int) -> list[int]:
        raise NotImplemented

    #############################################################################
    def spells(self, level: int) -> list[Spells]:
        raise NotImplemented

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        raise NotImplemented

    #############################################################################
    def name(self):
        if self.sub_class_name == CharSubclassName.NONE:
            return f"{self.class_name.title()}"
        return f"{self.class_name.title()} ({self.sub_class_name.title()})"

    #############################################################################
    def weapon_proficiency(self) -> set[Proficiencies]:
        raise NotImplemented

    #############################################################################
    def armour_proficiency(self) -> set[Proficiencies]:
        raise NotImplemented

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        raise NotImplemented

    #############################################################################
    def class_abilities(self, level: int) -> set[Ability]:
        raise NotImplemented


#################################################################################
class BarbarianClass(CharClass):
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

    def spells(self, level: int) -> list[Spells]:
        return []


#################################################################################
class DruidClass(CharClass):
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
        return {Proficiencies.SIMPLE_WEAPONS}

    #############################################################################
    def armour_proficiency(self) -> set[Proficiencies]:
        return {
            Proficiencies.SHIELDS,
            Proficiencies.LIGHT_ARMOUR,
        }

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        if stat in (Stat.INTELLIGENCE, Stat.WISDOM):
            return True

        return False

    #############################################################################
    def class_abilities(self, level: int) -> set[Ability]:
        abilities = set()
        abilities.add(Ability.DRUIDIC)
        abilities.add(Ability.PRIMAL_ORDER)
        if level >= 2:
            abilities.add(Ability.WILD_SHAPE)
            abilities.add(Ability.WILD_COMPANION)
        return abilities

    #############################################################################
    def spell_slots(self, level: int) -> list[int]:
        return {
            1: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [4, 2, 0, 0, 0, 0, 0, 0, 0],
            4: [4, 3, 0, 0, 0, 0, 0, 0, 0],
            5: [4, 3, 2, 0, 0, 0, 0, 0, 0],
        }[level]

    #############################################################################
    def spells(self, level: int) -> list[Spells]:
        druid_spells: dict[int, list[Spells]] = {
            0: [
                Spells.DRUIDCRAFT,
                Spells.ELEMENTALISM,
                Spells.GUIDANCE,
                Spells.MENDING,
                Spells.MESSAGE,
                Spells.POISON_SPRAY,
                Spells.PRODUCE_FLAME,
                Spells.RESISTANCE,
                Spells.SHILLELAGH,
                Spells.SPARE_THE_DYING,
                Spells.STARRY_WISP,
                Spells.THORN_WHIP,
                Spells.THUNDERCLAP,
            ],
            1: [
                Spells.ANIMAL_FRIENDSHIP,
                Spells.CHARM_PERSON,
                Spells.CREATE_OR_DESTROY_WATER,
                Spells.CURE_WOUNDS,
                Spells.DETECT_MAGIC,
                Spells.DETECT_POISON_AND_DISEASE,
                Spells.ENTANGLE,
                Spells.FAIRIE_FIRE,
                Spells.FOG_CLOUD,
                Spells.GOODBERRY,
                Spells.HEALING_WORD,
                Spells.ICE_KNIFE,
                Spells.JUMP,
                Spells.LONGSTRIDER,
                Spells.PROTECTION_FROM_EVIL_AND_GOOD,
                Spells.PURIFY_FOOD_AND_DRINK,
                Spells.SPEAK_WITH_ANIMALS,
                Spells.THUNDERWAVE,
            ],
            2: [
                Spells.AID,
                Spells.ANIMAL_MESSENGER,
                Spells.AUGURY,
                Spells.BARKSKIN,
                Spells.BEAST_SENSE,
                Spells.CONTINUAL_FLAME,
                Spells.DARKVISION,
                Spells.ENHANCE_ABILITY,
                Spells.ENLARGE_REDUCE,
                Spells.FIND_TRAPS,
                Spells.FLAME_BLADE,
                Spells.FLAMING_SPHERE,
                Spells.GUST_OF_WIND,
                Spells.HEAT_METAL,
                Spells.HOLD_PERSON,
                Spells.LESSER_RESTORATION,
                Spells.LOCATE_ANIMALS_OR_PLANTS,
                Spells.LOCATE_OBJECT,
                Spells.MOONBEAM,
                Spells.PASS_WITHOUT_TRACE,
                Spells.PROTECTION_FROM_POISON,
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
        return druid_spells[level]


#################################################################################
class RangerClass(CharClass):
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
    def spells(self, level: int) -> list[Spells]:
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

        return ranger_spells[level]


#################################################################################
def char_class_picker(char_class: CharClassName, char_sub_class: CharSubclassName) -> CharClass:
    match char_class:
        case CharClassName.BARBARIAN:
            return BarbarianClass(char_class, char_sub_class)
        case CharClassName.DRUID:
            return DruidClass(char_class, char_sub_class)
        case CharClassName.RANGER:
            return RangerClass(char_class, char_sub_class)
    raise UnhandledException(f"char_class_picker({char_class=}) unhandled")
