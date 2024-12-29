from charsheets.classes.druid import Druid
from charsheets.constants import Ability


#################################################################################
class CircleOfTheStarsDruid(Druid):
    _class_name = "Druid (Circle of the Stars)"

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities: set[Ability] = {Ability.STAR_MAP, Ability.STARRY_FORM}
        abilities |= super().class_abilities()
        return abilities
