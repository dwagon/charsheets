from charsheets.abilities import DarkOnesBlessing
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.warlock import Warlock
from charsheets.spells import Spells


#################################################################################
class WarlockFiend(Warlock):
    _class_name = "Warlock (Fiend Patron)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        self.prepare_spells(Spells.BURNING_HANDS, Spells.COMMAND, Spells.SCORCHING_RAY, Spells.SUGGESTION)

        abilities: set[BaseAbility] = {DarkOnesBlessing()}
        abilities |= super().class_abilities()
        return abilities


# EOF
