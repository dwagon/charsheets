from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Maul(BaseWeapon):
    tag = Weapon.MAUL

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.weapon_mastery = WeaponMasteryProperty.TOPPLE
        self.weapon_type = WeaponCategory.MARTIAL_MELEE
        self.damage_type = DamageType.BLUDGEONING
        self.damage_dice = "2d6"
        self.properties = [WeaponProperty.HEAVY, WeaponProperty.TWO_HANDED]
