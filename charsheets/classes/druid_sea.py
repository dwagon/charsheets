from charsheets.classes.druid import Druid
from charsheets.constants import Ability
from charsheets.spells import Spells


#################################################################################
class CircleOfTheSeaDruid(Druid):
    _class_name = "Druid (Circle of the Sea)"

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities: set[Ability] = set()
        abilities |= super().class_abilities()
        abilities |= {
            Ability.WRATH_OF_THE_SEA,
        }
        self.prepare_spells(Spells.FOG_CLOUD, Spells.GUST_OF_WIND, Spells.RAY_OF_FROST, Spells.SHATTER, Spells.THUNDERWAVE)
        return abilities
