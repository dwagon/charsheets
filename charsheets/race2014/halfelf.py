from typing import TYPE_CHECKING

from aenum import extend_enum
from charsheets.constants import Language, Feature, Stat, Skill
from charsheets.features import Darkvision60
from charsheets.features.base_feature import BaseFeature
from charsheets.race2014.base_race import BaseRace
from charsheets.reason import Reason

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter

extend_enum(Feature, "HALFELF_FEY_ANCESTRY14", "Fey Ancestry")


#############################################################################
class HalfElf(BaseRace):
    #########################################################################
    def __init__(self, language: Language, stat1: Stat, stat2: Stat, skill1: Skill, skill2: Skill):
        super().__init__()
        self.speed = 30
        self.language = language
        self.stats = (stat1, stat2)
        self.skills = (skill1, skill2)
        assert stat1 != Stat.CHARISMA
        assert stat2 != Stat.CHARISMA

    #########################################################################
    def race_feature(self) -> set[BaseFeature]:
        return {Darkvision60(), FeyAncestry()}

    #########################################################################
    def mod_add_language(self, character: "BaseCharacter") -> Reason[Language]:
        return Reason("HalfElf", Language.ELVISH, self.language)

    #########################################################################
    def mod_stat_str(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("HalfElf", 1) if Stat.STRENGTH in self.stats else Reason()

    #########################################################################
    def mod_stat_dex(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("HalfElf", 1) if Stat.DEXTERITY in self.stats else Reason()

    #########################################################################
    def mod_stat_con(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("HalfElf", 1) if Stat.CONSTITUTION in self.stats else Reason()

    #########################################################################
    def mod_stat_int(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("HalfElf", 1) if Stat.INTELLIGENCE in self.stats else Reason()

    #########################################################################
    def mod_stat_wis(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("HalfElf", 1) if Stat.WISDOM in self.stats else Reason()

    #########################################################################
    def mod_stat_cha(self, character: "BaseCharacter") -> Reason[int]:
        return Reason("HalfElf", 2)

    #############################################################################
    def mod_add_skill_proficiency(self, character: "BaseCharacter") -> Reason[Skill]:
        return Reason("HalfElf", *self.skills)


#############################################################################
class FeyAncestry(BaseFeature):
    tag = Feature.HALFELF_FEY_ANCESTRY14
    _desc = """You have advantage on saving throws against being charmed, and magic can't put you to sleep."""


# EOF
