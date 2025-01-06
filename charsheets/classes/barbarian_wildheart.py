from charsheets.abilities import AnimalSpeaker, RageOfTheWilds
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.barbarian import Barbarian


#################################################################################
class BarbarianPathOfTheWildHeart(Barbarian):
    _class_name = "Barbarian (Path of the Wild Heart)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {AnimalSpeaker(), RageOfTheWilds()}
        abilities |= super().class_abilities()
        return abilities


# EOF
