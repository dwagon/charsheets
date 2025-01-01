from charsheets.abilities import AbjurationSavant, ArcaneWard
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.wizard import Wizard


#################################################################################
class Abjurer(Wizard):
    pass

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = set()
        abilities |= super().class_abilities()
        abilities |= {AbjurationSavant(), ArcaneWard()}
        return abilities


# EOF
