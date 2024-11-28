from typing import TYPE_CHECKING
from charsheets.weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class WeaponScimitar(BaseWeapon):
    tag = Weapon.SCIMITAR

    def __init__(self, wielder: "Character"):
        super().__init__(wielder)
        self.weapon_mastery = WeaponMasteryProperty.NICK
        self.weapon_type = WeaponCategory.MARTIAL_MELEE
        self.damage_type = DamageType.SLASHING
        self.damage_dice = "1d6"
        self.properties = [WeaponProperty.FINESSE, WeaponProperty.LIGHT]
