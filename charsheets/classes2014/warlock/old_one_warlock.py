from typing import Any, TYPE_CHECKING

from aenum import extend_enum
from charsheets.classes2014.warlock.warlock import Warlock
from charsheets.constants import Stat, Feature
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter

extend_enum(Feature, "AWAKENED_MIND14", "Awakened Mind")
extend_enum(Feature, "GREATOLDONE_EXPANDED_SPELLS14", "GreatOldOne Expanded Spell List")


#############################################################################
class GreatOldOneWarlock(Warlock):
    def level1(self, **kwargs: Any):
        super().level1(**kwargs)
        self.add_feature(GreatOldOneExpandedSpells())
        self.add_feature(AwakenedMind())


#############################################################################
class DarkOnesBlessing(BaseFeature):
    tag = Feature.DARKONES_BLESSING14

    @property
    def desc(self) -> str:
        assert self.owner.warlock is not None
        hp = max(1, self.owner.stats[Stat.CHARISMA].modifier + self.owner.warlock.level)
        return f"""When you reduce a hostile creature to 0 hit points, you gain {hp} temporary hit points."""


#############################################################################
class GreatOldOneExpandedSpells(BaseFeature):
    tag = Feature.GREATOLDONE_EXPANDED_SPELLS14
    hide = True
    _desc = """You know more spells"""

    def mod_add_prepared_spells(self, character: "BaseCharacter") -> Reason[Spell]:
        return Reason("GreatOldOne Spells", Spell.DISSONANT_WHISPERS, Spell.TASHAS_HIDEOUS_LAUGHTER)


#############################################################################
class AwakenedMind(BaseFeature):
    tag = Feature.AWAKENED_MIND14
    _desc = """You can telepathically speak to any creature you can see within 30 feet of you. You don't need to 
    share a language with the creature for ot to understand your telepathic utterances, but the creature must be able 
    to understand at least one language."""


# EOF
