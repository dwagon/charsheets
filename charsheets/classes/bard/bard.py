from typing import Optional, cast, Any, TYPE_CHECKING

from aenum import extend_enum

from charsheets.classes.base_class import BaseClass
from charsheets.constants import Stat, Proficiency, Skill, Feature, Recovery, CharacterClass
from charsheets.exception import InvalidOption
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character

extend_enum(Feature, "BARDIC_INSPIRATION", "Bardic Inspiration")
extend_enum(Feature, "JACK_OF_ALL_TRADES", "Jack of all Trades")
extend_enum(Feature, "FONT_OF_INSPIRATION", "Font of Inspiration")
extend_enum(Feature, "COUNTERCHARM", "Countercharm")
extend_enum(Feature, "MAGICAL_SECRETS", "Magical Secrets")


#################################################################################
class Bard(BaseClass):
    _base_skill_proficiencies = {
        Skill.ACROBATICS,
        Skill.ANIMAL_HANDLING,
        Skill.ARCANA,
        Skill.ATHLETICS,
        Skill.DECEPTION,
        Skill.HISTORY,
        Skill.INSIGHT,
        Skill.INTIMIDATION,
        Skill.INVESTIGATION,
        Skill.MEDICINE,
        Skill.NATURE,
        Skill.PERCEPTION,
        Skill.PERFORMANCE,
        Skill.PERSUASION,
        Skill.RELIGION,
        Skill.SLEIGHT_OF_HAND,
        Skill.STEALTH,
        Skill.SURVIVAL,
    }
    _base_class = CharacterClass.BARD

    #############################################################################
    def level1init(self, **kwargs: Any):
        assert self.character is not None
        self.character.add_weapon_proficiency(Reason("Bard", cast(Proficiency, Proficiency.SIMPLE_WEAPONS)))
        self.character.set_saving_throw_proficiency(Stat.DEXTERITY, Stat.CHARISMA)

    #############################################################################
    def level1multi(self, **kwargs: Any):
        if "skills" not in kwargs or len(kwargs["skills"]) != 1:
            raise InvalidOption("Level 1 Bards multiclass one skill: skills='...'")

    #############################################################################
    def level1(self, **kwargs: Any):
        assert self.character is not None
        self.add_feature(BardicInspiration())
        self.character.add_armor_proficiency(Reason("Bard", cast(Proficiency, Proficiency.LIGHT_ARMOUR)))

    #############################################################################
    def level2(self, **kwargs: Any):
        if "expertise" not in kwargs:
            raise InvalidOption("Level 2 Bards get Expertise: level2(expertise=Expertise(...))")
        self.add_feature(kwargs["expertise"])
        self.add_feature(JackOfAllTrades())

    #############################################################################
    def level5(self, **kwargs: Any):
        self.add_feature(FontOfInspiration())

    #############################################################################
    def level7(self, **kwargs: Any):
        self.add_feature(Countercharm())

    #############################################################################
    def level9(self, **kwargs: Any):
        if "expertise" not in kwargs:
            raise InvalidOption("Level 9 Bards get Expertise: level9(expertise=Expertise(...))")
        self.add_feature(kwargs["expertise"])

    #############################################################################
    def level10(self, **kwargs: Any):
        self.add_feature(MagicalSecrets())

    #############################################################################
    @property
    def hit_dice(self) -> int:
        return 8

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.CHARISMA

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
    def max_spell_level(self) -> int:
        return min(9, ((self.level + 1) // 2))

    #############################################################################
    def mod_add_known_spells(self, character: "Character") -> Reason[Spell]:
        bard_spells = {
            0: [
                # Cantrips are learnt
            ],
            1: [
                Spell.ANIMAL_FRIENDSHIP,
                Spell.BANE,
                Spell.CHARM_PERSON,
                Spell.COLOR_SPRAY,
                Spell.COMMAND,
                Spell.COMPREHEND_LANGUAGES,
                Spell.CURE_WOUNDS,
                Spell.DETECT_MAGIC,
                Spell.DISGUISE_SELF,
                Spell.DISSONANT_WHISPERS,
                Spell.FAERIE_FIRE,
                Spell.FEATHER_FALL,
                Spell.HEALING_WORD,
                Spell.HEROISM,
                Spell.IDENTIFY,
                Spell.ILLUSORY_SCRIPT,
                Spell.LONGSTRIDER,
                Spell.SILENT_IMAGE,
                Spell.SLEEP,
                Spell.SPEAK_WITH_ANIMALS,
                Spell.TASHAS_HIDEOUS_LAUGHTER,
                Spell.THUNDERWAVE,
                Spell.UNSEEN_SERVANT,
            ],
            2: [
                Spell.AID,
                Spell.ANIMAL_MESSENGER,
                Spell.BLINDNESS_DEAFNESS,
                Spell.CALM_EMOTIONS,
                Spell.CLOUD_OF_DAGGERS,
                Spell.CROWN_OF_MADNESS,
                Spell.DETECT_THOUGHTS,
                Spell.ENHANCE_ABILITY,
                Spell.ENTHRALL,
                Spell.HEAT_METAL,
                Spell.HOLD_PERSON,
                Spell.INVISIBILITY,
                Spell.KNOCK,
                Spell.LESSER_RESTORATION,
                Spell.LOCATE_ANIMALS_OR_PLANTS,
                Spell.LOCATE_OBJECT,
                Spell.MAGIC_MOUTH,
                Spell.MIRROR_IMAGE,
                Spell.PHANTASMAL_FORCE,
                Spell.SEE_INVISIBILITY,
                Spell.SHATTER,
                Spell.SILENCE,
                Spell.SUGGESTION,
                Spell.ZONE_OF_TRUTH,
            ],
            3: [
                Spell.BESTOW_CURSE,
                Spell.CLAIRVOYANCE,
                Spell.DISPEL_MAGIC,
                Spell.FEAR,
                Spell.FEIGN_DEATH,
                Spell.GLYPH_OF_WARDING,
                Spell.HYPNOTIC_PATTERN,
                Spell.LEOMUNDS_TINY_HUT,
                Spell.MAJOR_IMAGE,
                Spell.MASS_HEALING_WORD,
                Spell.NONDETECTION,
                Spell.PLANT_GROWTH,
                Spell.SENDING,
                Spell.SLOW,
                Spell.SPEAK_WITH_DEAD,
                Spell.STINKING_CLOUD,
                Spell.TONGUES,
            ],
            4: [
                Spell.CHARM_MONSTER,
                Spell.COMPULSION,
                Spell.CONFUSION,
                Spell.DIMENSION_DOOR,
                Spell.FOUNT_OF_MOONLIGHT,
                Spell.FREEDOM_OF_MOVEMENT,
                Spell.GREATER_INVISIBILITY,
                Spell.HALLUCINATORY_TERRAIN,
                Spell.LOCATE_CREATURE,
                Spell.PHANTASMAL_KILLER,
                Spell.POLYMORPH,
            ],
            5: [
                Spell.ANIMATE_OBJECT,
                Spell.AWAKEN,
                Spell.DOMINATE_PERSON,
                Spell.DREAM,
                Spell.GEAS,
                Spell.GREATER_RESTORATION,
                Spell.HOLD_MONSTER,
                Spell.LEGEND_LORE,
                Spell.MASS_CURE_WOUNDS,
                Spell.MISLEAD,
                Spell.MODIFY_MEMORY,
                Spell.PLANAR_BINDING,
                Spell.RAISE_DEAD,
                Spell.RARYS_TELEPATHIC_BOND,
                Spell.SCRYING,
                Spell.SEEMING,
                Spell.SYNAPTIC_STATIC,
                Spell.TELEPORTATION_CIRCLE,
                Spell.YOLANDES_REGAL_PRESENCE,
            ],
            6: [
                Spell.EYEBITE,
                Spell.FIND_THE_PATH,
                Spell.GUARDS_AND_WARDS,
                Spell.HEROES_FEAST,
                Spell.MASS_SUGGESTION,
                Spell.OTTOS_IRRESISTIBLE_DANCE,
                Spell.PROGRAMMED_ILLUSION,
                Spell.TRUE_SEEING,
            ],
            7: [
                Spell.ETHEREALNESS,
                Spell.FORCECAGE,
                Spell.MIRAGE_ARCANE,
                Spell.MORDENKAINENS_MAGNFICENT_MASION,
                Spell.MORDENKAINENS_SWORD,
                Spell.POWER_WORD_FORTIFY,
                Spell.PRISMATIC_SPRAY,
                Spell.PROJECT_IMAGE,
                Spell.REGENERATE,
                Spell.RESURRECTION,
                Spell.SYMBOL,
                Spell.TELEPORT,
            ],
            8: [
                Spell.ANTIPATHY_SYMPATHY,
                Spell.BEFUDDLEMENT,
                Spell.DOMINATE_MONSTER,
                Spell.GLIBNESS,
                Spell.MIND_BLANK,
                Spell.POWER_WORD_STUN,
            ],
            9: [Spell.FORESIGHT, Spell.POWER_WORD_HEAL, Spell.POWER_WORK_KILL, Spell.PRISMATIC_WALL, Spell.TRUE_POLYMORPH],
        }

        known_spells: Reason[Spell] = Reason()
        for level in range(self.max_spell_level()):
            for spell in bard_spells[level]:
                known_spells |= Reason("Bard Spell", spell)
        return known_spells

    #############################################################################
    def num_bardic_inspiration(self) -> int:
        assert self.character is not None
        return max(1, self.character.charisma.modifier)

    #############################################################################
    def bardic_inspiration_die(self) -> str:
        assert self.character is not None
        assert self.character.bard is not None
        if self.character.bard.level >= 15:
            return "d12"
        elif self.character.bard.level >= 10:
            return "d10"
        elif self.character.bard.level >= 5:
            return "d8"
        return "d6"

    #############################################################################
    @property
    def class_special(self) -> str:
        return f"Bardic Inspiration: {self.num_bardic_inspiration()}{self.bardic_inspiration_die()}"


#############################################################################
class BardicInspiration(BaseFeature):
    tag = Feature.BARDIC_INSPIRATION
    recovery = Recovery.LONG_REST

    @property
    def goes(self) -> int:
        assert self.owner.bard is not None
        return self.owner.bard.num_bardic_inspiration()

    _desc = """As a Bonus Action, you can inspire another creature within 60 feet of yourself who can see or hear 
    you. That creature gains one of your Bardic Inspiration dice. A creature can have only one Bardic Inspiration die 
    at a time.
    
    Once within the next hour when the creature fails a D20 Test, the creature can roll the Bardic Inspiration die 
    and add the number rolled to the d20, potentially turning the failure into a success."""


#############################################################################
class JackOfAllTrades(BaseFeature):
    tag = Feature.JACK_OF_ALL_TRADES

    @property
    def desc(self) -> str:
        bonus = self.owner.proficiency_bonus // 2
        return f"""You can add {bonus} to any ability check you make that uses a skill proficiency you lack and that 
        doesn't otherwise use your Proficiency Bonus."""


#############################################################################
class FontOfInspiration(BaseFeature):
    tag = Feature.FONT_OF_INSPIRATION
    _desc = """You now regain all your expended uses of Bardic Inspiration when you finish a Short or Long Rest. You 
    can expend a spell slot (no action required) to regain one expended use of Bardic Inspiration."""


#############################################################################
class Countercharm(BaseFeature):
    tag = Feature.COUNTERCHARM
    _desc = """You can use musical notes or words of power to disrupt mind-influencing effects. If you or a creature 
    within 30 feet of you fails a saving throw against an effect that applies the Charmed or Frightened condition, 
    you can take a Reaction to cause the save to be rerolled, and the new roll has Advantage."""


#############################################################################
class MagicalSecrets(BaseFeature):
    tag = Feature.MAGICAL_SECRETS
    hide = True
    _desc = """You've learned secrets from various magical traditions. Whenever you reach a Bard level (including 
    this level) and the Prepared Spells number in the Bard Features table increases, you can choose any of your new 
    prepared spells from the Bard, Cleric, Druid, and Wizard spell lists, and the chosen spells count as Bard spells 
    for you (see a class's section for its spell list). In addition, whenever you replace a spell prepared for this 
    class, you can replace it with a spell from those lists."""


# EOF
