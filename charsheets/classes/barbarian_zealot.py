from charsheets.classes.barbarian import Barbarian
from charsheets.constants import Ability


#################################################################################
class PathOfTheZealot(Barbarian):
    _class_name = "Barbarian (Path of the Zealot)"

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities: set[Ability] = set()
        abilities |= super().class_abilities()
        return abilities


# EOF