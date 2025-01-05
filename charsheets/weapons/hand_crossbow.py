from charsheets.weapons.base_weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty


#############################################################################
class HandCrossbow(BaseWeapon):
    tag = Weapon.HAND_CROSSBOW

    def __init__(self):
        super().__init__()
        self.weapon_mastery = WeaponMasteryProperty.VEX
        self.weapon_type = WeaponCategory.MARTIAL_RANGED
        self.damage_type = DamageType.PIERCING
        self.damage_dice = "1d6"
        self.properties = [WeaponProperty.AMMUNITION, WeaponProperty.RANGE, WeaponProperty.LIGHT, WeaponProperty.LOADING]
        self.range = (30, 120)
