from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class WarPick(BaseWeapon):
    tag = Weapon.WAR_PICK

    def __init__(self, **kwargs):
        super().__init__(DamageType.PIERCING, WeaponCategory.MARTIAL_MELEE, "1d8", **kwargs)
        self.weapon_mastery = WeaponMasteryProperty.SAP
        self.properties = [WeaponProperty.VERSATILE]
        self.versatile_damage_dice = "1d10"
