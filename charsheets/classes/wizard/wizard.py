from typing import Optional, Any

from aenum import extend_enum

from charsheets.character import Character
from charsheets.constants import Stat, Proficiency, Skill, Feature, Recovery
from charsheets.exception import InvalidOption
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason


#################################################################################
class Wizard(Character):
    _base_skill_proficiencies = {
        Skill.ARCANA,
        Skill.HISTORY,
        Skill.INSIGHT,
        Skill.INVESTIGATION,
        Skill.MEDICINE,
        Skill.NATURE,
        Skill.RELIGION,
    }

    #########################################################################
    @property
    def hit_dice(self) -> int:
        return 6

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.INTELLIGENCE

    #############################################################################
    def weapon_proficiency(self) -> Reason[Proficiency]:
        return Reason("Class Proficiency", Proficiency.SIMPLE_WEAPONS)

    #############################################################################
    def armour_proficiency(self) -> Reason[Proficiency]:
        return Reason()

    #############################################################################
    def saving_throw_proficiency(self, stat: Stat) -> bool:
        return stat in (Stat.INTELLIGENCE, Stat.WISDOM)

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {RitualAdept()}
        abilities.add(ArcaneRecovery())

        if self.level >= 5:
            abilities.add(MemorizeSpell())

        return abilities

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
            16: [4, 3, 3, 3, 2, 1, 0, 1, 0],
            17: [4, 3, 3, 3, 2, 1, 0, 1, 1],
            18: [4, 3, 3, 3, 3, 1, 1, 1, 1],
            19: [4, 3, 3, 3, 3, 2, 1, 1, 1],
            20: [4, 3, 3, 3, 3, 2, 2, 1, 1],
        }[self.level][spell_level - 1]

    #############################################################################
    def max_spell_level(self) -> int:
        return min(9, ((self.level + 1) // 2))

    #############################################################################
    def level2(self, **kwargs: Any):
        if "scholar" not in kwargs:
            raise InvalidOption("Level 2 Wizards get Scholar: level2(scholar=Scholar(...))")
        self.add_feature(kwargs["scholar"])
        super().level2(**kwargs)


extend_enum(Feature, "ARCANE_RECOVERY", "Arcane Recovery")
extend_enum(Feature, "MEMORIZE_SPELL", "Memorize Spell")
extend_enum(Feature, "RITUAL_ADEPT", "Ritual Adept")
extend_enum(Feature, "SCHOLAR", "Scholar")


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
        slots = self.owner.level // 2
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


# EOF
