from charsheets.abilities import DivineFury, WarriorOfTheGods, FanaticalFocus
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.barbarian import Barbarian


#################################################################################
class BarbarianPathOfTheZealot(Barbarian):
    _class_name = "Barbarian (Path of the Zealot)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {DivineFury(), WarriorOfTheGods()}
        if self.level >= 6:
            abilities.add(FanaticalFocus())
        abilities |= super().class_abilities()
        return abilities


# EOF
