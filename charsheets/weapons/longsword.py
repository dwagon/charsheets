from charsheets.weapons.base_weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty


#############################################################################
class Longsword(BaseWeapon):
    tag = Weapon.LONGSWORD

    def __init__(self):
        super().__init__()
        self.weapon_mastery = WeaponMasteryProperty.TOPPLE
        self.weapon_type = WeaponCategory.MARTIAL_MELEE
        self.damage_type = DamageType.SLASHING
        self.damage_dice = "1d8"
        self.properties = [WeaponProperty.VERSATILE]
        self.versatile_damage_dice = "1d10"
