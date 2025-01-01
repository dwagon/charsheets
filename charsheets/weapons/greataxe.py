from typing import TYPE_CHECKING
from charsheets.weapons.base_weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty

if TYPE_CHECKING:   # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class Greataxe(BaseWeapon):
    tag = Weapon.GREATAXE

    def __init__(self, wielder: "Character"):
        super().__init__(wielder)
        self.weapon_mastery = WeaponMasteryProperty.CLEAVE
        self.weapon_type = WeaponCategory.MARTIAL_MELEE
        self.damage_type = DamageType.SLASHING
        self.damage_dice = "1d12"
        self.properties = [WeaponProperty.HEAVY, WeaponProperty.TWO_HANDED]
