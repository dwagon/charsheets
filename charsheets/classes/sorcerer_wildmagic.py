from charsheets.abilities import WildMagicSurge, TidesOfChaos
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.sorcerer import Sorcerer


#################################################################################
class SorcererWildMagic(Sorcerer):
    pass

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {WildMagicSurge(), TidesOfChaos()}
        abilities |= super().class_abilities()

        return abilities


# EOF
