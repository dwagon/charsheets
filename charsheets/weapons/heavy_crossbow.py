from typing import TYPE_CHECKING
from charsheets.weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty

if TYPE_CHECKING:   # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class WeaponHeavyCrossbow(BaseWeapon):
    tag = Weapon.HEAVY_CROSSBOW

    def __init__(self, wielder: "Character"):
        super().__init__(wielder)
        self.weapon_mastery = WeaponMasteryProperty.PUSH
        self.weapon_type = WeaponCategory.MARTIAL_RANGED
        self.damage_type = DamageType.PIERCING
        self.damage_dice = "1d10"
        self.properties = [
            WeaponProperty.AMMUNITION,
            WeaponProperty.HEAVY,
            WeaponProperty.LOADING,
            WeaponProperty.RANGE,
            WeaponProperty.TWO_HANDED,
        ]
        self.range = (100, 400)
