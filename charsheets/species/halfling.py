from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Ability
from charsheets.species.base_species import BaseSpecies


#############################################################################
class Halfling(BaseSpecies):
    #########################################################################
    def species_abilities(self) -> set[BaseAbility]:
        return {Brave(), HalflingNimbleness(), Luck(), NaturallyStealthy()}


#############################################################################
class Brave(BaseAbility):
    tag = Ability.BRAVE
    _desc = """You have Advantage on saving throws you make to avoid or end the Frightened condition."""


#############################################################################
class HalflingNimbleness(BaseAbility):
    tag = Ability.HALFLING_NIMBLENESS
    _desc = """You can move through the space of any creature that is a size larger than you, but you can't stop in
    the same space"""


#############################################################################
class Luck(BaseAbility):
    tag = Ability.LUCK
    desc = """When you roll a 1 on the d20 of a D20 Test, you can reroll the die, and you must use the new roll."""


#############################################################################
class NaturallyStealthy(BaseAbility):
    tag = Ability.NATURALLY_STEALTHY
    _desc = """You can take the Hide action even when you are obscured only by a creature that is at least one size larger
    than you."""


# EOF


# EOF
