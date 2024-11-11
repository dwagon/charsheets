from charsheets.ability import BaseAbility
from charsheets.constants import Ability


#############################################################################
class AbilityEldritchInvocation(BaseAbility):
    tag = Ability.ELDRITCH_INVOCATIONS
    desc = ""


#############################################################################
class AbilityPactMagic(BaseAbility):
    tag = Ability.PACT_MAGIC
    desc = """You know two Warlock cantrips"""


#############################################################################
class AbilityMagicalCunning(BaseAbility):
    tag = Ability.MAGICAL_CUNNING
    desc = """You can perform an esoteric rite for 1 minute. At the end of it, you regain expended Pact Magic spell
    slots but no more than a numer equal to half your maximum (round up). Once you use this feature, you can't do so
    again until you finish a Long Rest."""


# EOF
