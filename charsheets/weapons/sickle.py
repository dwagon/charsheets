from charsheets.weapons.base_weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty


#############################################################################
class Sickle(BaseWeapon):
    tag = Weapon.SICKLE

    def __init__(self):
        super().__init__()
        self.weapon_mastery = WeaponMasteryProperty.NICK
        self.weapon_type = WeaponCategory.SIMPLE_MELEE
        self.damage_type = DamageType.SLASHING
        self.damage_dice = "1d4"
        self.properties = [WeaponProperty.LIGHT]
