from typing import TYPE_CHECKING

from charsheets.features import Darkvision120
from charsheets.features.base_feature import BaseFeature
from charsheets.constants import Feature, DamageType
from charsheets.reason import Reason
from charsheets.species.base_species import BaseSpecies

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class Dwarf(BaseSpecies):
    #########################################################################
    def species_feature(self) -> set[BaseFeature]:
        return {Darkvision120(), DwarvenToughness(), DwarvenResilience(), Stonecunning()}


#############################################################################
class Stonecunning(BaseFeature):
    tag = Feature.STONE_CUNNING
    _desc = """As a Bonus Action, you gain Tremorsense with a range of 60 feet for 10 minutes. You must be on a stone 
    surface or touching a stone surface to use this Tremorsense. The stone can be natural or worked.
    
    You can use this Bonus Action a number of times equal to your Proficiency Bonus, and you regain expended uses 
    when you finish a Long Rest."""


#############################################################################
class DwarvenResilience(BaseFeature):
    tag = Feature.DWARVEN_RESILIENCE
    _desc = """You have Advantage on saving throws you make to avoid or
    end the Poisoned condition,."""

    def mod_add_damage_resistances(self, character: "Character") -> Reason[DamageType]:
        return Reason("Dwarven Resilience", DamageType.POISON)


#############################################################################
class DwarvenToughness(BaseFeature):
    tag = Feature.DWARVEN_TOUGHNESS
    _desc = """Your Hit Point maximum increases by 1, and it increases by 1 again whenever you gain a level."""
    hide = True

    def mod_hp_bonus(self, character: "Character") -> Reason[int]:
        return Reason[int]("Dwarven Toughness", character.level)


# EOF
