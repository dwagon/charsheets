"""Details about weapons"""

from enum import StrEnum, auto
from typing import TYPE_CHECKING, Optional, Any, cast

from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty, Feature, Stat
from charsheets.exception import NotDefined, UnhandledException
from charsheets.reason import Reason, SignedReason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#############################################################################
class Modifiers(StrEnum):
    ATK_BONUS = auto()
    DMG_BONUS = auto()
    NAME = auto()


#############################################################################
class BaseWeapon:
    tag: Weapon

    def __init__(self, **kwargs: Any):
        self.wielder: Optional["Character"] = None
        self.damage_type: DamageType = DamageType.PIERCING
        self.damage_dice: str = ""
        self.weapon_type: Optional[WeaponCategory] = None
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
            except ValueError:
                raise UnhandledException(f"{key} not handled by Weapon")
        return modifiers

    #########################################################################
    def is_ranged(self) -> bool:
        return (
            self.weapon_type in (WeaponCategory.SIMPLE_RANGED, WeaponCategory.MARTIAL_RANGED)
            or WeaponProperty.THROWN in self.properties
        )

    #########################################################################
    def is_finesse(self) -> bool:
        return WeaponProperty.FINESSE in self.properties

    #########################################################################
    @property
    def name(self) -> str:
        if self.modifiers.get(Modifiers.NAME):
            return cast(str, self.modifiers.get(Modifiers.NAME))
        return self.tag.name.title().replace("_", " ")

    #########################################################################
    @property
    def atk_bonus(self) -> SignedReason:
        if self.wielder is None:  # pragma: no coverage
            raise NotDefined("Weapon needs to be added to character")
        result = SignedReason()
        stat = Stat.STRENGTH
        if self.is_ranged():
            stat = Stat.DEXTERITY
        if self.is_finesse():
            if self.wielder.stats[Stat.DEXTERITY].modifier > self.wielder.stats[Stat.STRENGTH].modifier:
                stat = Stat.DEXTERITY
            else:
                stat = Stat.STRENGTH

        if stat == Stat.STRENGTH:
            result.extend(self.check_modifiers("mod_melee_atk_bonus"))  # Str based
            result.extend(self.wielder.melee_atk_bonus())
        else:
            # TODO - Make archery not apply to this
            result.extend(self.check_modifiers("mod_ranged_atk_bonus"))  # Dex based
            result.extend(self.wielder.ranged_atk_bonus())

        if self.modifiers.get(Modifiers.ATK_BONUS):
            result.add("atk_bonus", self.modifiers.get(Modifiers.ATK_BONUS))
        return result

    #########################################################################
    @property
    def dmg_bonus(self) -> SignedReason:
        if self.wielder is None:  # pragma: no coverage
            raise NotDefined("Weapon needs to be added to character")
        result = SignedReason()
        stat = Stat.STRENGTH
        if self.is_ranged():
            stat = Stat.DEXTERITY
        if self.is_finesse():
            if self.wielder.stats[Stat.DEXTERITY].modifier > self.wielder.stats[Stat.STRENGTH].modifier:
                stat = Stat.DEXTERITY
            else:
                stat = Stat.STRENGTH
        if stat == Stat.DEXTERITY:
            result.extend(self.wielder.ranged_dmg_bonus())
            result.extend(self.check_modifiers("mod_ranged_dmg_bonus"))
        else:
            result.extend(self.wielder.melee_dmg_bonus())
            result.extend(self.check_modifiers("mod_melee_dmg_bonus"))
        if self.modifiers.get(Modifiers.DMG_BONUS):
            result.add("dmg_bonus", self.modifiers.get(Modifiers.DMG_BONUS))
        return result

    #########################################################################
    @property
    def dmg_dice(self) -> str:
        return self.damage_dice

    #########################################################################
    @property
    def dmg_type(self) -> str:
        return self.damage_type.name

    #########################################################################
    @property
    def mastery(self) -> str:
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

        result = Reason[Any]()
        for feat in self.wielder.features:
            if hasattr(feat, modifier):
                result.add(str(feat), getattr(feat, modifier)(self, self.wielder))
        return result


# EOF
