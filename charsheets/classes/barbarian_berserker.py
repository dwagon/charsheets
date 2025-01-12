from charsheets.abilities import Frenzy, MindlessRage
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.barbarian import Barbarian


#################################################################################
class BarbarianPathOfTheBeserker(Barbarian):
    _class_name = "Barbarian (Path of the Beserker)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {Frenzy()}
        if self.level >= 6:
            abilities.add(MindlessRage())
        abilities |= super().class_abilities()
        return abilities


# EOF
