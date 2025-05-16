from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Halberd(BaseWeapon):
    tag = Weapon.HALBERD

    def __init__(self, **kwargs):
        super().__init__(DamageType.SLASHING, WeaponCategory.MARTIAL_MELEE, "1d10", **kwargs)
        self.weapon_mastery = WeaponMasteryProperty.CLEAVE
        self.properties = [WeaponProperty.HEAVY, WeaponProperty.REACH, WeaponProperty.TWO_HANDED]
