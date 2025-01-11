from typing import TYPE_CHECKING

from aenum import extend_enum

from charsheets.abilities.base_ability import BaseAbility
from charsheets.constants import Ability, Sense
from charsheets.reason import Reason
from charsheets.species.base_species import BaseSpecies
from charsheets.abilities import Darkvision60

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
    def species_abilities(self) -> set[BaseAbility]:
        results: set[BaseAbility] = {
            Amphibious(),
            Darkvision60(),
            SpeakWithFish(),
            Swim(),
            Slippery(),
            DarkvisionUnderwater120(),
        }

        return results


#############################################################################
extend_enum(Ability, "AMPHIBIOUS", "Amphibious")
extend_enum(Ability, "SPEAK_WITH_FISH", "Speak with Fish")
extend_enum(Ability, "SLIPPERY", "Slippery")
extend_enum(Ability, "OTHERWORLDLY_PERCEPTION", "Otherworldly Perception")
extend_enum(Ability, "SWIM", "Swim")
extend_enum(Ability, "DARKVISION_UNDERWATER120", "Darkvision Underwater 120")


#############################################################################
class Amphibious(BaseAbility):
    tag = Ability.AMPHIBIOUS
    _desc = """You can breathe air and water."""


#############################################################################
class SpeakWithFish(BaseAbility):
    tag = Ability.SPEAK_WITH_FISH
    _desc = """As a bonus action you can cast Speak With Animals that works only on aquatic or underwater animals.
    You can use this Bonus Action a number of times equal to your Proficiency Bonus, and you regain all expended uses
    when you finish a Long Rest."""


#############################################################################
class Slippery(BaseAbility):
    tag = Ability.SLIPPERY
    _desc = """You have advantage on ability checks and saving throws made to escape a grapple."""


#############################################################################
class OtherworldlyPerception(BaseAbility):
    tag = Ability.OTHERWORLDLY_PERCEPTION
    _desc = """As a bonus action you can sense invisible creatures within 30 feet and pinpoint
    such a creature that is moving."""


#############################################################################
class Swim(BaseAbility):
    tag = Ability.SWIM
    _desc = """Swim 30 feet"""

    def mod_swim_movement(self, character: "Character") -> int:
        return 30


extend_enum(Sense, "DARKVISION_UNDERWATER120", "Darkvision Underwater 120'")


#############################################################################
class DarkvisionUnderwater120(BaseAbility):
    tag = Ability.DARKVISION_UNDERWATER120
    _desc = """Darkvision Underwater for 120 feet"""
    hide = True

    def mod_add_sense(self, character: "Character") -> Reason[Sense]:
        return Reason("KuaToa", Sense.DARKVISION_UNDERWATER120)


# EOF
