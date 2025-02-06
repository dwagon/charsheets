from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Shortbow(BaseWeapon):
    tag = Weapon.SHORTBOW

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.weapon_mastery = WeaponMasteryProperty.VEX
        self.weapon_type = WeaponCategory.SIMPLE_RANGED
        self.damage_type = DamageType.PIERCING
        self.damage_dice = "1d6"
        self.properties = [WeaponProperty.AMMUNITION, WeaponProperty.TWO_HANDED, WeaponProperty.RANGE]
        self.range = (80, 320)
