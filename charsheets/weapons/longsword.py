from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Longsword(BaseWeapon):
    tag = Weapon.LONGSWORD

    def __init__(self, **kwargs):
        super().__init__(DamageType.SLASHING, WeaponCategory.MARTIAL_MELEE, "1d8", **kwargs)
        self.weapon_mastery = WeaponMasteryProperty.TOPPLE
        self.properties = [WeaponProperty.VERSATILE]
        self.versatile_damage_dice = "1d10"
