from charsheets.species import Species
from charsheets.ability import BaseAbility
from charsheets.constants import Ability


#############################################################################
class Dwarf(Species):
    #########################################################################
    def species_abilities(self) -> set[Ability]:
        return {Ability.DARKVISION120, Ability.DWARVEN_RESILIANCE, Ability.DWARVEN_TOUGHNESS, Ability.STONE_CUNNING}


#############################################################################
class AbilityStonecunning(BaseAbility):
    tag = Ability.STONE_CUNNING
    desc = """As a Bonus Action, you gain Tremorsense with a range of 60 feet for 10 minutes.
    You must be on a stone surface or touching a stone surface to use this Tremorsense. 
    The stone can be natural or worked. You can use this Bonus Action a number of times equal to your Proficiency Bonus,
     and you regain expended uses when you finish a Long Rest."""


#############################################################################
class AbilityDwarvenResilience(BaseAbility):
    tag = Ability.DWARVEN_RESILIANCE
    desc = """You have Resistance to Poison damage. You also have Advantage on saving throws you make to avoid or
    end the Poisoned condition,."""


#############################################################################
class AbilityDwarvenToughness(BaseAbility):
    tag = Ability.DWARVEN_TOUGHNESS
    desc = """Your Hit Point maximum increases by 1, and it increases by 1 again whenever you gain a level."""


# EOF
