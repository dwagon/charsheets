from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Flail(BaseWeapon):
    tag = Weapon.FLAIL

    def __init__(self, **kwargs):
        super().__init__(DamageType.BLUDGEONING, WeaponCategory.MARTIAL_MELEE, "1d8", **kwargs)
        self.weapon_mastery = WeaponMasteryProperty.SAP
        self.properties = []
