from enum import StrEnum, auto

from aenum import extend_enum
from charsheets.constants import Feature, Recovery
from charsheets.exception import InvalidOption
from charsheets.features.base_feature import BaseFeature
from charsheets.species.base_species import BaseSpecies

extend_enum(Feature, "GIANT_CLOUDS_JAUNT", "Cloud’s Jaunt")
extend_enum(Feature, "GIANT_FIRES_BURN", "Fire’s Burn")
extend_enum(Feature, "GIANT_FROSTS_CHILL", "Frost's Chill")
extend_enum(Feature, "GIANT_HILLS_TUMBLE", "Hill’s Tumble")
extend_enum(Feature, "GIANT_STONES_ENDURANCE", "Stone's Endurance")
extend_enum(Feature, "GIANT_STORMS_THUNDER", "Storm's Thunder")
extend_enum(Feature, "GIANT_ANCESTRY", "Giant Ancestry")


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
    def species_feature(self) -> set[BaseFeature]:
        features: set[BaseFeature] = {GiantAncestry()}
        match self.ancestry:
            case GiantsAncestry.CLOUD_GIANT:
                features.add(CloudsJaunt())
            case GiantsAncestry.FIRE_GIANT:
                features.add(FiresBurn())
            case GiantsAncestry.FROST_GIANT:
                features.add(FrostsChill())
            case GiantsAncestry.HILL_GIANT:
                features.add(HillsTumble())
            case GiantsAncestry.STORM_GIANT:
                features.add(StormsThunder())
            case GiantsAncestry.STONE_GIANT:
                features.add(StonesEndurance())
            case _:  # pragma: no coverage
                raise InvalidOption(f"Giant Ancestry {self.ancestry} not valid")
        return features

    #########################################################################
    @property
    def speed(self) -> int:
        return 35


#############################################################################
class CloudsJaunt(BaseFeature):
    tag = Feature.GIANT_CLOUDS_JAUNT
    recovery = Recovery.LONG_REST
    _desc = """As a Bonus Action, you magically teleport up to 30 feet to an unoccupied space you can see."""

    @property
    def goes(self) -> int:
        return self.owner.proficiency_bonus


#############################################################################
class FiresBurn(BaseFeature):
    tag = Feature.GIANT_FIRES_BURN
    recovery = Recovery.LONG_REST

    _desc = """When you hit a target with an attack roll and deal damage to it, you can also deal 1d10 Fire damage to 
    that target."""

    @property
    def goes(self) -> int:
        return self.owner.proficiency_bonus


#############################################################################
class FrostsChill(BaseFeature):
    tag = Feature.GIANT_FROSTS_CHILL
    recovery = Recovery.LONG_REST

    _desc = """ When you hit a target with an attack roll and deal damage to it, you can also deal 1d6 Cold damage to 
    that target and reduce its Speed by 10 feet until the start of your next turn."""

    @property
    def goes(self) -> int:
        return self.owner.proficiency_bonus


#############################################################################
class HillsTumble(BaseFeature):
    tag = Feature.GIANT_HILLS_TUMBLE
    recovery = Recovery.LONG_REST

    _desc = """When you hit a Large or smaller creature with an attack roll and deal damage to it, you can give that 
    target the Prone condition."""

    @property
    def goes(self) -> int:
        return self.owner.proficiency_bonus


#############################################################################
class StonesEndurance(BaseFeature):
    tag = Feature.GIANT_STONES_ENDURANCE
    recovery = Recovery.LONG_REST

    _desc = """When you take damage, you can take a Reaction to roll 1d12. Add your Constitution modifier to the 
    number rolled and reduce the damage by that total."""

    @property
    def goes(self) -> int:
        return self.owner.proficiency_bonus


#############################################################################
class StormsThunder(BaseFeature):
    tag = Feature.GIANT_STORMS_THUNDER
    recovery = Recovery.LONG_REST

    _desc = """When you take damage from a creature within 60 feet of you, you can take a Reaction to deal 1d8 Thunder damage to 
    that creature."""

    @property
    def goes(self) -> int:
        return self.owner.proficiency_bonus


#############################################################################
class GiantAncestry(BaseFeature):
    tag = Feature.GIANT_ANCESTRY
    recovery = Recovery.LONG_REST

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
            you have Advantage on Strength checks, and your Speed increases by 10 feet.\n\n"""

        ans += """Powerful Build. You have Advantage on any saving throw you make to end the Grappled condition. 
        You also count as one size larger when determining your carrying capacity."""

        return ans


# EOF
