from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Sling(BaseWeapon):
    tag = Weapon.SLING

    def __init__(self, **kwargs):
        super().__init__(DamageType.BLUDGEONING, WeaponCategory.SIMPLE_RANGED, "1d4", **kwargs)
        self.weapon_mastery = WeaponMasteryProperty.SLOW
        self.properties = [WeaponProperty.AMMUNITION, WeaponProperty.RANGE]
        self.range = (30, 120)
