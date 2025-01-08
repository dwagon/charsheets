from charsheets.abilities import CircleForms
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.druid import Druid
from charsheets.spells import Spells


#################################################################################
class DruidCircleOfTheMoon(Druid):
    _class_name = "Druid (Circle of the Moon)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = set()
        abilities |= super().class_abilities()
        abilities |= {CircleForms()}
        self.prepare_spells(Spells.CURE_WOUNDS, Spells.MOONBEAM, Spells.STARRY_WISP)
        if self.level >= 5:
            self.prepare_spells(Spells.CONJURE_ANIMALS)

        return abilities
