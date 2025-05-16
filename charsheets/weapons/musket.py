"""https://www.dndbeyond.com/equipment/43-musket"""

from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Musket(BaseWeapon):
    tag = Weapon.MUSKET

    def __init__(self, **kwargs):
        super().__init__(DamageType.PIERCING, WeaponCategory.MARTIAL_RANGED, "1d12", **kwargs)
        self.weapon_mastery = WeaponMasteryProperty.SLOW
        self.properties = [WeaponProperty.AMMUNITION, WeaponProperty.RANGE, WeaponProperty.LOADING, WeaponProperty.TWO_HANDED]
        self.range = (40, 120)
