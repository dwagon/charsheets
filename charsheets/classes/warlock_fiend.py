from charsheets.abilities import DarkOnesBlessing, DarkOnesOwnLuck
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.warlock import Warlock
from charsheets.spells import Spells


#################################################################################
class WarlockFiend(Warlock):
    _class_name = "Warlock (Fiend Patron)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {DarkOnesBlessing()}
        abilities |= super().class_abilities()

        self.prepare_spells(Spells.BURNING_HANDS, Spells.COMMAND, Spells.SCORCHING_RAY, Spells.SUGGESTION)
        if self.level >= 5:
            self.prepare_spells(Spells.FIREBALL, Spells.STINKING_CLOUD)
        if self.level >= 6:
            abilities |= {DarkOnesOwnLuck()}
        return abilities


# EOF
