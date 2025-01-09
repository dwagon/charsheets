from charsheets.abilities import DraconicResilience
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.sorcerer import Sorcerer
from charsheets.spells import Spells


#################################################################################
class SorcererDraconic(Sorcerer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Draconic Sorceror"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {DraconicResilience()}
        abilities |= super().class_abilities()
        self.prepare_spells(Spells.ALTER_SELF, Spells.CHROMATIC_ORB, Spells.COMMAND)
        if self.level >= 5:
            self.prepare_spells(Spells.FEAR, Spells.FLY)

        return abilities


# EOF
