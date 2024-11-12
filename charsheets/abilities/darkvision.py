from charsheets.ability import BaseAbility
from charsheets.constants import Ability


#############################################################################
class AbilityDarkvision120(BaseAbility):
    tag = Ability.DARKVISION120
    desc = """You have Darkvision with a range of 120 feet"""


#############################################################################
class AbilityDarkvision60(BaseAbility):
    tag = Ability.DARKVISION60
    desc = """You have Darkvision with a range of 60 feet"""


# EOF
