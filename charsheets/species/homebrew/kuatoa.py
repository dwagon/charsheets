from typing import TYPE_CHECKING

from aenum import extend_enum

from charsheets.constants import Feature, Sense, Recovery
from charsheets.features import Darkvision60
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.species.base_species import BaseSpecies

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class Kuatoa(BaseSpecies):
    """## Kua-Toa Traits

    **Creature Type:** Humanoid
    **Size:** Medium (about 3-4 feet tall)
    **Speed:** 30 feet, Swim 30 feet

    As a Kua-Toa, you have these special traits.
    ** _Amphibious._ ** You can breathe air and water.
    **_Darkvision._** You have Darkvision with a range of 60 feet, or 120 feet underwater.
    **_Otherworldy Perception._** As a bonus action you can sense invisible creatures within 30 feet and pinpoint such
        a creature that is moving.
    ** _Slippery._** You have advantage on ability checks and saving throws made to escape a grapple.
    ** _Speak with Fish._** As a bonus action you can cast [[speak-with-animals]] that works only on aquatic or
        underwater animals. You can use this Bonus Action a number of times equal to your Proficiency Bonus, and you
        regain all expended uses when you finish a Long Rest.
    """

    #########################################################################
    def species_feature(self) -> set[BaseFeature]:
        results: set[BaseFeature] = {
            Amphibious(),
            Darkvision60(),
            SpeakWithFish(),
            Swim(),
            Slippery(),
            DarkvisionUnderwater120(),
        }

        return results


#############################################################################
extend_enum(Feature, "AMPHIBIOUS", "Amphibious")
extend_enum(Feature, "SPEAK_WITH_FISH", "Speak with Fish")
extend_enum(Feature, "SLIPPERY", "Slippery")
extend_enum(Feature, "OTHERWORLDLY_PERCEPTION", "Otherworldly Perception")
extend_enum(Feature, "SWIM", "Swim")
extend_enum(Feature, "DARKVISION_UNDERWATER120", "Darkvision Underwater 120")


#############################################################################
class Amphibious(BaseFeature):
    tag = Feature.AMPHIBIOUS
    _desc = """You can breathe air and water."""


#############################################################################
class SpeakWithFish(BaseFeature):
    tag = Feature.SPEAK_WITH_FISH
    recovery = Recovery.LONG_REST
    _desc = """As a Bonus action you can cast Speak With Animals that works only on aquatic or underwater 
        animals."""

    @property
    def goes(self) -> int:
        return self.owner.proficiency_bonus


#############################################################################
class Slippery(BaseFeature):
    tag = Feature.SLIPPERY
    _desc = """You have advantage on ability checks and saving throws made to escape a grapple."""


#############################################################################
class OtherworldlyPerception(BaseFeature):
    tag = Feature.OTHERWORLDLY_PERCEPTION
    _desc = """As a Bonus action you can sense invisible creatures within 30 feet and pinpoint
    such a creature that is moving."""


#############################################################################
class Swim(BaseFeature):
    tag = Feature.SWIM
    _desc = """Swim 30 feet"""

    def mod_swim_movement(self, character: "Character") -> Reason[int]:
        return Reason[int]("Swim", 30)


extend_enum(Sense, "DARKVISION_UNDERWATER120", "Darkvision Underwater 120'")


#############################################################################
class DarkvisionUnderwater120(BaseFeature):
    tag = Feature.DARKVISION_UNDERWATER120
    _desc = """Darkvision Underwater for 120 feet"""
    hide = True

    def mod_add_sense(self, character: "Character") -> Reason[Sense]:
        return Reason("KuaToa", Sense.DARKVISION_UNDERWATER120)


# EOF
