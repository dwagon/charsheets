from charsheets.weapons.base_weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty


#############################################################################
class Greataxe(BaseWeapon):
    tag = Weapon.GREATAXE

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.weapon_mastery = WeaponMasteryProperty.CLEAVE
        self.weapon_type = WeaponCategory.MARTIAL_MELEE
        self.damage_type = DamageType.SLASHING
        self.damage_dice = "1d12"
        self.properties = [WeaponProperty.HEAVY, WeaponProperty.TWO_HANDED]
