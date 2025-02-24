from typing import TYPE_CHECKING, Any

from charsheets.classes.bard import Bard
from charsheets.constants import Feature, Skill
from charsheets.exception import InvalidOption
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#################################################################################
class BardLoreCollege(Bard):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Bard (College of Lore)"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {BonusProficiencies(), CuttingWords()}
        abilities |= super().class_features()

        return abilities

    #############################################################################
    def level3(self, **kwargs: Any):
        if "bonus" not in kwargs:
            raise InvalidOption("Level 3 Lore Bards get Bonus Proficiencies: level3(bonus=BonusProficiencies(...))")
        self.add_feature(kwargs["bonus"])
        self._add_level(3, **kwargs)


#################################################################################
class BonusProficiencies(BaseFeature):
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


# EOF
