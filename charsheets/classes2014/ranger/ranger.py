from typing import Optional, Any, cast, TYPE_CHECKING

from aenum import extend_enum

from charsheets.classes.base_class import BaseClass
from charsheets.constants import Stat, Proficiency, Skill, Feature, CharacterClass, Language
from charsheets.exception import InvalidOption
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter


extend_enum(Feature, "FAVOURED_ENEMY14", "Favoured Enemy")
extend_enum(Feature, "NATURAL_EXPLORER14", "Natural Explorer")


#################################################################################
class Ranger(BaseClass):
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
    _base_class = CharacterClass.RANGER
    _class_name = "Ranger"

    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 10

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.WISDOM

    #############################################################################
    def level1init(self, **kwargs: Any):
        assert self.character is not None
        self.character.set_saving_throw_proficiency(Stat.DEXTERITY, Stat.STRENGTH)

    #############################################################################
    def level1multi(self, **kwargs: Any):  # pragma: no coverage
        assert self.character is not None

    #############################################################################
    def level1(self, **kwargs: Any):
        assert self.character is not None
        if "favored" not in kwargs:
            raise InvalidOption("Level 1 Rangers specify a favored enemy with 'favored=FavoredEnemy(...)'")
        self.add_feature(kwargs["favored"])
        self.add_feature(NaturalExplorer())
        self.character.add_weapon_proficiency(Reason("Ranger", cast(Proficiency, Proficiency.MARTIAL_WEAPONS)))
        self.character.add_armor_proficiency(Reason("Ranger", cast(Proficiency, Proficiency.LIGHT_ARMOUR)))
        self.character.add_armor_proficiency(Reason("Ranger", cast(Proficiency, Proficiency.MEDIUM_ARMOUR)))
        self.character.add_armor_proficiency(Reason("Ranger", cast(Proficiency, Proficiency.SHIELDS)))

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return {
            1: [0, 0, 0, 0, 0, 0, 0, 0, 0],
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
    def mod_add_known_spells(self, character: "BaseCharacter") -> Reason[Spell]:
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
            4: [
                Spell.CONJURE_WOODLAND_BEINGS,
                Spell.DOMINATE_BEAST,
                Spell.FREEDOM_OF_MOVEMENT,
                Spell.GRASPING_VINE,
                Spell.LOCATE_CREATURE,
                Spell.STONESKIN,
                Spell.SUMMON_ELEMENTAL,
            ],
            5: [
                Spell.COMMUNE_WITH_NATURE,
                Spell.CONJURE_VOLLEY,
                Spell.GREATER_RESTORATION,
                Spell.STEEL_WIND_STRIKE,
                Spell.SWIFT_QUIVER,
                Spell.TREE_STRIDE,
            ],
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
class FavoredEnemy(BaseFeature):
    tag = Feature.FAVOURED_ENEMY14

    @property
    def desc(self) -> str:
        return f"""You have significant experience studying, tracking, hunting, and even talking 
        to a certain type of enemy: {self.enemy}.
    
        You have advantage on Wisdom (Survival) checks to track your favored enemies, as well as on Intelligence checks 
        to recall information about them."""

    def __init__(self, enemy: str, language: Optional[Language] = None):
        self.language = language
        self.enemy = enemy

    def mod_add_language(self, character: "BaseCharacter") -> Reason[Language]:
        if self.language:
            return Reason("Favored Enemy", self.language)
        return Reason()


#############################################################################
class NaturalExplorer(BaseFeature):
    tag = Feature.NATURAL_EXPLORER14

    _desc = """You are particularly familiar with one type of natural environment and are adept at traveling and 
    surviving in such regions. Choose one type of favored terrain: arctic, coast, desert, forest, grassland, 
    mountain, swamp, or the Underdark. When you make an Intelligence or Wisdom check related to your favored terrain, 
    your proficiency bonus is doubled if you are using a skill that you’re proficient in.

    While traveling for an hour or more in your favored terrain, you gain the following benefits:

    Difficult terrain doesn’t slow your group’s travel.
    
    Your group can’t become lost except by magical means.
    
    Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), 
    you remain alert to danger.
    
    If you are traveling alone, you can move stealthily at a normal pace.
    
    When you forage, you find twice as much food as you normally would.
    
    While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed 
    through the area."""


# EOF
