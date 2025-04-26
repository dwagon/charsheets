from typing import TYPE_CHECKING

from aenum import extend_enum

from charsheets.constants import Feature, Language
from charsheets.features.base_feature import BaseFeature
from charsheets.race2014.base_race import BaseRace
from charsheets.reason import Reason

if TYPE_CHECKING:
    from charsheets.character import BaseCharacter

extend_enum(Feature, "LUCKY14", "Lucky")
extend_enum(Feature, "BRAVE14", "Brave")
extend_enum(Feature, "HALFLING_NIMBLENESS14", "Halfling Nimbleness")
extend_enum(Feature, "NATURALLY_STEALTHY14", "Naturally Stealthy")
extend_enum(Feature, "STOUT_RESILIENCE14", "Stout Resilience")


#############################################################################
class Halfling(BaseRace):
    #########################################################################
    def __init__(self):
        super().__init__()
        self.speed = 25

    #########################################################################
    def race_feature(self) -> set[BaseFeature]:
        return {
            Lucky(),
            Brave(),
            HalflingNimbleness(),
        }

    #########################################################################
    def mod_stat_dex(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Halfling", 2)

    #########################################################################
    def mod_add_language(self, character: "BaseCharacter") -> Reason[Language]:
        return Reason("Halflinf", Language.HALFLING)


#############################################################################
class Lightfoot(Halfling):
    #########################################################################
    def mod_stat_cha(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Lightfoot Halfling", 1)

    #########################################################################
    def race_feature(self) -> set[BaseFeature]:
        feats = super().race_feature()
        feats.add(NaturallyStealthy())
        return feats


#############################################################################
class Stout(Halfling):

    #########################################################################
    def mod_stat_con(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("Stout Halfling", 1)

    #########################################################################
    def race_feature(self) -> set[BaseFeature]:
        feats = super().race_feature()
        feats.add(StoutResilience())
        return feats


#############################################################################
class Lucky(BaseFeature):
    tag = Feature.LUCKY14
    _desc = """When you roll a 1 on a d20 for an attack roll, ability check, or saving throw, you can reroll the die and
    must use the new roll."""


#############################################################################
class Brave(BaseFeature):
    tag = Feature.BRAVE14
    _desc = """You have advantage on saving throws against being frightened."""


#############################################################################
class HalflingNimbleness(BaseFeature):
    tag = Feature.HALFLING_NIMBLENESS14
    _desc = """You can move through the space of any creature that is of a size larger than yours."""


#############################################################################
class NaturallyStealthy(BaseFeature):
    tag = Feature.NATURALLY_STEALTHY14
    _desc = """You can attempt to hide even when you are obscured only by a creatures that is at least one size
    larger than you."""


#############################################################################
class StoutResilience(BaseFeature):
    tag = Feature.STOUT_RESILIENCE14
    _desc = """You have advantage on saving throws against poison, and you have resistance against poison damage."""


# EOF
