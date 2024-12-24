from typing import TYPE_CHECKING
from charsheets.weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty

if TYPE_CHECKING:   # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class WeaponLance(BaseWeapon):
    tag = Weapon.LANCE

    def __init__(self, wielder: "Character"):
        super().__init__(wielder)
        self.weapon_mastery = WeaponMasteryProperty.TOPPLE
        self.weapon_type = WeaponCategory.MARTIAL_MELEE
        self.damage_type = DamageType.PIERCING
        self.damage_dice = "1d10"
        self.properties = [WeaponProperty.HEAVY, WeaponProperty.REACH, WeaponProperty.TWO_HANDED]
