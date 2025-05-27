from enum import StrEnum, auto
from typing import TYPE_CHECKING

from aenum import extend_enum
from charsheets.attack import Attack
from charsheets.constants import Feature, Language, DamageType, Stat
from charsheets.exception import UnhandledException
from charsheets.features.base_feature import BaseFeature
from charsheets.race2014.base_race import BaseRace
from charsheets.reason import Reason, SignedReason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter

extend_enum(Feature, "DRACONIC_ANCESTRY14", "Draconic Ancestry")
extend_enum(Feature, "BREATH_WEAPON14", "Breath Weapon")
extend_enum(Feature, "DAMAGE_RESISTANCE14", "Damage Resistance")


#############################################################################
class Ancestry14(StrEnum):
    BLACK = auto()
    BLUE = auto()
    BRASS = auto()
    BRONZE = auto()
    COPPER = auto()
    GOLD = auto()
    GREEN = auto()
    RED = auto()
    SILVER = auto()
    WHITE = auto()


#############################################################################
class Dragonborn(BaseRace):
    #########################################################################
    def __init__(self, ancestry: Ancestry14):
        super().__init__()
        self.ancestry = ancestry
        self.speed = 30

    #########################################################################
    def race_feature(self) -> set[BaseFeature]:
        return {DraconicAncestry(), BreathWeapon(), DamageResistance()}

    #########################################################################
    def mod_stat_str(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Dragonborn", 2)

    #########################################################################
    def mod_stat_cha(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Dragonborn", 1)

    #########################################################################
    def mod_add_language(self, character: "BaseCharacter") -> Reason[Language]:
        return Reason("Dragonborn", Language.DRACONIC)

    #########################################################################
    def mod_add_damage_resistances(self, character: "BaseCharacter") -> Reason[DamageType]:
        return Reason("Dragonborn", damage_type(self.ancestry)[0])


#############################################################################
class DraconicAncestry(BaseFeature):
    tag = Feature.DRACONIC_ANCESTRY14
    hide = True
    _desc = """You have draconic ancestry"""


#############################################################################
class BreathWeapon(BaseFeature):
    tag = Feature.BREATH_WEAPON14

    @property
    def desc(self) -> str:
        assert self.owner is not None
        save_type = damage_type(self.owner.race.ancestry)[1]
        dc = 8 + self.owner.stats[Stat.CONSTITUTION].modifier + self.owner.proficiency_bonus
        return f"""You can use your action to exhale destructive energy. When you use your breath weapon, each creature in
    the area of the exhalation must make a {save_type.title()} saving throw DC {dc}"""

    def mod_add_attack(self, character: "BaseCharacter") -> Reason[Attack]:
        if character.level >= 16:
            dmg_dice = "5d6"
        elif character.level >= 11:
            dmg_dice = "4d6"
        elif character.level >= 6:
            dmg_dice = "3d6"
        else:
            dmg_dice = "2d6"

        return Reason(
            "Breath Weapon",
            Attack(
                f"{character.race.ancestry.title()} breath weapon",
                atk_bonus=SignedReason("None", 0),
                dmg_dice=dmg_dice,
                dmg_bonus=SignedReason("None", 0),
                dmg_type=damage_type(character.race.ancestry)[0],
            ),
        )


#############################################################################
class DamageResistance(BaseFeature):
    tag = Feature.DAMAGE_RESISTANCE14

    @property
    def desc(self) -> str:
        assert self.owner is not None
        return f"""You have resistance to {damage_type(self.owner.race.ancestry)[0].title()}"""


#########################################################################
def damage_type(ancestry: Ancestry14) -> tuple[DamageType, Stat]:
    match ancestry:
        case Ancestry14.BLACK:
            return DamageType.ACID, Stat.DEXTERITY
        case Ancestry14.BLUE:
            return DamageType.LIGHTNING, Stat.DEXTERITY
        case Ancestry14.BRASS:
            return DamageType.FIRE, Stat.DEXTERITY
        case Ancestry14.BRONZE:
            return DamageType.LIGHTNING, Stat.DEXTERITY
        case Ancestry14.COPPER:
            return DamageType.ACID, Stat.DEXTERITY
        case Ancestry14.GOLD:
            return DamageType.FIRE, Stat.DEXTERITY
        case Ancestry14.GREEN:
            return DamageType.POISON, Stat.CONSTITUTION
        case Ancestry14.RED:
            return DamageType.FIRE, Stat.DEXTERITY
        case Ancestry14.SILVER:
            return DamageType.COLD, Stat.CONSTITUTION
        case Ancestry14.WHITE:
            return DamageType.COLD, Stat.CONSTITUTION
    raise UnhandledException(f"Unhandled dragonborn ancestry {ancestry}")  # pragma: no coverage


# EOF
