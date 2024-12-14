from charsheets.classes.druid import Druid
from charsheets.constants import Ability


#################################################################################
class CircleOfTheLandDruid(Druid):
    _class_name = "Druid (Circle of the Land)"

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities: set[Ability] = set()
        abilities |= super().class_abilities()
        abilities |= {
            Ability.LANDS_AID,
            Ability.LAND_SPELL_ARID,
            Ability.LAND_SPELL_TROPICAL,
            Ability.LAND_SPELL_POLAR,
            Ability.LAND_SPELL_TEMPERATE,
        }
        return abilities
