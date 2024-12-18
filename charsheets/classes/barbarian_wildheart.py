from charsheets.classes.barbarian import Barbarian
from charsheets.constants import Ability


#################################################################################
class PathOfTheWildHeart(Barbarian):
    _class_name = "Barbarian (Path of the Wild Heart)"

    #############################################################################
    def class_abilities(self) -> set[Ability]:
        abilities: set[Ability] = {Ability.ANIMAL_SPEAKER, Ability.RAGE_OF_THE_WILDS}
        abilities |= super().class_abilities()
        return abilities


# EOF
