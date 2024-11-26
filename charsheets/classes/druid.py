from typing import Optional

from charsheets.character import Character
from charsheets.constants import Stat, Proficiencies, Ability
from charsheets.spells import Spells


#################################################################################
class Druid(Character):

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
    def max_spell_level(self, char_level: int) -> int:
        return (1 + char_level) // 2

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
        return druid_spells[spell_level]
