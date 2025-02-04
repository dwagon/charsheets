from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Dart(BaseWeapon):
    tag = Weapon.DART

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.weapon_mastery = WeaponMasteryProperty.VEX
        self.weapon_type = WeaponCategory.SIMPLE_RANGED
        self.damage_type = DamageType.PIERCING
        self.damage_dice = "1d4"
        self.properties = [WeaponProperty.FINESSE, WeaponProperty.THROWN, WeaponProperty.RANGE]
        self.range = (20, 60)
