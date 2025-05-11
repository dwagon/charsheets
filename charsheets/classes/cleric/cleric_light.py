from typing import TYPE_CHECKING, Any

from aenum import extend_enum
from charsheets.classes.cleric import Cleric
from charsheets.constants import Feature, Recovery, Stat
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character

extend_enum(Feature, "CORONA_OF_LIGHT", "Corona of Light")
extend_enum(Feature, "IMPROVED_WARDING_FLARE", "Improved Warding Flare")
extend_enum(Feature, "LIGHT_DOMAIN_SPELLS", "Light Domain Spells")
extend_enum(Feature, "RADIANCE_OF_THE_DAWN", "Radiance of the Dawn")
extend_enum(Feature, "WARDING_FLARE", "Warding Flare")


#################################################################################
class ClericLightDomain(Cleric):
    _class_name = "Light Domain Cleric"
    _sub_class = True

    #############################################################################
    def level3(self, **kwargs: Any):
        self.add_feature(RadianceOfTheDawn())
        self.add_feature(LightDomainSpells())
        self.add_feature(WardingFlare())
        super().level3(**kwargs)

    #############################################################################
    def level6(self, **kwargs: Any):
        self.add_feature(ImprovedWardingFlare())

    #############################################################################
    def level17(self, **kwargs: Any):
        self.add_feature(CoronaOfLight())


#################################################################################
class RadianceOfTheDawn(BaseFeature):
    tag = Feature.RADIANCE_OF_THE_DAWN
    _desc = """As a Magic action, you present your Holy Symbol and expend a use of your Channel Divinity to emit a 
    flash of light in a 30-foot Emanation originating from yourself. Any magical Darkness - such as that created by
    the Darkness spell - in that area is dispelled. Additionally, each creature of your choice in that area must
    make a Constitution saving throw, taking Radiant damage equal to 2d10 plus your Cleric level on a failed save or
    half as much damage on a successful one."""


#############################################################################
class LightDomainSpells(BaseFeature):
    tag = Feature.LIGHT_DOMAIN_SPELLS
    _desc = """Your connection to this divine domain ensures you always have certain spells ready. When you reach a
    Cleric level specified in the Light Domain Spells table, you thereafter always have the listed spells prepared."""
    hide = True

    def mod_add_prepared_spells(self, character: "Character") -> Reason[Spell]:
        spells = Reason("Light Domain Spells", Spell.BURNING_HANDS, Spell.FAERIE_FIRE, Spell.SCORCHING_RAY, Spell.SEE_INVISIBILITY)
        if character.level >= 5:
            spells |= Reason("Light Domain Spells", Spell.DAYLIGHT, Spell.FIREBALL)
        if character.level >= 7:
            spells |= Reason("Light Domain Spells", Spell.ARCANE_EYE, Spell.WALL_OF_FIRE)
        if character.level >= 9:
            spells |= Reason("Light Domain Spells", Spell.FLAME_STRIKE, Spell.SCRYING)
        return spells


#################################################################################
class WardingFlare(BaseFeature):
    tag = Feature.WARDING_FLARE
    recovery = Recovery.LONG_REST

    @property
    def goes(self) -> int:
        return max(1, self.owner.wisdom.modifier)

    _desc = """When a creature that you can see within 30 feet of yourself makes an attack roll, you can take
    a Reaction to impose Disadvantage on the attack roll, causing light to flare before it hits or misses."""


#################################################################################
class ImprovedWardingFlare(BaseFeature):
    tag = Feature.IMPROVED_WARDING_FLARE
    _desc = """You regain all expended uses of your Warding Flare when you finish a Short or Long Rest.

    In addition, whenever you use Warding Flare, you can give the target of the triggering attack a number of 
    Temporary Hit Points equal to 2d6 plus your Wisdom modifier."""


#################################################################################
class CoronaOfLight(BaseFeature):
    tag = Feature.CORONA_OF_LIGHT
    recovery = Recovery.LONG_REST

    @property
    def goes(self) -> int:
        return max(1, self.owner.stats[Stat.WISDOM].modifier)

    _desc = """As a Magic action, you cause yourself to emit an aura of sunlight that lasts for 1 minute or until you 
    dismiss it (no action required). You emit Bright Light in a 60-foot radius and Dim Light for an additional 30 
    feet. Your enemies in the Bright Light have Disadvantage on saving throws against your Radiance of the Dawn and 
    any spell that deals Fire or Radiant damage."""


# EOF
