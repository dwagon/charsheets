from charsheets.abilities import LandsAid, LandSpellArid, LandSpellTropical, LandSpellPolar, LandSpellTemperate, NaturalRecovery
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.druid import Druid


#################################################################################
class DruidCircleOfTheLand(Druid):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Druid (Circle of the Land)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        """Only one of these should be active at one time"""
        abilities: set[BaseAbility] = set()
        abilities |= super().class_abilities()
        abilities |= {
            LandsAid(),
            LandSpellArid(),
            LandSpellTropical(),
            LandSpellPolar(),
            LandSpellTemperate(),
        }
        if self.level >= 6:
            abilities.add(NaturalRecovery())
        return abilities
