from charsheets.weapons.base_weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty


#############################################################################
class Quarterstaff(BaseWeapon):
    tag = Weapon.QUARTERSTAFF

    def __init__(self):
        super().__init__()
        self.weapon_mastery = WeaponMasteryProperty.TOPPLE
        self.weapon_type = WeaponCategory.SIMPLE_MELEE
        self.damage_type = DamageType.BLUDGEONING
        self.damage_dice = "1d6"
        self.properties = [WeaponProperty.VERSATILE]
        self.versatile_damage_dice = "1d8"
