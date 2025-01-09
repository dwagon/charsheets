from charsheets.abilities import WildMagicSurge, TidesOfChaos
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.sorcerer import Sorcerer


#################################################################################
class SorcererWildMagic(Sorcerer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Wild Magic Sorceror"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {WildMagicSurge(), TidesOfChaos()}
        abilities |= super().class_abilities()

        return abilities


# EOF
