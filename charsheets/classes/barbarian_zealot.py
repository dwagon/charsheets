from charsheets.classes.barbarian import Barbarian
from charsheets.constants import Ability


#################################################################################
class PathOfTheZealot(Barbarian):
    _class_name = "Barbarian (Path of the Zealot)"

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities: set[Ability] = {Ability.DIVINE_FURY, Ability.WARRIOR_OF_THE_GODS}
        abilities |= super().class_abilities()
        return abilities


# EOF
