from charsheets.constants import Weapon, DamageType, WeaponCategory
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Unarmed(BaseWeapon):
    tag = Weapon.UNARMED

    def __init__(self, **kwargs):
        super().__init__(DamageType.BLUDGEONING, WeaponCategory.SIMPLE_MELEE, "1", **kwargs)
