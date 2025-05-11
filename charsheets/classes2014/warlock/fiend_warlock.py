from typing import Any, TYPE_CHECKING

from aenum import extend_enum
from charsheets.classes2014.warlock.warlock import Warlock
from charsheets.constants import Stat, Feature
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter

extend_enum(Feature, "DARKONES_BLESSING14", "Dark One's Blessing")
extend_enum(Feature, "FIEND_EXPANDED_SPELLS14", "Fiend Expanded Spell List")


#############################################################################
class FiendWarlock(Warlock):
    def level1(self, **kwargs: Any):
        super().level1(**kwargs)
        self.add_feature(FiendExpandedSpells())
        self.add_feature(DarkOnesBlessing())


#############################################################################
class FiendExpandedSpells(BaseFeature):
    tag = Feature.FIEND_EXPANDED_SPELLS14
    hide = True
    _desc = """You know more spells"""

    def mod_add_prepared_spells(self, character: "BaseCharacter") -> Reason[Spell]:
        return Reason("Fiend Spells", Spell.BURNING_HANDS, Spell.COMMAND)


#############################################################################
class DarkOnesBlessing(BaseFeature):
    tag = Feature.DARKONES_BLESSING14

    @property
    def desc(self) -> str:
        assert self.owner.warlock is not None
        hp = max(1, self.owner.stats[Stat.CHARISMA].modifier + self.owner.warlock.level)
        return f"""When you reduce a hostile creature to 0 hit points, you gain {hp} temporary hit points."""


# EOF
