from charsheets.abilities import DreadAmbusher, UmbralSight
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.ranger import Ranger
from charsheets.spells import Spells


#################################################################################
class GloomStalker(Ranger):
    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {DreadAmbusher(), UmbralSight()}
        abilities |= super().class_abilities()

        self.prepare_spells(Spells.DISGUISE_SELF)
        return abilities


# EOF
