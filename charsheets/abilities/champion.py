from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Ability


############################################################################
class ImprovedCritical(BaseAbility):
    tag = Ability.IMPROVED_CRITICAL
    _desc = "Your attack rolls with weapons and Unarmed Strikes can score a Critical Hit on a roll of 19 or 20 on the d20"


############################################################################
class RemarkableAthlete(BaseAbility):
    tag = Ability.REMARKABLE_ATHLETE
    _desc = """Thanks to your athleticism, you have Advantage on Initiative rolls and Strength(Athletics) checks.

    In addition, immediately after you score a Critical Hit, you can move up to half your Speed without provoking
    Opportunity Attacks."""


# EOF
