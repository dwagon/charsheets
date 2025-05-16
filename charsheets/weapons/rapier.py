from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Rapier(BaseWeapon):
    tag = Weapon.RAPIER

    def __init__(self, **kwargs):
        super().__init__(DamageType.PIERCING, WeaponCategory.MARTIAL_MELEE, "1d8", **kwargs)
        self.weapon_mastery = WeaponMasteryProperty.VEX
        self.properties = [WeaponProperty.FINESSE]
