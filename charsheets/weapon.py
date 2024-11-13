""" Details about weapons"""

from typing import TYPE_CHECKING, Optional, Type

from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty
from charsheets.util import import_generic
from charsheets.exception import UnhandledException


if TYPE_CHECKING:
    from charsheets.character import Character


#############################################################################
class BaseWeapon:
    tag: Weapon

    def __init__(self, wielder: "Character"):
        self.wielder: "Character" = wielder
        self.damage_type: DamageType = DamageType.PIERCING
        self.damage_dice = ""
        self.weapon_type: Optional[WeaponCategory] = None
        self.weapon_mastery: Optional[WeaponMasteryProperty] = None
        self.properties: list[WeaponProperty] = []
        self.range: tuple[int, int] = (0, 0)
        self.versatile_damage_dice = ""

    #########################################################################
    def is_ranged(self) -> bool:
        return self.weapon_type in (WeaponCategory.SIMPLE_RANGED, WeaponCategory.MARTIAL_RANGED)

    #########################################################################
    @property
    def name(self) -> str:
        return self.tag.name.replace("_", " ")

    #########################################################################
    @property
    def atk_bonus(self) -> str:
        mod = 0
        if self.is_ranged():
            mod += self.wielder.dexterity.modifier
            mod += self.wielder.ranged_atk_bonus()
        else:
            mod += self.wielder.strength.modifier
            mod += self.wielder.melee_atk_bonus()
        sign = "+" if mod >= 0 else "-"
        return f"{sign}{abs(mod)}"

    #########################################################################
    @property
    def dmg_bonus(self) -> str:
        if self.is_ranged():
            mod = self.wielder.dexterity.modifier
            mod += self.wielder.ranged_dmg_bonus()
        else:
            mod = self.wielder.strength.modifier
            mod += self.wielder.melee_dmg_bonus()
        sign = "+" if mod >= 0 else "-"
        return f"{sign}{abs(mod)}"

    #########################################################################
    @property
    def dmg_dice(self):
        return self.damage_dice

    #########################################################################
    @property
    def dmg_type(self) -> str:
        return self.damage_type.name

    #########################################################################
    @property
    def mastery(self) -> str:
        return self.weapon_mastery.name if self.weapon_mastery else ""

    #########################################################################
    def __repr__(self):
        return f"<Weapon {self.name} {self.atk_bonus} {self.dmg_dice} + {self.dmg_bonus}/{self.dmg_type}>"


#############################################################################
WEAPON_MAPPING: dict[Weapon, Type[BaseWeapon]] = import_generic(class_prefix="Weapon", path="weapons")


#################################################################################
def weapon_picker(weapon: Weapon, wielder: "Character") -> BaseWeapon:
    try:
        return WEAPON_MAPPING[weapon](wielder)
    except KeyError as e:
        raise UnhandledException(f"Unknown weapon {weapon}") from e


# EOF
