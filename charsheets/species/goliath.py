from enum import StrEnum, auto

from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Ability
from charsheets.exception import InvalidOption
from charsheets.species.base_species import BaseSpecies


#############################################################################
class GiantsAncestry(StrEnum):
    NONE = auto()
    CLOUD_GIANT = auto()
    FIRE_GIANT = auto()
    FROST_GIANT = auto()
    HILL_GIANT = auto()
    STONE_GIANT = auto()
    STORM_GIANT = auto()


#############################################################################
class Goliath(BaseSpecies):
    #########################################################################
    def __init__(self, ancestry: GiantsAncestry):
        super().__init__()
        self.ancestry = ancestry

    #########################################################################
    def species_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {GiantAncestry()}
        match self.ancestry:
            case GiantsAncestry.CLOUD_GIANT:
                abilities.add(CloudsJaunt())
            case GiantsAncestry.FIRE_GIANT:
                abilities.add(FiresBurn())
            case GiantsAncestry.FROST_GIANT:
                abilities.add(FrostsChill())
            case GiantsAncestry.HILL_GIANT:
                abilities.add(HillsTumble())
            case GiantsAncestry.STORM_GIANT:
                abilities.add(StormsThunder())
            case GiantsAncestry.STONE_GIANT:
                abilities.add(StonesEndurance())
            case _:  # pragma: no coverage
                raise InvalidOption(f"Giant Ancestry {self.ancestry} not valid")
        return abilities

    #########################################################################
    @property
    def speed(self) -> int:
        return 35


#############################################################################
class CloudsJaunt(BaseAbility):
    tag = Ability.GIANT_CLOUDS_JAUNT
    _desc = """You regain all expended uses when you finish a Long Rest.
    
    As a Bonus Action, you magically teleport up to 30 feet to an unoccupied space you can see."""

    @property
    def goes(self) -> int:
        return self.owner.proficiency_bonus


#############################################################################
class FiresBurn(BaseAbility):
    tag = Ability.GIANT_FIRES_BURN

    _desc = """You regain all expended uses when you finish a Long Rest.
    
    When you hit a target with an attack roll and deal damage to it, you can also deal 1d10 Fire damage to 
    that target."""

    @property
    def goes(self) -> int:
        return self.owner.proficiency_bonus


#############################################################################
class FrostsChill(BaseAbility):
    tag = Ability.GIANT_FROSTS_CHILL

    _desc = """You regain all expended uses when you finish a Long Rest.
    
    When you hit a target with an attack roll and deal damage to it, you can also deal 1d6 Cold damage to 
    that target and reduce its Speed by 10 feet until the start of your next turn."""

    @property
    def goes(self) -> int:
        return self.owner.proficiency_bonus


#############################################################################
class HillsTumble(BaseAbility):
    tag = Ability.GIANT_HILLS_TUMBLE

    _desc = """You regain all expended uses when you finish a Long Rest.
    
    When you hit a Large or smaller creature with an attack roll and deal damage to it, you can give that 
    target the Prone condition."""

    @property
    def goes(self) -> int:
        return self.owner.proficiency_bonus


#############################################################################
class StonesEndurance(BaseAbility):
    tag = Ability.GIANT_STONES_ENDURANCE

    _desc = """You regain all expended uses when you finish a Long Rest.
    
    When you take damage, you can take a Reaction to roll 1d12. Add your Constitution modifier to the 
    number rolled and reduce the damage by that total."""

    @property
    def goes(self) -> int:
        return self.owner.proficiency_bonus


#############################################################################
class StormsThunder(BaseAbility):
    tag = Ability.GIANT_STORMS_THUNDER
    _desc = """You regain all expended uses when you finish a Long Rest.
     
    When you take damage from a creature within 60 feet of you, you can take a Reaction to deal 1d8 Thunder damage to 
    that creature."""

    @property
    def goes(self) -> int:
        return self.owner.proficiency_bonus


#############################################################################
class GiantAncestry(BaseAbility):
    tag = Ability.GIANT_ANCESTRY

    @property
    def goes(self) -> int:
        if self.owner.level >= 5:
            return 1
        return 0

    @property
    def desc(self) -> str:
        ans = ""
        if self.owner.level >= 5:
            ans += """You can change your size to Large as a Bonus Action if you're in a big enough space. This 
            transformation lasts for 10 minutes or until you end it (no action required). For that duration, 
            you have Advantage on Strength checks, and your Speed increases by 10 feet. Once you use this trait, 
            you can’t use it again until you finish a Long Rest.\n\n"""

        ans += """Powerful Build. You have Advantage on any saving throw you make to end the Grappled condition. 
        You also count as one size larger when determining your carrying capacity."""

        return ans


# EOF
