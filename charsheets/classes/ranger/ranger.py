from typing import Optional, Any, cast

from aenum import extend_enum

from charsheets.character import Character
from charsheets.constants import Stat, Proficiency, Skill, Feature, Recovery, Language
from charsheets.exception import InvalidOption
from charsheets.features import WeaponMastery, ExtraAttack
from charsheets.features.base_feature import BaseFeature
from charsheets.origins.base_origin import BaseOrigin
from charsheets.reason import Reason
from charsheets.species.base_species import BaseSpecies
from charsheets.spell import Spell, spell_name

extend_enum(Feature, "DEFT_EXPLORER", "Deft Explorer")
extend_enum(Feature, "DRUIDIC_WARRIOR", "Druidic Warrior")
extend_enum(Feature, "FAVOURED_ENEMY", "Favoured Enemy")
extend_enum(Feature, "ROVING", "Roving")
extend_enum(Feature, "TIRELESS", "Tireless")


#################################################################################
class Ranger(Character):
    _base_skill_proficiencies = {
        Skill.ANIMAL_HANDLING,
        Skill.ATHLETICS,
        Skill.INSIGHT,
        Skill.INVESTIGATION,
        Skill.NATURE,
        Skill.PERCEPTION,
        Skill.STEALTH,
        Skill.SURVIVAL,
    }

    #############################################################################
    def __init__(
        self,
        name: str,
        origin: BaseOrigin,
        species: BaseSpecies,
        skill1: Skill,
        skill2: Skill,
        skill3: Skill,
        **kwargs: Any,
    ):
        super().__init__(name, origin, species, skill1, skill2, skill3, **kwargs)

    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 10

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.WISDOM

    #############################################################################
    def weapon_proficiency(self) -> Reason[Proficiency]:
        return Reason("Ranger", cast(Proficiency, Proficiency.SIMPLE_WEAPONS), cast(Proficiency, Proficiency.MARTIAL_WEAPONS))

    #############################################################################
    def armour_proficiency(self) -> Reason[Proficiency]:
        return Reason(
            "Ranger",
            cast(Proficiency, Proficiency.SHIELDS),
            cast(Proficiency, Proficiency.LIGHT_ARMOUR),
            cast(Proficiency, Proficiency.MEDIUM_ARMOUR),
        )
        # type: ignore

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        return stat in (Stat.STRENGTH, Stat.DEXTERITY)

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {FavoredEnemy(), WeaponMastery()}
        if self.level >= 5:
            abilities.add(ExtraAttack())
        if self.level >= 5:
            abilities.add(Roving())
        if self.level >= 10:
            abilities.add(Tireless())
        return abilities

    #############################################################################
    def level2(self, **kwargs: Any):
        if "deft" not in kwargs:
            raise InvalidOption("Level 2 Rangers get DeftExplorer: level2(deft=DeftExplorer(...))")
        if "style" not in kwargs:
            raise InvalidOption("Level 2 Rangers get Fighting Style: level2(style=DruidicWarrior(...))")
        self.add_feature(kwargs["deft"])
        self.add_feature(kwargs["style"])
        super().level2(**kwargs)

    #############################################################################
    def level9(self, **kwargs: Any):
        if "expertise" not in kwargs:
            raise InvalidOption("Level 9 Rangers get Expertise: level9(expertise=Expertise(...))")
        self.add_feature(kwargs["expertise"])
        super().level9(**kwargs)

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return {
            1: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            4: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            5: [4, 2, 0, 0, 0, 0, 0, 0, 0],
            6: [4, 2, 0, 0, 0, 0, 0, 0, 0],
            7: [4, 3, 0, 0, 0, 0, 0, 0, 0],
            8: [4, 3, 0, 0, 0, 0, 0, 0, 0],
            9: [4, 3, 2, 0, 0, 0, 0, 0, 0],
            10: [4, 3, 2, 0, 0, 0, 0, 0, 0],
            11: [4, 3, 3, 0, 0, 0, 0, 0, 0],
            12: [4, 3, 3, 0, 0, 0, 0, 0, 0],
            13: [4, 3, 3, 1, 0, 0, 0, 0, 0],
            14: [4, 3, 3, 1, 0, 0, 0, 0, 0],
            15: [4, 3, 3, 2, 0, 0, 0, 0, 0],
            16: [4, 3, 3, 2, 0, 0, 0, 0, 0],
            17: [4, 3, 3, 3, 1, 0, 0, 0, 0],
            18: [4, 3, 3, 3, 1, 0, 0, 0, 0],
            19: [4, 3, 3, 3, 2, 0, 0, 0, 0],
            20: [4, 3, 3, 3, 2, 0, 0, 0, 0],
        }[self.level][spell_level - 1]

    #############################################################################
    def mod_add_known_spells(self, character: "Character") -> Reason[Spell]:
        ranger_spells = {
            0: [],
            1: [
                Spell.ALARM,
                Spell.ANIMAL_FRIENDSHIP,
                Spell.CURE_WOUNDS,
                Spell.DETECT_MAGIC,
                Spell.DETECT_POISON_AND_DISEASE,
                Spell.ENSNARING_STRIKE,
                Spell.ENTANGLE,
                Spell.FOG_CLOUD,
                Spell.GOODBERRY,
                Spell.HAIL_OF_THORNS,
                Spell.HUNTERS_MARK,
                Spell.JUMP,
                Spell.LONGSTRIDER,
                Spell.SPEAK_WITH_ANIMALS,
            ],
            2: [
                Spell.AID,
                Spell.ANIMAL_MESSENGER,
                Spell.BARKSKIN,
                Spell.BEAST_SENSE,
                Spell.CORDON_OF_ARROWS,
                Spell.DARKVISION,
                Spell.ENHANCE_ABILITY,
                Spell.FIND_TRAPS,
                Spell.GUST_OF_WIND,
                Spell.LESSER_RESTORATION,
                Spell.LOCATE_ANIMALS_OR_PLANTS,
                Spell.MAGIC_WEAPON,
                Spell.PASS_WITHOUT_TRACE,
                Spell.PROTECTION_FROM_POISON,
                Spell.SILENCE,
                Spell.SPIKE_GROWTH,
                Spell.SUMMON_BEAST,
            ],
            3: [
                Spell.CONJURE_ANIMALS,
                Spell.CONJURE_BARRAGE,
                Spell.DAYLIGHT,
                Spell.DISPEL_MAGIC,
                Spell.ELEMENTAL_WEAPON,
                Spell.LIGHTNING_ARROW,
                Spell.MELD_INTO_STONE,
                Spell.NONDETECTION,
                Spell.PLANT_GROWTH,
                Spell.PROTECTION_FROM_ENERGY,
                Spell.REVIVIFY,
                Spell.SPEAK_WITH_PLANTS,
                Spell.SUMMON_FEY,
                Spell.WATER_BREATHING,
                Spell.WATER_WALK,
                Spell.WIND_WALL,
            ],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
        }

        known_spells: Reason[Spell] = Reason()
        for spells in ranger_spells.values():
            for spell in spells:
                known_spells |= Reason("Ranger Spell", spell)
        return known_spells

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


