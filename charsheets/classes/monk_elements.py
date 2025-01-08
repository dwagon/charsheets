from charsheets.abilities import ElementalAttunement, ManipulateElements
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.monk import Monk


#################################################################################
class MonkWarriorOfTheElements(Monk):
    pass

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {ElementalAttunement(), ManipulateElements()}
        abilities |= super().class_abilities()
        return abilities


# EOF
