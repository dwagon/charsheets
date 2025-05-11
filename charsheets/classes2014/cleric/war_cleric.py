from typing import cast, Any, TYPE_CHECKING

from aenum import extend_enum
from charsheets.classes2014.cleric.cleric import Cleric
from charsheets.constants import Feature, Proficiency, Recovery, Stat
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter

extend_enum(Feature, "WAR_DOMAIN_SPELLS14", "War Domain Spells")
extend_enum(Feature, "WAR_PRIEST14", "War Priest")


#################################################################################
class WarCleric(Cleric):
    def level1(self, **kwargs: Any):
        super().level1(**kwargs)
        self.add_feature(WarDomainSpells())
        self.add_feature(WarPriest())
        assert self.character is not None
        self.character.add_armor_proficiency(Reason("War Cleric", cast(Proficiency, Proficiency.HEAVY_ARMOUR)))
        self.character.add_weapon_proficiency(Reason("War Cleric", cast(Proficiency, Proficiency.MARTIAL_WEAPONS)))


#################################################################################
class WarDomainSpells(BaseFeature):
    tag = Feature.WAR_DOMAIN_SPELLS14
    _desc = "Spells"
    hide = True

    def mod_add_prepared_spells(self, character: "BaseCharacter") -> Reason[Spell]:
        return Reason("War Domain Spells", Spell.DIVINE_FAVOR, Spell.SHIELD_OF_FAITH)


#################################################################################
class WarPriest(BaseFeature):
    tag = Feature.WAR_PRIEST14
    recovery = Recovery.LONG_REST
    _desc = """Your god delivers bolts of inspiration to you while you are engaged in battle. When you use the Attack 
    action, you can make one weapon attack as a bonus action"""

    @property
    def goes(self) -> int:
        return max(1, self.owner.stats[Stat.WISDOM].modifier)


# EOF
