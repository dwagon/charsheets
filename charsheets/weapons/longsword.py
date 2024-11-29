from typing import TYPE_CHECKING
from charsheets.weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class WeaponLongswordMaul(BaseWeapon):
    tag = Weapon.LONGSWORD

    def __init__(self, wielder: "Character"):
        super().__init__(wielder)
        self.weapon_mastery = WeaponMasteryProperty.TOPPLE
        self.weapon_type = WeaponCategory.MARTIAL_MELEE
        self.damage_type = DamageType.SLASHING
        self.damage_dice = "1d8"
        self.properties = [WeaponProperty.VERSATILE]
        self.versatile_damage_dice = "1d10"
