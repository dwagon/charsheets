from typing import TYPE_CHECKING
from charsheets.weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty

if TYPE_CHECKING:   # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class WeaponHandCrossbow(BaseWeapon):
    tag = Weapon.HAND_CROSSBOW

    def __init__(self, wielder: "Character"):
        super().__init__(wielder)
        self.weapon_mastery = WeaponMasteryProperty.VEX
        self.weapon_type = WeaponCategory.MARTIAL_RANGED
        self.damage_type = DamageType.PIERCING
        self.damage_dice = "1d6"
        self.properties = [WeaponProperty.AMMUNITION, WeaponProperty.RANGE, WeaponProperty.LIGHT, WeaponProperty.LOADING]
        self.range = (30, 120)
