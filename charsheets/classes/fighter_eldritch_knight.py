from typing import Optional

from charsheets.abilities import WarBond
from charsheets.abilities.base_ability import BaseAbility
from charsheets.classes.fighter import Fighter
from charsheets.constants import Stat


#################################################################################
class EldritchKnight(Fighter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Eldritch Knight"

    #############################################################################
    @property
    def spell_casting_ability(self) -> Optional[Stat]:
        return Stat.INTELLIGENCE

    #############################################################################
    def class_abilities(self) -> set[BaseAbility]:
        abilities: set[BaseAbility] = {WarBond()}
        abilities |= super().class_abilities()
        return abilities

    #############################################################################
    def spell_slots(self, spell_level: int) -> int:
        return {
            1: [0, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [0, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [1, 0, 0, 0, 0, 0, 0, 0, 0],
            4: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            5: [3, 0, 0, 0, 0, 0, 0, 0, 0],
        }[self.level][spell_level - 1]

    #############################################################################
    def max_spell_level(self) -> int:
        if self.level >= 19:
            return 4
        elif self.level >= 13:
            return 3
        elif self.level >= 7:
            return 2
        elif self.level >= 3:
            return 1
        return 0


# EOF
