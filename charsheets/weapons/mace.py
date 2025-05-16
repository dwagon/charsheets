from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Mace(BaseWeapon):
    tag = Weapon.MACE

    def __init__(self, **kwargs):
        super().__init__(DamageType.BLUDGEONING, WeaponCategory.SIMPLE_MELEE, "1d6", **kwargs)
        self.weapon_mastery = WeaponMasteryProperty.SAP
        self.properties = []
