from typing import Any

from aenum import extend_enum

from charsheets.classes.fighter import Fighter
from charsheets.constants import Feature
from charsheets.exception import InvalidOption
from charsheets.features.base_feature import BaseFeature

extend_enum(Feature, "HEROIC_WARRIOR", "Heroic Warrior")
extend_enum(Feature, "IMPROVED_CRITICAL", "Improved Critical")
extend_enum(Feature, "REMARKABLE_ATHLETE", "Remarkable Athlete")


#################################################################################
class FighterChampion(Fighter):
    _class_name = "Fighter (Champion)"

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(ImprovedCritical())
        self.add_feature(RemarkableAthlete())

    #############################################################################
    def level7(self, **kwargs: Any):
        if "style" not in kwargs:
            raise InvalidOption("Level 7 Champion specify another fighting style with 'style=xxx'")
        self.fighting_style(kwargs["style"])

    #############################################################################
    def level10(self, **kwargs: Any):
        self.add_feature(HeroicWarrior())


############################################################################
class ImprovedCritical(BaseFeature):
    tag = Feature.IMPROVED_CRITICAL
    _desc = """Your attack rolls with weapons and Unarmed Strikes can score a Critical Hit on a roll of 19 or 20 on
    the d20"""


############################################################################
class RemarkableAthlete(BaseFeature):
    tag = Feature.REMARKABLE_ATHLETE
    _desc = """Thanks to your athleticism, you have Advantage on Initiative rolls and Strength(Athletics) checks.

    In addition, immediately after you score a Critical Hit, you can move up to half your Speed without provoking
    Opportunity Attacks."""


############################################################################
class HeroicWarrior(BaseFeature):
    tag = Feature.HEROIC_WARRIOR
    _desc = "During combat, you can give yourself Heroic Inspiration whenever you start your turn without it."


# EOF
