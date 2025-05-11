from typing import cast, TYPE_CHECKING, Any

from aenum import extend_enum
from charsheets.classes2014.cleric.cleric import Cleric
from charsheets.constants import Proficiency, Feature
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter

extend_enum(Feature, "DISCIPLE_OF_LIFE14", "Disciple of Life")
extend_enum(Feature, "LIFE_DOMAIN_SPELLS14", "Life Domain Spells")


#################################################################################
class LifeCleric(Cleric):
    def level1(self, **kwargs: Any):
        super().level1(**kwargs)
        assert self.character is not None
        self.add_feature(LifeDomainSpells())
        self.add_feature(DiscipleOfLife())
        self.character.add_armor_proficiency(Reason("Life Cleric", cast(Proficiency, Proficiency.HEAVY_ARMOUR)))


#################################################################################
class DiscipleOfLife(BaseFeature):
    tag = Feature.DISCIPLE_OF_LIFE14
    _desc = """Whenever you use a spell of 1st level or higher to restore hit points to a creature, the creature 
            regains additional hit points equal to 2 + the spells level"""


#################################################################################
class LifeDomainSpells(BaseFeature):
    tag = Feature.LIFE_DOMAIN_SPELLS14
    _desc = "Spells"
    hide = True

    def mod_add_prepared_spells(self, character: "BaseCharacter") -> Reason[Spell]:
        return Reason("Life Domain Spells", Spell.BLESS, Spell.CURE_WOUNDS)
