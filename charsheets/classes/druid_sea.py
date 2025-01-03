from charsheets.abilities import WrathOfTheSea
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.druid import Druid
from charsheets.spells import Spells


#################################################################################
class CircleOfTheSeaDruid(Druid):
    _class_name = "Druid (Circle of the Sea)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = set()
        abilities |= super().class_abilities()
        abilities |= {
            WrathOfTheSea(),
        }
        self.prepare_spells(Spells.FOG_CLOUD, Spells.GUST_OF_WIND, Spells.RAY_OF_FROST, Spells.SHATTER, Spells.THUNDERWAVE)
        return abilities
