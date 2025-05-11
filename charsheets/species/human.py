from typing import TYPE_CHECKING

from aenum import extend_enum
from charsheets.constants import Skill, Feature
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.species.base_species import BaseSpecies

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character

extend_enum(Feature, "RESOURCEFUL", "Resourceful")
extend_enum(Feature, "SKILLFUL", "Skillful")
extend_enum(Feature, "VERSATILE", "Versatile")


#############################################################################
class Resourceful(BaseFeature):
    tag = Feature.RESOURCEFUL
    _desc = """You gain Heroic Inspiration whenever you finish a Long Rest."""


#############################################################################
class Skillful(BaseFeature):
    tag = Feature.SKILLFUL
    _desc = """You gain proficiency in one skill of your choice."""
    hide = True

    #########################################################################
    def __init__(self, skill: Skill):
        super().__init__()
        self.skillful_skill = skill

    #########################################################################
    @property
    def desc(self) -> str:
        return f"You gained proficiency in {self.skillful_skill}"

    #########################################################################
    def mod_add_skill_proficiency(self, character: "Character") -> Reason[Skill]:
        return Reason("Skillful", self.skillful_skill)


#############################################################################
class Versatile(BaseFeature):
    tag = Feature.VERSATILE
    _desc = """You gain an origin feat of your choice"""
    hide = True

    #########################################################################
    def __init__(self, feat: BaseFeature):
        super().__init__()
        self.feat = feat


#############################################################################
class Human(BaseSpecies):
    #########################################################################
    def __init__(self, skillful: Skillful, versatile: Versatile):
        super().__init__()
        self.skillful = skillful
        self.versatile = versatile

    #########################################################################
    def species_feature(self) -> set[BaseFeature]:
        return {Resourceful(), self.skillful, self.versatile, self.versatile.feat}


# EOF
