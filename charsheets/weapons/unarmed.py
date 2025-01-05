from charsheets.weapons.base_weapon import BaseWeapon
from charsheets.constants import Weapon, DamageType, WeaponCategory


#############################################################################
class Unarmed(BaseWeapon):
    tag = Weapon.UNARMED

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.weapon_mastery = None
        self.weapon_type = WeaponCategory.SIMPLE_MELEE
        self.damage_type = DamageType.BLUDGEONING
        self.damage_dice = "1"
