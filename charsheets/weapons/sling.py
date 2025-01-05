from charsheets.weapons.base_weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty


#############################################################################
class Sling(BaseWeapon):
    tag = Weapon.SLING

    def __init__(self):
        super().__init__()
        self.weapon_mastery = WeaponMasteryProperty.SLOW
        self.weapon_type = WeaponCategory.SIMPLE_RANGED
        self.damage_type = DamageType.BLUDGEONING
        self.damage_dice = "1d4"
        self.properties = [WeaponProperty.AMMUNITION, WeaponProperty.RANGE]
        self.range = (30, 120)
