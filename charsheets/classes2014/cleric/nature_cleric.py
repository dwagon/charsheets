from typing import cast, TYPE_CHECKING, Any

from aenum import extend_enum
from charsheets.classes2014.cleric.cleric import Cleric
from charsheets.constants import Proficiency, Skill, Feature
from charsheets.exception import InvalidOption
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell, is_cantrip

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter

extend_enum(Feature, "ACOLYTE_OF_NATURE14", "Acolyte of Nature")
extend_enum(Feature, "NATURE_DOMAIN_SPELLS14", "Nature Domain Spells")


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
