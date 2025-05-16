from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Handaxe(BaseWeapon):
    tag = Weapon.HANDAXE

    def __init__(self, **kwargs):
        super().__init__(DamageType.SLASHING, WeaponCategory.SIMPLE_MELEE, "1d6", **kwargs)
        self.weapon_mastery = WeaponMasteryProperty.VEX
        self.properties = [WeaponProperty.LIGHT, WeaponProperty.THROWN, WeaponProperty.RANGE]
        self.range = (20, 60)
