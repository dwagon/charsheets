from charsheets.abilities import OpenHandTechnique, WholenessOfBody
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.monk import Monk


#################################################################################
class MonkWarriorOfTheOpenHand(Monk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Monk (Warrior of the Open Hand)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {OpenHandTechnique()}
        abilities |= super().class_abilities()
        if self.level >= 6:
            abilities.add(WholenessOfBody())
        return abilities


# EOF
