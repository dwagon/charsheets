from charsheets.abilities import AbjurationSavant, ArcaneWard, ProjectedWard
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.wizard import Wizard


#################################################################################
class WizardAbjurer(Wizard):
    pass

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {AbjurationSavant(), ArcaneWard()}
        abilities |= super().class_abilities()
        if self.level >= 6:
            abilities |= {ProjectedWard()}
        return abilities


# EOF
