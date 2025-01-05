from charsheets.weapons.base_weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty


#############################################################################
class Halberd(BaseWeapon):
    tag = Weapon.HALBERD

    def __init__(self):
        super().__init__()
        self.weapon_mastery = WeaponMasteryProperty.CLEAVE
        self.weapon_type = WeaponCategory.MARTIAL_MELEE
        self.damage_type = DamageType.SLASHING
        self.damage_dice = "1d10"
        self.properties = [WeaponProperty.HEAVY, WeaponProperty.REACH, WeaponProperty.TWO_HANDED]
