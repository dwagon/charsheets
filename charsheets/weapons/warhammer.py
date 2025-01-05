from charsheets.weapons.base_weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty


#############################################################################
class Warhammer(BaseWeapon):
    tag = Weapon.WARHAMMER

    def __init__(self):
        super().__init__()
        self.weapon_mastery = WeaponMasteryProperty.PUSH
        self.weapon_type = WeaponCategory.MARTIAL_MELEE
        self.damage_type = DamageType.BLUDGEONING
        self.damage_dice = "1d8"
        self.properties = [WeaponProperty.VERSATILE]
        self.versatile_damage_dice = "1d10"
