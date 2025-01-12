from charsheets.abilities import AnimalSpeaker, RageOfTheWilds, AspectsOfTheWilds
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.barbarian import Barbarian


#################################################################################
class BarbarianPathOfTheWildHeart(Barbarian):
    _class_name = "Barbarian (Path of the Wild Heart)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {AnimalSpeaker(), RageOfTheWilds()}
        if self.level >= 6:
            abilities.add(AspectsOfTheWilds())
        abilities |= super().class_abilities()
        return abilities


# EOF
