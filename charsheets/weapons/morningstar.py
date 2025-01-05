from charsheets.weapons.base_weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory


#############################################################################
class Morningstar(BaseWeapon):
    tag = Weapon.MORNINGSTAR

    def __init__(self):
        super().__init__()
        self.weapon_mastery = WeaponMasteryProperty.SAP
        self.weapon_type = WeaponCategory.MARTIAL_MELEE
        self.damage_type = DamageType.PIERCING
        self.damage_dice = "1d8"
        self.properties = []
