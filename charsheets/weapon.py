""" Details about weapons"""

from enum import StrEnum, auto
from typing import TYPE_CHECKING

from charsheets.constants import WeaponType

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class DamageType(StrEnum):
    BLUDGEONING = auto()
    PIERCING = auto()
    SLASHING = auto()


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
    WeaponType.UNARMED: {Keys.DMG_TYPE: DamageType.BLUDGEONING, Keys.DMG_DICE: "1", Keys.WEAPON_TYPE: WeaponTypes.MELEE},
    WeaponType.CLUB: {Keys.DMG_TYPE: DamageType.BLUDGEONING, Keys.DMG_DICE: "1d4", Keys.WEAPON_TYPE: WeaponTypes.MELEE},
    WeaponType.SHORT_SWORD: {Keys.DMG_TYPE: DamageType.PIERCING, Keys.DMG_DICE: "1d6", Keys.WEAPON_TYPE: WeaponTypes.MELEE},
    WeaponType.LONGBOW: {Keys.DMG_TYPE: DamageType.PIERCING, Keys.DMG_DICE: "1d8", Keys.WEAPON_TYPE: WeaponTypes.RANGED},
    WeaponType.WARHAMMER: {Keys.DMG_TYPE: DamageType.BLUDGEONING, Keys.DMG_DICE: "1d8", Keys.WEAPON_TYPE: WeaponTypes.MELEE},
    WeaponType.SHORTBOW: {Keys.DMG_TYPE: DamageType.PIERCING, Keys.DMG_DICE: "1d6", Keys.WEAPON_TYPE: WeaponTypes.RANGED},
    WeaponType.SICKLE: {Keys.DMG_TYPE: DamageType.SLASHING, Keys.DMG_DICE: "1d4", Keys.WEAPON_TYPE: WeaponTypes.MELEE},
    WeaponType.MAUL: {Keys.DMG_TYPE: DamageType.BLUDGEONING, Keys.DMG_DICE: "2d6", Keys.WEAPON_TYPE: WeaponTypes.MELEE},
}


#############################################################################
class Weapon:
    def __init__(self, weapon_name: WeaponType, wielder: "Character"):
        self.weapon_name = weapon_name
        self.name = weapon_name.replace("_", " ")
        self.wielder = wielder

    #########################################################################
    @property
    def atk_bonus(self) -> str:
        mod = 0
        if WEAPONS[self.weapon_name][Keys.WEAPON_TYPE] == WeaponTypes.RANGED:
            mod += self.wielder.dexterity.modifier
            mod += self.wielder.ranged_atk_bonus()
        else:
            mod += self.wielder.strength.modifier
            mod += self.wielder.melee_atk_bonus()
        sign = "+" if mod >= 0 else "-"
        return f"{sign}{abs(mod)}"

    #########################################################################
    @property
    def dmg_bonus(self) -> str:
        if WEAPONS[self.weapon_name][Keys.WEAPON_TYPE] == WeaponTypes.RANGED:
            mod = self.wielder.dexterity.modifier
            mod += self.wielder.ranged_dmg_bonus()
        else:
            mod = self.wielder.strength.modifier
            mod += self.wielder.melee_dmg_bonus()
        sign = "+" if mod >= 0 else "-"
        return f"{sign}{abs(mod)}"

    #########################################################################
    @property
    def dmg_dice(self):
        return WEAPONS[self.weapon_name][Keys.DMG_DICE]

    #########################################################################
    @property
    def dmg_type(self) -> str:
        return WEAPONS[self.weapon_name][Keys.DMG_TYPE]

    #########################################################################
    def __repr__(self):
        return f"<Weapon {self.name} {self.atk_bonus} {self.dmg_dice} + {self.dmg_bonus}/{self.dmg_type}"


# EOF
