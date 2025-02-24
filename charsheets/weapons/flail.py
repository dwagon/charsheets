from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Flail(BaseWeapon):
    tag = Weapon.FLAIL

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.weapon_mastery = WeaponMasteryProperty.SAP
        self.weapon_type = WeaponCategory.MARTIAL_MELEE
        self.damage_type = DamageType.BLUDGEONING
        self.damage_dice = "1d8"
        self.properties = []
