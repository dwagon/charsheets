from charsheets.abilities import DraconicResilience, DraconicSpells
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.sorcerer import Sorcerer


#################################################################################
class SorcererDraconic(Sorcerer):
    pass

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {DraconicResilience(), DraconicSpells()}
        abilities |= super().class_abilities()

        return abilities


# EOF
