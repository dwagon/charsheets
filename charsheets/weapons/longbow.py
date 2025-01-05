from charsheets.weapons.base_weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty


#############################################################################
class Longbow(BaseWeapon):
    tag = Weapon.LONGBOW

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.weapon_mastery = WeaponMasteryProperty.SLOW
        self.weapon_type = WeaponCategory.MARTIAL_RANGED
        self.damage_type = DamageType.PIERCING
        self.damage_dice = "1d8"
        self.properties = [
            WeaponProperty.AMMUNITION,
            WeaponProperty.RANGE,
            WeaponProperty.HEAVY,
            WeaponProperty.TWO_HANDED,
        ]
        self.range = (150, 600)
