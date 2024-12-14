from charsheets.classes.druid import Druid
from charsheets.constants import Ability
from charsheets.spells import Spells


#################################################################################
class CircleOfTheMoonDruid(Druid):
    _class_name = "Druid (Circle of the Moon)"

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities: set[Ability] = set()
        abilities |= super().class_abilities()
        abilities |= {Ability.CIRCLE_FORMS}
        self.prepare_spells(Spells.CURE_WOUNDS, Spells.MOONBEAM, Spells.STARRY_WISP)

        return abilities
