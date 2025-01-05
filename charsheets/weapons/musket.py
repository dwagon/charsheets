from charsheets.weapons.base_weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty



#############################################################################
class Musket(BaseWeapon):
    tag = Weapon.MUSKET

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.weapon_mastery = WeaponMasteryProperty.SLOW
        self.weapon_type = WeaponCategory.MARTIAL_RANGED
        self.damage_type = DamageType.PIERCING
        self.damage_dice = "1d12"
        self.properties = [WeaponProperty.AMMUNITION, WeaponProperty.RANGE, WeaponProperty.LOADING, WeaponProperty.TWO_HANDED]
        self.range = (40, 12)
