from charsheets.abilities import ShadowArts, ShadowStep
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.monk import Monk


#################################################################################
class MonkWarriorOfShadow(Monk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Monk (Warrior of Shadow)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {ShadowArts()}
        abilities |= super().class_abilities()
        if self.level >= 6:
            abilities.add(ShadowStep())
        return abilities


# EOF
