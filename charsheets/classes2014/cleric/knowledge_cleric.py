from typing import TYPE_CHECKING, Any

from aenum import extend_enum
from charsheets.classes2014.cleric.cleric import Cleric
from charsheets.constants import Skill, Feature, Language
from charsheets.exception import InvalidOption
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter

extend_enum(Feature, "BLESSINGS_OF_KNOWLEDGE14", "Blessings of Knowledge")
extend_enum(Feature, "KNOWLEDGE_DOMAIN_SPELLS14", "Knowledge Domain Spells")


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
