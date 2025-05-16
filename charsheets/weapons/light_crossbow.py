from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.weapons.base_weapon import BaseWeapon


#############################################################################
class LightCrossbow(BaseWeapon):
    tag = Weapon.LIGHT_CROSSBOW

    def __init__(self, **kwargs):
        super().__init__(DamageType.PIERCING, WeaponCategory.SIMPLE_RANGED, "1d8", **kwargs)
        self.weapon_mastery = WeaponMasteryProperty.SLOW
        self.properties = [WeaponProperty.AMMUNITION, WeaponProperty.RANGE, WeaponProperty.LOADING, WeaponProperty.TWO_HANDED]
        self.range = (80, 320)
