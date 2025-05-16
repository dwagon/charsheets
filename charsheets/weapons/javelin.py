from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Javelin(BaseWeapon):
    tag = Weapon.JAVELIN

    def __init__(self, **kwargs):
        super().__init__(DamageType.PIERCING, WeaponCategory.SIMPLE_MELEE, "1d6", **kwargs)
        self.weapon_mastery = WeaponMasteryProperty.SLOW
        self.properties = [WeaponProperty.THROWN, WeaponProperty.RANGE]
        self.range = (30, 120)
