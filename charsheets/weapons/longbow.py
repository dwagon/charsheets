from typing import TYPE_CHECKING
from charsheets.weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class WeaponLongbow(BaseWeapon):
    tag = Weapon.LONGBOW

    def __init__(self, wielder: "Character"):
        super().__init__(wielder)
        self.weapon_mastery = WeaponMasteryProperty.SLOW
        self.weapon_type = WeaponCategory.MARTIAL_RANGED
        self.damage_type = DamageType.PIERCING
        self.damage_dice = "1d8"
        self.properties = [
            WeaponProperty.AMMUNITION,
            WeaponProperty.RANGE,
            WeaponProperty.HEAVY,
            WeaponProperty.TWO_HANDED,
        ]
        self.range = (150, 600)
