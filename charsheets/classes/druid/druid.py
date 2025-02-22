from typing import Optional

from charsheets.character import Character
from charsheets.constants import Stat, Proficiency, Skill, Feature, Language, Recovery
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell


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
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {Druidic()}
        if self.level >= 2:
            abilities.add(WildShape())
            abilities.add(WildCompanion())
        if self.level >= 5:
            abilities.add(WildResurgence())
        if self.level >= 7:
            abilities.add(ElementalFury())
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
            17: [4, 3, 3, 3, 2, 1, 1, 1, 0],
            18: [4, 3, 3, 3, 3, 1, 1, 1, 0],
            19: [4, 3, 3, 3, 3, 2, 1, 1, 0],
            20: [4, 3, 3, 3, 3, 2, 2, 1, 0],
        }[self.level][spell_level - 1]

    #############################################################################
    def mod_add_known_spells(self, character: "Character") -> Reason[Spell]:
        druid_spells: dict[int, list[Spell]] = {
            0: [
                Spell.DRUIDCRAFT,
                Spell.ELEMENTALISM,
                Spell.GUIDANCE,
                Spell.MENDING,
                Spell.MESSAGE,
                Spell.POISON_SPRAY,
                Spell.PRODUCE_FLAME,
                Spell.RESISTANCE,
                Spell.SHILLELAGH,
                Spell.SPARE_THE_DYING,
                Spell.STARRY_WISP,
                Spell.THORN_WHIP,
                Spell.THUNDERCLAP,
            ],
            1: [
                Spell.ANIMAL_FRIENDSHIP,
                Spell.CHARM_PERSON,
                Spell.CREATE_OR_DESTROY_WATER,
                Spell.CURE_WOUNDS,
                Spell.DETECT_MAGIC,
                Spell.DETECT_POISON_AND_DISEASE,
                Spell.ENTANGLE,
                Spell.FAERIE_FIRE,
                Spell.FOG_CLOUD,
                Spell.GOODBERRY,
                Spell.HEALING_WORD,
                Spell.ICE_KNIFE,
                Spell.JUMP,
                Spell.LONGSTRIDER,
                Spell.PROTECTION_FROM_EVIL_AND_GOOD,
                Spell.PURIFY_FOOD_AND_DRINK,
                Spell.SPEAK_WITH_ANIMALS,
                Spell.THUNDERWAVE,
            ],
            2: [
                Spell.AID,
                Spell.ANIMAL_MESSENGER,
                Spell.AUGURY,
                Spell.BARKSKIN,
                Spell.BEAST_SENSE,
                Spell.CONTINUAL_FLAME,
                Spell.DARKVISION,
                Spell.ENHANCE_ABILITY,
                Spell.ENLARGE_REDUCE,
                Spell.FIND_TRAPS,
                Spell.FLAME_BLADE,
                Spell.FLAMING_SPHERE,
                Spell.GUST_OF_WIND,
                Spell.HEAT_METAL,
                Spell.HOLD_PERSON,
                Spell.LESSER_RESTORATION,
                Spell.LOCATE_ANIMALS_OR_PLANTS,
                Spell.LOCATE_OBJECT,
                Spell.MOONBEAM,
                Spell.PASS_WITHOUT_TRACE,
                Spell.PROTECTION_FROM_POISON,
                Spell.SPIKE_GROWTH,
                Spell.SUMMON_BEAST,
            ],
            3: [
                Spell.AURA_OF_VITALITY,
                Spell.CALL_LIGHTNING,
                Spell.CONJURE_ANIMALS,
                Spell.DAYLIGHT,
                Spell.DISPEL_MAGIC,
                Spell.ELEMENTAL_WEAPON,
                Spell.FEIGN_DEATH,
                Spell.MELD_INTO_STONE,
                Spell.PLANT_GROWTH,
                Spell.PROTECTION_FROM_ENERGY,
                Spell.REVIVIFY,
                Spell.SLEET_STORM,
                Spell.SPEAK_WITH_PLANTS,
                Spell.SUMMON_FEY,
                Spell.WATER_BREATHING,
                Spell.WATER_WALK,
                Spell.WIND_WALL,
            ],
            4: [
                Spell.BLIGHT,
                Spell.CHARM_MONSTER,
                Spell.CONFUSION,
                Spell.CONJURE_MINOR_ELEMENTALS,
                Spell.CONJURE_WOODLAND_BEINGS,
                Spell.CONTROL_WATER,
                Spell.DIVINATION,
                Spell.DOMINATE_BEAST,
                Spell.FIRE_SHIELD,
                Spell.FOUNT_OF_MOONLIGHT,
                Spell.FREEDOM_OF_MOVEMENT,
                Spell.GIANT_INSECT,
                Spell.GRASPING_VINE,
                Spell.HALLUCINATORY_TERRAIN,
                Spell.ICE_STORM,
                Spell.LOCATE_CREATURE,
                Spell.POLYMORPH,
                Spell.STONE_SHAPE,
                Spell.STONESKIN,
                Spell.SUMMON_ELEMENTAL,
                Spell.WALL_OF_FIRE,
            ],
            5: [
                Spell.ANTILIFE_SHELL,
                Spell.AWAKEN,
                Spell.COMMUNE_WITH_NATURE,
                Spell.CONE_OF_COLD,
                Spell.CONJURE_ELEMENTAL,
                Spell.CONTAGION,
                Spell.GEAS,
                Spell.GREATER_RESTORATION,
                Spell.INSECT_PLAGUE,
                Spell.MASS_CURE_WOUNDS,
                Spell.PLANAR_BINDING,
                Spell.REINCARNATE,
                Spell.SCRYING,
                Spell.TREE_STRIDE,
                Spell.WALL_OF_STONE,
            ],
            6: [],
            7: [],
            8: [],
            9: [],
        }

        known_spells: Reason[Spell] = Reason()
        for spells in druid_spells.values():
            for spell in spells:
                known_spells |= Reason("Ranger Spell", spell)
        return known_spells


