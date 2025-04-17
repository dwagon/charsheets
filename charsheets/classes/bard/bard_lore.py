from typing import TYPE_CHECKING, Any

from aenum import extend_enum  # type: ignore

from charsheets.classes.bard import Bard
from charsheets.constants import Feature, Skill
from charsheets.exception import InvalidOption
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character

extend_enum(Feature, "BONUS_PROFICIENCIES", "Bonus Proficiencies")
extend_enum(Feature, "CUTTING_WORDS", "Cutting Words")
extend_enum(Feature, "MAGICAL_DISCOVERIES", "Magical Discoveries")
extend_enum(Feature, "PEERLESS_SKILL", "Peerless Skill")


#################################################################################
class BardLoreCollege(Bard):
    _class_name = "Lore College Bard"
    _sub_class = True

    #############################################################################
    def level3(self, **kwargs: Any):
        if "bonus" not in kwargs:
            raise InvalidOption("Level 3 Lore Bards get Bonus Proficiencies: level3(bonus=BonusProficiencies(...))")
        self.add_feature(kwargs["bonus"])
        self.add_feature(CuttingWords())

    #############################################################################
    def level6(self, **kwargs: Any):
        if "bonus" not in kwargs:
            raise InvalidOption("Level 6 Lore Bards get Magical Discoveries: level6(bonus=MagicalDiscoveries(...))")
        self.add_feature(kwargs["bonus"])

    #############################################################################
    def level14(self, **kwargs: Any):
        self.add_feature(PeerlessSkill())


#################################################################################
class BonusProficiencies(BaseFeature):
    """You gain proficiency with three skills of your choice."""

    tag = Feature.BONUS_PROFICIENCIES
    hide = True
    _desc = """You gain proficiency with three skills of your choice."""

    def __init__(self, *skills: Skill):
        self.skills = skills

    def mod_add_skill_proficiency(self, character: "Character") -> Reason[Skill]:
        return Reason("Bonus Proficiencies", *self.skills)


#################################################################################
class CuttingWords(BaseFeature):
    tag = Feature.CUTTING_WORDS
    _desc = """When a creature that you can see within 60 feet of yourself makes a damage roll or succeeds 
    on an ability check or attack roll, you can take a Reaction to expend one use of your Bardic Inspiration; roll 
    your Bardic Inspiration die, and subtract the number rolled from the creature's roll, reducing the damage or 
    potentially turning the success into a failure."""


#################################################################################
class MagicalDiscoveries(BaseFeature):
    tag = Feature.MAGICAL_DISCOVERIES
    hide = True
    _desc = """You learn two spells of your choice. These spells can come from the Cleric, Druid, or Wizard spell 
    list or any combination thereof. A spell you choose must be a cantrip or a spell for which you have spell slots, 
    as shown in the Bard Features table."""

    def __init__(self, spell1: Spell, spell2: Spell):
        self.spells = [spell1, spell2]

    def mod_add_known_spells(self, character: "Character") -> Reason[Spell]:
        return Reason("Magical Discoveries", *self.spells)


#################################################################################
class PeerlessSkill(BaseFeature):
    tag = Feature.PEERLESS_SKILL
    _desc = """When you make an ability check or attack roll and fail, you can expend one use of Bardic Inspiration; 
    roll the Bardic Inspiration die, and add the number rolled to the d20, potentially turning a failure into a 
    success. On a failure, the Bardic Inspiration isn't expended."""


# EOF
