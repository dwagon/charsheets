""" Ability Score"""

from typing import TYPE_CHECKING

from charsheets.constants import Mod, Stat
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class AbilityScore:
    def __init__(self, stat: Stat, character: "Character", value: int = 0):
        self.stat = stat
        self._value: Reason = Reason("Base", value)
        self.proficient = 0
        self.character: "Character" = character

    #########################################################################
    @property
    def value(self) -> Reason:
        v = self._value.copy()
        match self.stat:
            case Stat.STRENGTH:
                v.extend(self.character.check_modifiers(Mod.MOD_STAT_STR))
            case Stat.DEXTERITY:
                v.extend(self.character.check_modifiers(Mod.MOD_STAT_DEX))
            case Stat.CONSTITUTION:
                v.extend(self.character.check_modifiers(Mod.MOD_STAT_CON))
            case Stat.INTELLIGENCE:
                v.extend(self.character.check_modifiers(Mod.MOD_STAT_INT))
            case Stat.WISDOM:
                v.extend(self.character.check_modifiers(Mod.MOD_STAT_WIS))
            case Stat.CHARISMA:
                v.extend(self.character.check_modifiers(Mod.MOD_STAT_CHA))
        return v

    #########################################################################
    @property
    def saving_throw(self) -> int:
        if self.proficient:
            return self.modifier + self.character.proficiency_bonus
        return self.modifier

    #########################################################################
    @property
    def modifier(self):
        return (int(self.value) - 10) // 2

    #########################################################################
    def __str__(self):
        return f"{self.value} {self.modifier} {self.proficient}"
