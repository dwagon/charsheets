from charsheets.constants import Ability
from charsheets.species import Species


#############################################################################
class Kuatoa(Species):
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
    def species_abilities(self) -> set[Ability]:
        results: set[Ability] = {
            Ability.AMPHIBIOUS,
            Ability.DARKVISION60,
            Ability.SPEAK_WITH_FISH,
            Ability.SWIM,
            Ability.SLIPPERY,
            Ability.DARKVISION_UNDERWATER120,
        }

        return results


# EOF
