from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Shortbow(BaseWeapon):
    tag = Weapon.SHORTBOW

    def __init__(self, **kwargs):
        super().__init__(DamageType.PIERCING, WeaponCategory.SIMPLE_RANGED, "1d6", **kwargs)
        self.weapon_mastery = WeaponMasteryProperty.VEX
        self.properties = [WeaponProperty.AMMUNITION, WeaponProperty.TWO_HANDED, WeaponProperty.RANGE]
        self.range = (80, 320)
