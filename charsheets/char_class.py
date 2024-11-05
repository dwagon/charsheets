""" Class based Stuff"""

import sys
from typing import Optional

from charsheets.constants import CharClassName, Stat, Proficiencies, Ability, CharSubclassName
from charsheets.spells import Spells
from charsheets.exception import UnhandledException


#############################################################################
class CharClass:
    def __init__(self, name: CharClassName, sub_class: CharSubclassName):
        self.class_name = name
        self.sub_class_name = sub_class

    #########################################################################
    @property
    def hit_dice(self) -> int:
        match self.class_name:
            case CharClassName.BARBARIAN:
                return 12
            case CharClassName.DRUID:
                return 8
            case CharClassName.RANGER:
                return 8

        raise UnhandledException(f"{self.class_name} doesn't have hit dice defined")

    #############################################################################
    def spell_slots(self, level: int) -> list[int]:
        ranger_slots = {
            1: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            4: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            5: [4, 2, 0, 0, 0, 0, 0, 0, 0],
        }
        druid_slots = {
            1: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [4, 2, 0, 0, 0, 0, 0, 0, 0],
            4: [4, 3, 0, 0, 0, 0, 0, 0, 0],
            5: [4, 3, 2, 0, 0, 0, 0, 0, 0],
        }
        match self.class_name:
            case CharClassName.BARBARIAN:
                return [0, 0, 0, 0, 0, 0, 0, 0, 0]
            case CharClassName.DRUID:
                return druid_slots[level]
            case CharClassName.RANGER:
                return ranger_slots[level]

        raise UnhandledException(f"{self.class_name} doesn't have spell_slots() defined")

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
        match self.class_name:
            case CharClassName.RANGER:
                return ranger_spells[level]
            case CharClassName.BARBARIAN:
                return []
            case _:
                raise UnhandledException(f"{self.class_name} doesn't have spells() defined")

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        match self.class_name:
            case CharClassName.BARBARIAN:
                return None
            case CharClassName.DRUID:
                return Stat.WISDOM
            case CharClassName.RANGER:
                return Stat.WISDOM
        raise UnhandledException(f"{self.class_name} doesn't have spell_casting_ability() defined")

    #############################################################################
    def name(self):
        if self.sub_class_name == CharSubclassName.NONE:
            return f"{self.class_name.title()}"
        return f"{self.class_name.title()} ({self.sub_class_name.title()})"

    #############################################################################
    def weapon_proficiency(self) -> set[Proficiencies]:
        """Weapon proficiency"""
        match self.class_name:
            case CharClassName.BARBARIAN:
                return {
                    Proficiencies.SIMPLE_WEAPONS,
                    Proficiencies.MARTIAL_WEAPONS,
                }
            case CharClassName.DRUID:
                return {Proficiencies.SIMPLE_WEAPONS}
            case CharClassName.RANGER:
                return {
                    Proficiencies.SIMPLE_WEAPONS,
                    Proficiencies.MARTIAL_WEAPONS,
                }

        raise UnhandledException(f"{self.class_name} doesn't have weapon_proficiency() defined")

    #############################################################################
    def armour_proficiency(self) -> set[Proficiencies]:
        """Armour proficiency"""
        match self.class_name:
            case CharClassName.BARBARIAN:
                return {
                    Proficiencies.SHIELDS,
                    Proficiencies.LIGHT_ARMOUR,
                    Proficiencies.MEDIUM_ARMOUR,
                }
            case CharClassName.DRUID:
                return {
                    Proficiencies.SHIELDS,
                    Proficiencies.LIGHT_ARMOUR,
                }
            case CharClassName.RANGER:
                return {
                    Proficiencies.SHIELDS,
                    Proficiencies.LIGHT_ARMOUR,
                    Proficiencies.MEDIUM_ARMOUR,
                }

        raise UnhandledException(f"{self.class_name} doesn't have armour_proficiency() defined")

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        match self.class_name:

            case CharClassName.BARBARIAN:
                if stat in (Stat.STRENGTH, Stat.CONSTITUTION):
                    return True
            case CharClassName.DRUID:
                if stat in (Stat.INTELLIGENCE, Stat.WISDOM):
                    return True
            case CharClassName.RANGER:
                if stat in (Stat.STRENGTH, Stat.DEXTERITY):
                    return True
            case _:
                raise UnhandledException(f"{self.class_name} doesn't have saving_throw_proficiency() defined")

        return False

    #############################################################################
    def ranger_class_abilities(self, level: int) -> set[Ability]:
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
    def druid_abilities(self, level: int) -> set[Ability]:
        abilities = set()
        abilities.add(Ability.DRUIDIC)
        abilities.add(Ability.PRIMAL_ORDER)
        if level >= 2:
            abilities.add(Ability.WILD_SHAPE)
            abilities.add(Ability.WILD_COMPANION)
        return abilities

    #############################################################################
    def class_abilities(self, level: int) -> set[Ability]:
        abilities = set()
        match self.class_name:
            case CharClassName.RANGER:
                abilities = self.ranger_class_abilities(level)
            case CharClassName.BARBARIAN:
                abilities.add(Ability.UNARMORED_DEFENSE)
                abilities.add(Ability.WEAPON_MASTERY)
                abilities.add(Ability.RAGE)
                if level >= 2:
                    abilities.add(Ability.DANGER_SENSE)
                    abilities.add(Ability.RECKLESS_ATTACK)
            case CharClassName.DRUID:
                abilities = self.druid_abilities(level)
            case _:
                raise UnhandledException(f"{self.class_name} doesn't have class_abilities() defined")
        return abilities
