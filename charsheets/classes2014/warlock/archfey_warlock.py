from typing import Any, TYPE_CHECKING

from aenum import extend_enum
from charsheets.classes2014.warlock.warlock import Warlock
from charsheets.constants import Feature, Recovery
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter

extend_enum(Feature, "ARCHFEY_EXPANDED_SPELLS14", "Archfey Expanded Spell List")
extend_enum(Feature, "FEY_PRESENCE14", "Fey Presence")


#############################################################################
class ArchFeyWarlock(Warlock):
    def level1(self, **kwargs: Any):
        super().level1(**kwargs)
        self.add_feature(ArchfFeyExpandedSpells())
        self.add_feature(FeyPresence())


#############################################################################
class ArchfFeyExpandedSpells(BaseFeature):
    tag = Feature.ARCHFEY_EXPANDED_SPELLS14
    hide = True
    _desc = """You know more spells"""

    def mod_add_prepared_spells(self, character: "BaseCharacter") -> Reason[Spell]:
        return Reason("ArchFey Spells", Spell.FAERIE_FIRE, Spell.SLEEP)


#############################################################################
class FeyPresence(BaseFeature):
    tag = Feature.FEY_PRESENCE14
    recovery = Recovery.SHORT_REST
    _desc = """As an action you can cause each creature in a 10-foot cube originating from you to make a Wisdom
    saving throw against your walock spell save DC. The creatures that fail their saving throws are all charmed
    or frightened by you (your choice) until the end of your next turn."""


# EOF
