from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.fighter import Fighter
from charsheets.constants import Ability


#################################################################################
class FighterChampion(Fighter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Champion"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {ImprovedCritical(), RemarkableAthlete()}
        abilities |= super().class_abilities()
        return abilities


############################################################################
class ImprovedCritical(BaseAbility):
    tag = Ability.IMPROVED_CRITICAL
    _desc = """Your attack rolls with weapons and Unarmed Strikes can score a Critical Hit on a roll of 19 or 20 on
    the d20"""


############################################################################
class RemarkableAthlete(BaseAbility):
    tag = Ability.REMARKABLE_ATHLETE
    _desc = """Thanks to your athleticism, you have Advantage on Initiative rolls and Strength(Athletics) checks.

    In addition, immediately after you score a Critical Hit, you can move up to half your Speed without provoking
    Opportunity Attacks."""


# EOF
