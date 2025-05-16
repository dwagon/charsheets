from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Sickle(BaseWeapon):
    tag = Weapon.SICKLE

    def __init__(self, **kwargs):
        super().__init__(DamageType.SLASHING, WeaponCategory.SIMPLE_MELEE, "1d4", **kwargs)
        self.weapon_mastery = WeaponMasteryProperty.NICK
        self.properties = [WeaponProperty.LIGHT]
