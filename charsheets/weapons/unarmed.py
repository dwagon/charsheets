from typing import TYPE_CHECKING
from charsheets.weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class WeaponShortSword(BaseWeapon):
    tag = Weapon.UNARMED

    def __init__(self, wielder: "Character"):
        super().__init__(wielder)
        self.weapon_mastery = None
        self.weapon_type = WeaponCategory.SIMPLE_MELEE
        self.damage_type = DamageType.BLUDGEONING
        self.damage_dice = "1"
