from charsheets.abilities import ClockworkSpells, RestoreBalance
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.sorcerer import Sorcerer


#################################################################################
class SorcererClockwork(Sorcerer):
    pass

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {ClockworkSpells(), RestoreBalance()}
        abilities |= super().class_abilities()

        return abilities


# EOF
