from charsheets.weapons.base_weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty


#############################################################################
class Scimitar(BaseWeapon):
    tag = Weapon.SCIMITAR

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.weapon_mastery = WeaponMasteryProperty.NICK
        self.weapon_type = WeaponCategory.MARTIAL_MELEE
        self.damage_type = DamageType.SLASHING
        self.damage_dice = "1d6"
        self.properties = [WeaponProperty.FINESSE, WeaponProperty.LIGHT]
