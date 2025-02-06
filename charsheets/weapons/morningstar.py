from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Morningstar(BaseWeapon):
    tag = Weapon.MORNINGSTAR

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.weapon_mastery = WeaponMasteryProperty.SAP
        self.weapon_type = WeaponCategory.MARTIAL_MELEE
        self.damage_type = DamageType.PIERCING
        self.damage_dice = "1d8"
        self.properties = []
