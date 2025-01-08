from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Ability


#############################################################################
class Darkvision120(BaseAbility):
    tag = Ability.DARKVISION120
    _desc = """You have Darkvision with a range of 120 feet"""


#############################################################################
class Darkvision60(BaseAbility):
    tag = Ability.DARKVISION60
    _desc = """You have Darkvision with a range of 60 feet"""


#############################################################################
class ExtraAttack(BaseAbility):
    tag = Ability.EXTRA_ATTACK
    _desc = """You can attack twice instead of once whenever you take the Attack action on your turn."""


# EOF
