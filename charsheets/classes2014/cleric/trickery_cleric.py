from typing import TYPE_CHECKING, Any

from aenum import extend_enum
from charsheets.classes2014.cleric.cleric import Cleric
from charsheets.constants import Feature
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter

extend_enum(Feature, "TRICKERY_DOMAIN_SPELLS14", "Trickery Domain Spells")
extend_enum(Feature, "BLESSING_OF_THE_TRICKSTER14", "Blessing of the Trickster")


#################################################################################
class TrickeryCleric(Cleric):
    def level1(self, **kwargs: Any):
        super().level1(**kwargs)
        self.add_feature(TrickeryDomainSpells())
        self.add_feature(BlessingOfTheTrickster())


#################################################################################
class TrickeryDomainSpells(BaseFeature):
    tag = Feature.TRICKERY_DOMAIN_SPELLS14
    _desc = "Spells"
    hide = True

    def mod_add_prepared_spells(self, character: "BaseCharacter") -> Reason[Spell]:
        return Reason("Trickery Domain Spells", Spell.CHARM_PERSON, Spell.DISGUISE_SELF)


#################################################################################
class BlessingOfTheTrickster(BaseFeature):
    tag = Feature.BLESSING_OF_THE_TRICKSTER14
    _desc = """You can use your action to touch a willing creature other than yourself to give it advantage on 
    Dexterity(Stealth) checks. This blessin lasts for 1 hour or until you use this feature again."""
