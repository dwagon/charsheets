from charsheets.abilities import HandOfHarm, HandOfHealing, ImplementsOfMercy
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.monk import Monk


#################################################################################
class MonkWarriorOfMercy(Monk):
    pass

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {HandOfHarm(), HandOfHealing(), ImplementsOfMercy()}
        abilities |= super().class_abilities()

        return abilities


# EOF
