from charsheets.weapons.base_weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty


#############################################################################
class Pistol(BaseWeapon):
    tag = Weapon.PISTOL

    def __init__(self):
        super().__init__()
        self.weapon_mastery = WeaponMasteryProperty.VEX
        self.weapon_type = WeaponCategory.MARTIAL_RANGED
        self.damage_type = DamageType.PIERCING
        self.damage_dice = "1d10"
        self.properties = [WeaponProperty.AMMUNITION, WeaponProperty.LOADING, WeaponProperty.RANGE]
        self.range = (30, 90)
