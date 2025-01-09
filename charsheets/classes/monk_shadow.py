from charsheets.abilities import ShadowArts
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.monk import Monk


#################################################################################
class MonkWarriorOfShadow(Monk):
    pass

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {ShadowArts()}
        abilities |= super().class_abilities()
        return abilities


# EOF
