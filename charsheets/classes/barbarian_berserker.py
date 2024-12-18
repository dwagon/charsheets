from charsheets.classes.barbarian import Barbarian
from charsheets.constants import Ability


#################################################################################
class PathOfTheBeserker(Barbarian):
    _class_name = "Barbarian (Path of the Beserker)"

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities: set[Ability] = {Ability.FRENZY}
        abilities |= super().class_abilities()
        return abilities


# EOF
