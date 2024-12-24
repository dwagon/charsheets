from typing import TYPE_CHECKING
from charsheets.weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty

if TYPE_CHECKING:   # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class WeaponGreatsword(BaseWeapon):
    tag = Weapon.GREATSWORD

    def __init__(self, wielder: "Character"):
        super().__init__(wielder)
        self.weapon_mastery = WeaponMasteryProperty.GRAZE
        self.weapon_type = WeaponCategory.MARTIAL_MELEE
        self.damage_type = DamageType.SLASHING
        self.damage_dice = "2d6"
        self.properties = [WeaponProperty.HEAVY, WeaponProperty.TWO_HANDED]
