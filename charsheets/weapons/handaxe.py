from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Handaxe(BaseWeapon):
    tag = Weapon.HANDAXE

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.weapon_mastery = WeaponMasteryProperty.VEX
        self.weapon_type = WeaponCategory.SIMPLE_MELEE
        self.damage_type = DamageType.SLASHING
        self.damage_dice = "1d6"
        self.properties = [WeaponProperty.LIGHT, WeaponProperty.THROWN, WeaponProperty.RANGE]
        self.range = (20, 60)
