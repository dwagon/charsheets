from typing import TYPE_CHECKING

from charsheets.abilities import Darkvision120
from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Ability
from charsheets.reason import Reason
from charsheets.species.base_species import BaseSpecies

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class Dwarf(BaseSpecies):
    #########################################################################
    def species_abilities(self) -> set[BaseAbility]:
        return {Darkvision120(), DwarvenToughness(), DwarvenResilience(), Stonecunning()}


#############################################################################
class Stonecunning(BaseAbility):
    tag = Ability.STONE_CUNNING
    _desc = """As a Bonus Action, you gain Tremorsense with a range of 60 feet for 10 minutes.
    You must be on a stone surface or touching a stone surface to use this Tremorsense. 
    The stone can be natural or worked. You can use this Bonus Action a number of times equal to your Proficiency Bonus,
     and you regain expended uses when you finish a Long Rest."""


#############################################################################
class DwarvenResilience(BaseAbility):
    tag = Ability.DWARVEN_RESILIENCE
    _desc = """You have Resistance to Poison damage. You also have Advantage on saving throws you make to avoid or
    end the Poisoned condition,."""


#############################################################################
class DwarvenToughness(BaseAbility):
    tag = Ability.DWARVEN_TOUGHNESS
    _desc = """Your Hit Point maximum increases by 1, and it increases by 1 again whenever you gain a level."""
    hide = True

    def mod_hp_bonus(self, character: "Character") -> Reason[int]:
        return Reason[int]("Dwarven Toughness", character.level)


# EOF
