from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Dart(BaseWeapon):
    tag = Weapon.DART

    def __init__(self, **kwargs):
        super().__init__(DamageType.PIERCING, WeaponCategory.SIMPLE_RANGED, "1d4", **kwargs)
        self.weapon_mastery = WeaponMasteryProperty.VEX
        self.properties = [WeaponProperty.FINESSE, WeaponProperty.THROWN, WeaponProperty.RANGE]
        self.range = (20, 60)
