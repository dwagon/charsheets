from charsheets.ability import BaseAbility
from charsheets.constants import Ability


############################################################################
class AbilityImprovedCritical(BaseAbility):
    tag = Ability.IMPROVED_CRITICAL
    desc = "Your attack rolls with weapons and Unarmed Strikes can score a Critical Hit on a roll of 19 or 20 on the d20"


############################################################################
class AbilityRemarkableAthlete(BaseAbility):
    tag = Ability.REMARKABLE_ATHLETE
    desc = """Thanks to your athleticism, you have Advantage on Initiative rolls and Strength(Athletics) checks.

    In addition, immediately after you score a Critical Hit, you can move up to half your Speed without provoking
    Opportunity Attacks."""


# EOF
