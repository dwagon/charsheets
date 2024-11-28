from typing import TYPE_CHECKING
from charsheets.weapon import BaseWeapon
from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty

if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class WeaponGreatclub(BaseWeapon):
    tag = Weapon.GREATCLUB

    def __init__(self, wielder: "Character"):
        super().__init__(wielder)
        self.weapon_mastery = WeaponMasteryProperty.PUSH
        self.weapon_type = WeaponCategory.SIMPLE_MELEE
        self.damage_type = DamageType.BLUDGEONING
        self.damage_dice = "1d8"
        self.properties = [WeaponProperty.TWO_HANDED]
