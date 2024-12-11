from typing import Optional

from charsheets.character import Character
from charsheets.constants import Stat, Proficiencies, Ability, CharSubclassName
from charsheets.spells import Spells
from charsheets.reason import Reason


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
    def class_abilities(self) -> set[Ability]:
        abilities = set()
        abilities.add(Ability.DRUIDIC)
        if self.level >= 2:
            abilities.add(Ability.WILD_SHAPE)
            abilities.add(Ability.WILD_COMPANION)
        if self.level >= 3:
            match self.sub_class_name:
                case CharSubclassName.CIRCLE_OF_THE_LAND:
                    abilities |= self.circle_of_the_land()
                case CharSubclassName.CIRCLE_OF_THE_MOON:
                    abilities |= self.circle_of_the_moon()
                case CharSubclassName.CIRCLE_OF_THE_SEA:
                    abilities |= self.circle_of_the_sea()
                case CharSubclassName.CIRCLE_OF_THE_STARS:
                    abilities |= self.circle_of_the_stars()

        return abilities

    #############################################################################
    def circle_of_the_land(self) -> set[Ability]:
        abilities: set[Ability] = {
            Ability.LANDS_AID,
            Ability.LAND_SPELL_ARID,
            Ability.LAND_SPELL_TROPICAL,
            Ability.LAND_SPELL_POLAR,
            Ability.LAND_SPELL_TEMPERATE,
        }
        return abilities

    #############################################################################
    def circle_of_the_moon(self) -> set[Ability]:
        abilities: set[Ability] = {Ability.CIRCLE_FORMS}
        self.prepare_spells(Spells.CURE_WOUNDS, Spells.MOONBEAM, Spells.STARRY_WISP)
        return abilities

    #############################################################################
    def circle_of_the_sea(self) -> set[Ability]:
        abilities: set[Ability] = {Ability.WRATH_OF_THE_SEA}
        self.prepare_spells(Spells.FOG_CLOUD, Spells.GUST_OF_WIND, Spells.RAY_OF_FROST, Spells.SHATTER, Spells.THUNDERWAVE)
        return abilities

    #############################################################################
    def circle_of_the_stars(self) -> set[Ability]:
        abilities: set[Ability] = {Ability.STAR_MAP, Ability.STARRY_FORM}
        return abilities

    #############################################################################
    def max_spell_level(self) -> int:
        return (1 + self.level) // 2

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
                Spells.FAERIE_FIRE,
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


#################################################################################
class Magician(Druid):
    """You know one extra cantrip from the Druid spell list. In addition, your mystical connection to nature gives
    you a bonus to your Intelligence (Arcana or Nature) checks.
    The bonus equals your Wisdom modifier (minimum bonus of +1)"""

    def mod_skill_arcana(self, character: Character) -> Reason:
        return Reason("magician", min(1, character.wisdom.modifier))

    def mod_skill_nature(self, character: Character) -> Reason:
        return Reason("magician", min(1, character.wisdom.modifier))


#################################################################################
class Warden(Druid):
    """Trained for battle, you gain proficiency with Martial weapons and training with Medium armour"""

    #############################################################################
    def weapon_proficiency(self) -> set[Proficiencies]:
        return {Proficiencies.SIMPLE_WEAPONS, Proficiencies.MARTIAL_WEAPONS}

    #############################################################################
    def armour_proficiency(self) -> set[Proficiencies]:
        return {Proficiencies.SHIELDS, Proficiencies.LIGHT_ARMOUR, Proficiencies.MEDIUM_ARMOUR}
