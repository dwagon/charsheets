from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Warhammer(BaseWeapon):
    tag = Weapon.WARHAMMER

    def __init__(self, **kwargs):
        super().__init__(DamageType.BLUDGEONING, WeaponCategory.MARTIAL_MELEE, "1d8", **kwargs)
        self.weapon_mastery = WeaponMasteryProperty.PUSH
        self.properties = [WeaponProperty.VERSATILE]
        self.versatile_damage_dice = "1d10"
