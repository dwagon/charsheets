from charsheets.abilities import DreadfulStrikes, OtherworldlyGlamour, FeyWandererSpells
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.ranger import Ranger


#################################################################################
class RangerFeyWanderer(Ranger):
    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {DreadfulStrikes(), OtherworldlyGlamour(), FeyWandererSpells()}
        abilities |= super().class_abilities()
        return abilities


# EOF
