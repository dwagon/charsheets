from typing import Any

from aenum import extend_enum

from charsheets.classes.ranger import Ranger
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature

extend_enum(Feature, "DEFENSIVE_TACTICS", "Defensive Tactics")
extend_enum(Feature, "HUNTERS_LORE", "Hunters Lore")
extend_enum(Feature, "HUNTERS_PREY", "Hunters Prey")
extend_enum(Feature, "SUPERIOR_HUNTERS_PREY", "Superior Hunters Prey")


#################################################################################
class RangerHunter(Ranger):

    #############################################################################
    def level3(self, **kwargs: Any):
        assert self.character is not None
        self.add_feature(HuntersLore())
        self.add_feature(HuntersPrey())

    #############################################################################
    def level7(self, **kwargs: Any):
        assert self.character is not None
        self.add_feature(DefensiveTactics())

    #############################################################################
    def level11(self, **kwargs: Any):
        assert self.character is not None
        self.add_feature(SuperiorHuntersPrey())


#############################################################################
class HuntersPrey(BaseFeature):
    tag = Feature.HUNTERS_PREY
    _desc = """You gain one of the following. Whenever you finish a Long Rest you can replace the option.

    Colossus Slayer. Your tenacity can wear down even the most resilient foes. When you hit a creature with a weapon,
    the weapon deals an extra 1d8 damage to the target if its missing any of its Hit Points. You can deal this extra 
    damage only once per turn.

    Horde Breaker. Once on each of your turns when you make an attack with a weapon, you can make another attack with 
    the same weapon against a different creature that is within 5 feet of the original target, that is within the 
    weapon's range, and you haven't attacked this turn.
    """


#############################################################################
class HuntersLore(BaseFeature):
    tag = Feature.HUNTERS_LORE
    _desc = """While a creature is marked by your Hunter’s Mark, you know whether that creature has any
    Immunities, Resistances, or Vulnerabilities, and if the creature has any, you know what they are."""


#############################################################################
class DefensiveTactics(BaseFeature):
    tag = Feature.DEFENSIVE_TACTICS
    _desc = """You gain one of the following feature options of your choice. Whenever you finish a Short or Long 
    Rest, you can replace the chosen option with the other one.
    
    Escape the Horde. Opportunity Attacks have disadvantage against you.
    
    Multiattack Defense. When a creature hits you with an attack roll, that creature has Disadvantage on all other 
    attack rolls against you this turn."""


#############################################################################
class SuperiorHuntersPrey(BaseFeature):
    tag = Feature.SUPERIOR_HUNTERS_PREY
    _desc = """Once per turn when you deal damage to a creature marked by your 'Hunter's Mark', you can also deal that 
    spell's extra damage to a different creature that you can see within 30 feet of the first creature."""


# EOF
