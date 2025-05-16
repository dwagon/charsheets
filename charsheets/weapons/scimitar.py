from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Scimitar(BaseWeapon):
    tag = Weapon.SCIMITAR

    def __init__(self, **kwargs):
        super().__init__(DamageType.SLASHING, WeaponCategory.MARTIAL_MELEE, "1d6", **kwargs)
        self.weapon_mastery = WeaponMasteryProperty.NICK
        self.properties = [WeaponProperty.FINESSE, WeaponProperty.LIGHT]
