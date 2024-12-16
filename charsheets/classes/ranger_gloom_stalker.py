from charsheets.classes.ranger import Ranger
from charsheets.constants import Ability
from charsheets.spells import Spells


#################################################################################
class GloomStalker(Ranger):
    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities: set[Ability] = {Ability.DREAD_AMBUSHER, Ability.UMBRAL_SIGHT}
        abilities |= super().class_abilities()

        self.prepare_spells(Spells.DISGUISE_SELF)
        return abilities


# EOF
