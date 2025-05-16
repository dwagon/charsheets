from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Greatclub(BaseWeapon):
    tag = Weapon.GREATCLUB

    def __init__(self, **kwargs):
        super().__init__(DamageType.BLUDGEONING, WeaponCategory.SIMPLE_MELEE, "1d8", **kwargs)
        self.weapon_mastery = WeaponMasteryProperty.PUSH
        self.properties = [WeaponProperty.TWO_HANDED]
