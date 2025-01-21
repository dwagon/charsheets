from typing import TYPE_CHECKING

from charsheets.features.base_feature import BaseFeature
from charsheets.classes.ranger import Ranger
from charsheets.constants import Feature

if TYPE_CHECKING:  # pragma: no coverage
    pass


#################################################################################
class RangerHunter(Ranger):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Ranger (Hunter)"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = {HuntersLore(), HuntersPrey()}
        abilities |= super().class_features()
        if self.level >= 7:
            abilities |= {DefensiveTactics()}
        return abilities


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
    _desc = """You can call on the forces of nature to reveal certain strengths and weaknesses of your prey.
    While a creature is marked by your Hunter’s Mark, you know whether that creature has any
    Immunities, Resistances, or Vulnerabilities, and if the creature has any, you know what they are."""


#############################################################################
class DefensiveTactics(BaseFeature):
    tag = Feature.DEFENSIVE_TACTICS
    _desc = """You gain one of the following feature options of your choice. Whenever you finish a Short or Long 
    Rest, you can replace the chosen option with the other one.
    
    Escape the Horde. Opportunity Attacks have disadvantage against you.
    
    Multiattack Defense. When a creature hits you with an attack roll, that creature has Disadvantage on all other 
    attack rolls against you this turn."""


# EOF
