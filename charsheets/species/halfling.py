from charsheets.species import Species
from charsheets.ability import BaseAbility
from charsheets.constants import Ability


#############################################################################
class Halfling(Species):
    #########################################################################
    def species_abilities(self) -> set[Ability]:
        return {Ability.BRAVE, Ability.HALFLING_NIMBLENESS, Ability.LUCK, Ability.NATURALLY_STEALTHY}


#############################################################################
class AbilityBrave(BaseAbility):
    tag = Ability.BRAVE
    desc = """You have Advantage on saving throws you make to avoid or end the Frightened condition."""


#############################################################################
class AbilityHalflingNimbleness(BaseAbility):
    tag = Ability.HALFLING_NIMBLENESS
    desc = """You can move through the space of any creature that is a size larger than you, but you can't stop in
    the same space"""


#############################################################################
class AbilityLuck(BaseAbility):
    tag = Ability.LUCK
    desc = """When you roll a 1 on the d20 of a D20 Test, you can reroll the die, and you must use the new roll."""


#############################################################################
class AbilityNaturallyStealthy(BaseAbility):
    tag = Ability.NATURALLY_STEALTHY
    desc = """You can take the Hide action even when you are obscured only by a creature that is at least one size larger
    than you."""


# EOF


# EOF
