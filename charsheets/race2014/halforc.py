from typing import TYPE_CHECKING

from aenum import extend_enum

from charsheets.constants import Feature, Language, Skill, Recovery
from charsheets.features import Darkvision60
from charsheets.features.base_feature import BaseFeature
from charsheets.race2014.base_race import BaseRace
from charsheets.reason import Reason

if TYPE_CHECKING:
    from charsheets.character import BaseCharacter

extend_enum(Feature, "MENACING14", "Menacing")
extend_enum(Feature, "RELENTLESS_ENDURANCE14", "Relentless Endurance")
extend_enum(Feature, "SAVAGE_ATTACKS14", "Savage Attacks")


#############################################################################
class HalfOrc(BaseRace):
    #########################################################################
    def __init__(self):
        super().__init__()
        self.speed = 30

    #########################################################################
    def race_feature(self) -> set[BaseFeature]:
        return {Darkvision60(), Menacing(), RelentlessEndurance(), SavageAttacks()}

    #########################################################################
    def mod_stat_str(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("HalfOrc", 2)

    #########################################################################
    def mod_stat_con(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("HalfOrc", 1)

    #########################################################################
    def mod_add_language(self, character: "BaseCharacter") -> Reason[Language]:
        return Reason("HalfOrc", Language.ORC)


#############################################################################
class Menacing(BaseFeature):
    tag = Feature.MENACING14
    hide = True
    _desc = """You gain proficiency in the Intimidation skill."""

    def mod_add_skill_proficiency(self, character: "BaseCharacter") -> Reason[Skill]:
        return Reason("Menacing", Skill.INTIMIDATION)


#############################################################################
class RelentlessEndurance(BaseFeature):
    tag = Feature.RELENTLESS_ENDURANCE14
    _goes = 1
    recovery = Recovery.LONG_REST
    _desc = """When you are reduced to 0 hit points byt not killed outright, you can drop to 1 hit points instead."""


#############################################################################
class SavageAttacks(BaseFeature):
    tag = Feature.SAVAGE_ATTACKS14
    _desc = """When you score a critical hit with a melee weapon attack, you can roll one of the weapon's
    damage dice one additional time and add it to the extra damage of the critical hit."""


# EOF
