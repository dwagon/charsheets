"""Details about weapons"""

import sys
import traceback
from enum import StrEnum, auto
from typing import TYPE_CHECKING, Optional, Any, cast

from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty, Feature, Stat, Mod
from charsheets.exception import NotDefined, UnhandledException
from charsheets.reason import Reason, SignedReason
from charsheets.items.base_item import BaseItem

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class Modifiers(StrEnum):
    """For magic modifiers to weapons"""

    ATK_BONUS = auto()
    DMG_BONUS = auto()
    NAME = auto()


#############################################################################
class BaseWeapon(BaseItem):
    """Base Weapon Class"""

    tag: Weapon

    def __init__(self, damage_type: DamageType, weapon_category: WeaponCategory, damage_dice: str, **kwargs: Any):
        super().__init__(**kwargs)
        self.wielder: Optional["Character"] = None
        self._damage_type: DamageType = damage_type
        self._damage_dice: str = damage_dice
        self.weapon_category: WeaponCategory = weapon_category
        self.weapon_mastery: Optional[WeaponMasteryProperty] = None
        self.properties: list[WeaponProperty] = []
        self.range: tuple[int, int] = (0, 0)
        self.versatile_damage_dice: str = ""
        self.modifiers: dict[Modifiers, Any] = self.validate_kwargs(kwargs)

    #########################################################################
    def validate_kwargs(self, kwargs) -> dict[Modifiers, Any]:
        """Ensure that all the kwargs are spelt correctly etc."""
        modifiers: dict[Modifiers, Any] = {}

        for key, value in kwargs.items():
            try:
                modifiers[Modifiers(key)] = value
            except ValueError as exc:
                raise UnhandledException(f"{key} not handled by Weapon") from exc
        return modifiers

    #########################################################################
    def is_ranged(self) -> bool:
        """Is this weapon considered ranged?"""
        return (
            self.weapon_category in (WeaponCategory.SIMPLE_RANGED, WeaponCategory.MARTIAL_RANGED)
            or WeaponProperty.THROWN in self.properties
        )

    #########################################################################
    def is_finesse(self) -> bool:
        """Is this a finesse weapon?"""
        return WeaponProperty.FINESSE in self.properties

    #########################################################################
    @property
    def name(self) -> str:
        """Return name of weapon"""
        if self.modifiers.get(Modifiers.NAME):
            return cast(str, self.modifiers.get(Modifiers.NAME))
        return self.tag.name.title().replace("_", " ")

    #########################################################################
    @property
    def atk_bonus(self) -> SignedReason:
        """Return the attack bonus"""
        result = SignedReason()

        try:
            if self.wielder is None:  # pragma: no coverage
                raise NotDefined("Weapon needs to be added to character")
            stat = self.stat_to_use()
            result.add("Prof Bonus", self.wielder.proficiency_bonus)
            if stat == Stat.STRENGTH:
                result.extend(self.check_modifiers(Mod.MOD_MELEE_ATK_BONUS))
                result.add("str mod", self.wielder.stats[Stat.STRENGTH].modifier)
            else:
                if self.is_ranged():
                    result.extend(self.check_modifiers(Mod.MOD_RANGED_ATK_BONUS))
                result.add("dex mod", self.wielder.stats[Stat.DEXTERITY].modifier)

            if self.modifiers.get(Modifiers.ATK_BONUS):
                result.add("atk_bonus", self.modifiers.get(Modifiers.ATK_BONUS))
        except Exception as exc:
            print(f"Exception '{exc}' in atk_bonus", file=sys.stderr)
            print(traceback.format_exc(), file=sys.stderr)
            raise
        return result

    #########################################################################
    def stat_to_use(self) -> Stat:
        """What stat to use (Str or Dex) for determining to hit / dmg"""
        assert self.wielder is not None
        stat = Stat.STRENGTH
        if self.is_ranged():
            stat = Stat.DEXTERITY
        if self.is_finesse():
            if self.wielder.stats[Stat.DEXTERITY].modifier > self.wielder.stats[Stat.STRENGTH].modifier:
                stat = Stat.DEXTERITY
            else:
                stat = Stat.STRENGTH
        return stat

    #########################################################################
    @property
    def dmg_bonus(self) -> SignedReason:
        """Return the damage bonus"""
        if self.wielder is None:  # pragma: no coverage
            raise NotDefined("Weapon needs to be added to character")
        result = SignedReason()
        stat = self.stat_to_use()
        if stat == Stat.STRENGTH:
            result.extend(Reason("str mod", self.wielder.stats[Stat.STRENGTH].modifier))
            result.extend(self.check_modifiers(Mod.MOD_MELEE_DMG_BONUS))
        else:
            result.extend(Reason("dex mod", self.wielder.stats[Stat.DEXTERITY].modifier))
            result.extend(self.check_modifiers(Mod.MOD_RANGED_DMG_BONUS))
        if self.modifiers.get(Modifiers.DMG_BONUS):
            result.add("dmg_bonus", self.modifiers.get(Modifiers.DMG_BONUS))
        return result

    #########################################################################
    @property
    def dmg_dice(self) -> str:
        """What damage dice to use"""
        if mod := self.check_modifiers(Mod.MOD_DMG_DICE):
            return sorted(_.value for _ in mod)[-1]
        return self._damage_dice

    #########################################################################
    @property
    def damage_type(self) -> DamageType:
        """What type of damage does this weapon inflict?"""
        if dmg_type := self.check_modifiers(Mod.MOD_DMG_TYPE):
            return dmg_type[0].value
        return self._damage_type

    #########################################################################
    @property
    def dmg_type(self) -> str:
        """A string version of the damage type"""
        return self.damage_type.name

    #########################################################################
    @property
    def mastery(self) -> str:
        """Name of the weapon mastery - if appropriate"""
        if self.wielder is None:  # pragma: no coverage
            raise NotDefined("Weapon needs to be added to character")
        if self.wielder.has_feature(Feature.WEAPON_MASTERY):
            return self.weapon_mastery.name if self.weapon_mastery else ""
        return ""

    #########################################################################
    def __repr__(self):
        return f"<Weapon {self.name} {self.atk_bonus} {self.dmg_dice} + {self.dmg_bonus}/{self.dmg_type.title()}>"

    #########################################################################
    def __lt__(self, other: "Weapon") -> bool:
        return self.name < other.name

    #########################################################################
    def __eq__(self, other: object) -> bool:
        # sourcery skip: assign-if-exp, reintroduce-else
        if not isinstance(other, BaseWeapon):
            return False
        return self.tag == other.tag

    #########################################################################
    def __hash__(self):
        return hash(self.tag)

    #########################################################################
    def check_modifiers(self, modifier: str) -> Reason[Any]:
        """Check everything that can modify a value"""
        # print(f"DBG weapon.check_modifiers {modifier=}", file=sys.stderr)

        if self.wielder is None:  # pragma: no coverage
            raise NotDefined("Weapon needs to be added to character")

        result = self.wielder.check_weapon_modifiers(self, modifier)

        return result


# EOF
