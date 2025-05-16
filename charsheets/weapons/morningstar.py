from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Morningstar(BaseWeapon):
    tag = Weapon.MORNINGSTAR

    def __init__(self, **kwargs):
        super().__init__(DamageType.PIERCING, WeaponCategory.MARTIAL_MELEE, "1d8", **kwargs)
        self.weapon_mastery = WeaponMasteryProperty.SAP
        self.properties = []
