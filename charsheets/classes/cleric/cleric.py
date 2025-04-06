from typing import Optional, cast, TYPE_CHECKING, Any

from aenum import extend_enum

from charsheets.classes.base_class import BaseClass
from charsheets.constants import Stat, Proficiency, Skill, Feature, Recovery, CharacterClass
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


extend_enum(Feature, "BLESSED_STRIKES", "Blessed Strikes")
extend_enum(Feature, "CHANNEL_DIVINITY_CLERIC", "Channel Divinity")
extend_enum(Feature, "DIVINE_INTERVENTION", "Divine Intervention")
extend_enum(Feature, "DIVINE_ORDER_PROTECTOR", "Divine Order Protector")
extend_enum(Feature, "DIVINE_ORDER_THAUMATURGE", "Divine Order Thaumaturge")
extend_enum(Feature, "SEAR_UNDEAD", "Sear Undead")


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
    def level1multi(self, **kwargs: Any):
        pass

    #############################################################################
    def level1(self, **kwargs: Any):
        assert self.character is not None
        self.character.add_armor_proficiency(Reason("Cleric", cast(Proficiency, Proficiency.LIGHT_ARMOUR)))
        self.character.add_armor_proficiency(Reason("Cleric", cast(Proficiency, Proficiency.MEDIUM_ARMOUR)))
        self.character.add_armor_proficiency(Reason("Cleric", cast(Proficiency, Proficiency.SHIELDS)))

    #############################################################################
    def level2(self, **kwargs: Any):
        self.add_feature(ChannelDivinityCleric())

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(SearUndead())

    #############################################################################
    def level10(self, **kwargs: Any):
        self.add_feature(DivineIntervention())

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
    def mod_add_known_spells(self, character: "Character") -> Reason[Spell]:
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

    #############################################################################
    def max_spell_level(self) -> int:
        return min(9, ((self.level + 1) // 2))


#############################################################################
class SearUndead(BaseFeature):
    tag = Feature.SEAR_UNDEAD
    _desc = ""

    @property
    def desc(self) -> str:
        bonus = max(1, self.owner.wisdom.modifier)
        return f"""Whenever you use Turn Undead, you can roll {bonus}d8's
    and add the rolls together. Each Undead that fails its saving throw against that use of Turn Undead takes Radiant
    damage equal to the roll's total. This damage doesn't end the turn effect."""


#################################################################################
class DivineProtector(BaseFeature):
    tag = Feature.DIVINE_ORDER_PROTECTOR
    _desc = """Trained for battle, you gain proficiency with Martial weapons and training with Heavy armor."""
    hide = True

    #############################################################################
    def mod_weapon_proficiency(self, character: "Character") -> Reason[Proficiency]:
        return Reason[Proficiency]("Protector", cast(Proficiency, Proficiency.MARTIAL_WEAPONS))

    #############################################################################
    def mod_armour_proficiency(self, character: "Character") -> Reason[Proficiency]:
        return Reason("Protector", cast(Proficiency, Proficiency.HEAVY_ARMOUR))


#################################################################################
class Thaumaturge(BaseFeature):
    tag = Feature.DIVINE_ORDER_THAUMATURGE
    _desc = """Thaumaturge. You know one extra cantrip from the Cleric spell list."""

    # Users will have to add their own cantrip to the learnt spells.

    def mod_skill_arcana(self, character: "Character") -> Reason[int]:
        return Reason[int]("thaumaturge", max(1, character.wisdom.modifier))

    def mod_skill_religion(self, character: "Character") -> Reason[int]:
        return Reason[int]("thaumaturge", max(1, character.wisdom.modifier))


#############################################################################
class ChannelDivinityCleric(BaseFeature):
    tag = cast(Feature, Feature.CHANNEL_DIVINITY_CLERIC)
    recovery = Recovery.PARTIAL

    @property
    def goes(self) -> int:
        if self.owner.level >= 18:
            return 4
        elif self.owner.level >= 6:
            return 3
        return 2

    @property
    def desc(self) -> str:
        if self.owner.level >= 18:
            dice = "4d8"
        elif self.owner.level >= 13:
            dice = "3d8"
        elif self.owner.level >= 7:
            dice = "2d8"
        else:
            dice = "1d8"
        mod = self.owner.wisdom.modifier
        return f"""You can channel divine energy.

    Divine Spark. As a Magic action, you point your Holy Symbol at another creature you can see within 30 feet of
    yourself and focus divine energy at it. Roll {dice} and add your Wisdom modifier ({mod}). You either restore Hit
    Points to the creature equal to that total or force the creature to Make a Constitution saving throw. On a failed
    save, the creature takes Necrotic or Radiant damage (your choice) equal to that total. On a successful save,
    the creature takes half as much damage.

    Turn Undead. As a Magic action, you present your Hold Symbol and censure Undead creatures. Each Undead of your
    choice within 30 feet of you must make a Wisdom saving throw. If the creature fails its save, it has the Frightened
    and Incapacitated condition for 1 minute. For that duration, it tries to mave as far from you as it can on its
    turns. This effect ends early on the creature if it takes any damage, if you have the Incapacitated condition,
    or if you die
    """


#################################################################################
class BlessedStrikes(BaseFeature):
    tag = Feature.BLESSED_STRIKES
    _desc = """You gain one of the following options of your choice.

    Divine Strike. Once on each of your turns when you hit a creature with an attack roll using a weapon,
    you can cause the target to take an extra 1d8 Necrotic or Radiant damage (your choice).
    
    Potent Spellcasting. Add your Wisdom modifier to the damage you deal with any Cleric cantrip."""


#################################################################################
class DivineIntervention(BaseFeature):
    tag = Feature.DIVINE_INTERVENTION
    _goes = 1
    recovery = Recovery.LONG_REST
    _desc = """As a Magic action, choose any 
    Cleric spell of level 5 or lower that doesn't require a Reaction to cast. As part of the same action, 
    you cast that spell without expending a spell slot or needing Material components.."""


# EOF
