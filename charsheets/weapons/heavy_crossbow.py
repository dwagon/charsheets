from typing import cast

from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class HeavyCrossbow(BaseWeapon):
    tag = cast(Weapon, Weapon.HEAVY_CROSSBOW)

    def __init__(self, **kwargs):
        super().__init__(DamageType.PIERCING, WeaponCategory.MARTIAL_RANGED, "1d10", **kwargs)
        self.weapon_mastery = WeaponMasteryProperty.PUSH
        self.properties = [
            WeaponProperty.AMMUNITION,
            WeaponProperty.HEAVY,
            WeaponProperty.LOADING,
            WeaponProperty.RANGE,
            WeaponProperty.TWO_HANDED,
        ]
        self.range = (100, 400)


# EOF
