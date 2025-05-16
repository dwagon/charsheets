from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Spear(BaseWeapon):
    tag = Weapon.SPEAR

    def __init__(self, **kwargs):
        super().__init__(DamageType.PIERCING, WeaponCategory.SIMPLE_MELEE, "1d6", **kwargs)
        self.weapon_mastery = WeaponMasteryProperty.SAP
        self.properties = [WeaponProperty.THROWN, WeaponProperty.VERSATILE, WeaponProperty.RANGE]
        self.range = (20, 60)
        self.versatile_damage_dice = "1d8"
