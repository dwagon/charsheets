from typing import Optional

from charsheets.abilities import Druidic, WildShape, WildCompanion, WildResurgence
from charsheets.abilities.base_ability import BaseAbility
from charsheets.character import Character
from charsheets.constants import Stat, Proficiency, Skill
from charsheets.reason import Reason
from charsheets.spells import Spells


#################################################################################
class Druid(Character):
    _base_skill_proficiencies = {
        Skill.ARCANA,
        Skill.ANIMAL_HANDLING,
        Skill.INSIGHT,
        Skill.MEDICINE,
        Skill.NATURE,
        Skill.PERCEPTION,
        Skill.RELIGION,
        Skill.SURVIVAL,
    }

    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 8

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.WISDOM

    #############################################################################
    def weapon_proficiency(self) -> Reason[Proficiency]:
        return Reason("Druid", Proficiency.SIMPLE_WEAPONS)

    #############################################################################
    def armour_proficiency(self) -> Reason[Proficiency]:
        return Reason("Druid", Proficiency.SHIELDS, Proficiency.LIGHT_ARMOUR)

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        return stat in (Stat.INTELLIGENCE, Stat.WISDOM)

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {Druidic()}
        if self.level >= 2:
            abilities.add(WildShape())
            abilities.add(WildCompanion())
        if self.level >= 5:
            abilities.add(WildResurgence())
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
            6: [4, 3, 3, 0, 0, 0, 0, 0, 0],
        }[self.level][spell_level - 1]

    #############################################################################
    def mod_add_known_spells(self, character: "Character") -> Reason[Spells]:
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
            3: [
                Spells.AURA_OF_VITALITY,
                Spells.CALL_LIGHTNING,
                Spells.CONJURE_ANIMALS,
                Spells.DAYLIGHT,
                Spells.DISPEL_MAGIC,
                Spells.ELEMENTAL_WEAPON,
                Spells.FEIGN_DEATH,
                Spells.MELD_INTO_STONE,
                Spells.PLANT_GROWTH,
                Spells.PROTECTION_FROM_ENERGY,
                Spells.REVIVIFY,
                Spells.SLEET_STORM,
                Spells.SPEAK_WITH_PLANTS,
                Spells.SUMMON_FEY,
                Spells.WATER_BREATHING,
                Spells.WATER_WALK,
                Spells.WIND_WALL,
            ],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
        }

        known_spells: Reason[Spells] = Reason()
        for spells in druid_spells.values():
            for spell in spells:
                known_spells |= Reason("Ranger Spell", spell)
        return known_spells


# EOF
