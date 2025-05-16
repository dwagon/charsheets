from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class LightHammer(BaseWeapon):
    tag = Weapon.LIGHT_HAMMER

    def __init__(self, **kwargs):
        super().__init__(DamageType.BLUDGEONING, WeaponCategory.SIMPLE_MELEE, "1d4", **kwargs)
        self.weapon_mastery = WeaponMasteryProperty.NICK
        self.properties = [WeaponProperty.LIGHT, WeaponProperty.THROWN, WeaponProperty.RANGE]
        self.range = (20, 60)
