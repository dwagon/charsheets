from charsheets.abilities import VitalityOfTheTree, BranchesOfTheTree
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.barbarian import Barbarian


#################################################################################
class BarbarianPathOfTheWorldTree(Barbarian):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Barbarian (Path of the World Tree)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {VitalityOfTheTree()}
        if self.level >= 6:
            abilities.add(BranchesOfTheTree())
        abilities |= super().class_abilities()
        return abilities


# EOF
