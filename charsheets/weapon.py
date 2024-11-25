""" Details about weapons"""

from typing import TYPE_CHECKING, Optional, Type

from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty, Ability
from charsheets.util import import_generic
from charsheets.exception import UnhandledException
from charsheets.reason import Reason, SignedReason


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
    def atk_bonus(self) -> SignedReason:
        result = SignedReason()
        if self.is_ranged():
            result.extend(self.wielder.ranged_atk_bonus())
            result.extend(self.check_modifiers("ranged_atk_bonus"))
        else:
            result.extend(self.wielder.melee_atk_bonus())
            result.extend(self.check_modifiers("melee_atk_bonus"))
        return result

    #########################################################################
    @property
    def dmg_bonus(self) -> SignedReason:
        result = SignedReason()
        if self.is_ranged():
            result.extend(self.wielder.ranged_dmg_bonus())
            result.extend(self.check_modifiers("ranged_dmg_bonus"))
        else:
            result.extend(self.wielder.melee_dmg_bonus())
            result.extend(self.check_modifiers("melee_dmg_bonus"))
        return result

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
        if Ability.WEAPON_MASTERY not in self.wielder.abilities:
            return ""
        return self.weapon_mastery.name if self.weapon_mastery else ""

    #########################################################################
    def __repr__(self):
        return f"<Weapon {self.name} {self.atk_bonus} {self.dmg_dice} + {self.dmg_bonus}/{self.dmg_type}>"

    #########################################################################
    def check_modifiers(self, modifier: str) -> Reason:
        """Check everything that can modify a value"""
        result = Reason()
        for feat in self.wielder.feats_list:
            if hasattr(feat, modifier):
                result.add(f"feat {feat}", getattr(feat, modifier)(self, self.wielder))
        for ability in self.wielder.abilities:
            if hasattr(ability, modifier):
                result.add(f"ability {ability}", getattr(ability, modifier)(self, self.wielder))
        return result


#############################################################################
WEAPON_MAPPING: dict[Weapon, Type[BaseWeapon]] = import_generic(class_prefix="Weapon", path="weapons")


#################################################################################
def weapon_picker(weapon: Weapon, wielder: "Character") -> BaseWeapon:
    try:
        return WEAPON_MAPPING[weapon](wielder)
    except KeyError as e:
        raise UnhandledException(f"Unknown weapon {weapon}") from e


# EOF
