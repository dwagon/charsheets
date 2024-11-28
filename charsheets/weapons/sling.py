from typing import TYPE_CHECKING
from charsheets.weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class WeaponSling(BaseWeapon):
    tag = Weapon.SLING

    def __init__(self, wielder: "Character"):
        super().__init__(wielder)
        self.weapon_mastery = WeaponMasteryProperty.SLOW
        self.weapon_type = WeaponCategory.SIMPLE_RANGED
        self.damage_type = DamageType.BLUDGEONING
        self.damage_dice = "1d4"
        self.properties = [WeaponProperty.AMMUNITION, WeaponProperty.RANGE]
        self.range = (30, 120)
