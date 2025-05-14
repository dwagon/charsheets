"""Ability Score"""

from typing import TYPE_CHECKING

from charsheets.constants import Mod, Stat
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter


#############################################################################
class AbilityScore:
    """An ability score"""

    def __init__(self, stat: Stat, character: "BaseCharacter", value: int = 0):
        self.stat = stat
        self._value: Reason = Reason("Base", value)
        self.proficient = 0
        self.character: "BaseCharacter" = character

    #########################################################################
    @property
    def value(self) -> Reason[int]:
        """Return the value of the ability score"""
        v = self._value.copy()
        match self.stat:
            case Stat.STRENGTH:
                v.extend(self.character.check_modifiers(Mod.MOD_STAT_STR))
                if stat_set := self.character.check_modifiers(Mod.MOD_STAT_STR_SET):
                    v = stat_set.copy()
            case Stat.DEXTERITY:
                v.extend(self.character.check_modifiers(Mod.MOD_STAT_DEX))
                if stat_set := self.character.check_modifiers(Mod.MOD_STAT_DEX_SET):
                    v = stat_set.copy()
            case Stat.CONSTITUTION:
                v.extend(self.character.check_modifiers(Mod.MOD_STAT_CON))
                if stat_set := self.character.check_modifiers(Mod.MOD_STAT_CON_SET):
                    v = stat_set.copy()
            case Stat.INTELLIGENCE:
                v.extend(self.character.check_modifiers(Mod.MOD_STAT_INT))
                if stat_set := self.character.check_modifiers(Mod.MOD_STAT_INT_SET):
                    v = stat_set.copy()
            case Stat.WISDOM:
                v.extend(self.character.check_modifiers(Mod.MOD_STAT_WIS))
                if stat_set := self.character.check_modifiers(Mod.MOD_STAT_WIS_SET):
                    v = stat_set.copy()
            case Stat.CHARISMA:
                v.extend(self.character.check_modifiers(Mod.MOD_STAT_CHA))
                if stat_set := self.character.check_modifiers(Mod.MOD_STAT_CHA_SET):
                    v = stat_set.copy()
        return v

    #########################################################################
    @property
    def saving_throw(self) -> int:
        """Return the saving throw DC for the ability score"""
        if self.proficient:
            return self.modifier + self.character.proficiency_bonus
        return self.modifier

    #########################################################################
    @property
    def modifier(self):
        """Ability modifier"""
        return (int(self.value) - 10) // 2

    #########################################################################
    def __str__(self):
        return f"{self.value} {self.modifier} {self.proficient}"
