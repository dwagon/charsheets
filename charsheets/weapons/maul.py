from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Maul(BaseWeapon):
    tag = Weapon.MAUL

    def __init__(self, **kwargs):
        super().__init__(DamageType.BLUDGEONING, WeaponCategory.MARTIAL_MELEE, "2d6", **kwargs)
        self.weapon_mastery = WeaponMasteryProperty.TOPPLE
        self.properties = [WeaponProperty.HEAVY, WeaponProperty.TWO_HANDED]
