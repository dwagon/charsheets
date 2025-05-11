from typing import cast, TYPE_CHECKING, Any

from aenum import extend_enum
from charsheets.classes2014.cleric.cleric import Cleric
from charsheets.constants import Stat, Proficiency, Feature, Recovery
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import BaseCharacter

extend_enum(Feature, "TEMPEST_DOMAIN_SPELLS14", "Tempest Domain Spells")
extend_enum(Feature, "WRATH_OF_THE_STORM14", "Wrath of the Storm")


#################################################################################
class TempestCleric(Cleric):
    def level1(self, **kwargs: Any):
        super().level1(**kwargs)
        assert self.character is not None
        self.add_feature(TempestDomainSpells())
        self.character.add_armor_proficiency(Reason("Tempest Cleric", cast(Proficiency, Proficiency.HEAVY_ARMOUR)))
        self.character.add_weapon_proficiency(Reason("Tempest Cleric", cast(Proficiency, Proficiency.MARTIAL_WEAPONS)))
        self.add_feature(WrathOfTheStorm())


#################################################################################
class TempestDomainSpells(BaseFeature):
    tag = Feature.TEMPEST_DOMAIN_SPELLS14
    _desc = "Spells"
    hide = True

    def mod_add_prepared_spells(self, character: "BaseCharacter") -> Reason[Spell]:
        return Reason("Tempest Domain Spells", Spell.FOG_CLOUD, Spell.THUNDERWAVE)


#################################################################################
class WrathOfTheStorm(BaseFeature):
    tag = Feature.WRATH_OF_THE_STORM14
    recovery = Recovery.LONG_REST
    _desc = """When a creature within 5 feet of you that you can seee hits you with an attack, you can use your 
    reaction to cause the creature to make a Dexterity saving throw. The creature takes 2d8 lightning or thunder 
    damage (your choice) on a failed saving throw, and half as much damage on a successful one."""

    @property
    def goes(self) -> int:
        return max(1, self.owner.stats[Stat.WISDOM].modifier)
