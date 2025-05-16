from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Greatsword(BaseWeapon):
    tag = Weapon.GREATSWORD

    def __init__(self, **kwargs):
        super().__init__(DamageType.SLASHING, WeaponCategory.MARTIAL_MELEE, "2d6", **kwargs)
        self.weapon_mastery = WeaponMasteryProperty.GRAZE
        self.properties = [WeaponProperty.HEAVY, WeaponProperty.TWO_HANDED]
