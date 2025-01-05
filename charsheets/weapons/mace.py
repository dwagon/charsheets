from charsheets.weapons.base_weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory


#############################################################################
class Mace(BaseWeapon):
    tag = Weapon.MACE

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.weapon_mastery = WeaponMasteryProperty.SAP
        self.weapon_type = WeaponCategory.SIMPLE_MELEE
        self.damage_type = DamageType.BLUDGEONING
        self.damage_dice = "1d6"
        self.properties = []
