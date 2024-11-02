""" Details about weapons"""

from typing import TYPE_CHECKING
from enum import StrEnum, auto
from charsheets.constants import WeaponType

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class DamageType(StrEnum):
    BLUDGEONING = auto()
    PIERCING = auto()


#############################################################################
class Keys(StrEnum):
    DMG_TYPE = auto()
    DMG_DICE = auto()
    WEAPON_TYPE = auto()


#############################################################################
class WeaponTypes(StrEnum):
    RANGED = auto()
    MELEE = auto()


#############################################################################
WEAPONS = {
    WeaponType.CLUB: {Keys.DMG_TYPE: DamageType.BLUDGEONING, Keys.DMG_DICE: "1d4", Keys.WEAPON_TYPE: WeaponTypes.MELEE},
    WeaponType.SHORT_SWORD: {Keys.DMG_TYPE: DamageType.PIERCING, Keys.DMG_DICE: "1d6", Keys.WEAPON_TYPE: WeaponTypes.MELEE},
    WeaponType.LONGBOW: {Keys.DMG_TYPE: DamageType.PIERCING, Keys.DMG_DICE: "1d8", Keys.WEAPON_TYPE: WeaponTypes.RANGED},
}


#############################################################################
class Weapon:
    def __init__(self, name: WeaponType, wielder: "Character"):
        self.name = name
        self.wielder = wielder

    #########################################################################
    @property
    def atk_bonus(self) -> str:
        mod = self.wielder.strength.modifier
        if WEAPONS[self.name][Keys.WEAPON_TYPE] == WeaponTypes.RANGED:
            mod += self.wielder.ranged_atk_bonus()
        else:
            mod += self.wielder.melee_atk_bonus()
        sign = "+" if mod >= 0 else "-"
        return f"{sign}{mod}"

    #########################################################################
    @property
    def dmg_bonus(self) -> int:
        return self.wielder.strength.modifier

    #########################################################################
    @property
    def dmg_dice(self):
        return WEAPONS[self.name][Keys.DMG_DICE]

    #########################################################################
    @property
    def dmg_type(self) -> str:
        return WEAPONS[self.name][Keys.DMG_TYPE]

    #########################################################################
    def __repr__(self):
        return f"<Weapon {self.name} {self.atk_bonus} {self.dmg_dice} + {self.dmg_bonus}/{self.dmg_type}"


# EOF
