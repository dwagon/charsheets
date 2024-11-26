from typing import Optional

from charsheets.character import Character
from charsheets.constants import Stat, Proficiencies, Ability, CharSubclassName
from charsheets.exception import UnhandledException
from charsheets.spells import Spells, SPELL_LEVELS


#################################################################################
class Cleric(Character):
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
        if stat in (Stat.WISDOM, Stat.CHARISMA):
            return True

        return False

    #############################################################################
    def class_abilities(self, level: int) -> set[Ability]:
        abilities = set()

        abilities.add(Ability.DIVINE_ORDER)
        if level >= 2:
            abilities.add(Ability.CHANNEL_DIVINITY)

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
    def spells(self, spell_level: int) -> list[Spells]:
        cleric_spells = {
            0: [
                # Cantrips are learnt
            ],
            1: [
                Spells.BANE,
                Spells.BLESS,
                Spells.COMMAND,
                Spells.CREATE_OR_DESTROY_WATER,
                Spells.CURE_WOUNDS,
                Spells.DETECT_EVIL_AND_GOOD,
                Spells.DETECT_MAGIC,
                Spells.DETECT_POISON_AND_DISEASE,
                Spells.GUIDING_BOLT,
                Spells.HEALING_WORD,
                Spells.INFLICT_WOUNDS,
                Spells.PROTECTION_FROM_EVIL_AND_GOOD,
                Spells.PURIFY_FOOD_AND_DRINK,
                Spells.SANCTUARY,
                Spells.SHIELD_OF_FAITH,
            ],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
        }

        result = cleric_spells[spell_level]
        for spell in self.known_spells:
            if SPELL_LEVELS[spell] == spell_level:
                result.append(spell)
        return result

    #############################################################################
    def max_spell_level(self, char_level: int) -> int:
        return min(9, (self.level // 2) + 1)


# EOF
