from typing import Optional, cast, TYPE_CHECKING, Any

from aenum import extend_enum
from charsheets.classes.base_class import BaseClass
from charsheets.constants import Stat, Proficiency, Skill, Feature, Recovery, CharacterClass, Language
from charsheets.exception import InvalidOption
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell, is_cantrip

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter

extend_enum(Feature, "ACOLYTE_OF_NATURE14", "Acolyte of Nature")
extend_enum(Feature, "BLESSINGS_OF_KNOWLEDGE14", "Blessings of Knowledge")
extend_enum(Feature, "BLESSING_OF_THE_TRICKSTER14", "Blessing of the Trickster")
extend_enum(Feature, "DISCIPLE_OF_LIFE14", "Disciple of Life")
extend_enum(Feature, "KNOWLEDGE_DOMAIN_SPELLS14", "Knowledge Domain Spells")
extend_enum(Feature, "LIFE_DOMAIN_SPELLS14", "Life Domain Spells")
extend_enum(Feature, "LIGHT_DOMAIN_SPELLS14", "Light Domain Spells")
extend_enum(Feature, "NATURE_DOMAIN_SPELLS14", "Nature Domain Spells")
extend_enum(Feature, "TEMPEST_DOMAIN_SPELLS14", "Tempest Domain Spells")
extend_enum(Feature, "TRICKERY_DOMAIN_SPELLS14", "Trickery Domain Spells")
extend_enum(Feature, "WARDING_FLARE14", "Warding Flare")
extend_enum(Feature, "WAR_DOMAIN_SPELLS14", "War Domain Spells")
extend_enum(Feature, "WAR_PRIEST14", "War Priest")
extend_enum(Feature, "WRATH_OF_THE_STORM14", "Wrath of the Storm")


