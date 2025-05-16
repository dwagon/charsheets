from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Pistol(BaseWeapon):
    tag = Weapon.PISTOL

    def __init__(self, **kwargs):
        super().__init__(DamageType.PIERCING, WeaponCategory.MARTIAL_RANGED, "1d10", **kwargs)
        self.weapon_mastery = WeaponMasteryProperty.VEX
        self.properties = [WeaponProperty.AMMUNITION, WeaponProperty.LOADING, WeaponProperty.RANGE]
        self.range = (30, 90)
