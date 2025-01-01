from charsheets.abilities import DreadfulStrikes, OtherworldlyGlamour
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.ranger import Ranger
from charsheets.spells import Spells


#################################################################################
class FeyWanderer(Ranger):
    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {DreadfulStrikes(), OtherworldlyGlamour()}
        abilities |= super().class_abilities()
        self.prepare_spells(Spells.CHARM_PERSON)
        return abilities


# EOF
