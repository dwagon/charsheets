from typing import TYPE_CHECKING
from aenum import extend_enum

from charsheets.classes.cleric import Cleric
from charsheets.constants import Feature, Recovery
from charsheets.features.base_feature import BaseFeature
from charsheets.reason import Reason
from charsheets.spell import Spell

if TYPE_CHECKING:  # pragma: no coverage
    from charsheets.character import Character


#################################################################################
class ClericLightDomain(Cleric):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._class_name = "Light Domain Cleric"

    #############################################################################
    def class_features(self) -> set[BaseFeature]:
        abilities: set[BaseFeature] = set()
        abilities |= super().class_features()
        abilities |= {RadianceOfTheDawn(), LightDomainSpells(), WardingFlare()}
        if self.level >= 6:
            abilities |= {ImprovedWardingFlare()}
        return abilities


extend_enum(Feature, "IMPROVED_WARDING_FLARE", "Improved Warding Flare")
extend_enum(Feature, "LIGHT_DOMAIN_SPELLS", "Light Domain Spells")
extend_enum(Feature, "RADIANCE_OF_THE_DAWN", "Radiance of the Dawn")
extend_enum(Feature, "WARDING_FLARE", "Warding Flare")


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


# EOF
