from charsheets.abilities import StepsOfTheFey
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.warlock import Warlock
from charsheets.spells import Spells


#################################################################################
class WarlockArchFey(Warlock):
    _class_name = "Warlock (Archfey Patron)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        self.prepare_spells(Spells.CALM_EMOTIONS, Spells.FAERIE_FIRE, Spells.MISTY_STEP, Spells.PHANTASMAL_FORCE, Spells.SLEEP)
        if self.level >= 5:
            self.prepare_spells(Spells.BLINK, Spells.PLANT_GROWTH)
        abilities: set[BaseAbility] = set()
        abilities |= super().class_abilities()
        abilities |= {StepsOfTheFey()}
        return abilities


# EOF
