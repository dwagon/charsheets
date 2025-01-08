from charsheets.abilities import DreadAmbusher, UmbralSight
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.ranger import Ranger
from charsheets.spells import Spells


#################################################################################
class RangerGloomStalker(Ranger):
    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {DreadAmbusher(), UmbralSight()}
        abilities |= super().class_abilities()

        self.prepare_spells(Spells.DISGUISE_SELF)
        if self.level >= 5:
            self.prepare_spells(Spells.ROPE_TRICK)

        return abilities


# EOF
