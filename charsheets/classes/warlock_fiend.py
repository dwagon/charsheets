from charsheets.constants import Ability
from charsheets.classes.warlock import Warlock
from charsheets.spells import Spells


#################################################################################
class FiendWarlock(Warlock):
    _class_name = "Warlock (Fiend Patron)"

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        self.prepare_spells(Spells.BURNING_HANDS, Spells.COMMAND, Spells.SCORCHING_RAY, Spells.SUGGESTION)

        abilities: set[Ability] = {Ability.DARK_ONES_BLESSING}
        abilities |= super().class_abilities()
        return abilities


# EOF
