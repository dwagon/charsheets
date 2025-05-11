from typing import TYPE_CHECKING, cast

from aenum import extend_enum
from charsheets.constants import Feature, Weapon, Language, Proficiency
from charsheets.features import Darkvision60
from charsheets.features.base_feature import BaseFeature
from charsheets.race2014.base_race import BaseRace
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter

extend_enum(Feature, "DWARVEN_RESILIENCE14", "Dwarven Resilience")
extend_enum(Feature, "DWARVEN_TOUGHNESS14", "Dwarven Toughness")
extend_enum(Feature, "STONE_CUNNING14", "Stonecunning")


#############################################################################
class Dwarf(BaseRace):
    #########################################################################
    def __init__(self):
        super().__init__()
        self.speed = 25

    #########################################################################
    def race_feature(self) -> set[BaseFeature]:
        return {Darkvision60(), DwarvenResilience(), Stonecunning()}

    #########################################################################
    def mod_stat_con(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Dwarf", 2)

    #########################################################################
    def mod_specific_weapon_proficiency(self, character: "BaseCharacter") -> Reason[Weapon]:
        return Reason("Dwarven Combat Training", Weapon.BATTLEAXE, Weapon.HANDAXE, Weapon.LIGHT_HAMMER, Weapon.WARHAMMER)

    #########################################################################
    def mod_add_language(self, character: "BaseCharacter") -> Reason[Language]:
        return Reason("Dwarf", Language.DWARVISH)


#############################################################################
class HillDwarf(Dwarf):
    #########################################################################
    def mod_stat_wis(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Hill Dwarf", 1)

    #########################################################################
    def race_feature(self) -> set[BaseFeature]:
        features = super().race_feature()
        features |= {DwarvenToughness()}
        return features


#############################################################################
class MountainDwarf(Dwarf):
    #########################################################################
    def mod_stat_str(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Mountain Dwarf", 2)

    #########################################################################
    def mod_armour_proficiency(self, character: "BaseCharacter") -> Reason[Proficiency]:
        return Reason(
            "Dwarven Armor Training", cast(Proficiency, Proficiency.LIGHT_ARMOUR), cast(Proficiency, Proficiency.MEDIUM_ARMOUR)
        )


#############################################################################
class DwarvenResilience(BaseFeature):
    tag = Feature.DWARVEN_RESILIENCE14
    _desc = """You have advantage on saving throws against poison, and you have resistance against poison damage."""


#############################################################################
class DwarvenToughness(BaseFeature):
    tag = Feature.DWARVEN_TOUGHNESS14
    hide = True
    _desc = """Your hit point maximum increases by 1, and it increases by 1 every time you gain a level."""

    def mod_hp_bonus(self, character: "BaseCharacter") -> Reason[int]:
        return Reason[int]("Dwarven Toughness", character.level)


#############################################################################
class Stonecunning(BaseFeature):
    tag = Feature.STONE_CUNNING14
    _desc = """Whenever you make an Intelligence (History) check related to the origin of stonework, you are
    considered proficient in the History skill and add double your proficiency bonus to the check instead of your
    normal proficiency bonus."""


# EOF
