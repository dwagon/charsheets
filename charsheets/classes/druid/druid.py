from typing import Optional

from charsheets.abilities.base_ability import BaseAbility
from charsheets.character import Character
from charsheets.constants import Stat, Proficiency, Skill, Ability, Language
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


#############################################################################
class Druidic(BaseAbility):
    tag = Ability.DRUIDIC
    _desc = """You know Druidic, the secret language of Druids."""
    hide = True

    def mod_add_language(self, character: "Character") -> Reason[Language]:
        return Reason("Druidic", Language.DRUIDIC)


#############################################################################
class WildShape(BaseAbility):
    tag = Ability.WILD_SHAPE
    _desc = """The power of nature allows you to assume the form of an animal.
    As a Bonus Action, you shape-shift into a Beast form that you have learned for this feature."""


#############################################################################
class WildCompanion(BaseAbility):
    tag = Ability.WILD_COMPANION
    _desc = """You can summon a nature spirit that assumes an animal form to aid you. As a Magic action,
    you can expend a spell slot or a use of Wild Shape to cast the Find Familiar spell without Material components.
    When you cast the spell in this way, the familiar is Fey and disappears when you finish a long rest."""


#################################################################################
class Magician(BaseAbility):
    tag = Ability.MAGICIAN
    _desc = """You know one extra cantrip from the Druid spell list. In addition, your mystical connection to nature gives
    you a bonus to your Intelligence (Arcana or Nature) checks.
    The bonus equals your Wisdom modifier (minimum bonus of +1)"""

    def mod_skill_arcana(self, character: "Character") -> Reason:
        return Reason("Magician", max(1, character.wisdom.modifier))

    def mod_skill_nature(self, character: "Character") -> Reason:
        return Reason("Magician", max(1, character.wisdom.modifier))


#################################################################################
class Warden(BaseAbility):
    tag = Ability.WARDEN
    _desc = """Trained for battle, you gain proficiency with Martial weapons and training with Medium armour"""
    hide = True

    #############################################################################
    def mod_weapon_proficiency(self, character: "Character") -> Reason[Proficiency]:
        return Reason("Warden", Proficiency.MARTIAL_WEAPONS)

    #############################################################################
    def mod_armour_proficiency(self, character: "Character") -> Reason[Proficiency]:
        return Reason("Warden", Proficiency.MEDIUM_ARMOUR)


#############################################################################
class WildResurgence(BaseAbility):
    tag = Ability.WILD_RESURGENCE
    goes = 1
    _desc = """Once on each of your turns, if you have no uses of Wild Shape left, you can give yourself one use by
    expending a spell slot (no action required). In addition,you can expend one use of Wild Shape (no action
    required) to give yourself a level 1 spell slot, but you can’t do so again until you finish a Long Rest."""


# EOF
