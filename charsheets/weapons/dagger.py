from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class Dagger(BaseWeapon):
    tag = Weapon.DAGGER

    def __init__(self, **kwargs):
        super().__init__(DamageType.PIERCING, WeaponCategory.SIMPLE_MELEE, "1d4", **kwargs)
        self.weapon_mastery = WeaponMasteryProperty.NICK
        self.properties = [WeaponProperty.FINESSE, WeaponProperty.LIGHT, WeaponProperty.THROWN, WeaponProperty.RANGE]
        self.range = (20, 60)


# EOF
