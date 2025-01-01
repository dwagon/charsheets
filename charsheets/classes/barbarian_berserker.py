from charsheets.abilities import Frenzy
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.barbarian import Barbarian


#################################################################################
class PathOfTheBeserker(Barbarian):
    _class_name = "Barbarian (Path of the Beserker)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {Frenzy()}
        abilities |= super().class_abilities()
        return abilities


# EOF
