from charsheets.classes.ranger import Ranger
from charsheets.constants import Ability


#################################################################################
class Hunter(Ranger):
    pass

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities: set[Ability] = {Ability.HUNTERS_LORE, Ability.HUNTERS_PREY}
        abilities |= super().class_abilities()
        abilities |= {Ability.HUNTERS_LORE}
        return abilities


# EOF
