from typing import Any

from charsheets.features.base_feature import BaseFeature
from charsheets.classes.fighter import Fighter
from charsheets.constants import Feature
from charsheets.exception import InvalidOption


#################################################################################
class FighterChampion(Fighter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Champion"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {ImprovedCritical(), RemarkableAthlete()}
        abilities |= super().class_features()
        return abilities

    #############################################################################
    def level7(self, **kwargs: Any):
        self._add_level(7, **kwargs)
        if "style" not in kwargs:
            raise InvalidOption("Level 7 Champion specify another fighting style with 'style=xxx'")
        self.fighting_style(kwargs["style"])


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


# EOF
