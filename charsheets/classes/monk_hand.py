from charsheets.abilities import OpenHandTechnique
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.monk import Monk
from charsheets.spells import Spells


#################################################################################
class MonkWarriorOfTheOpenHand(Monk):
    pass

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {OpenHandTechnique()}
        abilities |= super().class_abilities()
        return abilities


# EOF
