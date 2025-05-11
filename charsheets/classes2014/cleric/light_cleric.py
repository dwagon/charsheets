from typing import TYPE_CHECKING, Any

from aenum import extend_enum
from charsheets.classes2014.cleric.cleric import Cleric
from charsheets.constants import Stat, Feature, Recovery
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter


extend_enum(Feature, "LIGHT_DOMAIN_SPELLS14", "Light Domain Spells")
extend_enum(Feature, "WARDING_FLARE14", "Warding Flare")


#################################################################################
class LightCleric(Cleric):
    def level1(self, **kwargs: Any):
        super().level1(**kwargs)
        self.add_feature(LightDomainSpells())
        self.add_feature(WardingFlare())


#################################################################################
class LightDomainSpells(BaseFeature):
    tag = Feature.LIGHT_DOMAIN_SPELLS14
    _desc = "Spells"
    hide = True

    def mod_add_prepared_spells(self, character: "BaseCharacter") -> Reason[Spell]:
        return Reason("Light Domain Spells", Spell.BURNING_HANDS, Spell.FAERIE_FIRE, Spell.LIGHT)


#################################################################################
class WardingFlare(BaseFeature):
    tag = Feature.WARDING_FLARE14
    recovery = Recovery.LONG_REST
    _desc = """When you are attacked by a creature within 20 feet of you that you can see, you can use your reaction 
    to impose disadvantage on the attack roll causing light to flare before the attacker before it hits or misses. An 
    attacker that can't be blinded is immune to this feature."""

    @property
    def goes(self) -> int:
        return max(1, self.owner.stats[Stat.WISDOM].modifier)
