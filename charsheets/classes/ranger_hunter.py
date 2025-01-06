from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.ranger import Ranger
from charsheets.constants import Ability
from charsheets.abilities import HuntersLore, HuntersPrey


#################################################################################
class RangerHunter(Ranger):
    pass

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {HuntersLore(), HuntersPrey()}
        abilities |= super().class_abilities()
        return abilities


# EOF
