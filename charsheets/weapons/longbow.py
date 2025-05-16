from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Longbow(BaseWeapon):
    tag = Weapon.LONGBOW

    def __init__(self, **kwargs):
        super().__init__(DamageType.PIERCING, WeaponCategory.MARTIAL_RANGED, "1d8", **kwargs)
        self.weapon_mastery = WeaponMasteryProperty.SLOW
        self.properties = [
            WeaponProperty.AMMUNITION,
            WeaponProperty.RANGE,
            WeaponProperty.HEAVY,
            WeaponProperty.TWO_HANDED,
        ]
        self.range = (150, 600)
