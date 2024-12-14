from typing import Optional

from charsheets.character import Character
from charsheets.constants import Stat, Proficiencies, Ability
from charsheets.reason import Reason
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
    def class_abilities(self) -> set[Ability]:
        abilities = set()

        if self.level >= 2:
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
            2: [
                Spells.AID,
                Spells.AUGURY,
                Spells.BLINDNESS_DEAFNESS,
                Spells.CALM_EMOTIONS,
                Spells.CONTINUAL_FLAME,
                Spells.ENHANCE_ABILITY,
                Spells.FIND_TRAPS,
                Spells.GENTLE_REPOSE,
                Spells.HOLD_PERSON,
                Spells.LESSER_RESTORATION,
                Spells.LOCATE_OBJECT,
                Spells.PRAYER_OF_HEALING,
                Spells.PROTECTION_FROM_POISON,
                Spells.SILENCE,
                Spells.SPIRITUAL_WEAPON,
                Spells.WARDING_BOND,
                Spells.ZONE_OF_TRUTH,
            ],
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
    def max_spell_level(self) -> int:
        return min(9, (self.level // 2) + 1)


#################################################################################
class DivineProtector(Cleric):
    """Protector. Trained for battle, you gain proficiency with Martial weapons and training with Heavy armor."""

    #############################################################################
    def weapon_proficiency(self) -> set[Proficiencies]:
        return {Proficiencies.SIMPLE_WEAPONS, Proficiencies.MARTIAL_WEAPONS}

    #############################################################################
    def armour_proficiency(self) -> set[Proficiencies]:
        return {Proficiencies.SHIELDS, Proficiencies.LIGHT_ARMOUR, Proficiencies.MEDIUM_ARMOUR, Proficiencies.HEAVY_ARMOUR}


#################################################################################
class Thaumaturge(Cleric):
    """Thaumaturge. You know one extra cantrip from the Cleric spell list. In addition, your mystical connection to the
    divine gives you a bonus to your Intelligence (Arcana or Religion) checks.
    The bonus equals your Wisdom modifier (minimum of +1).
    """

    # Users will have to add their own cantrip to the learnt spells.

    def mod_skill_arcana(self, character: "Character") -> Reason:
        modifier = Reason("thaumaturge", min(1, character.wisdom.modifier))
        return modifier

    def mod_skill_religion(self, character: "Character") -> Reason:
        modifier = Reason("thaumaturge", min(1, character.wisdom.modifier))
        return modifier


# EOF