#############################################################################
class FavoredEnemy(BaseFeature):
    tag = Feature.FAVOURED_ENEMY
    goes = 2
    recovery = Recovery.LONG_REST
    _desc = """You always have the Hunter's Mark spell prepared. You can cast it twice without expending a spell slot.
    """

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Favoured Enemy", Spell.HUNTERS_MARK)


#############################################################################
class DruidicWarrior(BaseFeature):
    tag = Feature.DRUIDIC_WARRIOR

    def __init__(self, cantrip1: Spell, cantrip2: Spell):
        super().__init__()
        self.spells = [cantrip1, cantrip2]

    def mod_add_known_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Druidic Warrior", *self.spells)

    @property
    def desc(self) -> str:
        return f"""Druidic Warrior. You learn '{spell_name(self.spells[0])}' and '{spell_name(self.spells[1])}'.
        They count as Ranger spells for you, and Wisdom is your spellcasting ability for them."""


#############################################################################
class DeftExplorer(BaseFeature):
    tag = Feature.DEFT_EXPLORER
    hide = True
    _desc = """Expertise. Choose one of your skill proficiencies with which you lack Expertise. 
    You gain Expertise in that skill.

    Languages. You know two languages of your choice"""

    def __init__(self, language1: Language, language2: Language, skill: Skill):
        super().__init__()
        self.languages = [language1, language2]
        self.skill = skill

    def mod_add_language(self, character: "Character") -> Reason[Language]:
        return Reason("Deft Explorer", *self.languages)

    def mod_add_skill_expertise(self, character: "Character") -> Reason[Skill]:
        return Reason("Deft Explorer", self.skill)


#############################################################################
class Roving(BaseFeature):
    tag = Feature.ROVING
    _desc = """You have a Climb Speed and Swim Speed equal to your Speed."""

    def mod_add_movement_speed(self, character: "Character") -> Reason[int]:
        return Reason() if character.armour.is_heavy() else Reason("Roving", 10)


#############################################################################
class Tireless(BaseFeature):
    tag = Feature.TIRELESS
    recovery = Recovery.LONG_REST

    @property
    def goes(self) -> int:
        return max(1, self.owner.wisdom.modifier)

    @property
    def desc(self) -> str:
        return f"""Temporary Hit Points. As a Magic action, you can give yourself a number of Temporary Hit Points equal 
    to 1d8 + {max(1, self.owner.wisdom.modifier)}. 
    
    Decrease Exhaustion. 
    Whenever you finish a Short Rest, your Exhaustion level, if any, decreases by 1."""


# EOF
