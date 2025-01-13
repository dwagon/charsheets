from charsheets.abilities import HandOfHarm, HandOfHealing, ImplementsOfMercy, PhysiciansTouch
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.monk import Monk


#################################################################################
class MonkWarriorOfMercy(Monk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Monk (Warrior of Mercy)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {HandOfHarm(), HandOfHealing(), ImplementsOfMercy()}
        abilities |= super().class_abilities()

        if self.level >= 6:
            abilities.add(PhysiciansTouch())

        return abilities


# EOF
