from typing import TYPE_CHECKING
from charsheets.weapons.base_weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty

if TYPE_CHECKING:   # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class Handaxe(BaseWeapon):
    tag = Weapon.HANDAXE

    def __init__(self, wielder: "Character"):
        super().__init__(wielder)
        self.weapon_mastery = WeaponMasteryProperty.VEX
        self.weapon_type = WeaponCategory.SIMPLE_MELEE
        self.damage_type = DamageType.SLASHING
        self.damage_dice = "1d6"
        self.properties = [WeaponProperty.LIGHT, WeaponProperty.THROWN, WeaponProperty.RANGE]
        self.range = (20, 60)
