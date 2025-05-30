from typing import Optional, TYPE_CHECKING, Any, cast

from aenum import extend_enum
from charsheets.classes.base_class import BaseClass
from charsheets.constants import Stat, Proficiency, Skill, Feature, Language, Recovery, CharacterClass
from charsheets.exception import InvalidOption
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character

extend_enum(Feature, "ARCHDRUID", "Archdruid")
extend_enum(Feature, "BEAST_SPELLS", "Beast Spells")
extend_enum(Feature, "DRUIDIC", "Druidic")
extend_enum(Feature, "ELEMENTAL_FURY", "Elemental Fury")
extend_enum(Feature, "IMPROVED_ELEMENTAL_FURY", "Improved Elemental Fury")
extend_enum(Feature, "MAGICIAN", "Magician")
extend_enum(Feature, "WARDEN", "Warden")
extend_enum(Feature, "WILD_COMPANION", "Wild Companion")
extend_enum(Feature, "WILD_RESURGENCE", "Wild Resurgence")
extend_enum(Feature, "WILD_SHAPE", "Wild Shape")


#################################################################################
class Druid(BaseClass):
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
    _base_class = CharacterClass.DRUID
    _class_name = "Druid"

    #############################################################################
    def level1init(self, **kwargs: Any):
        assert self.character is not None
        self.character.set_saving_throw_proficiency(Stat.INTELLIGENCE, Stat.WISDOM)

    #############################################################################
    def level1multi(self, **kwargs: Any):
        assert self.character is not None

    #############################################################################
    def level1(self, **kwargs: Any):
        assert self.character is not None
        if "primal" not in kwargs:
            raise InvalidOption("Level 1 druids need to define a Primal Order with 'primal=...'")
        self.add_feature(kwargs["primal"])
        self.character.add_armor_proficiency(Reason("Druid", cast(Proficiency, Proficiency.LIGHT_ARMOUR)))
        self.character.add_armor_proficiency(Reason("Druid", cast(Proficiency, Proficiency.SHIELDS)))
        self.add_feature(Druidic())

    #############################################################################
    def level2(self, **kwargs: Any):
        self.add_feature(WildShape())
        self.add_feature(WildCompanion())

    #############################################################################
    def level5(self, **kwargs: Any):
        self.add_feature(WildResurgence())

    #############################################################################
    def level7(self, **kwargs: Any):
        self.add_feature(ElementalFury())

    #############################################################################
    def level15(self, **kwargs: Any):
        self.add_feature(ImprovedElementalFury())

    #############################################################################
    def level18(self, **kwargs: Any):
        self.add_feature(BeastSpells())

    #############################################################################
    def level20(self, **kwargs: Any):
        self.add_feature(Archdruid())

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
        druid_spells: dict[int, list[Spell]] = {
            0: [
                # Spell.DRUIDCRAFT,
                # Spell.ELEMENTALISM,
                # Spell.GUIDANCE,
                # Spell.MENDING,
                # Spell.MESSAGE,
                # Spell.POISON_SPRAY,
                # Spell.PRODUCE_FLAME,
                # Spell.RESISTANCE,
                # Spell.SHILLELAGH,
                # Spell.SPARE_THE_DYING,
                # Spell.STARRY_WISP,
                # Spell.THORN_WHIP,
                # Spell.THUNDERCLAP,
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
            6: [
                Spell.CONJURE_FEY,
                Spell.FIND_THE_PATH,
                Spell.FLESH_TO_STONE,
                Spell.HEAL,
                Spell.HEROES_FEAST,
                Spell.MOVE_EARTH,
                Spell.SUNBEAM,
                Spell.TRANSPORT_VIA_PLANTS,
                Spell.WALL_OF_THORNS,
                Spell.WIND_WALK,
            ],
            7: [Spell.FIRE_STORM, Spell.MIRAGE_ARCANE, Spell.PLANE_SHIFT, Spell.REGENERATE, Spell.REVERSE_GRAVITY, Spell.SYMBOL],
            8: [
                Spell.ANIMAL_SHAPES,
                Spell.ANTIPATHY_SYMPATHY,
                Spell.BEFUDDLEMENT,
                Spell.CONTROL_WEATHER,
                Spell.EARTHQUAKE,
                Spell.INCENDIARY_CLOUD,
                Spell.SUNBURST,
                Spell.TSUNAMI,
            ],
            9: [Spell.FORESIGHT, Spell.SHAPECHANGE, Spell.STORM_OF_VENGEANCE, Spell.TRUE_RESURRECTION],
        }

        known_spells: Reason[Spell] = Reason()
        for level, spells in druid_spells.items():
            if self.spell_slots(level) == 0:
                continue
            for spell in spells:
                known_spells |= Reason("Druid Spell", spell)
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

    @property
    def goes(self) -> int:
        if self.owner.level >= 17:
            return 4
        elif self.owner.level >= 6:
            return 3
        else:
            return 2

    @property
    def cr(self) -> str:
        if self.owner.level >= 8:
            return "1"
        elif self.owner.level >= 4:
            return "1/2"
        return "1/4"

    @property
    def desc(self) -> str:
        assert self.owner.druid is not None
        return f"""The power of nature allows you to assume the form of an animal. As a Bonus Action, you shape-shift 
        into a Beast form (Max CR {self.cr}) that you have learned for this feature. You stay in that form for
        {self.owner.druid.level // 2} hours or until you use Wild Shape again, have the Incapacitated condition,
        or die. You can also leave the form early as a Bonus Action."""


#############################################################################
class WildCompanion(BaseFeature):
    tag = Feature.WILD_COMPANION
    _desc = """You can summon a nature spirit that assumes an animal form to aid you. As a Magic action,
    you can expend a spell slot or a use of Wild Shape to cast the 'Find Familiar' spell without Material components.
    When you cast the spell in this way, the familiar is Fey and disappears when you finish a long rest."""


#################################################################################
class Magician(BaseFeature):
    tag = Feature.MAGICIAN
    hide = True
    _desc = """You know one extra cantrip from the Druid spell list."""

    def mod_skill_arcana(self, character: "Character") -> Reason:
        return Reason("Magician", self.bonus())

    def mod_skill_nature(self, character: "Character") -> Reason:
        return Reason("Magician", self.bonus())

    def bonus(self) -> int:
        return max(1, self.owner.wisdom.modifier)


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
    expending a spell slot (no action required). In addition, you can expend one use of Wild Shape (no action
    required) to give yourself a level 1 spell slot."""


#############################################################################
class ElementalFury(BaseFeature):
    tag = Feature.ELEMENTAL_FURY

    @property
    def desc(self) -> str:
        return f"""You gain one of the following options of your choice.
    
    Potent Spellcasting. Add {self.owner.wisdom.modifier} to the damage you deal with any Druid cantrip.
    
    Primal Strike. Once on each of your turns when you hit a creature with an attack roll using a weapon or a Beast 
    form's attack in Wild Shape, you can cause the target to take an extra 1d8 Cold, Fire, Lightning, or Thunder 
    damage (choose when you hit)."""


#############################################################################
class ImprovedElementalFury(BaseFeature):
    tag = Feature.IMPROVED_ELEMENTAL_FURY

    _desc = """Potent Spellcasting. When you cast a Druid cantrip with a range of 10 feet or greater, the spell's
        range increases by 300 feet.
        
        Primal Strike. The extra damage of your Primal Strike increases to 2d8."""


#############################################################################
class BeastSpells(BaseFeature):
    tag = Feature.BEAST_SPELLS

    _desc = """While using Wild Shape, you can cast spells in Beast form, except for any spell that has a Material 
    component with a cost specified or that consumes its Material component."""


#############################################################################
class Archdruid(BaseFeature):
    tag = Feature.ARCHDRUID

    _desc = """The vitality of nature constantly blooms within you, granting you the following benefits. Evergreen 
    Wild Shape. Whenever you roll Initiative and have no uses of Wild Shape left, you regain one expended use of it.

    Nature Magician. You can convert uses of Wild Shape into a spell slot (no action required). Choose a number of 
    your unexpended uses of Wild Shape and convert them into a single spell slot, with each use contributing 2 spell 
    levels. For example, if you convert two uses of Wild Shape, you produce a level 4 spell slot. Once you use this 
    benefit, you can't do so again until you finish a Long Rest.

    Longevity. The primal magic that you wield causes you to age more slowly. For every ten years that pass, 
    your body ages only one year."""


# EOF