#############################################################################
class Druidic(BaseFeature):
    tag = Feature.DRUIDIC
    _desc = """You know Druidic, the secret language of Druids."""
    hide = True

    def mod_add_language(self, character: "Character") -> Reason[Language]:
        return Reason("Druidic", Language.DRUIDIC)


#############################################################################
class WildShape(BaseFeature):
    tag = Feature.WILD_SHAPE
    _desc = """The power of nature allows you to assume the form of an animal.
    As a Bonus Action, you shape-shift into a Beast form that you have learned for this feature."""


#############################################################################
class WildCompanion(BaseFeature):
    tag = Feature.WILD_COMPANION
    _desc = """You can summon a nature spirit that assumes an animal form to aid you. As a Magic action,
    you can expend a spell slot or a use of Wild Shape to cast the Find Familiar spell without Material components.
    When you cast the spell in this way, the familiar is Fey and disappears when you finish a long rest."""


#################################################################################
class Magician(BaseFeature):
    tag = Feature.MAGICIAN
    _desc = """You know one extra cantrip from the Druid spell list. In addition, your mystical connection to nature
    gives you a bonus to your Intelligence (Arcana or Nature) checks.
    The bonus equals your Wisdom modifier (minimum bonus of +1)"""

    def mod_skill_arcana(self, character: "Character") -> Reason:
        return Reason("Magician", max(1, character.wisdom.modifier))

    def mod_skill_nature(self, character: "Character") -> Reason:
        return Reason("Magician", max(1, character.wisdom.modifier))


#################################################################################
class Warden(BaseFeature):
    tag = Feature.WARDEN
    _desc = """Trained for battle, you gain proficiency with Martial weapons and training with Medium armour"""
    hide = True

    #############################################################################
    def mod_weapon_proficiency(self, character: "Character") -> Reason[Proficiency]:
        return Reason("Warden", Proficiency.MARTIAL_WEAPONS)

    #############################################################################
    def mod_armour_proficiency(self, character: "Character") -> Reason[Proficiency]:
        return Reason("Warden", Proficiency.MEDIUM_ARMOUR)


#############################################################################
class WildResurgence(BaseFeature):
    tag = Feature.WILD_RESURGENCE
    goes = 1
    recovery = Recovery.LONG_REST
    _desc = """Once on each of your turns, if you have no uses of Wild Shape left, you can give yourself one use by
    expending a spell slot (no action required). In addition,you can expend one use of Wild Shape (no action
    required) to give yourself a level 1 spell slot."""


#############################################################################
class ElementalFury(BaseFeature):
    tag = Feature.ELEMENTAL_FURY
    _desc = """You gain one of the following options of your choice.
    
    Potent Spellcasting. Add your Wisdom modifier to the damage you deal with any Druid cantrip.
    
    Primal Strike. Once on each of your turns when you hit a creature with an attack roll using a weapon or a Beast 
    form's attack in Wild Shape, you can cause the target to take an extra 1d8 Cold, Fire, Lightning, or Thunder 
    damage (choose when you hit)."""


# EOF
