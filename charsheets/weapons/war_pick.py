from typing import TYPE_CHECKING
from charsheets.weapons.base_weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class WarPick(BaseWeapon):
    tag = Weapon.WAR_PICK

    def __init__(self, wielder: "Character"):
        super().__init__(wielder)
        self.weapon_mastery = WeaponMasteryProperty.SAP
        self.weapon_type = WeaponCategory.MARTIAL_MELEE
        self.damage_type = DamageType.PIERCING
        self.damage_dice = "1d8"
        self.properties = [WeaponProperty.VERSATILE]
        self.versatile_damage_dice = "1d10"
