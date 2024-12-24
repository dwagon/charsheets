from typing import TYPE_CHECKING
from charsheets.weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty

if TYPE_CHECKING:   # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class WeaponShortbow(BaseWeapon):
    tag = Weapon.SHORTBOW

    def __init__(self, wielder: "Character"):
        super().__init__(wielder)
        self.weapon_mastery = WeaponMasteryProperty.VEX
        self.weapon_type = WeaponCategory.SIMPLE_RANGED
        self.damage_type = DamageType.PIERCING
        self.damage_dice = "1d6"
        self.properties = [WeaponProperty.AMMUNITION, WeaponProperty.TWO_HANDED, WeaponProperty.RANGE]
        self.range = (80, 320)