#################################################################################
class Cleric(BaseClass):
    _base_skill_proficiencies = {Skill.HISTORY, Skill.INSIGHT, Skill.MEDICINE, Skill.PERSUASION, Skill.RELIGION}
    _base_class = CharacterClass.CLERIC
    _class_name = "Cleric"

    #############################################################################
    def level1init(self, **kwargs: Any):
        assert self.character is not None
        self.character.set_saving_throw_proficiency(Stat.WISDOM, Stat.CHARISMA)

    #############################################################################
    def level1multi(self, **kwargs: Any):  # pragma: no coverage
        pass

    #############################################################################
    def level1(self, **kwargs: Any):
        assert self.character is not None
        self.character.add_armor_proficiency(Reason("Cleric", cast(Proficiency, Proficiency.LIGHT_ARMOUR)))
        self.character.add_armor_proficiency(Reason("Cleric", cast(Proficiency, Proficiency.MEDIUM_ARMOUR)))
        self.character.add_armor_proficiency(Reason("Cleric", cast(Proficiency, Proficiency.SHIELDS)))

    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 8

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.WISDOM

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return {
            1: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [3, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [4, 2, 0, 0, 0, 0, 0, 0, 0],
            4: [4, 3, 0, 0, 0, 0, 0, 0, 0],
            5: [4, 3, 2, 0, 0, 0, 0, 0, 0],
            6: [4, 3, 3, 0, 0, 0, 0, 0, 0],
            7: [4, 3, 3, 1, 0, 0, 0, 0, 0],
            8: [4, 3, 3, 2, 0, 0, 0, 0, 0],
            9: [4, 3, 3, 3, 1, 0, 0, 0, 0],
            10: [4, 3, 3, 3, 2, 0, 0, 0, 0],
            11: [4, 3, 3, 3, 2, 1, 0, 0, 0],
            12: [4, 3, 3, 3, 2, 1, 0, 0, 0],
            13: [4, 3, 3, 3, 2, 1, 1, 0, 0],
            14: [4, 3, 3, 3, 2, 1, 1, 0, 0],
            15: [4, 3, 3, 3, 2, 1, 1, 1, 0],
            16: [4, 3, 3, 3, 2, 1, 1, 1, 0],
            17: [4, 3, 3, 3, 2, 1, 1, 1, 1],
            18: [4, 3, 3, 3, 3, 1, 1, 1, 1],
            19: [4, 3, 3, 3, 3, 2, 1, 1, 1],
            20: [4, 3, 3, 3, 3, 2, 2, 1, 1],
        }[self.level][spell_level - 1]

    #############################################################################
    def mod_add_known_spells(self, character: "BaseCharacter") -> Reason[Spell]:
        cleric_spells = {
            0: [
                # Cantrips are learnt
            ],
            1: [
                Spell.BANE,
                Spell.BLESS,
                Spell.COMMAND,
                Spell.CREATE_OR_DESTROY_WATER,
                Spell.CURE_WOUNDS,
                Spell.DETECT_EVIL_AND_GOOD,
                Spell.DETECT_MAGIC,
                Spell.DETECT_POISON_AND_DISEASE,
                Spell.GUIDING_BOLT,
                Spell.HEALING_WORD,
                Spell.INFLICT_WOUNDS,
                Spell.PROTECTION_FROM_EVIL_AND_GOOD,
                Spell.PURIFY_FOOD_AND_DRINK,
                Spell.SANCTUARY,
                Spell.SHIELD_OF_FAITH,
            ],
            2: [
                Spell.AID,
                Spell.AUGURY,
                Spell.BLINDNESS_DEAFNESS,
                Spell.CALM_EMOTIONS,
                Spell.CONTINUAL_FLAME,
                Spell.ENHANCE_ABILITY,
                Spell.FIND_TRAPS,
                Spell.GENTLE_REPOSE,
                Spell.HOLD_PERSON,
                Spell.LESSER_RESTORATION,
                Spell.LOCATE_OBJECT,
                Spell.PRAYER_OF_HEALING,
                Spell.PROTECTION_FROM_POISON,
                Spell.SILENCE,
                Spell.SPIRITUAL_WEAPON,
                Spell.WARDING_BOND,
                Spell.ZONE_OF_TRUTH,
            ],
            3: [
                Spell.ANIMATE_DEAD,
                Spell.AURA_OF_VITALITY,
                Spell.BEACON_OF_HOPE,
                Spell.BESTOW_CURSE,
                Spell.CLAIRVOYANCE,
                Spell.CREATE_FOOD_AND_WATER,
                Spell.DAYLIGHT,
                Spell.DISPEL_MAGIC,
                Spell.FEIGN_DEATH,
                Spell.GLYPH_OF_WARDING,
                Spell.MAGIC_CIRCLE,
                Spell.MASS_HEALING_WORD,
                Spell.MELD_INTO_STONE,
                Spell.PROTECTION_FROM_ENERGY,
                Spell.REMOVE_CURSE,
                Spell.REVIVIFY,
                Spell.SENDING,
                Spell.SPEAK_WITH_DEAD,
                Spell.SPIRIT_GUARDIANS,
                Spell.TONGUES,
                Spell.WATER_WALK,
            ],
            4: [
                Spell.AURA_OF_LIFE,
                Spell.AURA_OF_PURITY,
                Spell.BANISHMENT,
                Spell.CONTROL_WATER,
                Spell.DEATH_WARD,
                Spell.DIVINATION,
                Spell.FREEDOM_OF_MOVEMENT,
                Spell.GUARDIAN_OF_FAITH,
                Spell.LOCATE_CREATURE,
                Spell.STONE_SHAPE,
            ],
            5: [
                Spell.CIRCLE_OF_POWER,
                Spell.COMMUNE,
                Spell.CONTAGION,
                Spell.DISPEL_EVIL_AND_GOOD,
                Spell.FLAME_STRIKE,
                Spell.GEAS,
                Spell.GREATER_RESTORATION,
                Spell.HALLOW,
                Spell.INSECT_PLAGUE,
                Spell.LEGEND_LORE,
                Spell.MASS_CURE_WOUNDS,
                Spell.PLANAR_BINDING,
                Spell.RAISE_DEAD,
                Spell.SCRYING,
                Spell.SUMMON_CELESTIAL,
            ],
            6: [
                Spell.BLADE_BARRIER,
                Spell.CREATE_UNDEAD,
                Spell.FIND_THE_PATH,
                Spell.FORBIDDANCE,
                Spell.HARM,
                Spell.HEROES_FEAST,
                Spell.PLANAR_ALLY,
                Spell.SUNBEAM,
                Spell.TRUE_SEEING,
                Spell.WORD_OF_RECALL,
            ],
            7: [
                Spell.CONJURE_CELESTIAL,
                Spell.DIVINE_WORD,
                Spell.ETHEREALNESS,
                Spell.FIRE_STORM,
                Spell.PLANE_SHIFT,
                Spell.POWER_WORD_FORTIFY,
                Spell.REGENERATE,
                Spell.RESURRECTION,
                Spell.SYMBOL,
            ],
            8: [Spell.ANTIMAGIC_FIELD, Spell.CONTROL_WEATHER, Spell.EARTHQUAKE, Spell.HOLY_AURA, Spell.SUNBURST],
            9: [Spell.ASTRAL_PROJECTION, Spell.GATE, Spell.MASS_HEAL, Spell.POWER_WORD_HEAL, Spell.TRUE_RESURRECTION],
        }

        known_spells: Reason[Spell] = Reason()
        for spells in cleric_spells.values():
            for spell in spells:
                known_spells |= Reason("Cleric Spell", spell)
        return known_spells


#################################################################################
class KnowledgeCleric(Cleric):
    def level1(self, **kwargs: Any):
        super().level1(**kwargs)
        self.add_feature(KnowledgeDomainSpells())
        if "blessing" not in kwargs:
            raise InvalidOption("Level 1 Knowledge Domain Clerics get Blessings of Knowledge. 'blessing=...'")
        assert isinstance(kwargs["blessing"], BlessingsOfKnowledge)
        self.add_feature(kwargs["blessing"])


#################################################################################
class KnowledgeDomainSpells(BaseFeature):
    tag = Feature.KNOWLEDGE_DOMAIN_SPELLS14
    _desc = "Spells"
    hide = True

    def mod_add_prepared_spells(self, character: "BaseCharacter") -> Reason[Spell]:
        return Reason("Knowledge Domain Spells", Spell.COMMAND, Spell.IDENTIFY)


#################################################################################
class BlessingsOfKnowledge(BaseFeature):
    tag = Feature.BLESSINGS_OF_KNOWLEDGE14
    _desc = "Skillz"
    hide = True

    def __init__(self, language1: Language, language2: Language, skill1: Skill, skill2: Skill):
        available_skills = (Skill.ARCANA, Skill.HISTORY, Skill.NATURE, Skill.RELIGION)
        self.languages = (language1, language2)
        self.skills = (skill1, skill2)
        if skill1 not in available_skills:
            raise InvalidOption(f"Skill {skill1} must be in {available_skills}")
        if skill2 not in available_skills:
            raise InvalidOption(f"Skill {skill2} must be in {available_skills}")

    def mod_add_language(self, character: "BaseCharacter") -> Reason[Language]:
        return Reason("Blessings of Knowledge", *self.languages)

    def mod_add_skill_proficiency(self, character: "BaseCharacter") -> Reason[Skill]:
        return Reason("Blessings of Knowledge", *self.skills)


#################################################################################
class LifeCleric(Cleric):
    def level1(self, **kwargs: Any):
        super().level1(**kwargs)
        assert self.character is not None
        self.add_feature(LifeDomainSpells())
        self.add_feature(DiscipleOfLife())
        self.character.add_armor_proficiency(Reason("Life Cleric", cast(Proficiency, Proficiency.HEAVY_ARMOUR)))


#################################################################################
class DiscipleOfLife(BaseFeature):
    tag = Feature.DISCIPLE_OF_LIFE14
    _desc = """Whenever you use a spell of 1st level or higher to restore hit points to a creature, the creature 
            regains additional hit points equal to 2 + the spells level"""


#################################################################################
class LifeDomainSpells(BaseFeature):
    tag = Feature.LIFE_DOMAIN_SPELLS14
    _desc = "Spells"
    hide = True

    def mod_add_prepared_spells(self, character: "BaseCharacter") -> Reason[Spell]:
        return Reason("Life Domain Spells", Spell.BLESS, Spell.CURE_WOUNDS)


#################################################################################
class LightCleric(Cleric):
    def level1(self, **kwargs: Any):
        super().level1(**kwargs)
        self.add_feature(LightDomainSpells())
        self.add_feature(WardingFlare())


#################################################################################
class LightDomainSpells(BaseFeature):
    tag = Feature.LIGHT_DOMAIN_SPELLS14
    _desc = "Spells"
    hide = True

    def mod_add_prepared_spells(self, character: "BaseCharacter") -> Reason[Spell]:
        return Reason("Light Domain Spells", Spell.BURNING_HANDS, Spell.FAERIE_FIRE, Spell.LIGHT)


#################################################################################
class WardingFlare(BaseFeature):
    tag = Feature.WARDING_FLARE14
    recovery = Recovery.LONG_REST
    _desc = """When you are attacked by a creature within 20 feet of you that you can see, you can use your reaction 
    to impose disadvantage on the attack roll causing light to flare before the attacker before it hits or misses. An 
    attacker that can't be blinded is immune to this feature."""

    @property
    def goes(self) -> int:
        return max(1, self.owner.stats[Stat.WISDOM].modifier)


#################################################################################
class NatureCleric(Cleric):
    def level1(self, **kwargs: Any):
        assert self.character is not None

        super().level1(**kwargs)
        self.add_feature(NatureDomainSpells())
        self.character.add_armor_proficiency(Reason("Nature Cleric", cast(Proficiency, Proficiency.HEAVY_ARMOUR)))

        if "acolyte" not in kwargs:
            raise InvalidOption("Level 1 Nature Domain Clerics get Acolyte of Nature. 'acolyte=...'")
        assert isinstance(kwargs["acolyte"], AcolyteOfNature)
        self.add_feature(kwargs["acolyte"])


#################################################################################
class NatureDomainSpells(BaseFeature):
    tag = Feature.NATURE_DOMAIN_SPELLS14
    _desc = "Spells"
    hide = True

    def mod_add_prepared_spells(self, character: "BaseCharacter") -> Reason[Spell]:
        return Reason("Nature Domain Spells", Spell.ANIMAL_FRIENDSHIP, Spell.SPEAK_WITH_ANIMALS)


#################################################################################
class AcolyteOfNature(BaseFeature):
    tag = Feature.NATURE_DOMAIN_SPELLS14

    def __init__(self, cantrip: Spell, skill: Skill):
        available_skills = (Skill.ANIMAL_HANDLING, Skill.NATURE, Skill.SURVIVAL)
        self.cantrip = cantrip
        assert is_cantrip(cantrip)
        self.skill = skill
        assert skill in available_skills

    def mod_add_skill_proficiency(self, character: "BaseCharacter") -> Reason[Skill]:
        return Reason("Acolyte of Nature", self.skill)

    def mod_add_prepared_spells(self, character: "BaseCharacter") -> Reason[Spell]:
        return Reason("Acolyte of Nature", self.cantrip)


#################################################################################
class TempestCleric(Cleric):
    def level1(self, **kwargs: Any):
        super().level1(**kwargs)
        assert self.character is not None
        self.add_feature(TempestDomainSpells())
        self.character.add_armor_proficiency(Reason("Tempest Cleric", cast(Proficiency, Proficiency.HEAVY_ARMOUR)))
        self.character.add_weapon_proficiency(Reason("Tempest Cleric", cast(Proficiency, Proficiency.MARTIAL_WEAPONS)))
        self.add_feature(WrathOfTheStorm())


#################################################################################
class TempestDomainSpells(BaseFeature):
    tag = Feature.TEMPEST_DOMAIN_SPELLS14
    _desc = "Spells"
    hide = True

    def mod_add_prepared_spells(self, character: "BaseCharacter") -> Reason[Spell]:
        return Reason("Tempest Domain Spells", Spell.FOG_CLOUD, Spell.THUNDERWAVE)


#################################################################################
class WrathOfTheStorm(BaseFeature):
    tag = Feature.WRATH_OF_THE_STORM14
    recovery = Recovery.LONG_REST
    _desc = """When a creature within 5 feet of you that you can seee hits you with an attack, you can use your 
    reaction to cause the creature to make a Dexterity saving throw. The creature takes 2d8 lightning or thunder 
    damage (your choice) on a failed saving throw, and half as much damage on a successful one."""

    @property
    def goes(self) -> int:
        return max(1, self.owner.stats[Stat.WISDOM].modifier)


#################################################################################
class TrickeryCleric(Cleric):
    def level1(self, **kwargs: Any):
        super().level1(**kwargs)
        self.add_feature(TrickeryDomainSpells())
        self.add_feature(BlessingOfTheTrickster())


#################################################################################
class TrickeryDomainSpells(BaseFeature):
    tag = Feature.TRICKERY_DOMAIN_SPELLS14
    _desc = "Spells"
    hide = True

    def mod_add_prepared_spells(self, character: "BaseCharacter") -> Reason[Spell]:
        return Reason("Trickery Domain Spells", Spell.CHARM_PERSON, Spell.DISGUISE_SELF)


#################################################################################
class BlessingOfTheTrickster(BaseFeature):
    tag = Feature.BLESSING_OF_THE_TRICKSTER14
    _desc = """You can use your action to touch a willing creature other than yourself to give it advantage on 
    Dexterity(Stealth) checks. This blessin lasts for 1 hour or until you use this feature again."""


#################################################################################
class WarCleric(Cleric):
    def level1(self, **kwargs: Any):
        super().level1(**kwargs)
        self.add_feature(WarDomainSpells())
        self.add_feature(WarPriest())
        assert self.character is not None
        self.character.add_armor_proficiency(Reason("War Cleric", cast(Proficiency, Proficiency.HEAVY_ARMOUR)))
        self.character.add_weapon_proficiency(Reason("War Cleric", cast(Proficiency, Proficiency.MARTIAL_WEAPONS)))


#################################################################################
class WarDomainSpells(BaseFeature):
    tag = Feature.WAR_DOMAIN_SPELLS14
    _desc = "Spells"
    hide = True

    def mod_add_prepared_spells(self, character: "BaseCharacter") -> Reason[Spell]:
        return Reason("War Domain Spells", Spell.DIVINE_FAVOR, Spell.SHIELD_OF_FAITH)


#################################################################################
class WarPriest(BaseFeature):
    tag = Feature.WAR_PRIEST14
    recovery = Recovery.LONG_REST
    _desc = """Your god delivers bolts of inspiration to you while you are engaged in battle. When you use the Attack 
    action, you can make one weapon attack as a bonus action"""

    @property
    def goes(self) -> int:
        return max(1, self.owner.stats[Stat.WISDOM].modifier)


# EOF
