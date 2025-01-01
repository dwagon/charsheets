from typing import TYPE_CHECKING
from charsheets.weapons.base_weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class ShortSword(BaseWeapon):
    tag = Weapon.SHORTSWORD

    def __init__(self, wielder: "Character"):
        super().__init__(wielder)
        self.weapon_mastery = WeaponMasteryProperty.VEX
        self.weapon_type = WeaponCategory.MARTIAL_MELEE
        self.damage_type = DamageType.PIERCING
        self.damage_dice = "1d6"
        self.properties = [WeaponProperty.FINESSE, WeaponProperty.LIGHT]
