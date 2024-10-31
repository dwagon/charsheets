""" Details about weapons"""

from enum import StrEnum, auto
from constants import WeaponType


#############################################################################
class DamageType(StrEnum):
    BLUDGEONING = auto()
    PIERCING = auto()


#############################################################################
class Keys(StrEnum):
    DMG_TYPE = auto()
    DMG_DICE = auto()


#############################################################################
WEAPONS = {
    WeaponType.CLUB: {Keys.DMG_TYPE: DamageType.BLUDGEONING, Keys.DMG_DICE: "1d4"},
    WeaponType.SHORT_SWORD: {Keys.DMG_TYPE: DamageType.PIERCING, Keys.DMG_DICE: "1d6"},
    WeaponType.LONGBOW: {Keys.DMG_TYPE: DamageType.PIERCING, Keys.DMG_DICE: "1d8"},
}


#############################################################################
class Weapon:
    def __init__(self, wtype: WeaponType, wielder):
        self.wtype = wtype
        self.wielder = wielder

    #########################################################################
    @property
    def atk_bonus(self) -> str:
        mod = self.wielder.strength.modifier
        sign = "+" if mod >= 0 else "-"
        return f"{sign}{mod}"

    #########################################################################
    @property
    def dmg_bonus(self) -> int:
        return self.wielder.strength.modifier

    #########################################################################
    @property
    def dmg_dice(self):
        return WEAPONS[self.wtype][Keys.DMG_DICE]

    #########################################################################
    @property
    def dmg_type(self) -> str:
        return WEAPONS[self.wtype][Keys.DMG_TYPE]

    #########################################################################
    def __repr__(self):
        return f"<Weapon {self.wtype} {self.atk_bonus} {self.dmg_dice} + {self.dmg_bonus}/{self.dmg_type}"


# EOF
