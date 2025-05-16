from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Whip(BaseWeapon):
    tag = Weapon.WHIP

    def __init__(self, **kwargs):
        super().__init__(DamageType.SLASHING, WeaponCategory.MARTIAL_MELEE, "1d4", **kwargs)
        self.weapon_mastery = WeaponMasteryProperty.SLOW
        self.properties = [WeaponProperty.FINESSE, WeaponProperty.REACH]
