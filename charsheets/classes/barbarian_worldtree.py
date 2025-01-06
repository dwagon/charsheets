from charsheets.abilities import VitalityOfTheTree
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.barbarian import Barbarian


#################################################################################
class BarbarianPathOfTheWorldTree(Barbarian):
    _class_name = "Barbarian (Path of the World Tree)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {VitalityOfTheTree()}
        abilities |= super().class_abilities()
        return abilities


# EOF
