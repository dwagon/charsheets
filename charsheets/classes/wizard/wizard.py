import math
from typing import Optional, Any, TYPE_CHECKING

from aenum import extend_enum
from charsheets.classes.base_class import BaseClass
from charsheets.constants import Stat, Skill, Feature, Recovery, CharacterClass
from charsheets.exception import InvalidOption
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character

extend_enum(Feature, "ARCANE_RECOVERY", "Arcane Recovery")
extend_enum(Feature, "MEMORIZE_SPELL", "Memorize Spell")
extend_enum(Feature, "RITUAL_ADEPT", "Ritual Adept")
extend_enum(Feature, "SCHOLAR", "Scholar")
extend_enum(Feature, "SIGNATURE_SPELLS", "Signature Spells")
extend_enum(Feature, "SPELL_MASTERY", "Spell Mastery")


#################################################################################
class Wizard(BaseClass):
    _base_skill_proficiencies = {
        Skill.ARCANA,
        Skill.HISTORY,
        Skill.INSIGHT,
        Skill.INVESTIGATION,
        Skill.MEDICINE,
        Skill.NATURE,
        Skill.RELIGION,
    }
    _base_class = CharacterClass.WIZARD
    _class_name = "Wizard"

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
        self.add_feature(RitualAdept())
        self.add_feature(ArcaneRecovery())

    #############################################################################
    def level2(self, **kwargs: Any):
        if "scholar" not in kwargs:
            raise InvalidOption("Level 2 Wizards get Scholar: level2(scholar=Scholar(...))")
        self.add_feature(kwargs["scholar"])

    #############################################################################
    def level5(self, **kwargs: Any):
        self.add_feature(MemorizeSpell())

    #############################################################################
    def level18(self, **kwargs: Any):
        self.add_feature(SpellMastery())

    #############################################################################
    def level20(self, **kwargs: Any):
        self.add_feature(SignatureSpells())

    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 6

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.INTELLIGENCE

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
class RitualAdept(BaseFeature):
    tag = Feature.RITUAL_ADEPT
    _desc = """You can cast any spell as a Ritual if that spell has the Ritual tag and the spell is in your spellbook.
    You needn't have the spell prepared, but you must read from the book to cast a spell in this way."""


#############################################################################
class ArcaneRecovery(BaseFeature):
    tag = Feature.ARCANE_RECOVERY
    recovery = Recovery.SHORT_REST
    goes = 1

    @property
    def desc(self) -> str:
        slots = math.ceil(self.owner.level / 2)
        return f"""You can regain some of your magical energy by studying your spellbook. When you finish a Short 
        Rest, you can choose expended spell slots to recover. The spell slots can have a combined level equal to no 
        more than {slots}, and none of the slots can be level 6 or higher."""


#############################################################################
class Scholar(BaseFeature):
    tag = Feature.SCHOLAR
    hide = True
    _desc = """While studying magic, you also specialized in another field of study. Choose on of the following skills
    in which you have proficiency: Arcana, History, Investigation, Medicine, Nature, or Religion. You have Expertise
    in the chosen skill."""

    def __init__(self, skill: Skill):
        super().__init__()
        if skill not in (Skill.ARCANA, Skill.HISTORY, Skill.INVESTIGATION, Skill.MEDICINE, Skill.NATURE, Skill.RELIGION):
            raise InvalidOption("Scholar must be one of Arcana, History, Investigation, Medicine, Nature or Religion")
        self.skill = skill

    def mod_add_skill_expertise(self, character: "Character") -> Reason[Skill]:
        return Reason("Scholar", self.skill)


#############################################################################
class MemorizeSpell(BaseFeature):
    tag = Feature.MEMORIZE_SPELL
    _desc = """Whenever you finish a Short Rest, you can study your spellbook and replace one of the level 1+ Wizard 
    spells you have prepared for your Spellcasting feature with another level 1+ spell from the book."""


#############################################################################
class SignatureSpells(BaseFeature):
    tag = Feature.SIGNATURE_SPELLS
    _desc = """Choose two level 3 spells in your spellbook as your signature spells. You always have these spells 
    prepared, and you can cast each of them once at level 3 without expending a spell slot. When you do so, 
    you can't cast them in this way again until you finish a Short or Long Rest. To cast either spell at a higher 
    level, you must expend a spell slot."""


#############################################################################
class SpellMastery(BaseFeature):
    tag = Feature.SPELL_MASTERY
    _desc = """You have achieved such mastery over certain spells that you can cast them at will. Choose a level 1 
    and a level 2 spell in your spellbook that have a casting time of an action. You always have those spells 
    prepared, and you can cast them at their lowest level without expending a spell slot. To cast either spell 
    at a higher level vou must expend a spell slot.

    Whenever you finish a Long Rest, you can study your spellbook and replace one of those spells with an eligible 
    spell of the same level from the book."""


# EOF
