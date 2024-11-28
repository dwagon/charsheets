from typing import TYPE_CHECKING
from charsheets.weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class WeaponFlail(BaseWeapon):
    tag = Weapon.FLAIL

    def __init__(self, wielder: "Character"):
        super().__init__(wielder)
        self.weapon_mastery = WeaponMasteryProperty.SAP
        self.weapon_type = WeaponCategory.MARTIAL_MELEE
        self.damage_type = DamageType.BLUDGEONING
        self.damage_dice = "1d8"
        self.properties = []
