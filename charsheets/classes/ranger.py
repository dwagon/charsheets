from typing import Optional

from charsheets.character import Character
from charsheets.constants import Stat, Proficiency, Ability
from charsheets.exception import UnhandledException
from charsheets.spells import Spells


#################################################################################
class Ranger(Character):
    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 10

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.WISDOM

    #############################################################################
    def weapon_proficiency(self) -> set[Proficiency]:
        return {
            Proficiency.SIMPLE_WEAPONS,
            Proficiency.MARTIAL_WEAPONS,
        }

    #############################################################################
    def armour_proficiency(self) -> set[Proficiency]:
        return {
            Proficiency.SHIELDS,
            Proficiency.LIGHT_ARMOUR,
            Proficiency.MEDIUM_ARMOUR,
        }

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        if stat in (Stat.STRENGTH, Stat.DEXTERITY):
            return True

        return False

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities = {Ability.FAVOURED_ENEMY, Ability.WEAPON_MASTERY}
        if self.level >= 2:
            abilities.add(Ability.DEFT_EXPLORER)
            abilities.add(Ability.FIGHTING_STYLE)
        return abilities

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return {
            1: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            4: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            5: [4, 2, 0, 0, 0, 0, 0, 0, 0],
        }[self.level][spell_level - 1]

    #############################################################################
    def mod_add_known_spells(self, character: "Character") -> set[Spells]:
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

        known_spells: list[Spells] = []
        for spells in ranger_spells.values():
            known_spells.extend(spells)
        return set(known_spells)

    #############################################################################
    def max_spell_level(self) -> int:
        if self.level >= 17:
            return 5
        elif self.level >= 13:
            return 4
        elif self.level >= 9:
            return 3
        elif self.level >= 5:
            return 2
        return 1


# EOF
