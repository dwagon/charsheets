""" Details about weapons"""

from typing import TYPE_CHECKING, Optional, Any

from charsheets.constants import Weapon, WeaponMasteryProperty, DamageType, WeaponCategory, WeaponProperty, Ability
from charsheets.reason import Reason, SignedReason

if TYPE_CHECKING:  # pragma: no coverage
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
        return (
            self.weapon_type in (WeaponCategory.SIMPLE_RANGED, WeaponCategory.MARTIAL_RANGED)
            or WeaponProperty.THROWN in self.properties
        )

    #########################################################################
    @property
    def name(self) -> str:
        return self.tag.name.title().replace("_", " ")

    #########################################################################
    @property
    def atk_bonus(self) -> SignedReason:
        result = SignedReason()
        if self.is_ranged():
            result.extend(self.wielder.ranged_atk_bonus())
            result.extend(self.check_modifiers("mod_ranged_atk_bonus"))
        else:
            result.extend(self.wielder.melee_atk_bonus())
            result.extend(self.check_modifiers("mod_melee_atk_bonus"))
        return result

    #########################################################################
    @property
    def dmg_bonus(self) -> SignedReason:
        result = SignedReason()
        if self.is_ranged():
            result.extend(self.wielder.ranged_dmg_bonus())
            result.extend(self.check_modifiers("mod_ranged_dmg_bonus"))
        else:
            result.extend(self.wielder.melee_dmg_bonus())
            result.extend(self.check_modifiers("mod_melee_dmg_bonus"))
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
        if self.wielder.has_ability(Ability.WEAPON_MASTERY):
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

        result = Reason[Any]()
        for feat in self.wielder.feats_list:
            if hasattr(feat, modifier):
                result.add(str(feat), getattr(feat, modifier)(self, self.wielder, self))
        for ability in self.wielder.abilities:
            if hasattr(ability, modifier):
                result.add(str(ability), getattr(ability, modifier)(self, self.wielder, self))
        return result


# EOF
