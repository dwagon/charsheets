from charsheets.abilities import WrathOfTheSea, AquaticAffinity
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.druid import Druid
from charsheets.spells import Spells


#################################################################################
class DruidCircleOfTheSea(Druid):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Druid (Circle of the Sea)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = set()
        abilities |= super().class_abilities()
        abilities |= {
            WrathOfTheSea(),
        }
        self.prepare_spells(Spells.FOG_CLOUD, Spells.GUST_OF_WIND, Spells.RAY_OF_FROST, Spells.SHATTER, Spells.THUNDERWAVE)
        if self.level >= 5:
            self.prepare_spells(Spells.LIGHTNING_BOLT, Spells.WATER_BREATHING)
        if self.level >= 6:
            abilities.add(AquaticAffinity())
        return abilities
