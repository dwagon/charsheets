from charsheets.abilities import ElementalAttunement, ManipulateElements, ElementalBurst
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.monk import Monk


#################################################################################
class MonkWarriorOfTheElements(Monk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Monk (Warrior of the Elements)"

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {ElementalAttunement(), ManipulateElements()}
        abilities |= super().class_abilities()
        if self.level >= 6:
            abilities.add(ElementalBurst())
        return abilities


# EOF
