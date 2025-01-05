from charsheets.weapons.base_weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty


#############################################################################
class Club(BaseWeapon):
    tag = Weapon.CLUB

    def __init__(self):
        super().__init__()
        self.weapon_mastery = WeaponMasteryProperty.SLOW
        self.weapon_type = WeaponCategory.SIMPLE_MELEE
        self.damage_type = DamageType.BLUDGEONING
        self.damage_dice = "1d4"
        self.properties = [WeaponProperty.LIGHT]
