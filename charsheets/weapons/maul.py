from charsheets.weapons.base_weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty


#############################################################################
class Maul(BaseWeapon):
    tag = Weapon.MAUL

    def __init__(self):
        super().__init__()
        self.weapon_mastery = WeaponMasteryProperty.TOPPLE
        self.weapon_type = WeaponCategory.MARTIAL_MELEE
        self.damage_type = DamageType.BLUDGEONING
        self.damage_dice = "2d6"
        self.properties = [WeaponProperty.HEAVY, WeaponProperty.TWO_HANDED]
