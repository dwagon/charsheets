from charsheets.abilities import LandsAid, LandSpellArid, LandSpellTropical, LandSpellPolar, LandSpellTemperate
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.druid import Druid


#################################################################################
class CircleOfTheLandDruid(Druid):
    _class_name = "Druid (Circle of the Land)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = set()
        abilities |= super().class_abilities()
        abilities |= {
            LandsAid(),
            LandSpellArid(),
            LandSpellTropical(),
            LandSpellPolar(),
            LandSpellTemperate(),
        }
        return abilities
